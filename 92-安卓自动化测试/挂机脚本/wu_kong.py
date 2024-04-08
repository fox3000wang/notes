import uiautomator2 as u2
import time
import util as u

__package_name = 'com.cat.readall'
__class_name = 'com.lynx.tasm.behavior.ui.text.FlattenUIText'


def sgin(ds):
    print("悟空签到")
    u.app_start(ds, __package_name, 10)
    u.click_btn_text(ds, '我的金币', 5, '点击“我的金币”', 0, 0)
    u.click_btn_text(ds, '立即领取', 5, '点击“立即领取”', 0, 0, __class_name)
    u.app_stop(ds, __package_name, 1)


def get_money(ds):
    print("悟空提现")
    u.app_start(ds, __package_name, 10)
    u.click_btn_text(ds, '我的金币', 6, '点击“我的金币”')
    u.click(ds, 586, 509, 1, '关掉弹窗')
    u.click_btn_text(ds, '去提现', 5, '点击“去提现”', 0, 0, __class_name)
    u.click(ds, 130, 660, 3, '点击0.3元')
    u.click(ds, 360, 1500, 3, '点击"立即提现"')
    u.app_stop(ds, __package_name, 1)


def get_box(ds):
    print("悟空宝箱")
    u.app_start(ds, __package_name, 10)
    u.click_btn_text(ds, '我的金币', 6, '点击“我的金币”')

    # 循环10次
    for i in range(10):
        u.click_btn_text(ds, '关闭', 3, '点击“关闭”', 0, 0, __class_name)
        u.click_btn_text(ds, '坚持退出', 3, '点击“看视频再得金币”', 0, -100, __class_name)
        time.sleep(60)
    u.app_stop(ds, __package_name, 1)


# ds = []
# ds.append(u2.connect('192.168.0.200'))
# ds.append(u2.connect('192.168.0.201'))
