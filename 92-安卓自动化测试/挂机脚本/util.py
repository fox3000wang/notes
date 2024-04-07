import uiautomator2 as u2
import time
import random
import requests

# 目标HTTPS URL
__url = 'https://api.day.app/etMsxSrdvToPv68aD4RQR3/'

# __name_image_view = 'android.widget.ImageView'


def app_start(ds, package_name, delay=5):
    for d in ds:
        d.app_start(package_name)
    time.sleep(delay)


def app_stop(ds, package_name, delay=5):
    for d in ds:
        d.app_stop(package_name)
    time.sleep(0)


def click(ds, x, y, delay=1, c=''):  # 点击坐标
    delay = delay + random.randint(0, 3)
    print('c ' + str(x) + ',' + str(y) + c + ' wait ' + str(delay))
    for d in ds:
        d.click(x, y)
    time.sleep(delay)
    return delay

# def click_btn(ds, type, id, delay, c): # 点击元素


def click_btn(ds, id, delay, c):  # 点击元素
    delay = delay + random.randint(0, 3)
    print('click_btn ' + ' ' + id + c + ' wait ' + str(delay))
    for d in ds:
        # btn = d(className=__name_image_view, resourceId=id)
        btn = d(resourceId=id)
        if btn.exists():
            bs = btn.bounds()
            d.click((bs[0] + bs[2]) / 2, (bs[1] + bs[3]) / 2)
            print(c)
        else:
            print(id + ' not found')
    time.sleep(delay)
    return delay


def click_btn_text(ds, t, delay, c, oX=0, oY=0):  # 点击文本+偏移
    delay = delay + random.randint(0, 3)
    print('click_btn_text ' + ' ' + t + c + ' wait ' + str(delay))
    for d in ds:
        btn = d(text=t)
        if btn.exists():
            bs = btn.bounds()
            d.click((bs[0] + bs[2]) / 2 + oX, (bs[1] + bs[3]) / 2 + oY)
            print(c)
        else:
            print(t + ' not found')
    time.sleep(delay)
    return delay


def get_value(ds, id, c):  # 获取元素值
    print('get_value ' + id + ' exist' + c)
    for d in ds:
        element = d(className=__name_image_view, resourceId=id)
        if element.exists():
            print(element.get_text())
            # print('element found ' + element.get_text())
            # return int(e.getText())
            return 0
        else:
            print('not found')
            return 0


# ['_UiObject__view_beside', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bounds', 'center', 'child', 'child_by_description', 'child_by_instance', 'child_by_text', 'child_selector', 'clear_text', 'click', 'click_exists', 'click_gone', 'count', 'down', 'drag_to', 'exists', 'fling', 'from_parent', 'gesture', 'get_text', 'info', 'jsonrpc', 'left', 'long_click', 'must_wait', 'parent', 'pinch_in', 'pinch_out', 'right', 'screenshot', 'scroll', 'selector', 'send_keys', 'session', 'set_text', 'sibling', 'swipe', 'up', 'wait', 'wait_gone', 'wait_timeout']


# 发送通知
def send_notice(txt):
    try:
        requests.get(__url + txt)
    except:
        print('send_notice error')
