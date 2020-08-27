# -*- coding: utf-8 -*-
import json
import os
from pathlib import Path
import shutil
import glob

from video_mp4_to_audio_mp3 import video_mp4_to_audio_mp3_converter
from video_to_frames import video_to_frames

def main(task):
    json_file_path = './MUSIC_dataset/'
    data_folder_path = '../data/'
    for file in os.listdir(json_file_path):
        if file.endswith('.json'):
            file_path =  os.path.join(json_file_path,file)
            #print(file_path)
            json_data = json.load(open(file_path))

            for currVideos in json_data['videos']:
                #print(currVideos)

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
                        #full_video_file_path = '"' + full_video_file_path + '"'
                        if os.path.exists(full_video_file_path):
                          #print(full_video_file_path)
                          video_frames.save_to_frames(full_video_file_path,8)
                        else:
                          print("video file does not exist - " + full_video_file_path)
                          video_file_with_path = full_video_file_path
                          path_to_video, video_file_name = os.path.split(video_file_with_path)
                          video_file_name = Path(video_file_with_path).stem
                          frame_files_path = os.path.join(path_to_video,video_file_name)

                          if os.path.exists(frame_files_path):
                            jpg_files = glob.glob(frame_files_path + "/" +'*.jpg')
                            if not len(jpg_files) > 0:
                              os.rmdir(frame_files_path)
                if task =="convert_video_mp4_to_audio_mp3":
                  audio_mp3_converter = video_mp4_to_audio_mp3_converter()
                  video_directory = data_folder_path + 'frames/' + currVideos + '/'
                  audio_directory = data_folder_path + 'audio/'  + currVideos + '/'
                  for videoID in json_data['videos'][currVideos]:
                    full_video_file_path = os.path.join(video_directory,videoID+".mp4")
                    if os.path.exists(full_video_file_path):
                      audio_mp3_converter.save_to_audio_mp3(audio_directory, full_video_file_path)

if __name__ == "__main__":
    #task = "youtube_download"
    task = "convert_video_to_frame"
    #task = "convert_video_mp4_to_audio_mp3"

    main(task)

