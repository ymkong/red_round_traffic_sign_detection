# Red Round Traffic Sign Detection

The goal of the project is to carry out red round sign detection. Type in terminal: 

sh run.sh

carries out the first step in this project, which is to download/prepare the dataset for training. Specifically, it
- Download 900 images from GTSDB saved in ~/FullIJCNN2013/ 
- Convert the PPM images to jpeg
- By looking at ground truths from ~/FullIJCNN2013/gt.txt, for each image that has red round signs, 1) generate a TXT file under ~/image/, which contains locations of the red round signs, 2) move the jpeg file to  ~/images/
- Annotate all the images under ~/images for YOLO, according to the input requirement of YOLO. 
- Select images for train set (80%), dev set (10%), and test set (10%). The names of the images in each set are given in ~/train.txt, ~/dev.txt, ~/test.txt
- Prepare YOLO configuration files in ~/cfg: Obj.data, obj.names, tiny-yolo.cfg
