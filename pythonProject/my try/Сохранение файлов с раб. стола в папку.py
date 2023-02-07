from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extention = filename.split('.')
            if len(extention) > 1 and (extention[1].lower() == 'jpg' or extention[1].lower() == 'png' or extention[1].lower() == 'svg'):
                file = folder_track + '/' + filename
                new_path = folder_dest + '/' + filename
                os.rename(file, new_path)

folder_track = '/Users/Admin/Desktop'
folder_dest = '/Users/Admin/Desktop/Обои'

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()