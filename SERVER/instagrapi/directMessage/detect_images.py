# TODO : image를 download 한 후, Canary_YOLOv5 에서 detect.py 돌리기
# 처리 완료 했으면 이미지 삭제하기
from tqdm import tqdm
import argparse

IMAGE_DOWNLOAD_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/directMessage/images'
IMAGE_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/directMessage/images_detect_output'
WARNING_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/directMessage/warning'

import os

class detectArgs:
    input_image_path = ''
    output_image_path = ''
    weight_path = ''
    blur = False
    output_warning_path = ''

if __name__ == '__main__':
	if __package__ is None:
		import sys
		from os import path
		# print(path.dirname(path.dirname(path.dirname( path.dirname( path.abspath(__file__) ) )) ))
		sys.path.append(path.dirname(path.dirname(path.dirname( path.dirname( path.abspath(__file__) ) )) ))
		from AI.yolov5.detect import *
	else:
		from ......AI.yolov5 import detect

def makeDirectorySaveImages(userOutputPath):
    path = f'{IMAGE_OUTPUT_ROOT}/{userOutputPath}'
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print("Error : Creating directory " + path)
    return path

def makeDirectorySaveWarning(userOutputPath):
    path = f'{WARNING_OUTPUT_ROOT}/{userOutputPath}'
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print("Error : Creating directory " + path)
    return path

def detectWithCanary():
    testNeededUserList = os.listdir(f'{IMAGE_DOWNLOAD_ROOT}')
    testNeededUserNumber = len(testNeededUserList)

    for i in tqdm(range(0, testNeededUserNumber)):
        print("== User Number : %d ==" % i)
        makeDirectorySaveImages(testNeededUserList[i])
        makeDirectorySaveWarning(testNeededUserList[i])

        testNeededPhotoList = os.listdir(f'{IMAGE_DOWNLOAD_ROOT}/{testNeededUserList[i]}')
        testNeededPhotoNumber = len(testNeededPhotoList)

        for j in range(0, testNeededPhotoNumber):
            print("== Photo Number : %d ==" % j)
            parser = argparse.ArgumentParser()

            userPhotoPath = f'{testNeededUserList[i]}/{testNeededPhotoList[j]}'

            IMAGE_INPUT_PATH = f'{IMAGE_DOWNLOAD_ROOT}/{userPhotoPath}'
            IMAGE_OUTPUT_PATH = f'{IMAGE_OUTPUT_ROOT}/{userPhotoPath}'
            WARNING_OUTPUT_PATH = f'{WARNING_OUTPUT_ROOT}/{userPhotoPath}'+('.txt')

            args = detectArgs()
            args.input_image_path = f'{IMAGE_INPUT_PATH}'
            args.output_image_path = f'{IMAGE_OUTPUT_PATH}'
            args.weight_path = './weight/yolov5m6.pt'
            args.output_warning_path = f'{WARNING_OUTPUT_PATH}'

            detect(args)
                

def main():
    detectWithCanary()

main()