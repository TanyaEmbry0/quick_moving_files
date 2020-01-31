import os 
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def modi(self, event):
        for fileName in os.listdir(first_folder):
            src = first_folder + "/" + fileName
            finall_destination = new_folder + "/" + fileName
            os.rename(src, finall_destination)

            
first_folder = "D:/Users/Embryo/Desktop/myFolder"
new_folder = "D:/Users/Embryo/Desktop/newFolder"
handler_event = MyHandler()
observer = Observer()
observer.schedule(handler_event, first_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()


        
