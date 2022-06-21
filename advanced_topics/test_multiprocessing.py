import logging
import time
from multiprocessing import Process
from threading import Thread


def cube(name):
    global my_numbers
    logging.info(f"process {name}: starting")
    time.sleep(20)
    for x in my_numbers:
        logging.info(f'{x} cube is {x**3}')

    my_numbers.append(12)
    logging.info(my_numbers)
    logging.info(id(my_numbers))
    time.sleep(15)
    logging.info(f"process {name}: finishing")


def is_even(name):
    logging.info(f"process {name}: starting")
    time.sleep(15)
    for x in my_numbers:
        if x % 2 == 0:
            logging.info(f'{x} is an even number')
    logging.info(f"process {name}: finishing")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    my_numbers = [3, 4, 5, 6, 7, 8]
    my_process1 = Process(target=cube, args=('cube',), daemon=False)
    my_process2 = Process(target=is_even, args=('is_even',), daemon=False)

    # my_thread1 = Thread(target=cube, args=('cube',), daemon=True)
    # my_thread2 = Thread(target=is_even, args=('is_even',), daemon=True)

    my_process1.start()
    my_process2.start()

    # my_thread1.start()
    # my_thread2.start()


    # my_process1.join()
    time.sleep(5)
    # logging.info(my_numbers)
    # time.sleep(15)

    logging.info("Done")