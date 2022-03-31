#WORKS ONLY ON WINDOWS!!
print("Welcome to QR Code Generator and Reader!")
print("Please allow 2-3 minutes to install the required dependencies!\n")
print('\033[1m' + "Please ignore any red error text; the program will run fine" + '\033[0m')
import os, sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
try:
    os.system('pip install -q --progress-bar on --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts qrcode')
    os.system('pip install -q --progress-bar on --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts opencv-contrib-python')
    os.system('pip install -q --progress-bar on --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts pillow')
    os.system('pip install -q --progress-bar on --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts datetime')
    os.system('pip install -q --progress-bar on --disable-pip-version-check --no-cache-dir --no-color --no-warn-conflicts prettytable')
except:
    print("Unable to install required dependencies!")
    sys.exit(2)
try:
    import qrcode, time, cv2, datetime, prettytable
except:
    print("Unable to import required dependencies!")
    sys.exit(3)
L=prettytable.PrettyTable(["QR Content", "File Name", "Timestamp"])
def create():
    while True:
        i = input("Enter text to make a QR Code: ")
        n = input("Enter file name (File will be generated in PNG format): ")
        if not i:
            print("Enter text to make QR Code!")
            continue
        if not n:
            print("Enter file name!")
            continue
        if i and n:
            break
    qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=1)
    qr_code.add_data(i)
    qr_code.make(fit=True)
    image = qr_code.make_image(fill_color="black", back_color="white")
    image.save(n + ".png")
    n = n + ".png"
    L.add_row([i, n, datetime.datetime.now()])
    time.sleep(2)
    os.startfile(n)

def read():
    while True:
        n = input("Enter file name with extension of QR code: ")
        if not n:
            print("Enter file name with extension of QR code!")
            continue
        if n:
            break
    image = cv2.imread(n)
    try:
        det = cv2.QRCodeDetector()
        data, pts, stc = det.detectAndDecode(image)
    except:
        print("Error occured!")
        sys.exit(1)
    print("QR Code Data:")
    print(data)
    print()

def history():
    print(L)

def about():
    print("ABOUT")
    print("Made by Taha Yaseen Parker")
    print("This was CS50!")

print("Welcome to QR Code Generator and Reader!")
while True:
    while True:
        print()
        print("1. Create QR Code in same directory")
        print("2. Read a QR Code in same directory")
        print("3. History")
        print("4. About")
        print("0. Exit")
        ch = input("Enter your choice: ")

        if ch not in ['1', '2', '3', '4', '0']:
            print("Wrong option! Plase choose from options printed above!")
            continue
        else:
            break
    if ch == '1':
        create()
    elif ch == '2':
        read()
    elif ch == '3':
        history()
    elif ch == '4':
        about()
    elif ch == '0':
        print("You have exited the program!")
        break
