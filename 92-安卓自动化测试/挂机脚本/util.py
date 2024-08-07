import uiautomator2 as u2
import time
import random
import requests

# 目标HTTPS URL
__url = 'https://api.day.app/etMsxSrdvToPv68aD4RQR3/'


def app_start(ds, package_name, delay=5):
    print('app_start ' + package_name)
    for d in ds:
        d.app_start(package_name)
    time.sleep(delay)


def app_stop(ds, package_name, delay=1):
    print('app_stop ' + package_name)
    for d in ds:
        d.app_stop(package_name)
    time.sleep(0)


def app_stop_all(ds, delay=1):
    print('app_stop_all')
    for d in ds:
        d.app_stop_all(excludes=['com.github.uiautomator'])
    time.sleep(0)


def click(ds, x, y, delay=1, c=''):  # 点击坐标
    delay = delay + random.randint(0, 3)
    print('c ' + str(x) + ',' + str(y) + c + ' wait ' + str(delay))
    for d in ds:
        d.click(x, y)
    time.sleep(delay)
    return delay

# def click_btn(ds, type, id, delay, c): # 点击元素


def click_btn(ds, id, delay, c, className='android.widget.ImageView'):  # 点击元素
    delay = delay + random.randint(0, 3)
    print('click_btn ' + ' ' + id + c + ' wait ' + str(delay))
    for d in ds:
        btn = d(className=className, resourceId=id)
        if btn.exists():
            bs = btn.bounds()
            d.click((bs[0] + bs[2]) / 2, (bs[1] + bs[3]) / 2)
            print(c)
        else:
            print(id + ' not found')
    time.sleep(delay)
    return delay


def click_btn_text(ds, txt, delay, c, oX=0, oY=0, className='android.widget.TextView'):  # 点击文本+偏移
    delay = delay + random.randint(0, 3)
    print('click_btn_text ' + ' ' + txt + c + ' wait ' + str(delay))
    for d in ds:
        btn = d(className=className, text=txt)
        if btn.exists():
            bs = btn.bounds()
            d.click((bs[0] + bs[2]) / 2 + oX, (bs[1] + bs[3]) / 2 + oY)
            print(c)
        else:
            print(txt + ' not found')
    time.sleep(delay)
    return delay


def s(ds, sx, sy, ex, ey, delay=5, r=0):  # 滑动
    delay = delay + random.randint(0, r)
    if sx == ex:
        print('上滑' + ' wait ' + str(delay))
    if sy == ey:
        print('左滑' + ' wait ' + str(delay))
    for d in ds:
        d.swipe(sx, sy, ex, ey, 0.1)
    time.sleep(delay)
    return delay


def swipe_up(ds, delay=5, r=0):
    # delay = s(ds, 360, 1200, 360, 500, delay, r)
    delay = s(ds, 80, 1000, 80, 0, delay, r)
    return delay


def swipe_left(ds, delay=5, r=0):
    delay = s(ds, 500, 800, 100, 800, delay, r)
    return delay


def hang_up(ds, total_time=1880, c='', delay=5, r=0):
    while total_time > 0:
        print(c + ' 剩余时间：' + str(total_time))
        total_time -= swipe_up(ds, delay, r)


def hang_left(ds, total_time=1880, c='', delay=5, r=0):
    while total_time > 0:
        print(c + ' 剩余时间：' + str(total_time))
        total_time -= swipe_left(ds, delay, r)


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

def is_exists(d, id, className='android.widget.ImageView'):
    return d(className=className, resourceId=id).exists()

# 发送通知


def send_notice(txt):
    try:
        requests.get(__url + txt)
    except:
        print('send_notice error')
