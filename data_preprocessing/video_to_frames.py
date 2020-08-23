#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:12:29 2020

@author: pradyumnaojha
"""

import os
from pathlib import Path
import subprocess
import glob

class video_to_frames:
  def save_to_frames(self,video_file_with_path,fps=8):
    try:
      """Extract frames from video"""
      path_to_video, video_file_name = os.path.split(video_file_with_path)
      video_file_name = Path(video_file_with_path).stem
      frame_files_path = os.path.join(path_to_video,video_file_name)
      #frame_files_path = '"' + frame_files_path + '"'

      #print("Path till video frame dir = " + frame_files_path)

      if not os.path.exists(frame_files_path):
        os.mkdir(frame_files_path)

      #jpg_files = glob.glob(frame_files_path + "/" +'*.jpg')
      #if len(jpg_files) > 0 :
      #  return

      print("Extracting frames for video - " + video_file_with_path)
      query = "ffmpeg -i " + '"' + video_file_with_path +'"' + " -vf fps=" + str(fps) + " " + '"'+frame_files_path+'"'+ "/%06d.jpg"
        
      response =  subprocess.Popen(query, shell=True, stdout=subprocess.PIPE).stdout.read()
    except Exception as e:
      print(e)
