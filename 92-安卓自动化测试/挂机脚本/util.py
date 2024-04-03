import uiautomator2 as u2
import time
import random

__name_image_view = "android.widget.ImageView"


def app_start(ds, package_name, delay=5):
    for d in ds:
        d.app_start(package_name)
    time.sleep(delay)


def app_stop(ds, package_name, delay=5):
    for d in ds:
        d.app_stop(package_name)
    time.sleep(0)


def click(ds, x, y, delay=1, c=''):  # 点击坐标
    delay = delay + random.randint(-1, 3)
    print('c ' + str(x) + ',' + str(y) + c + ' wait ' + str(delay))
    for d in ds:
        d.click(x, y)
    time.sleep(delay)
    return delay

# def click_btn(ds, type, id, delay, c): # 点击元素


def click_btn(ds, id, delay, c):  # 点击元素
    delay = delay + random.randint(-1, 3)
    print('c ' + ' ' + id + c + ' wait ' + str(delay))
    for d in ds:
        btn = d(className=__name_image_view, resourceId=id)
        if btn.exists():
            btn.click()
            print(c)
        else:
            print('btn not found')
    time.sleep(delay)
    return delay
