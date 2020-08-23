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

class video_mp4_to_audio_mp3_converter:
  def save_to_audio_mp3(self, audio_path, video_file_with_path):
    try:
      """Extract audio from video mp4"""
      path_to_video, video_file_name = os.path.split(video_file_with_path)
      audio_file_name = Path(video_file_with_path).stem
      audio_file_path = os.path.join(audio_path,audio_file_name)  + ".mp3"
      print("Path till audio mp3 file = " + audio_file_path)
      print("video file path = " + video_file_with_path)
      

      query = "ffmpeg -i " + '"' + video_file_with_path +'"' + " -b:a 192K  " + '"'+ audio_file_path +'"' 
      response =  subprocess.Popen(query, shell=True, stdout=subprocess.PIPE).stdout.read()
    except Exception as e:
      print(e)
