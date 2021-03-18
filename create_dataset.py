import os
import glob

from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("--train-size", required=False, default=0.7, type=float, help="Training images ratio")
parser.add_argument("--data-dir", required=True, type=str, help="Data directory")
args = vars(parser.parse_args())

data_dir    = args['data_dir']
train_ratio = args['train_size'] 

# Grab the label files 
label_files  = glob.glob(f"{data_dir}/*.txt")
dataset_size = len(label_files)
train_size   = int(train_ratio * dataset_size)

train_file = open(f"{data_dir}/train.txt", "w")
valid_file = open(f"{data_dir}/valid.txt", "w")
obj_file   = open(f"{data_dir}/obj.data",  "w")
class_file = f'{data_dir}/classes.txt'

for i, file_ in enumerate(label_files):
    filename = os.path.basename(file_)
    filename = filename.split(".")[0]
    img_filename = filename + ".jpg"
    img_filename = os.path.join(data_dir, img_filename)

    if(os.path.exists(img_filename)):
        if(i < train_size):
            train_file.write("../" + img_filename + '\n')
        else:
            valid_file.write("../" + img_filename + '\n')

obj_file.write("classes=1\n")
obj_file.write(f"train=../{data_dir}/train.txt\n")
obj_file.write(f"valid=../{data_dir}/valid.txt\n")
obj_file.write("names=../" + class_file + '\n')
obj_file.write("backup=backup\n")

### Close files ###
train_file.close()
valid_file.close()
obj_file.close()
