from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_resolution_stream = streams.get_highest_resolution()
        highest_resolution_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)
        
url = input("Enter the YouTube video URL: ")
save_path = filedialog.askdirectory()
save_path = save_path.replace("\\", "/")
url = f'"{url}"'
download_video(url, save_path)
