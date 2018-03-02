# organize imports
import os
import datetime
import shutil

# print start time
print ("[INFO] program started on - " + str(datetime.datetime.now))

# get the input and output path
input_img_path = raw_input("Enter the path of raw dataset you want to transfer...\n")
input_path  =  "../" + input_img_path
output_img_path = raw_input("Enter the path to the training dataset...\n")
#creating train directory
if not os.path.isdir(output_img_path) :
        os.system("mkdir " + output_img_path)
output_path = output_img_path

num_class = input("Enter the no. of classes you want to train...\n")

# get the class label limit
class_limit = num_class

num_image = input("Enter the no. of images you want to train...\n")

# variables to keep track
label = 0
i = 0
j = num_image
class_names = []

for cl in range(0, class_limit):
	cl = raw_input("Enter your class names..\n")
	class_names.append(cl)


# change the current working directory
os.chdir(output_path)

for x in range(0, class_limit):
    # create a folder for that class
    os.system("mkdir " + class_names[x])
    # get the current path
    cur_path = output_path + "/" + class_names[x] 
    # get image path
    image_path = input_path + "/" + class_names[x] 
    # get image files
    img_files = os.listdir(image_path)
    # loop over the images in the dataset
    for image in img_files:
        if i < j:
            image_name = os.path.join(image_path, image)
            shutil.copy(image_name, "../" + cur_path)
        i += 1
    i = 0

# print end time
print ("[INFO] program ended on - " + str(datetime.datetime.now))

