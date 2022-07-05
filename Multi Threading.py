import time
import logging
import threading
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# initialization
event_handler = LoggingEventHandler()
observer = Observer()

folder1 = r"C:\Users\Anu\Triassic solutions\watching program\folder1"
folder2 = r"C:\Users\Anu\Triassic solutions\watching program\folder2"


def monitor_folder(folder):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(message)s', datefmt='%Y-%m-%d %H:%H:%S')
    observer.schedule(event_handler, folder, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)  # set sleep time
    except KeyboardInterrupt:
        observer.stop()
        observer.join()


t = threading.Thread(target=monitor_folder, args=(folder1,))
t1 = threading.Thread(target=monitor_folder, args=(folder2,))
t.start()
t1.start()
t.join()
t1.join()
