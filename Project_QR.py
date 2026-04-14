import qrcode
import os

url = input("Enter the URL: ").strip()
file_name = input("Enter the file name: ").strip()

#Fixed location
folder_path = "C:\\QR"

#Create folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

#Join folder path + file name
file_path = os.path.join(folder_path, file_name)

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR generated")