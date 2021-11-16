import os
import time
from typing import DefaultDict

print("\nHBO DL Script by xblaze")
print("Merge ")


mp4decrypt = "./Bento4-SDK-1-6-0-639.x86_64-unknown-linux/bin/mp4decrypt"
mkvmerge = "./mkvmerge"

filename = input("Enter the output file name (no spaces): ")
video_1=input("Enter the Path for the video Stream: ")
audio_1=input("Enter the Path for the video Stream: ")

sub_url = input("\nEnter Subtitle URL: ")

os.system(f'aria2c -o {filename}.vtt {sub_url}')


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
os.system(f'{mp4decrypt} {keys} {video_1} decrypted.m4a')
os.system(f'{mp4decrypt} {keys} {audio_1} decrypted.mp4')
end = time.time()
print(f"Time Taken For Decryption: {(end - begin)/60} mins")

print("Merging .....")
os.system(f'{mkvmerge} -o /content/drive/Shareddrives/blaze/test/{filename}.mkv decrypted.mp4 decrypted.m4a {filename}.vtt')
print("\nAll Done .....")

print("\nDo you want to delete the Encrypted Files : Press 1 for yes , 2 for no")
delete_choice = int(input("Enter Response : "))

if delete_choice == 1:
    os.remove("encrypted.m4a")
    os.remove("encrypted.mp4")
    os.remove("C:\web_rip\decrypted.m4a")
    os.remove("C:\web_rip\decrypted.mp4")
    
else:
    quit()