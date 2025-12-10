import os
import shutil

#get the folder path
neo=(input("Enter the folder you want to organize ; "))

#get into that folder
os.chdir(neo)

#creating folders for different roots

if not os.path.exists("images"):
    os.mkdir("images")
if not os.path.exists("Docs"):
    os.mkdir("Docs")
if not os.path.exists("vids"):
    os.mkdir("vids")
if not os.path.exists("musics"):
    os.mkdir("musics")
if not os.path.exists("others"):
    os.mkdir("others")

# List all files
for item in os.listdir():
    #only select files
    if os.path.isfile(item):
        #move accordingly
        if item.endswith((".jpeg", ".png", ".jpg", ".gif")):
            shutil.move(item, "images/" + item)
        elif item.endswith((".pdf", ".txt", ".docx", ".pptx")):
            shutil.move(item, "Docs/" + item)
        elif item.endswith((".mp4", ".mkv", ".mov" )):
            shutil.move(item, "vids/" + item)
        elif item.endswith((".mp3", ".wav", ".aac" )):
            shutil.move(item, "musics/" + item)  
        else:
            shutil.move(item, "others/" + item) 

print("All files organized successfully")
