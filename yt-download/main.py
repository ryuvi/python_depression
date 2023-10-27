import argparse
from pytube import Playlist, YouTube
import customtkinter as ctk

class Layout(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('800x600')
        self.title('Youtube Downloader')
        
        label = ctk.CTkLabel(self, text='Youtube Downloader')
        label.pack(padx=10, pady=10, expand=True, fill='both')
        
        self.link = ctk.StringVar()
        entry = ctk.CTkEntry(self, textvariable=self.link, placeholder_text='Insert the link')
        entry.pack(padx=10, pady=10, expand=True, fill='both')
        
        self.tipo = ctk.IntVar(value=0)
        playlist = ctk.CTkRadioButton(self, text='Playlist', textvariable=self.tipo, value=0)
        playlist.pack(padx=10, pady=10, expand=True, fill='both')
        
        video = ctk.CTkRadioButton(self, text='Video Only', textvariable=self.tipo, value=1)
        video.pack(padx=10, pady=10, expand=True, fill='both')
        
        download = ctk.CTkButton(self, text='Download', command=self.download)
        download.pack(padx=10, pady=10, expand=True, fill='both')

    def download(self):
        if self.tipo.get() == 0:
            playlist = Playlist(self.link.get())
            for i in playlist.videos:
                i.streams.filter(only_audio=True, file_extension='mp4').first().download()
        else:
            video = YouTube(self.link.get())
            video.streams.filter(only_audio=True, file_extension='mp4').first().download()
        
    def run(self):
        self.mainloop()

AUDIO_DOWNLOAD_DIR = "audio"

if __name__ == "__main__":
    l = Layout()
    l.run()