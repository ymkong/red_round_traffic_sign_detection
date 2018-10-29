# convert ground truth file to the format required by YOLO
# written by: Yiming Kong
# date created: 10/28/2018

import os
from PIL import Image

# convert function is borrowed from: https://github.com/ManivannanMurugavel/YOLO-Annotation-Tool/blob/master/convert.py
def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

# get current working directory
cwd = os.getcwd()

# Configure Paths
mypath = cwd + "/images"
outpath = cwd + "/images/tmp"
if not os.path.exists(outpath):
    os.mkdir(outpath)

# Get input text file list
txt_name_list = []
for filename in os.listdir(mypath):
    if filename.endswith(".txt"):
        txt_name_list.append(filename)

# Process
for txt_name in txt_name_list:

    # Open input text files
    txt_file = open(mypath + "/" + txt_name, "r")
    lines = txt_file.read().split('\n') #for ubuntu, use "\r\n" instead of "\n"

    # Open output text files
    txt_outfile = open(outpath + "/" + txt_name, "w")

    # Convert the data to YOLO format
    for line in lines:

        elems = line.split(',')
        if(len(elems) >= 2):

            xmin = elems[0]
            xmax = elems[2]
            ymin = elems[1]
            ymax = elems[3]

            img_path = mypath + "/" + txt_name[0:5] + ".jpg"

            im = Image.open(img_path)
            w = int(im.size[0])
            h = int(im.size[1])

            b = (float(xmin), float(xmax), float(ymin), float(ymax))
            bb = convert((w, h), b)
            txt_outfile.write("1" + " " + " ".join([str(a) for a in bb]) + '\n')