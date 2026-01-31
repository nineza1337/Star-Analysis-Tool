import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
import glob

def plot_fits_image_with_wcs(fits_file, output_folder, graph_type):
    hdul = fits.open(fits_file)
    image_data = hdul[0].data
    wcs = WCS(hdul[0].header)
    
    x_pixels = np.random.randint(0, image_data.shape[1], 100)  # ตัวอย่างตำแหน่ง x
    y_pixels = np.random.randint(0, image_data.shape[0], 100)  # ตัวอย่างตำแหน่ง y

    ra, dec = wcs.all_pix2world(x_pixels, y_pixels, 0)

    output_file = os.path.join(output_folder, os.path.basename(fits_file).replace('.fits', f'_{graph_type}.png'))

    plt.figure(figsize=(10, 8))
    
    if graph_type == "scatter":
        plt.scatter(ra, dec, color='red', marker='o', s=10, label="ดาว")
    elif graph_type == "histogram":
        plt.hist(ra, bins=30, color='blue', alpha=0.7, label="RA Histogram")
        plt.hist(dec, bins=30, color='green', alpha=0.7, label="DEC Histogram")
    elif graph_type == "heatmap":
        plt.imshow(image_data, cmap='gray', origin='lower')
        plt.colorbar(label="Intensity")

    plt.xlabel('Right Ascension (RA)', fontsize=12)
    plt.ylabel('Declination (DEC)', fontsize=12)
    plt.title(f'{graph_type.capitalize()} Plot of Stars with WCS Coordinates ({os.path.basename(fits_file)})', fontsize=14)

    if graph_type == "scatter":
        for i in range(0, len(ra), 10):
            plt.text(ra[i], dec[i], f"({ra[i]:.4f}, {dec[i]:.4f})", fontsize=8, color='blue')

    plt.grid(True)
    plt.legend()

    plt.savefig(output_file, dpi=300)
    plt.close()

def plot_all_graphs_for_fits(fits_file, output_folder):
    graph_types = ["scatter", "histogram", "heatmap"]
    
    for graph_type in graph_types:
        specific_output_folder = os.path.join(output_folder, graph_type)
        if not os.path.exists(specific_output_folder):
            os.makedirs(specific_output_folder)
        plot_fits_image_with_wcs(fits_file, specific_output_folder, graph_type)

def choose_graph_type(fits_files):
    os.system('cls')
    print(f"load fits {len(fits_files)} files")
    print(f"")
    print("---------------------------------------------")
    print("1. Plot of Stars with WCS Coordinates (Scatter)")
    print("2. Histogram")
    print("3. Heatmap")
    print("4. all graphs")
    print("--------------------------------------------- ")
    print("")

    choice = input("opt (1/2/3/4): ")
    
    if choice == "1":
        return "scatter"
    elif choice == "2":
        return "histogram"
    elif choice == "3":
        return "heatmap"
    elif choice == "4":
        return "all"
    else:
        print("Scatter Plot")
        return "scatter"

def main():
    folder_name = 'fits'

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    else:
        pass
    print(f"โฟลเดอร์ '{folder_name}' มีอยู่แล้ว.")
    input_folder = 'fits' 
    
    graph_types = ["scatter", "histogram", "heatmap"]
    for graph_type in graph_types:
        output_folder = os.path.join('output', graph_type)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    fits_files = glob.glob(os.path.join(input_folder, '*.fits'))
    print(f"load fits {len(fits_files)} files")
    graph_type = choose_graph_type(fits_files)
    output_folder = os.path.join('output', graph_type)

    if graph_type == "all":
        for fits_file in fits_files:
            plot_all_graphs_for_fits(fits_file, 'output')
            print(f"Processed: {fits_file}")
    else:
        for fits_file in fits_files:
            plot_fits_image_with_wcs(fits_file, output_folder, graph_type)
            print(f"Processed: {fits_file}")

    print("All files processed and saved.")

if __name__ == "__main__":
    main()

