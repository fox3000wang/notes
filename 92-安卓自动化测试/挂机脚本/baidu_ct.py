import uiautomator2 as u2
import time
import util as u


def sgin(d):  # 百度畅听签到
    print("百度常听签到")
    package_name = 'com.baidu.searchbox.tomas'
    d.app_start(package_name)
    time.sleep(10)

    u.click([d], 640, 1500, 5, "点击我的图标")
    u.click([d], 140, 820, 5, "点击签到按钮")

    # d.click(450, 1000)  # 点击而外领取 等待1分钟广告
    d.app_stop(package_name)


def get_box(d):  # 百度常听开宝箱并且刷5个广告
    print("百度常听开宝箱得金币")
    package_name = 'com.baidu.searchbox.tomas'
    d.app_start(package_name)
    time.sleep(8)

    u.click([d], 500, 1500, 5, "点击福利")
    u.click([d], 630, 1260, 5, "点击宝箱")
    u.click([d], 360, 870, 60, "点击观看视频")

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

        u.click([d], 360, 940, 0, "点击再看一个")
        u.click([d], 360, 1080, 0, "点击再看一个")

        time.sleep(60)

    d.app_stop(package_name)


d = u2.connect('192.168.0.201')
get_box(d)
# sgin(d)
