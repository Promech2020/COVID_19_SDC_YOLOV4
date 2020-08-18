from helping_functions import image_resize, create_blank, get_human_box_detection, get_centroids, get_points_from_box, rescale_image
# from final_windows import Final
# from vidgear.gears import CamGear
# from playsound import playsound
# import sounddevice as sd
# import soundfile as sf
import numpy as np
import itertools
import threading
# import imutils
import time
import math
# import yaml
import cv2
import sys
import os
from frame_by_frame import call_frame_by_frame

video_path = input("Enter path to the video file: ")
vs = cv2.VideoCapture(video_path)
# Loop until the end of the video stream
while True:	
	(frame_exist, frame) = vs.read()
	if frame is None:
		break
	else:
		frame = image_resize(frame, width = 720)
		call_frame_by_frame(frame)

