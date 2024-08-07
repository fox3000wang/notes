import uiautomator2 as u2
import time
import util as u

__package_name = 'com.ss.android.ugc.aweme.lite'


def sgin(ds):
    print("抖音极速签到")
    u.app_start(ds, __package_name, 5)
    u.app_start(ds, __package_name, 10)
    # 这里会弹出关闭少儿模式, 等几秒会自动关掉
    u.click(ds, 360, 1500, 3, '点击中下方赚钱')

    for d in ds:
        if d.wlan_ip == '192.168.0.200':
            u.click([d], 360, 940, 1, '点击"立即签到"')
            u.click([d], 360, 940, 1, '点击"明天再来"')
        elif d.wlan_ip == '192.168.0.201':
            u.click(ds, 680, 600, 1, '点击"签到"')  # 有概率不弹签到窗
            u.click([d], 360, 1150, 1, '点击"立即签到"')
            u.click([d], 360, 1150, 1, '点击"明天再来"')
    u.app_stop(ds, __package_name, 1)


def get_money(ds):  # test pass
    print("抖音极速提现")
    u.app_start(ds, __package_name, 10)
    u.click(ds, 360, 1500, 5, '点击中下方赚钱')
    u.click(ds, 545, 250, 5, '点击"去提现"')
    for d in ds:
        if d.wlan_ip == '192.168.0.200':
            u.click(ds, 150, 880, 3, '点击"0.3元"')
            u.click(ds, 360, 1450, 3, '点击"确认提现"')
        if d.wlan_ip == '192.168.0.201':
            u.click(ds, 360, 1500, 2, '点击"0.3元"')
            u.click(ds, 360, 1450, 3, '点击"确认提现"')
    u.app_stop(ds, __package_name, 1)


def watch_video(ds):
    print("抖音极速观看视频")
    u.app_start(ds, __package_name, 10)
    u.hang_up(ds, 1880, '抖音极速', 5, 10)
    u.app_stop(ds, __package_name, 1)

# ds = []
# ds.append(u2.connect('192.168.0.200'))
# ds.append(u2.connect('192.168.0.201'))

# sgin(ds)
# get_money(ds)
# get_box(ds)
