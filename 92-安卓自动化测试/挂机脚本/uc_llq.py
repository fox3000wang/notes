import uiautomator2 as u2
import time
import util as u

__package_name = 'com.ucmobile.lite'


def sgin(ds):
    print("UC浏览器签到")
    u.app_start(ds, __package_name, 10)
    # TODO:
    u.app_stop(ds, __package_name)


def get_money(ds):
    print("UC浏览器提现")
    u.app_start(ds, __package_name, 10)
    u.click(ds, 650, 1500, 5, '点击任务')
    u.click(ds, 310, 220, 5, '点击现金')
    u.click(ds, 360, 400, 5, '点击提现')
    u.click(ds, 150, 870, 5, '点击0.30元')
    u.click(ds, 77, 1500, 1, '点击我已经确认')
    u.click(ds, 360, 1360, 10, '点击请分享')
    u.click(ds, 250, 1320, 10, '点击微信')
    u.app_stop(ds, 'com.tencent.mm')
    u.app_start(ds, __package_name, 2)
    u.app_stop(ds, __package_name)


def get_box(ds):
    print("UC浏览器宝箱")
    u.app_stop(ds, __package_name)
    u.app_start(ds, __package_name, 15)
    u.click(ds, 650, 1500, 5, '点击任务')
    u.click(ds, 580, 490, 60, '点击去完成')

    for i in range(3):
        for d in ds:
            if u.is_exists(d, id) == False:
                u.click(ds, 650, 1060, 1, '点击去完成')
                u.app_start(ds, __package_name, 30)

        u.click_btn(ds, id, 5, '点击关闭')
        u.click(ds, 360, 900, 60, '点击再看一个')
    u.app_stop(ds, __package_name)


ds = []
ds.append(u2.connect('192.168.0.200'))
ds.append(u2.connect('192.168.0.201'))

get_box(ds)
