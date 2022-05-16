import urllib.request
import time
import random
from concurrent.futures import *
from multiprocessing import *
from threading import *

task_id = [i for i in range(1, 21)]


def get_data(task_id):
    print(f"processing get_data({task_id})")
    time.sleep(random.randint(1, 3))
    print(f"completed get_data({task_id})")


def write_to_file(task_id):
    print(f"processing write_to_file({task_id})")
    time.sleep(random.randint(1, 5))
    print(f"completed write_to_file({task_id})")


def write_to_console(task_id):
    print(f"processing write_to_console({task_id})")
    time.sleep(random.randint(1, 5))
    print(f"completed write_to_console({task_id})")


with ThreadPoolExecutor(10) as executor:
    results1 = executor.map(get_data, task_id)

to_file1 = Thread(target=write_to_file, args=task_id)
to_file2 = Thread(target=write_to_file, args=task_id)
to_file3 = Thread(target=write_to_file, args=task_id)
to_file4 = Thread(target=write_to_file, args=task_id)
to_file5 = Thread(target=write_to_file, args=task_id)

thr_console1 = Thread(target=write_to_console, args=task_id)

thr_file1.start()
thr_file2.start()
thr_file3.start()
thr_file4.start()
thr_file5.start()

thr_console1.start()

thr_file1.join()
thr_file2.join()
thr_file3.join()
thr_file4.join()
thr_file5.join()

thr_console1.join()