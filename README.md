# yolov5-master
Number Plate detection using ultralytics YoloV5s

## YOLOv5
* Yolov5 pretrained architecture serve as basis of the trained network
#### Link to yolov5 repo - https://github.com/ultralytics/yolov5


## Trained Weights
The final trained weights can be downloaded from this link - https://drive.google.com/file/d/1-NCjC8-OZp9TxpWinHLEfLwUnG7hlqrN/view?usp=sharing

## Requirements

Python 3.8 or later with all [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) dependencies installed, including `torch>=1.7`. To install run:
<!-- $ sudo apt update && apt install -y libgl1-mesa-glx libsm6 libxext6 libxrender-dev -->
```bash
$ pip install -r requirements.txt
```

## Run Program

This will run the program which will use the images in ./images folder and saves the croped and detected images to runs/exp[x] 
```bash
$ python run.py
```

## Inference

`detect.py` runs inference on a variety of sources, downloading models automatically from the [latest YOLOv5 release](https://github.com/ultralytics/yolov5/releases) and saving results to `runs/detect`.
```bash
$ python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            'https://youtu.be/NUsoVlDFqZg'  # YouTube video
                            'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```
