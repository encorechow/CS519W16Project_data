#!/usr/bin/env python

##################################
# configuration

# select which group of ground truth to use
group = 1 # 0 ~ 4

source_path_gdt = './BSDS500/data/groundTruth/'
target_path_gdt = './BSDS500_BD/groundTruth/'

source_path_img = './BSDS500/data/images/'
target_path_img = './BSDS500_BD/images/'

##################################

import os
import numpy as np
import scipy.io as sio
from scipy import misc
from PIL import Image

def grab_groundtruth(filename):
	return sio.loadmat(filename)['groundTruth'][0,group]['Boundaries'][0,0] 

def convert_groundtruth(folderName):
	spath = source_path_gdt + folderName + '/'
	tPath = target_path_gdt + folderName + '/'

	if not os.path.exists(tPath):
		os.makedirs(tPath)

	counter = 0
	for file in os.listdir(spath):
		if file.endswith('.mat'):
			gt = grab_groundtruth(spath+file)
			img = Image.fromarray(np.uint8(gt)*255)
			#if img.size[0] > img.size[1]:
				#img = img.rotate(90,expand=True)
				
			img.save(tPath+str(file)[0:-4]+'.png', 'PNG')
			counter += 1
			#print str(file)[0:-4]
	return counter

def convert_images(folderName):
	spath = source_path_img + folderName + '/'
	tPath = target_path_img + folderName + '/'

	if not os.path.exists(tPath):
		os.makedirs(tPath)

	counter = 0
	for file in os.listdir(spath):
		if file.endswith('.jpg'):
			img = Image.open(spath+file)

			#if img.size[0] > img.size[1]:
				#img = img.rotate(90,expand=True)

			img.save(tPath+str(file)[0:-4]+'.jpg', 'JPEG')
			counter += 1

	return counter


if __name__ == '__main__':
	print 'converting ground truth ...'
	num_Y_train = convert_groundtruth('train')
	num_Y_val  	= convert_groundtruth('val')
	num_Y_test 	= convert_groundtruth('test')

	num_X_train = convert_images('train')
	num_X_val  	= convert_images('val')
	num_X_test 	= convert_images('test')

