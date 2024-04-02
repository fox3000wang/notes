import uiautomator2 as u2
import time


def sgin(d):  # 百度常听签到
    print("百度常听签到")
    # package_name = 'com.baidu.searchbox.tomas'
    # d.app_start(package_name, 10)
    # d.click(500, 1500)  # 点击福利

    # d.click(450, 1000)  # 点击而外领取 等待1分钟广告
    # time.sleep(60)


def get_box(d):  # 开宝箱并且刷5个广告
    print("开宝箱得金币")
    package_name = 'com.baidu.searchbox.tomas'
    d.app_start(package_name)
    time.sleep(8)

    print("点击福利")
    d.click(500, 1500)
    time.sleep(5)

    print("点击宝箱")
    d.click(630, 1260)
    time.sleep(5)

    print("点击观看视频")
    d.click(360, 870)
    time.sleep(60)

    # 循环5次
    for i in range(5):

        # 收掉弹窗, 这个可能有可能没有需要判断
        e = d(className="android.widget.ImageView",
              resourceId="com.baidu.searchbox.tomas:id/jfq")
        if e.exists:
            print("点击收起按键")
            e.click()
            time.sleep(3)
        else:
            print("没有收起按键")

        # 点击右上角叉叉
        e = d(className="android.widget.ImageView",
              resourceId="com.baidu.searchbox.tomas:id/h31")
        if e.exists:
            print("点击右上角叉叉")
            e.click()
            time.sleep(3)

        # 检查弹窗再看一个
        # e = d(className="android.widget.ImageView",
        #       resourceId="com.baidu.searchbox.tomas:id/t9")
        # if e.exists:
        print("点击再看一个")
        d.click(360, 1080)
        d.click(360, 940)

        time.sleep(60)

    d.app_stop(package_name)


# d = u2.connect('192.168.0.201')
# get_box(d)
