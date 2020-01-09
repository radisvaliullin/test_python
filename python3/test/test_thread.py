# Test Threads. Count process threads using "top M pid | wc -l".
import logging
import threading
import time


def thread_function(name, life_time):
    logging.info("Thread %s: starting", name)
    x = life_time
    while x > 0:
        logging.info("Thread %s: tick", name)
        time.sleep(1)
        x -= 1
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating threads")
    x = threading.Thread(target=thread_function, args=(1, 60), name='QWERTY')
    x2 = threading.Thread(target=thread_function, args=(2, 45), name='SCHMERTY')
    x3 = threading.Thread(target=thread_function, args=(1, 30), name='QWERTY')
    x4 = threading.Thread(target=thread_function, args=(2, 15), name='SCHMERTY')
    logging.info("Main    : before running threads")
    x.start()
    x2.start()
    x3.start()
    x4.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    time.sleep(60)
    logging.info("Main    : all done")
