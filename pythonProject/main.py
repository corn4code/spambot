from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import os.path
import json
import time

# unpacking the tuple
folder_to_track = "D:/Downloads"
class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            file_name, file_extension = os.path.splitext(src)

            if file_extension == ".bmp":
                new_destination = folder_destination_pics

folder_destination_pics = "D:Pictures/Download"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

