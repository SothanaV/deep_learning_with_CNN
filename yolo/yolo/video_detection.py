import socketio
from utils import VideoCamera
from darknet.python import darknet as dn
from darknet.python.darknet import detect

sio = socketio.Client()
sio.connect('http://socket:5000')
video_camera = None

weights = 'darknet/yolov2.weights'
netcfg  = 'darknet/cfg/yolov2.cfg'
data = 'darknet/cfg/coco.data'

net  = dn.load_net(netcfg.encode('utf-8'), weights.encode('utf-8'), 0)
meta = dn.load_meta(data.encode('utf-8'))

camera = 0 # RTSP IP For ip-cam OR 0 For Default video-cam

def video_stream():
    global video_camera, net, meta
    alert_classes = [] # target classes

    if video_camera == None:
        video_camera = VideoCamera(camera=camera, alert_classes=alert_classes)
        
    while True:
        img = video_camera.get_frame(byte=False)
        if img is not None:
            detected_objects = detect(net, meta, img, thresh=.30)
            frame = video_camera.draw_yolo(detected_objects=detected_objects)
            # print(frame)
            sio.emit('image', {
                'image': frame,
                })
            # sio.emit('image',frame)

if __name__ == '__main__':
    video_stream()
