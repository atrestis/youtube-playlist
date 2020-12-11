import os
import subprocess

from pytube import Playlist, YouTube

def run(pl):
    savepath = os.path.abspath(os.getcwd())
    
    for s in pl.videos:
        #s.streams.first()
        default_filename = s.title 
        default_filename = default_filename.replace('"', '')
        default_filename = default_filename.replace(',', '')
        default_filename = default_filename.replace(':', '')
        default_filename = default_filename.replace('.', '')
        default_filename = default_filename + ".mp4"
        print("Downloading " + default_filename + "...")
        # downloads first audio stream
        s.streams.first().download()
        
        #creates mp3 filename for downloaded file
        
        new_filename = default_filename[0:-3] + "mp3"
        print("Converting to mp3: " + new_filename)
        
        #converts mp4 audio to mp3 audio
        subprocess.run(['ffmpeg', '-i', default_filename, new_filename])
    print("Download finished.")


if __name__=="__main__":
    url = 'https://www.youtube.com/playlist?list=PLvN9mssJtx72axhkRg0D36ilAlMf1d6AL'
    #url = 'https://www.youtube.com/playlist?list=PLvN9mssJtx727zUgggU25JByhs46cqpnV'
    pl  = Playlist(url)
    run(pl)
