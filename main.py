import os
import shutil

files = os.listdir("test_files")
print("files:", files)

jpgs = []
mp3s = []
mp4s = []
lics = []
pptxs = []

os.makedirs("Images", exist_ok=True)
os.makedirs("music", exist_ok=True)
os.makedirs("videos", exist_ok=True)
os.makedirs("notes", exist_ok=True)
os.makedirs("presentations", exist_ok=True)


for file in files:
    name, extension = os.path.splitext(file)

    if extension == ".jpg":
        jpgs.append(file)
        shutil.move(f"test_files/{file}", "Images")

    elif extension == ".mp3":
        mp3s.append(file)
        shutil.move(f"test_files/{file}", "music")
    elif extension == ".mp4":
        mp4s.append(file)
        shutil.move(f"test_files/{file}", "videos")
    elif extension == ".lic":
        lics.append(file)
        shutil.move(f"test_files/{file}", "notes")
    elif extension == ".pptx":
        pptxs.append(file)
        shutil.move(f"test_files/{file}", "presentations")
    else:
        print("Unknown file type:", file)

    
print("JPG files:", jpgs)
print("MP3 files:", mp3s)
print("MP4 files:", mp4s)
print("LIC files:", lics)
print("PPTX files:", pptxs)
print("Total files:", len(files))




