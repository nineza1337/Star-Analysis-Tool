import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
import glob

# ฟังก์ชันสำหรับแปลงพิกัดและสร้างกราฟจากไฟล์ FITS
def plot_fits_image_with_wcs(fits_file, output_folder, graph_type):
    """
    ฟังก์ชันนี้จะทำการแปลงพิกัด WCS จากไฟล์ FITS และสร้างกราฟที่เลือก
    """
    # เปิดไฟล์ FITS
    hdul = fits.open(fits_file)
    
    # ดึงข้อมูลภาพ (Data) และ WCS
    image_data = hdul[0].data
    wcs = WCS(hdul[0].header)
    
    # Extracting sources from the image (สมมติว่าเรามีพิกัดของดาวในรูปแบบพิกเซล (x, y))
    # ตัวอย่างตำแหน่ง x, y ของดาวในรูปภาพ (ใช้ random points ในที่นี้)
    x_pixels = np.random.randint(0, image_data.shape[1], 100)  # ตัวอย่างตำแหน่ง x
    y_pixels = np.random.randint(0, image_data.shape[0], 100)  # ตัวอย่างตำแหน่ง y

    # แปลงพิกเซลเป็นพิกัด RA, DEC โดยใช้ WCS
    ra, dec = wcs.all_pix2world(x_pixels, y_pixels, 0)

    # สร้างชื่อไฟล์สำหรับบันทึกผลลัพธ์
    output_file = os.path.join(output_folder, os.path.basename(fits_file).replace('.fits', f'_{graph_type}.png'))
    
    # สร้างกราฟ
    plt.figure(figsize=(10, 8))
    
    if graph_type == "scatter":
        plt.scatter(ra, dec, color='red', marker='o', s=10, label="ดาว")
    elif graph_type == "histogram":
        plt.hist(ra, bins=30, color='blue', alpha=0.7, label="RA Histogram")
        plt.hist(dec, bins=30, color='green', alpha=0.7, label="DEC Histogram")
    elif graph_type == "heatmap":
        plt.imshow(image_data, cmap='gray', origin='lower')
        plt.colorbar(label="Intensity")
    
    # เพิ่มชื่อแกนและชื่อกราฟ
    plt.xlabel('Right Ascension (RA)', fontsize=12)
    plt.ylabel('Declination (DEC)', fontsize=12)
    plt.title(f'{graph_type.capitalize()} Plot of Stars with WCS Coordinates ({os.path.basename(fits_file)})', fontsize=14)

    # เพิ่มข้อมูลพิกัด WCS บนกราฟ (สำหรับ scatter plot)
    if graph_type == "scatter":
        for i in range(0, len(ra), 10):  # แสดงพิกัดบางจุดเท่านั้นเพื่อไม่ให้ข้อมูลแน่นเกินไป
            plt.text(ra[i], dec[i], f"({ra[i]:.4f}, {dec[i]:.4f})", fontsize=8, color='blue')

    # แสดงกริดและตำนาน
    plt.grid(True)
    plt.legend()

    # บันทึกกราฟลงในไฟล์ภาพ
    plt.savefig(output_file, dpi=300)  # บันทึกเป็น PNG ที่มีความละเอียดสูง
    plt.close()  # ปิดกราฟเพื่อไม่ให้เกิดการทับซ้อนของกราฟถัดไป

# ฟังก์ชันสร้างกราฟทุกประเภท (scatter, histogram, heatmap) สำหรับไฟล์ FITS
def plot_all_graphs_for_fits(fits_file, output_folder):
    """
    ฟังก์ชันนี้จะทำการสร้างกราฟทุกประเภท (scatter, histogram, heatmap) สำหรับไฟล์ FITS หนึ่งไฟล์
    """
    graph_types = ["scatter", "histogram", "heatmap"]
    
    for graph_type in graph_types:
        # สร้างโฟลเดอร์สำหรับแต่ละประเภทกราฟ
        specific_output_folder = os.path.join(output_folder, graph_type)
        if not os.path.exists(specific_output_folder):
            os.makedirs(specific_output_folder)
        
        # บันทึกกราฟในโฟลเดอร์ที่เหมาะสม
        plot_fits_image_with_wcs(fits_file, specific_output_folder, graph_type)

# ฟังก์ชันให้เลือกประเภทกราฟ
def choose_graph_type(fits_files):
    os.system('cls')
    print(f"load fits {len(fits_files)} files")
    print(f"")
    print("---------------------------------------------")
    print("1. Plot of Stars with WCS Coordinates (Scatter)")
    print("2. Histogram")
    print("3. Heatmap")
    print("4. all graphs")
    print("--------------------------------------------- by akanine.")
    print("")

    # รับข้อมูลการเลือกกราฟจากผู้ใช้
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

# ฟังก์ชันหลัก
def main():
    folder_name = 'fits'

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    else:
        pass
    print(f"โฟลเดอร์ '{folder_name}' มีอยู่แล้ว.")
    # โฟลเดอร์ที่เก็บไฟล์ FITS
    input_folder = 'fits'  # เปลี่ยนเส้นทางเป็นโฟลเดอร์ของคุณ
    
    # สร้างโฟลเดอร์สำหรับประเภทกราฟต่าง ๆ
    graph_types = ["scatter", "histogram", "heatmap"]
    for graph_type in graph_types:
        output_folder = os.path.join('output', graph_type)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    # หาทุกไฟล์ FITS ในโฟลเดอร์
    fits_files = glob.glob(os.path.join(input_folder, '*.fits'))
    
    # แสดงจำนวนไฟล์ FITS ที่พบ
    print(f"load fits {len(fits_files)} files")

    # ถามผู้ใช้เลือกประเภทกราฟ
    graph_type = choose_graph_type(fits_files)

    # กำหนดโฟลเดอร์ที่จะบันทึกผลลัพธ์ตามประเภทกราฟ
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
