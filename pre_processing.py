from perform_sdc import call_perform_sdc
from final_windows import Final
from colors import bcolors
from absl import app, flags, logging
from absl.flags import FLAGS
import scipy.io.wavfile as wav
import time
import sys
import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def check_social_distance(v_path, min_dist, wait_time_before, wait_time_between, out_frame, a_path, cam_distance):

	video_path = select_video(v_path)
	flags.DEFINE_string('video', video_path, 'path to input video')

	minimum_distance = get_minimum_distance(min_dist, cam_distance, out_frame)
	flags.DEFINE_float('minimum_distance', minimum_distance, 'time when execution starts')

	seconds = wait_to_play_warning(wait_time_before)
	flags.DEFINE_integer('seconds', seconds, 'time to wait before playing warning even if people are not maintaining social distance')

	waits = wait_between_warning(wait_time_between)
	flags.DEFINE_integer('waits', waits, 'time to wait between playing warning when need to play in loop')

	frame_size = refine_frame_size(out_frame)
	flags.DEFINE_integer('frame_size', frame_size, 'output frame size/quality of video to display')

	soundfile = select_audio(a_path)
	flags.DEFINE_string('sound_file', soundfile , 'path to warning/message audio file')

	# #Get length of audio file
	(source_rate, source_sig) = wav.read(soundfile)
	audio_file_length = len(source_sig) / float(source_rate)
	flags.DEFINE_float('audio_file_length', audio_file_length, 'warning/message audio file length')

	target_distance = get_target_distance(cam_distance)
	flags.DEFINE_integer('target_distance', target_distance, 'distance betweeen ')

	call_perform_sdc()


######################################### 
#		     Select the video 			#
#########################################
def select_video(video_name):
	if video_name == "":
		video_p="./input_video/New_Demo_Full_HD.mp4" 
	elif video_name == "WebCam":
		video_p = "0"
	else :
		video_p = video_name
	return video_p

######################################### 
#		    Minimal distance			#
#########################################
def get_minimum_distance(min, dist, fs):
	min_value = float(min.split(" ")[0])
	d = int(dist)
	frame_w = int(fs.split(" ")[0])
	minimum = (min_value*d* frame_w)/(d*(5+d))
	return minimum

######################################### 
#		    Time to wait			#
#########################################
def wait_to_play_warning(sec):
	#Take input for how many seconds do you want to wait when two people are close enough
	seconds = int(sec.split(" ")[0])
	return seconds

######################################### 
#		    Wait between Warning		#
#########################################
def wait_between_warning(secs):
	#Take input for how many seconds do you want to wait after playing warning.
	wait = int(secs.split(" ")[0])
	return wait

######################################### 
#		    Output Frame Size		#
#########################################
def refine_frame_size(size):
	#Take input for how many seconds do you want to wait after playing warning.
	frame_wide = int(size.split(" ")[0])
	return frame_wide

######################################### 
#		    Select Audio File		#
#########################################
def select_audio(audio):
	#Take input for how many seconds do you want to wait after playing warning.
	if audio == "":
		sound = "./sound/social_distance.wav"
	else:
		sound = audio
	return sound
	
######################################### 
#		    Camera Target Distance		#
#########################################
def get_target_distance(distance):
	#Take input for how many seconds do you want to wait after playing warning.
	dist = int(distance)
	return dist

# ######################################### 
# #		     Select the model 			#
# #########################################
# def get_model():
# 	try:
# 		model_path="../models/faster_rcnn_inception_v2_coco_2018_01_28/frozen_inference_graph.pb" 

# 		print(bcolors.WARNING + " [ Loading the TENSORFLOW MODEL ... ]"+bcolors.ENDC)
# 		m = Model(model_path)
# 		print(bcolors.OKGREEN +"Done : [ Model loaded and initialized ] ..."+bcolors.ENDC)
# 		return m
# 	except:
# 		Final("Model load Failed","Please check your model file and folder.")
# 		sys.exit(0)