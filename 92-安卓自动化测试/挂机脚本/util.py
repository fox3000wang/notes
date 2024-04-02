import uiautomator2 as u2
import time
import random


def click(ds, x, y, delay, c):
    delay = delay + random.randint(-1, 3)
    print('c ' + str(x) + ',' + str(y) + c + ' wait ' + str(delay))
    for d in ds:
        d.click(x, y)
    time.sleep(delay)
    return delay
