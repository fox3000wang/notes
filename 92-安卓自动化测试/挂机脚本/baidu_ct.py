import uiautomator2 as u2
import time
import util as u

__package_name = 'com.baidu.searchbox.tomas'


def sgin(ds):  # test pass
    print("百度畅听签到")
    u.app_start(ds, __package_name, 12)
    u.click_btn(ds, 'com.baidu.searchbox.tomas:id/bwn', 1, "关掉弹窗")
    u.click(ds, 640, 1500, 5, "点击我的图标")
    u.click(ds, 140, 820, 5, "点击签到按钮")
    u.click(ds, 190, 1100, 5, "点击直接领取按钮")
    u.app_stop(ds, __package_name, 1)


def get_money(ds):
    print("百度常听提现")
    u.app_start(ds, __package_name, 12)
    u.click(ds, 640, 1500, 5, "点击我的图标")
    # u.click(ds, 620, 620, 5, "点击立即提现") 这里位置会变
    id = 'com.baidu.searchbox.tomas:id/bag'
    u.click_btn(ds, id, 3, "点击立即提现", "android.widget.Button")
    u.click(ds, 140, 640, 3, "点击'0.3元'")
    u.click(ds, 360, 1080, 3, "点击提现到微信")
    u.app_stop(ds, __package_name, 1)


def get_box(ds):  # 百度常听开宝箱并且刷5个广告
    print("百度常听开宝箱得金币")
    u.app_start(ds, __package_name, 12)

    u.click(ds, 500, 1500, 5, "点击福利")
    u.click(ds, 360, 1050, 1, "关闭弹窗")
    u.click(ds, 630, 1260, 3, "点击宝箱")
    u.click(ds, 360, 940, 1, "遇到弹窗领取上次奖励")
    u.click(ds, 360, 870, 60, "点击观看视频")

    # 循环10次
    for i in range(10):
        u.click_btn(ds, "com.baidu.searchbox.tomas:id/jfq", 1, "点击收起按键")
        u.click_btn(ds, "com.baidu.searchbox.tomas:id/h31", 1, "点击右上角叉叉")
        u.click(ds, 360, 1080, 1, "点击再看一个")
        u.click(ds, 360, 940, 1, "点击再看一个")
        # u.get_value(ds, id, "获取左上角的时间") # TBD
        time.sleep(60)

    u.app_stop(ds, __package_name, 1)


# ds = []
# ds.append(u2.connect('192.168.0.200'))
# ds.append(u2.connect('192.168.0.201'))


# u.click_btn(ds, 'com.baidu.searchbox.tomas:id/bag', 3, "点击立即提现")


# get_box(ds)


# sgin(ds)
# get_money(ds)
# get_box(ds)
