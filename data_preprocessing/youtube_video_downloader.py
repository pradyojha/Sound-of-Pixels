#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 20:08:52 2020

@author: pradyumnaojha
"""
from pytube import YouTube

class youtube_video_downloader:         
    
    def saveYoutubeVideos(self, output_video_path,output_audio_path, videoID):
        try:
            #link of the video to be downloaded 
            link="https://www.youtube.com/watch?v=" + videoID
            video = YouTube(link)
            video.streams.get_by_itag(18).download(output_video_path,videoID)
            video.streams.get_by_itag(140).download(output_audio_path,videoID)
        except Exception as e:
            print(str(e))
            
        print('\n Task Completed!')