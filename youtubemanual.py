from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_vedio(url, save_path):
    try:
        yt = YouTube(url)
        strems = yt.streams.filter(progressive=True,file_extension="mp4")
        higest_resolution_stream = strems.get_highest_resolution()
        higest_resolution_stream.download(output_path=save_path)
        print("Video downloaded sucessfully!")
    except Exception as e:
        print(e)


url="https://youtu.be/XNvC3IbPN44?si=hvkn8zgdpw7fcgjE"
save_path="C:\Users\HP\OneDrive\Desktop\dsa".replace("\\", "/")