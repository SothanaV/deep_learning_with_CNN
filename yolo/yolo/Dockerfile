FROM nvidia/cuda:latest
RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa &&\
    add-apt-repository main && add-apt-repository universe && add-apt-repository restricted && add-apt-repository multiverse
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y wget git pkg-config build-essential cmake zlib1g-dev libjpeg-dev libwebp-dev libpng-dev \ 
    libtiff5-dev libopenexr-dev libgdal-dev libavcodec-dev libavformat-dev libswscale-dev \ 
    libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev \ 
    libxine2-dev libtbb-dev libeigen3-dev python-dev python-tk python-numpy python3-dev python3-tk python3-numpy python3.6 \
    python2.7 unzip wget qt5-default libvtk6-dev libopencv-dev libgl-dev libglu-dev libglib2.0-dev libsm-dev libxrender-dev \ 
    libfontconfig1-dev libxext-dev doxygen python3-pip opencv-data  && apt-get clean && rm -rf /var/cache/apt
RUN wget https://github.com/opencv/opencv/archive/4.1.0.zip
RUN unzip 4.1.0.zip && rm -rf 4.1.0.zip && mv opencv-4.1.0 OpenCV && cd OpenCV && mkdir build && cd build && \
    cmake -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON -DWITH_GDAL=ON -DWITH_XINE=ON -DBUILD_EXAMPLES=ON -DENABLE_PRECOMPILED_HEADERS=OFF .. && \
    make -j16 && make install && ldconfig
RUN apt-get -y autoremove && apt-get -y autoclean
RUN rm -rf /var/cache/apt
RUN apt install -y python-socketio
RUN apt-get -o Dpkg::Options::="--force-confmiss" install -y --reinstall netbase
ADD ./requirements.txt /yolo/
RUN pip3 install -r /yolo/requirements.txt
WORKDIR /yolo/
RUN git clone https://gitlab.com/SothanaV/darknet.git && cd darknet && make
# RUN cd darknet && wget https://pjreddie.com/media/files/yolov2.weights
ADD ./yolov2.weights /yolo/darknet/yolov2.weights
ADD ./video_detection.py ./video_detection.py
ADD . /yolo/
WORKDIR /yolo/
#RUN usermod -a -G video developer
