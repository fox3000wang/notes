import uiautomator2 as u2
import time
import util as u


def sgin(d):  # 百度极速版签到
    print("百度极速版签到")


def get_box(d):  # 百度极速版开宝箱并且刷5个广告
    print("百度极速版开宝箱并且刷5个广告")
    package_name = 'com.baidu.searchbox.lite'
    d.app_start(package_name)
    time.sleep(8)

    print("点下面的红包")
    d.click(360, 1530)
    time.sleep(5)

    print("点击宝箱")
    d.click(600, 1300)

    print("点击观看视频")
    d.click(360, 1120)
    time.sleep(60)

    # 循环5次
    for i in range(5):

        # 收掉弹窗, 这个可能有可能没有需要判断
        e = d(className="android.widget.ImageView",
              resourceId="com.baidu.searchbox.lite:id/hr8")
        if e.exists:
            print("点击收起按键")
            e.click()
            time.sleep(3)
        else:
            print("没有收起按键")

        # 点击右上角叉叉
        e = d(className="android.widget.ImageView",
              resourceId="com.baidu.searchbox.lite:id/hr7")
        if e.exists:
            print("点击右上角叉叉 hr7")
            e.click()
            time.sleep(3)

        e = d(className="android.widget.ImageView",
              resourceId="com.baidu.searchbox.lite:id/hr8")
        if e.exists:
            print("点击右上角叉叉 hr8")
            e.click()
            time.sleep(3)

        e = d(className="android.widget.ImageView",
              resourceId="com.baidu.searchbox.lite:id/iap")
        if e.exists:
            print("点击右上角叉叉 iap")
            e.click()
            time.sleep(3)

        d.click(360, 1350)
        d.click(360, 1050)
        d.click(360, 900)

        time.sleep(60)


d = u2.connect('192.168.0.201')
# print("点击观看视频")
# d.click(360, 1120)
# time.sleep(60)

# 循环5次
for i in range(5):

    # 收掉弹窗, 这个可能有可能没有需要判断
    e = d(className="android.widget.ImageView",
          resourceId="com.baidu.searchbox.lite:id/hr8")
    if e.exists:
        print("点击收起按键")
        e.click()
        time.sleep(3)
    else:
        print("没有收起按键")

    # 点击右上角叉叉
    e = d(className="android.widget.ImageView",
          resourceId="com.baidu.searchbox.lite:id/hr7")
    if e.exists:
        print("点击右上角叉叉 hr7")
        e.click()
        time.sleep(3)

    e = d(className="android.widget.ImageView",
          resourceId="com.baidu.searchbox.lite:id/hr8")
    if e.exists:
        print("点击右上角叉叉 hr8")
        e.click()
        time.sleep(3)

    e = d(className="android.widget.ImageView",
          resourceId="com.baidu.searchbox.lite:id/iap")
    if e.exists:
        print("点击右上角叉叉 iap")
        e.click()
        time.sleep(3)

    d.click(360, 1400)
    d.click(360, 1050)
    d.click(360, 900)

    time.sleep(60)
