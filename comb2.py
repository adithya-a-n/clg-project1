
import os
import time
from typing import DefaultDict

print("\nVideo Rip Script")

filename = input("Enter the output file name (no spaces) : ")
mpdurl = input("Enter MPD URL : ")

os.system(f'yt-dlp --external-downloader aria2c --allow-unplayable-formats --no-check-certificate -F "{mpdurl}"')

vid_id = input("\nEnter Video ID : ")
audio_id = input("Enter Audio ID : ")
os.system(f'yt-dlp --external-downloader aria2c --allow-unplayable-formats --no-check-certificate -f {vid_id}+{audio_id} "{mpdurl}"')

os.system("ren *.mp4 encrypted.mp4")
os.system("ren *.m4a encrypted.m4a")

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
os.system(f'mp4decrypt.exe {keys} encrypted.m4a C:\web_rip\decrypted.m4a')
os.system(f'mp4decrypt.exe {keys} encrypted.mp4 C:\web_rip\decrypted.mp4')
end = time.time()
print(f"Time Taken For Decryption: {end - begin}")

print("Merging .....")
os.system(f'mkvmerge.exe -o {filename}.mkv C:\web_rip\decrypted.mp4 C:\web_rip\decrypted.m4a')
print("\nAll Done .....")

print("\nDo you want to delete the Encrypted Files : Press 1 for yes , 2 for no")
delete_choice = int(input("Enter Response : "))

if delete_choice == 1:
    os.remove("encrypted.m4a")
    os.remove("encrypted.mp4")
    os.remove("decrypted.m4a")
    os.remove("decrypted.mp4")
else:
    quit()