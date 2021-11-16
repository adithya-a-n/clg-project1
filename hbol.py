import os
from typing import DefaultDict

print("\nHBO DL Script by xblaze")
print("Required files :mkvmerge.exe, mp4decrypt.exe, aria2c.exe,subtitle edit\n")



mp4decrypt = "./Bento4-SDK-1-6-0-639.x86_64-unknown-linux/bin/mp4decrypt"
mkvmerge = "./mkvmerge"

filename = input("Enter the output file name (no spaces) : ")


vid_url = input("\nEnter Video URL:")
audio_url = input("\nEnter Audio URL: ")
sub_url = input("\nEnter Subtitle URL: ")
os.system(f'aria2c -o encrypted.mp4 {vid_url}')
os.system(f'aria2c -o encrypted.m4a {audio_url}')
os.system(f'aria2c -o {filename}.vtt {sub_url}')




with open("key.txt", 'r') as f:
    file = f.readlines()

length = len(file)

keys = ""
for i in range(0, length):
    key = file[i][60 : 92]
    kid = file[i][98 : 130]

    keys += f'--key {kid}:{key} '

print("\nDecrypting Audio.....")
print("\n ")
os.system(f'{mp4decrypt} {keys} encrypted.m4a decrypted.m4a')
print("\nFinished Decrypting Audio.....")
os.remove("encrypted.m4a")
print("\n ")

print("\nDecrypting Video.....")
print("\n ")
os.system(f'{mp4decrypt} {keys} encrypted.mp4 decrypted.mp4')
print("\nFinished Decrypting Video.....")
os.remove("encrypted.mp4")
print("\n ")
print("Merging .....")
os.system(f'{mkvmerge} -o {filename}.mkv C:\web_rip\decrypted.mp4 C:\web_rip\decrypted.m4a {filename}.vtt')
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