import uiautomator2 as u2
import time
import util as u

__package_name = 'com.dragon.read'
__class_name = 'com.lynx.tasm.behavior.ui.text.FlattenUIText'


def sgin(ds):  # test pass
    print("番茄小说签到")
    u.app_start(ds, __package_name, 10)
    u.click_btn_text(ds, '福利', 5, '点击“福利”', 0, 0)
    u.click(ds, 360, 1000, 3, '点击"立即签到"')
    u.app_stop(ds, __package_name, 1)


def get_money(ds):
    print("番茄小说提现")
    u.app_start(ds, __package_name, 10)
    u.click_btn_text(ds, '福利', 5, '点击“福利”', 0, 0)
    u.click_btn_text(ds, '可微信提现', 5, '点击“可微信提现”', 0, 0, __class_name)

    u.click(ds, 600, 230, 2, '点击“去提现”')
    u.click_btn_text(ds, '去提现', 1, '点击“去提现”', 0, 0, __class_name)

    for d in ds:
        if d.wlan_ip == '192.168.0.200':
            u.click(ds, 600, 230, 1, '点击“去提现”')
            u.click(ds, 120, 550, 1, '点击“0.3元”')
            u.click_btn_text(ds, '立即观看', 1, '点击“立即观看”')

        elif d.wlan_ip == '192.168.0.201':
            u.click_btn_text(ds, '去提现', 1, '点击“去提现”', 0, 0, __class_name)
            u.click_btn_text(ds, '看视频提现', 1, '点击“看视频提现”', 0, 0, __class_name)
            u.click_btn_text(ds, '看视频', 1, '点击“看视频”', 0, 0, __class_name)

    # u.app_stop(ds, __package_name, 1)


# ds = []
# ds.append(u2.connect('192.168.0.200'))
# ds.append(u2.connect('192.168.0.201'))
