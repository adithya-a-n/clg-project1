import os
import time
from typing import DefaultDict

print("\nHBO DL Script by xblaze")
print("Merge ")

SubtitleEditexe="E:\webdl\SubtitleEdit\SubtitleEdit.exe"
mp4decrypt="utils\mp4decrypt.exe"
aria2c=" utils\\aria2c.exe"
mkvmerge="utils\mkvmerge"

filename = input("Enter the output file name (no spaces) : ")
sub_url = input("\nEnter Subtitle URL: ")

os.system(f'{aria2c} -o {filename}.vtt {sub_url}')
os.system(f'{SubtitleEditexe} /convert {filename}.vtt srt')

with open("key.txt", 'r') as f:
    file = f.readlines()

length = len(file)

keys = ""
for i in range(0, length):
    key = file[i][60 : 92]
    kid = file[i][98 : 130]

    keys += f'--key {kid}:{key} '

print("\nDecrypting .....")
begin = time.time()
os.system(f'{mp4decrypt} {keys} encrypted.m4a C:\web_rip\decrypted.m4a')
os.system(f'{mp4decrypt} {keys} encrypted.mp4 C:\web_rip\decrypted.mp4')
end = time.time()
print(f"Time Taken For Decryption: {(end - begin)/60} mins")

print("Merging .....")
os.system(f'{mkvmerge} -o {filename}.mkv C:\web_rip\decrypted.mp4 C:\web_rip\decrypted.m4a {filename}.srt')
print("\nAll Done .....")

print("\nDo you want to delete the Encrypted Files : Press 1 for yes , 2 for no")
delete_choice = int(input("Enter Response : "))

if delete_choice == 1:
    os.remove("encrypted.m4a")
    os.remove("encrypted.mp4")
    os.remove("C:\web_rip\decrypted.m4a")
    os.remove("C:\web_rip\decrypted.mp4")
    os.remove(filename},".vtt")
    os.remove(filename},".srt")
else:
    quit()