# FIRFaceDetection
Face detection on thermal images using YoLov4

# Prepare dataset :
1. Use labelImg to label images and put annotation files and image files into 1 folder
2. Run :
```bash
python3 prepare_data.py --data-dir <data_dir_path>
```
3. 3 files will be added to the data folder - train.txt, valid.txt and obj.data 

# To download the weights files:
```bash 
./download_weights.sh
```

# To start training :
```bash
cd darknet
./darknet detector train ../flir_data/obj.data # object data file 
	../yolov4-tiny.cfg # the config file
	../yolo4-tiny.conv.29 # the weights file
	-dont_show
	-map	
```
