import time
import random
from threading import Thread
from threading import BoundedSemaphore

data_semaphore = BoundedSemaphore(10)
file_semaphore = BoundedSemaphore(5)
console_semaphore = BoundedSemaphore(1)


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


def action(task_id):
    get_data(task_id)
    file = Thread(target=write_to_file, args=(task_id,))
    console = Thread(target=write_to_console, args=(task_id,))
    file.start()
    console.start()
    file.join()
    console.join()


if __name__ == '__main__':
    users = [Thread(target = action, args = (task_id,)) for task_id in range(1, 21)]
    for user in users:
        user.start()
    for user in users:
        user.join()