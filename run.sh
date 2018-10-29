# download GTSDB
cd ~ 
wget -P ~ "http://benchmark.ini.rub.de/Dataset_GTSDB/FullIJCNN2013.zip"
unzip FullIJCNN2013.zip

# convert to jpeg
mkdir images 
cd ~/FullIJCNN2013 
mogrify -format jpg *.ppm
cd .. 

# select images that have the red round signs and extract the ground truth for those images
python ~/extract.py

# convert the ground truth files according to the requirement of YOLO
python ~/convert.py
mv ~/images/tmp/*.txt ~/images/
rm -r ~/images/tmp

# get train, dev, and test set
python ~/divide.py