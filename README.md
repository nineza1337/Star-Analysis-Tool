# Tools for FITS Image (Star Analysis Tool)

เครื่องมือสำหรับวิเคราะห์และสร้างกราฟจากไฟล์ FITS (Flexible Image Transport System) สำหรับงานดาราศาสตร์ เขียนด้วยภาษา Python

## ความสามารถ (Features)

โปรแกรมนี้สามารถอ่านไฟล์ `.fits` และแสดงผลข้อมูลในรูปแบบกราฟต่างๆ ได้แก่:

1.  **Scatter Plot**: แสดงตำแหน่งดวงดาว (จำลอง) บนพิกัด RA/DEC
2.  **Histogram**: แสดงการกระจายตัวของค่า Right Ascension (RA) และ Declination (DEC)
3.  **Heatmap**: แสดงภาพถ่ายดาราศาสตร์จากข้อมูลในไฟล์ FITS

## สิ่งที่ต้องมี (Requirements)

*   Python 3.x
*   Library ที่จำเป็น (ติดตั้งผ่าน `requirements.txt.txt`):
    *   numpy
    *   matplotlib
    *   astropy
    *   opencv-python

## การติดตั้งและการใช้งาน (Installation & Usage)

1.  **Clone หรือดาวน์โหลดโปรเจคนี้**

2.  **ติดตั้ง Library ที่จำเป็น**
    ```bash
    pip install -r requirements.txt.txt
    ```

3.  **เตรียมไฟล์ FITS**
    *   นำไฟล์นามสกุล `.fits` ที่ต้องการวิเคราะห์ไปวางไว้ในโฟลเดอร์ `fits`
    *   หากไม่มีโฟลเดอร์ `fits` โปรแกรมจะสร้างให้เมื่อรันครั้งแรก

4.  **รันโปรแกรม**
    ```bash
    python main.py
    ```

5.  **เลือกโหมดการทำงาน**
    เมื่อรันโปรแกรม จะมีเมนูให้เลือกดังนี้:
    *   `1`: สร้าง Scatter Plot
    *   `2`: สร้าง Histogram
    *   `3`: สร้าง Heatmap
    *   `4`: สร้างกราฟทั้งหมด

6.  **ดูผลลัพธ์**
    *   ไฟล์รูปภาพกราฟที่ได้จะถูกบันทึกไว้ในโฟลเดอร์ `output` โดยแยกเป็นหมวดหมู่ตามประเภทของกราฟ

## โครงสร้างโปรเจค (Project Structure)

*   `main.py`: โค้ดหลักของโปรแกรม
*   `fits/`: โฟลเดอร์สำหรับเก็บไฟล์ FITS ต้นฉบับ
*   `output/`: โฟลเดอร์สำหรับเก็บไฟล์รูปภาพผลลัพธ์
*   `requirements.txt.txt`: รายชื่อ Library ที่ต้องติดตั้ง
