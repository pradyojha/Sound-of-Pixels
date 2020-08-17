# -*- coding: utf-8 -*-
import json
import os

from youtube_video_downloader import youtube_video_downloader
from video_to_frames import video_to_frames

def main(task):
    json_file_path = './MUSIC_dataset/'
    data_folder_path = '../data/'
    
    for file in os.listdir(json_file_path):
        if file.endswith('.json'):
            file_path =  os.path.join(json_file_path,file)
            print(file_path)      
            
            json_data = json.load(open(file_path))
            
            for currVideos in json_data['videos']:
                print(currVideos)
                
                if task == "youtube_download":
                    downloader = youtube_video_downloader()
                    video_directory = data_folder_path + 'frames/' + currVideos + '/'
                    audio_directory = data_folder_path + 'audio/'  + currVideos + '/'
                
                    for videoID in json_data['videos'][currVideos]:
                        print(videoID)                
                        downloader.saveYoutubeVideos(video_directory,audio_directory,videoID)
                
                
                if task == "convert_video_to_frame":
                    video_frames = video_to_frames()
                    video_directory = data_folder_path + 'frames/' + currVideos + '/'
                    for videoID in json_data['videos'][currVideos]:                        
                        full_video_file_path = os.path.join(video_directory,videoID+".mp4")
                        print(full_video_file_path)
                        video_frames.save_to_frames(full_video_file_path)
                        
                    
                    
        

if __name__ == "__main__":  
    #task = "youtube_download"
    task = "convert_video_to_frame"
    
    main(task)
    
  