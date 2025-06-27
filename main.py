import os
import shutil

downloads = "/home/abdelrahman/Downloads"
music = "/home/abdelrahman/Music"
Videos = "/home/abdelrahman/Videos"
Pictures = "/home/abdelrahman/Pictures"
Documents = "/home/abdelrahman/Documents"
files = os.listdir(downloads)

file_types = {Pictures: [".png", ".jpg", ".jpeg"]
              , Documents: [".txt", ".pdf", ".docs", ".yaml"],
                music : [".wav", ".mp3"],
                 Videos:[".mp4"]}

print(files)

for file in files:
    name, extension = os.path.splitext(file)
    file_path = os.path.join(downloads, file)
    print(extension)

    for category, extensions in file_types.items():
        if extension.lower() in extensions:
            shutil.move(file_path, category)
           


