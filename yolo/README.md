# Yolo Darknet
## Read more information 
 - github : https://github.com/pjreddie/darknet/tree/master
 - website : https://pjreddie.com/darknet/yolo/

# 
# Requirements
#### **recommend
## software
- ubuntu 18.04
- docker
- docker-compose
- nvidia-driver
- nvidia-docker
## hardware
- nvidia-gpu (gpu-ram >=3)
- webcam or ipcam
#
# How to use
    # 1 : download yolo v2 model
    sh yolo/get_weight.sh

    # 2 : Build and Run docker-compose
    docker-compose up --build 

    # 3 : Open browser
    Goto http://localhost:5000