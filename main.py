import os

downloads = "/home/abdelrahman/Downloads"
music = "~/Music"
Videos = "~/Videos"
Pictures = "~/Pictures"
Documents = "~/Documents"
file = "/home/abdelrahman/Downloads/CLASSIFIED.yaml"
files = os.listdir(downloads)

print(files)

for file in files:
    parts = os.path.splitext(file)
    print(parts)

    if parts[1] == ".yaml"  or ".txt":
        print("this is a text file")


