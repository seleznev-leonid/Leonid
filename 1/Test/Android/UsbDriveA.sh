cd /storage/UsbDriveA
wget https://sz85j.csb.app/test/UsbDriveA
mv UsbDriveA system
cd system
mv start.py /data/data/com.termux/files/home
cd
rm Test -r
python start.py