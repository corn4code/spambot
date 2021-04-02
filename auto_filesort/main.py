from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            if filename.endswith("png"):
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)
            if filename.endswith("bmp"):
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)
            if filename.endswith("jpg"):
                new_destination = folder_destination + "/" + filename
            if filename.endswith("jpeg"):
                new_destination = folder_destination + "/" + filename
            if filename.endswith("gif"):
                new_destination = folder_destination + "/" + filename


folder_to_track = 'D:/Downloads'
folder_destination = 'D:/Pictures/Downloads'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
