import threading
from queues import PriorityQueue

front_queue = PriorityQueue()
back_queue = PriorityQueue()

VERY_FREQUENT = 3
FREQUENT = 2
NOT_FREQUENT = 1


url_list = [
(NOT_FREQUENT,"www.facebook.com"), 
(FREQUENT, "www.cnn.com"), 
(VERY_FREQUENT, "www.9gag.com")
]




def front_worker():

    # for prioritization
    



    # Find a way to assign a priority value between 1 and K and enqued in the corresponding front queue
    
    # Then extract by selecting (e.g. randomized) one of the front queues; higher priority queues are more likely to be selected
    # or by round robin
    # Then dequeue the head element from the selected queue

    while True:
        item = front_queue.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        front_queue.task_done()


def back_worker():
    # For politeness

    while True:
        item = front_queue.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        front_queue.task_done()

# Crawler




def main():
    threading.Thread(target=front_worker, daemon=True).start()
    for item in url_list:
        front_queue.enqueue_with_priority(item)


    # front_queue.join()
    print("Front queue completed")

    threading.Thread(target=back_worker, daemon=True).start()
    for item in range(30):
        back_queue.put(item)


    # back_queue.join()
    print("All work completed")


if __name__ == "__main__":
    main()


