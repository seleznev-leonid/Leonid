print("In which directory do you want to download to work with files?")
print("1.home
2.root
3./#")
a = int(input(""))
if a == 1:
    os.system("bash Home.sh")

if a == 2:
    os.system("bash Root.sh")

if a == 3:
    os.system("bash #.sh")
