#!/usr/bin/env python3

import os
import shutil
import logging
from datetime import datetime

class FileOrganizer:
    def __init__(self, source_dir, log_file):
        self.source_dir = source_dir
        self.log_file = log_file
        self.file_types = {
            "Pictures": [".png", ".jpg", ".jpeg", ".gif", ".svg", ".bmp", ".heic"],
            "Documents": [".txt", ".pdf", ".docx", ".doc", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".csv", ".yaml", ".json"],
            "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
            "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
            "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
            "Scripts": [".py", ".js", ".sh", ".bat", ".html", ".css", ".cpp", ".cs", ".c"],
            "Other": [] 
        }
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(filename=self.log_file, level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def organize_files(self):
        try:
            files = os.listdir(self.source_dir)
        except FileNotFoundError:
            logging.error(f"Source directory not found: {self.source_dir}")
            print(f"Error: Source directory not found at {self.source_dir}")
            return

        for file in files:
            source_path = os.path.join(self.source_dir, file)
            if not os.path.isfile(source_path):
                continue

            try:
                self._organize_file(file, source_path)
            except Exception as e:
                logging.error(f"Failed to process file {file}: {e}")
                print(f"Error processing {file}: {e}")

    def _organize_file(self, file, source_path):
        _, extension = os.path.splitext(file)
        extension = extension.lower()

        destination_category = "Other"
        for category, extensions in self.file_types.items():
            if extension in extensions:
                destination_category = category
                break
        
        # Get file modification time for date-based subdirectories
        mod_time = os.path.getmtime(source_path)
        date = datetime.fromtimestamp(mod_time)
        year = str(date.year)
        month = date.strftime('%m')

        # Construct destination directory
        home = os.path.expanduser("~")
        destination_dir = os.path.join(home, destination_category, year, month)
        
        os.makedirs(destination_dir, exist_ok=True)
        
        destination_path = os.path.join(destination_dir, file)

        # Move the file
        shutil.move(source_path, destination_path)
        
        log_message = f"Moved '{file}' to '{destination_path}'"
        logging.info(log_message)
        print(log_message)


def main():
    # --- Configuration ---
    source_directory = os.path.join(os.path.expanduser("~"), "Downloads")
    log_file_path = os.path.join(os.path.expanduser("~"), "Documents", "file_organizer.log")
    
    organizer = FileOrganizer(source_dir=source_directory, log_file=log_file_path)
    organizer.organize_files()


if __name__ == "__main__":
    main()








