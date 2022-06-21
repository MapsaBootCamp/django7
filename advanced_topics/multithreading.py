import logging
import threading
import time
import random


class MyThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = random.randint(10**9, 10**10-1)

    def run(self):
        print(f"thread {self.id} start")
        super().run()


def thread_function(name, sleep_time):

    logging.info(f"Thread {name}: starting")

    time.sleep(sleep_time)

    logging.info(f"Thread {name}: finishing")


if __name__ == "__main__":

    format = "%(asctime)s-[%(levelname)s]: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO,

                        datefmt="%H:%M:%S")

    logging.info("Main: before creating thread")

    x_1 = MyThread(target=thread_function, args=(1, 25), daemon=True)
    x_2 = MyThread(target=thread_function, args=(2, 50), daemon=True)

    # thread_function(1, 2)
    # thread_function(2, 5)
    x_1.start()
    x_2.start()

    x_1.join()

    logging.info("Main: all done")