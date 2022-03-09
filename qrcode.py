# This is a sample Python script.
import  qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import cv2
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    qr = qrcode.QRCode(
        version= 1,
        error_correction= qrcode.constants.ERROR_CORRECT_H,
        box_size= 10,
        border= 4,
    )
    qr.add_data(name)
    qr.add_data("2")
    qr.add_data("3")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", black_color= "white")
    img.save('sample.png')

def deqr():
    decocdeQR = decode(Image.open("sample.png"))
    print(decocdeQR[0].data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('test')
    deqr()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
