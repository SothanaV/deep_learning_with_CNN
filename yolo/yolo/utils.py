import cv2
import threading
import os
import math
import random
import base64
from ctypes import *
from  random import randint
class VideoCamera(object):
    def __init__(self, camera, alert_classes):
        # Open a camera
        self.cap = cv2.VideoCapture(camera)
      
        # Initialize video recording environment
        self.is_record = False
        self.out = None

        # Thread for recording
        self.recording_thread = None
        self.alert_classes = set(alert_classes)
        self.colors = {}
    
    def __del__(self):
        self.cap.release()
    
    def get_frame(self, byte=False):
        ret, frame = self.cap.read()

        if not ret:
            return None

        if byte:
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        else:
            return frame

    def draw_yolo(self, detected_objects):
        frame = self.get_frame(False)
        is_detected_alert_class = False

        for obj, confidence, rect in detected_objects:
            x, y, w, h = rect
            w, h = round(w), round(h)
            x1, y1 = int(x-w/2), int(y-h/2)
            x2, y2 = x1+w, y1+h
            detected_class = obj.decode('utf-8')
            color = None
            if detected_class in self.colors:
                color = self.colors[detected_class]
            else:
                color = (randint(0,200),randint(0,200),randint(0,200))
                self.colors[detected_class] = color
            # color = (255,255,255)
            text = '{} {}%'.format(detected_class, round(confidence*100))
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            frame = cv2.putText(frame, text, (x1, y1), cv2.FONT_HERSHEY_DUPLEX, 0.8, color, lineType=cv2.LINE_AA)

        frame = cv2.resize(frame, (360, 270))
        ret, jpeg = cv2.imencode('.jpg', frame)

        jpeg_bytes = jpeg.tobytes()

        return base64.b64encode(jpeg_bytes)