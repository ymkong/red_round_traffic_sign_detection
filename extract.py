# extract images that has red round sign(s) and write to txt its ground truth
# written by: Yiming Kong
# date created: 10/28/2018

import numpy as np
import csv
import os
import shutil

# get current working directory
cwd = os.getcwd()

# red round sign corresponding class-ID
prohibitoryClassIds = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 15, 16]

# read in gt.txt
# ImgNo#.ppm;#leftCol#;##topRow#;#rightCol#;#bottomRow#;#ClassID#
datain = np.genfromtxt(cwd + "/FullIJCNN2013/gt.txt", delimiter = ';', dtype="string")  # [filename, cord, classID]

# write to .txt for each image that has red round sign
pre_id = ""
for i in range(0, len(datain)):

    # if that image has the red round sign
    if int(datain[i, 5]) in prohibitoryClassIds:

        # get image id
        curr_id = datain[i, 0][0:5]

        # if it is a new image id
        if curr_id != pre_id:

            # if it is not the first image id
            if pre_id != "":
                fh.close()
                shutil.move(cwd + "/FullIJCNN2013/" + pre_id + ".jpg", cwd + "/images/" + pre_id + ".jpg") # move jpeg image to ~/images/

            # create a handler for the txt file
            fh = open(cwd + "/images/" + curr_id + ".txt", "wb")
            writer = csv.writer(fh, lineterminator='\n')
            pre_id = curr_id

        # write the location in
        writer.writerow(datain[i, 1:5])

# last image that has red round sign
fh.close()
shutil.move(cwd + "/FullIJCNN2013/" + pre_id + ".jpg", cwd + "/images/" + pre_id + ".jpg")  # move jpeg image to ~/images/