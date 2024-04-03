import uiautomator2 as u2
import time
import util as u


def sgin(d):  # 点淘签到
    print("点淘签到")
    package_name = 'com.taobao.live'
    d.app_start(package_name)
    time.sleep(10)

    u.click([d], 650, 510, 5, "点击小元宝")


d = u2.connect('192.168.0.201')
sgin(d)
