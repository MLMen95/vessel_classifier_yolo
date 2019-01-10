# vessel_classifier_yolo
This is a repository for the object detection of vessels in video which is implemented using [YOLO](https://pjreddie.com/darknet/yolo/) by darknet.

#Instructions: 
- Using [BBox-Label-Tool](https://github.com/puzzledqs/BBox-Label-Tool), prepare the dataset by drawing the bounding boxes over the images.
- `pipenv install` to install all necessary packages
- run `generate_xml.py` to generate labels for the bounding boxes
- `pipenv run python flow (---)` to start training the model.
- using `processesing_video.py`, the video file will be processed and the frame will show the video with the detected vessels.

#Screenshots of video being processed:
![military](http://url/to/img.png)
![tugboat](http://url/to/img.png)
![passenger](http://url/to/img.png)


#Credits:
- Tutorial from [Mark Jay](https://www.youtube.com/watch?v=eFJOGsQ_YTA)
