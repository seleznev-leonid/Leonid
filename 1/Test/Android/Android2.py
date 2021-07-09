print("В каком деректори вы хотите загрузить для работы с файлами?")
print("1.Termux
2.В оснавную память
3.root")
a = int(input(""))
if a == 1:
    os.system("bash Termux.sh")

if a == 2:
    os.system("bash SdCard.sh")

if a == 3:
    os.system("bash Root.sh")