import os
import shutil

downloads = "/home/abdelrahman/Downloads"
music = "/home/abdelrahman/Music"
videos = "/home/abdelrahman/Videos"
pictures = "/home/abdelrahman/Pictures"
documents = "/home/abdelrahman/Documents"

file_types = {pictures: [".png", ".jpg", ".jpeg"]
              , documents: [".txt", ".pdf", ".docs", ".yaml"],
                music : [".wav", ".mp3"],
                 videos:[".mp4"]}

def access_files():
    files = os.listdir(downloads)

    for file in files:
        file_path = os.path.join(downloads, file)

        if not os.path.isfile(file_path):
            continue


        name, extension = os.path.splitext(file)

        for category, extensions in file_types.items():
            if extension.lower() in extensions:
                os.makedirs(category, exist_ok = True)
                shutil.move(file_path, category)
                break


def logging():

    return





def main():
    access_files()


if __name__ == "__main__":
    main()








