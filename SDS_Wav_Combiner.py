#!usr/local/bin/python

#Dependencies:
#pydub - pip install pydub
#ffmpeg - Copy ffmpeg to same directory as Python script

import os
import glob
from pydub import AudioSegment

#File format for export file (mp3, wav, aif, ogg, or raw)
export_format = "wav"

#Path to folder containing subfolders with wav files
path = r"C:\temp"

#Get subfolder names
subfolders = [f.path for f in os.scandir(path) if f.is_dir()]

#Loop through each subfolder
for subfolder in subfolders:

    wav_files =[]
    audio_output = AudioSegment.empty()

    #Get wav files in folder
    filenames = glob.glob(subfolder + r'\*.wav')

    #Add wav file names to list
    for filename in filenames:
        wav_file = AudioSegment.from_wav(filename)
        wav_files.extend([wav_file])
    #Add all segments 
    for file_name in wav_files:
        audio_output += file_name
    #Print new audio file name
    print("Creating file: " + subfolder + "." + export_format)
    #Use folder name for filename of new audio file  
    audio_output.export(subfolder + "." + export_format, format= export_format)
   
        
