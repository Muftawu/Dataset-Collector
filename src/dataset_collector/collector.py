"""
Dataset Collector Module
Uses "cv2" Package
By: Yiwere Muftawu Mohammed
Github: https://www.github.com/Muftawu
"""

import cv2
import os 
import time 
import typing
from src.dataset_collector.file_ops import copy_folder, delete_folder
from src.dataset_collector.loggings import warning_error, warning_info, warning_success
import sys 

class Collector:

    """
    Quickly collect data for your machine learning projects.
    Support images and videos through a connected camera/webcam.
    """

    def __init__(self, dst:None, cap_object:0):

        """
        Initialize the Collector object.

        :param dst: output directory to store collected data
        """
        self.dst = dst 
        self.cap_object = cap_object
        self.temp_dir = "temp"
        self.img_count = 0

        if self.dst is None:
            warning_error("No output directory specified. Please provide an output directory for your captures.")

        if os.path.isdir(self.temp_dir):
            delete_folder(self.temp_dir)

        if os.path.isdir(self.dst):
            warning_info(f"'{self.dst}' already exists. Do you want to continue. (y/n) or Press any key to quit ")
            res = input()
            if res == 'y':
                os.mkdir(self.temp_dir)
                self.img_count = copy_folder(self.dst, self.temp_dir)
            elif res == 'n':
                warning_info("Enter folder name for new directory: ")
                dir_name = input()
                self.dst = dir_name
            else:
                sys.exit()
        
        delete_folder(self.dst)
        os.mkdir(self.dst)
        
    def collect_images(self, n_imgs:int|None, img_frmt, frame_delay: typing.Union[int, float]):
        """
        Collect data as images from a webcam or camera
        
        :param n_imgs: Number of images to capture
        :param img_frmt: Format to store images - ['jpg', 'png, 'jpeg']
        :param frame_delay: Seconds to wait between frame captures - [1s, 2s, 3s, ...]. Use higher values to avoid blurryness between captures

        :return: Output directory containing captured images
        """
        
        if n_imgs is None:
            warning_error("n_imgs not specified. Please specify how many images to capture")
        
        assert isinstance(n_imgs, int), warning_error("n_imgs must be an integer")
        
        cap = cv2.VideoCapture(self.cap_object)

        for i in range(self.img_count, n_imgs+self.img_count):
            _, frame = cap.read()
            captured = cv2.imwrite(f'{self.dst}/img_{i}.{img_frmt}', frame)
            if captured:
                print(f"Saved image {i}.{img_frmt} to {self.dst}...")
            time.sleep(frame_delay)
            
        copy_folder(self.temp_dir, self.dst)
        delete_folder(self.temp_dir)
        warning_success("✅..FINISHED..✅")


    def collect_videos(self):
        """
        Collect data as video
        
        :return 
        To be implemented Soon
        """        


'''
EXAMPLE CODE TO COLLECT IMAGES

# import 'Collector' class
from Collector import Collector

# create collector instance 
mycollector = Collector('folder_name', 0)

# pass arguments 
    - collect 5 images
    - 'jpg' image format 
    - 1s delay

mycollector.collect_images(5, 'jpg', 1)

this create a new folder 'folder_name' and stores the captured images in there

'''