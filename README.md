# SDS_Wav_Combiner

#### Dependencies
* pydub (pip install pydub)
* ffmpeg (https://www.ffmpeg.org/download.html)

Change path variable to the location of the subfolders containing the wav files.  The script will generate one wav file from the multiple wav files in each subfolder.  The single wav file will be saved to the path variable location using the subfolder name.

#### Example
path = r"C:\temp"

Script will iterate through the first level of subfolders in C:\temp and create a single wav file for all the wav files found in each subfolder.

C:\temp\EARKF  
C:\temp\LKJID  
C:\temp\UYTEJ  
...  

Output  
C:\temp\EARKF.wav  
C:\temp\LKJID.wav  
C:\temp\UYTEJ.wav  
... 
