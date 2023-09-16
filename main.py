import threading
import queue

front_queue = queue.Queue()
back_queue = queue.Queue()


def front_worker():
    while True:
        item = front_queue.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        front_queue.task_done()


def back_worker():
    while True:
        item = front_queue.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        front_queue.task_done()

# Crawler


url_list = ["www.facebook.com", "www.cnn.com", "www.9gag.com"]


def main():
    threading.Thread(target=front_worker, daemon=True).start()
    for item in range(30):
        front_queue.put(item)


    front_queue.join()
    print("Front queue completed")

    threading.Thread(target=back_worker, daemon=True).start()
    for item in range(30):
        back_queue.put(item)


    back_queue.join()
    print("All work completed")


if __name__ == "__main__":
    main()


