#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:12:29 2020

@author: pradyumnaojha
"""

import os
from pathlib import Path
import cv2

class video_to_frames:
    def save_to_frames(self,video_file_with_path):
        """Extract frames from video"""
        path_to_video, video_file_name = os.path.split(video_file_with_path)
        video_file_name = Path(video_file_with_path).stem
        
        frame_files_path = os.path.join(path_to_video,video_file_name)        
        if not os.path.exists(frame_files_path):
            os.mkdir(frame_files_path)
        
        vidcap = cv2.VideoCapture(video_file_with_path)
        video_length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
        print("video_length = ", video_length)
        count  = 0
        
        while vidcap.isOpened():
            # Extract the frame
            ret, frame = vidcap.read()
            # Write the results back to output location.
            file_name = str(count + 1)
            padded_file_name = file_name.zfill(6)            
            frame_path = os.path.join(frame_files_path,padded_file_name +".jpg")
            cv2.imwrite(frame_path, frame)      
            #print(frame_path)
            count = count + 1
            
            # If there are no more frames left
            if (count > (video_length-1)):
                
                # Release the feed
                vidcap.release()                
                break