# divide images into train, dev, and test set
# written by: Yiming Kong
# date created: 10/28/2018

import glob, os
import random

# Current directory
cwd = os.getcwd()

# Percentage of images to be used for the test set
percentage_dev = 10
percentage_test = 10

# Create train.txt and test.txt, dev.txt
file_train = open('train.txt', 'w')  
file_dev = open('dev.txt', 'w')
file_test = open('test.txt', 'w')

# get the list of jpeg files
jpg_name_list = []
for filename in os.listdir(cwd + "/images/"):
    if filename.endswith(".jpg"):
        jpg_name_list.append(filename)

# get the number of train, dev, and test set
ll = len(jpg_name_list)
num_dev = int((1.0 * percentage_dev / 100) * ll)
num_test = int((1.0 * percentage_test / 100) * ll)
num_train = len(jpg_name_list) - num_dev - num_test

# populate train.txt, dev.txt, and test.txt
train_idx = random.sample(xrange(0, ll), num_train)
left_list = set(xrange(0, ll)) - set(train_idx)
dev_idx = random.sample(left_list, num_dev)
left_list = set(left_list) - set(dev_idx)
test_idx = left_list

for ind in train_idx:
    file_train.write(cwd + "/images/" + jpg_name_list[ind] + "\n")
for ind in dev_idx:
    file_dev.write(cwd + "/images/" + jpg_name_list[ind] + "\n")
for ind in test_idx:
    file_test.write(cwd + "/images/" + jpg_name_list[ind] + "\n")