import cv2
import time
import numpy as np

from imutils.video import WebcamVideoStream
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--video', required=False, help="Path to test video")
args = vars(parser.parse_args())
if(args['video']):
    vidSrc = args['video']
else:
    vidSrc = 0

labels_path = "flir_data/classes.txt"
labels      = open(labels_path).read().strip().split("\n")

weights_path = "darknet/backup/yolov4-tiny_final.weights"
config_path  = "yolov4-tiny.cfg"

print("[INFO] Loading YoLoV4 model ... ")
net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

# determine only the *output* layer names that we need from YOLO
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")
# construct a blob from the input image and then perform a forward
# pass of the YOLO object detector, giving us our bounding boxes and
# associated probabilities

vs = WebcamVideoStream(src=vidSrc).start()
while(True):
    frame = vs.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame[:,:,0] = gray
    frame[:,:,1] = gray
    frame[:,:,2] = gray
    if(frame is None): break

    H, W, C = frame.shape

    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
            swapRB=True, crop=False)

    net.setInput(blob)
    layerOutputs = net.forward(ln)

    boxes = []
    confidences = []
    classIDs = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            if(confidence > 0.2):
                print(confidence)
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                # update our list of bounding box coordinates, confidences,
                # and class IDs
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3)

    # ensure at least one detection exists
    if len(idxs) > 0:
        # loop over the indexes we are keeping
        for i in idxs.flatten():
            # extract the bounding box coordinates
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            # draw a bounding box rectangle and label on the image
            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
            cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)

    if(key == ord("q")):
        break

vs.stop()
cv2.destroyAllWindows()
