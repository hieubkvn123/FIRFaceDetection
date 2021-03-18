# FIRFaceDetection
Face detection on thermal images using YoLov4

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
