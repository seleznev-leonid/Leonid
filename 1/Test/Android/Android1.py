print("В каком деректори вы хотите загрузить для работы с файлами?")
print("1.Termux
2.В оснавную память
3.Карта память
4.Флешка")
a = int(input(""))
if a == 1:
    os.system("bash Termux.sh")

if a == 2:
    os.system("bash SdCard.sh")

if a == 3:
    os.system("bash extSdCard.sh")

if a == 4:
    os.system("bash UsbDriveA.sh")
