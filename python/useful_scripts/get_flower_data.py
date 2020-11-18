import os
import sys
import tarfile
from six.moves import urllib
print("Starting...")
# Downlooad data
FLOWERS_URL = "http://download.tensorflow.org/example_images/flower_photos.tgz"
FLOWERS_PATH = os.path.join(os.getcwd(),"datasets")
os.makedirs(FLOWERS_PATH,exist_ok=True)

urllib.request.urlretrieve(FLOWERS_URL, os.path.join(FLOWERS_PATH, "flower_photos.tgz"))
tgz_path=os.path.join(FLOWERS_PATH, "flower_photos.tgz")
flowers_tgz = tarfile.open(tgz_path)
flowers_tgz.extractall(path=FLOWERS_PATH)
flowers_tgz.close()
os.remove(tgz_path)
print("Data Download is Done")
# It is done

print("Split data")
#Copy flowers folder
# real flower folder directory
path=os.getcwd()
path=os.path.join(path,"datasets/flower_photos")
#os.listdir(path)

# copy flower folder directory
copy_path=os.path.join(os.getcwd(),"datasets/copy_flowers")
os.makedirs(copy_path,exist_ok=True)
#os.listdir(copy_path) # What see insede


# Copy  flower folder with files from real flower folder

from distutils.dir_util import copy_tree

fromDirectory = path
toDirectory = copy_path

copy_tree(fromDirectory, toDirectory)

## Chane Names"""

flower_path=os.path.join(os.getcwd(),"datasets/flower_photos")

names=['roses', 'daisy', 'sunflowers', 'tulips', 'dandelion']

for index in range(len(names)):

    name_path=os.path.join(flower_path,names[index])
    print(name_path)

    # new names
    new_names=['{}.jpg'.format(i) for i in range(len(os.listdir(name_path)))]
    print(len(os.listdir(name_path)))


    # old names
    old_names=os.listdir(name_path)


    # name change function
    for i in range(len(os.listdir(name_path))):
        src=os.path.join(name_path,new_names[i])
        dst=os.path.join(name_path,old_names[i])
        os.rename(dst,src)

os.listdir(name_path)

"""## Divide Data"""

import os 
import shutil

path=os.getcwd()
path

original_data_dir=os.path.join(path,"datasets/flower_photos")
original_data_dir

base_data_dir=os.path.join(path,"datasets/flower_data")
base_data_dir

train_dir=os.path.join(base_data_dir,"train")
os.makedirs(train_dir,exist_ok=True)

validation_dir=os.path.join(base_data_dir,"validation")
os.makedirs(validation_dir,exist_ok=True)

train_roses_dir=os.path.join(train_dir,"roses")
os.makedirs(train_roses_dir,exist_ok=True)


train_daisy_dir=os.path.join(train_dir,"daisy")
os.makedirs(train_daisy_dir,exist_ok=True)

train_tulips_dir=os.path.join(train_dir,"tulips")
os.makedirs(train_tulips_dir,exist_ok=True)

train_sunflower_dir=os.path.join(train_dir,"sunflowers")
os.makedirs(train_sunflower_dir,exist_ok=True)


train_dandelion_dir=os.path.join(train_dir,"dandelion")
os.makedirs(train_dandelion_dir,exist_ok=True)

# Directory validation data flowers

validation_roses_dir=os.path.join(validation_dir,"roses")
os.makedirs(validation_roses_dir,exist_ok=True)


validation_daisy_dir=os.path.join(validation_dir,"daisy")
os.makedirs(validation_daisy_dir,exist_ok=True)

validation_tulips_dir=os.path.join(validation_dir,"tulips")
os.makedirs(validation_tulips_dir,exist_ok=True)

validation_sunflower_dir=os.path.join(validation_dir,"sunflowers")
os.makedirs(validation_sunflower_dir,exist_ok=True)


validation_dandelion_dir=os.path.join(validation_dir,"dandelion")
os.makedirs(validation_dandelion_dir,exist_ok=True)

# Copy first 500 roses images to train
fnames = ['{}.jpg'.format(i) for i in range(500)]
o_flower=os.path.join(original_data_dir,"roses")
for fname in fnames:
    src = os.path.join(o_flower, fname)
    dst = os.path.join(train_roses_dir, fname)
    shutil.copyfile(src, dst)
        

# Copy first 500 daisy images to train
fnames = ['{}.jpg'.format(i) for i in range(500)]
o_flower=os.path.join(original_data_dir,"daisy")
for fname in fnames:
    src = os.path.join(o_flower, fname)
    dst = os.path.join(train_daisy_dir, fname)
    shutil.copyfile(src, dst)
        
# Copy first 500 tulips images to train
fnames = ['{}.jpg'.format(i) for i in range(500)]
o_flower=os.path.join(original_data_dir,"tulips")
for fname in fnames:
    src = os.path.join(o_flower, fname)
    dst = os.path.join(train_tulips_dir, fname)
    shutil.copyfile(src, dst)
        
# Copy first 500 sunflower images to train
fnames = ['{}.jpg'.format(i) for i in range(500)]
o_flower=os.path.join(original_data_dir,"sunflowers")
for fname in fnames:
    src = os.path.join(o_flower, fname)
    dst = os.path.join(train_sunflower_dir, fname)
    shutil.copyfile(src, dst)
    
# Copy first 500 dandelion images to train
fnames = ['{}.jpg'.format(i) for i in range(500)]
o_flower=os.path.join(original_data_dir,"dandelion")
for fname in fnames:
    src = os.path.join(o_flower, fname)
    dst = os.path.join(train_dandelion_dir, fname)
    shutil.copyfile(src, dst)

# Copy first 500:600 roses images to validation
fnames = ['{}.jpg'.format(i) for i in range(500,600)]
o_flower=os.path.join(original_data_dir,"roses")
for fname in fnames:
    src = os.path.join(o_flower, fname)
    dst = os.path.join(validation_roses_dir, fname)
    shutil.copyfile(src, dst)
        

# Copy first 500:600 daisy images to train
fnames = ['{}.jpg'.format(i) for i in range(500,600)]
o_flower=os.path.join(original_data_dir,"daisy")
for fname in fnames:
    src = os.path.join(o_flower, fname)
    dst = os.path.join(validation_daisy_dir, fname)
    shutil.copyfile(src, dst)
        
# Copy first 500:600 tulips images to train
fnames = ['{}.jpg'.format(i) for i in range(500,600)]
o_flower=os.path.join(original_data_dir,"tulips")
for fname in fnames:
    src = os.path.join(o_flower, fname)
    dst = os.path.join(validation_tulips_dir, fname)
    shutil.copyfile(src, dst)
        
# Copy first 500:600 sunflower images to train
fnames = ['{}.jpg'.format(i) for i in range(500,600)]
o_flower=os.path.join(original_data_dir,"sunflowers")
for fname in fnames:
    src = os.path.join(o_flower, fname)
    dst = os.path.join(validation_sunflower_dir, fname)
    shutil.copyfile(src, dst)
    
# Copy first 500:600 dandelion images to train
fnames = ['{}.jpg'.format(i) for i in range(500,600)]
o_flower=os.path.join(original_data_dir,"dandelion")
for fname in fnames:
    src = os.path.join(o_flower, fname)
    dst = os.path.join(validation_dandelion_dir, fname)
    shutil.copyfile(src, dst)

s=os.path.join(original_data_dir,"sunflowers")
len(os.listdir(s))

print(len(os.listdir(train_dandelion_dir)))


print("** Process is Done **")
