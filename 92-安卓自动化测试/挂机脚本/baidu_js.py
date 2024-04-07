import uiautomator2 as u2
import time
import util as u

__package_name = 'com.baidu.searchbox.lite'


def sgin(ds):  # 百度极速版签到
    print("百度极速版签到")
    u.app_start(ds, __package_name, 10)
    u.click(ds, 360, 1530, 3, "点下面的红包")
    u.click(ds, 270, 1040, 3, "点击立即领取")
    u.click(ds, 270, 1040, 3, "点击我知道了")
    u.app_stop(ds, __package_name, 2)


def get_money(ds):  # 百度极速版获取金币pass
    print("百度极速版获取金币")
    u.app_start(ds, __package_name, 10)
    u.click(ds, 360, 1530, 2, "点下面的红包")
    u.click(ds, 580, 230, 2, "点击微信提现")
    u.click(ds, 130, 640, 2, "点击提现0.3元")
    u.click(ds, 360, 1000, 2, "点击微信提现")
    u.app_stop(ds, __package_name, 2)


def get_box(ds):
    print("百度极速版开宝箱并且刷广告")
    u.app_start(ds, __package_name, 10)
    u.click(ds, 360, 1530, 5, "点下面的红包")
    u.click(ds, 600, 1300, 4, "点击宝箱")
    u.click(ds, 360, 1120, 60, "点击观看视频")

    # 循环5次
    for i in range(5):
        u.click_btn(ds, 'com.baidu.searchbox.lite:id/ms', 1, "再看一个领取更多福利")

        u.click_btn(ds, 'com.baidu.searchbox.lite:id/iao', 1, "点下端击收起按键")

        u.click_btn(ds, 'com.baidu.searchbox.lite:id/hr7', 1, "点击右上角叉叉")
        u.click_btn(ds, 'com.baidu.searchbox.lite:id/hr8', 1, "点击右上角叉叉")
        u.click_btn(ds, 'com.baidu.searchbox.lite:id/iap', 1, "点击右上角叉叉")

        u.click_btn_text(ds, '残忍离开', 1, '点击“残忍离开”上面的继续观看', 0, -100)
        u.click_btn(ds, 'com.baidu.searchbox.lite:id/ms', 1, "再看一个领取更多福利")
        u.click(ds, 360, 900, 1, '点击继续观看')

        time.sleep(60)
    u.app_stop(ds, __package_name, 2)


ds = []
ds.append(u2.connect('192.168.0.200'))
ds.append(u2.connect('192.168.0.201'))

# sgin(ds)
# get_money(ds)
get_box(ds)

# d = ds[0]
# btn = d(resourceId="com.baidu.searchbox.lite:id/hr7")
# btn = d(text='残忍离开')

# u.click_btn_text(ds, '残忍离开', 1, '点击“残忍离开”上面的继续观看', 0, -100)

# //*[re:match(text(), '^.*道了')]
# btn = d.xpath('*[re:match(text(), "^.*再看一个")]')


# print(btn.bounds())
