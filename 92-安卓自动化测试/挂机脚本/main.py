import uiautomator2 as u2
import time
import random

# import baidu as bd

ips = []
ips.append('192.168.0.200')
ips.append('192.168.0.201')

ds = []
for ip in ips:
    ds.append(u2.connect(ip))

print(ds[0].info)
print(ds[0].window_size())  # 获取屏幕大小

# 关闭所有app 千万不要用啊，会杀掉后台进程
# d.app_stop_all()


def c(x, y, delay, c):  # 点击
    delay = delay + random.randint(-3, 3)
    print('c ' + str(x) + ',' + str(y) + c + ' wait ' + str(delay))
    for d in ds:
        d.click(x, y)
    time.sleep(delay)
    return delay


def s(sx, sy, ex, ey, delay):  # 滑动
    delay = delay + random.randint(-3, 3)
    print('swipe ' + str(sx) + ',' + str(sy) + ' to ' +
          str(ex) + ',' + str(ey) + ' wait ' + str(delay))
    for d in ds:
        d.swipe(sx, sy, ex, ey, 0.1)
    time.sleep(delay)
    return delay


def p(name):
    print('press')
    for d in ds:
        d.press(name)
    time.sleep(random.randint(1, 3))


def s_up(delay=10):
    print('上滑')
    delay = s(360, 1200, 360, 500, delay)
    return delay


def s_left(delay=10):
    print('左滑')
    delay = s(500, 800, 100, 800, delay)
    return delay


def app_start(package_name, delay=5):
    for d in ds:
        d.app_start(package_name)
    time.sleep(delay)


def app_stop(package_name):
    for d in ds:
        d.app_stop(package_name)
    time.sleep(5)

###############################################################################


def pinduoduo_make_money():  # 拼多多刷短视频, 30分钟
    print('启动拼多多刷短视频')
    package_name = 'com.xunmeng.pinduoduo'
    app_start(package_name)
    app_stop(package_name)
    app_start(package_name)

    c(234, 1500, 5, '点击多多视频')
    c(360, 1000, 5, '点击领取今日奖励')
    c(360, 1000, 5, '点击确认领取今日奖励')

    total_time = 1900
    while total_time > 0:
        total_time -= s_up(6)
        print('剩余时间：' + str(total_time))
    app_stop(package_name)


def kuaishou_make_money():  # 快手挂机刷短视频, 30分钟
    print('快手挂机刷短视频')
    package_name = 'com.kuaishou.nebula'
    app_start(package_name, 8)
    app_stop(package_name)
    app_start(package_name, 8)
    app_stop(package_name)
    app_start(package_name)

    total_time = 100
    while total_time > 0:
        total_time -= s_up(6)
        print('剩余时间：' + str(total_time))
    app_stop(package_name)

    app_start(package_name)
    total_time = 1900
    while total_time > 0:
        total_time -= s_up(6)
        print('剩余时间：' + str(total_time))
    app_stop(package_name)


def dou_yin_ji_su_make_money():  # 抖音极速版本挂机, 30分钟
    print('启动抖音极速版本挂机')
    package_name = 'com.ss.android.ugc.aweme.lite'
    app_start(package_name, 10)

    total_time = 1900
    while total_time > 0:
        total_time -= s_up(6)
        print('剩余时间：' + str(total_time))
    app_stop(package_name)


def dou_yin_huo_shan_make_money():  # 抖音火山版本挂机, 30分钟
    print('抖音火山版本挂机')
    package_name = 'com.ss.android.ugc.live'
    app_start(package_name, 10)

    total_time = 1900
    while total_time > 0:
        total_time -= s_up(6)
        print('剩余时间：' + str(total_time))
    app_stop(package_name)


def jin_ri_toutiao_make_money():  # 今日头条极速版本挂机, 30分钟
    print('今日头条极速版本挂机')
    package_name = 'com.ss.android.article.lite'
    app_start(package_name, 10)

    total_time = 1900
    while total_time > 0:
        total_time -= s_up(6)
        print('剩余时间：' + str(total_time))
    app_stop(package_name)


###############################################################################


def baidu_ting_make_money():
    printprint('启动百度畅听赚钱')
    package_name = 'com.baidu.searchbox.lite'
    d.app_start(package_name)
    time.sleep(10)
    c(500, 1500, 10, '点击右下方“福利”')


def baidu_make_money():
    print('启动百度极速赚钱')
    package_name = 'com.baidu.searchbox.lite'
    d.app_start(package_name)
    time.sleep(10)
    c(360, 1530, 10, '点击中下方红包')

    for i in range(5):  # 随心搜索5次
        c(600, 920, 15, '点随心搜')
        p("back")
        c(590, 495, 1, '关闭弹窗')


def taobao():  # 淘宝签到
    # 获取包名
    package_name = 'com.taobao.taobao'

    # 打开淘宝app
    d.app_start(package_name)

    # 等待10秒钟 A10环境下经验值
    time.sleep(10)

    # 点击坐标100，100
    d.click(106, 106)

    time.sleep(10)

    # 关闭淘宝
    # d.app_stop(package_name)


def kuaishou_click_box():
    print('启动快手刷广告')
    package_name = 'com.kuaishou.nebula'
    d.app_start(package_name)
    time.sleep(8)

    c(508, 1520, 10, '点击去赚钱')

    c(620, 1476, 2, '点击宝箱')
    # c(508, 1520, 2, '点击宝箱')

    ########

    c(620, 1476, 60, '点看内容 1')  # 这里坐标不对

    c(284, 110, 2, '点击已经成功获取奖励')

    c(360, 900, 60, '点击再看一个的页面下的领取奖励 2')

    c(284, 110, 2, '点击已经成功获取奖励')

    c(360, 900, 60, '点击再看一个的页面下的领取奖励 3')

    c(284, 110, 2, '点击已经成功获取奖励')

    c(360, 900, 60, '点击再看一个的页面下的领取奖励 4')

    c(284, 110, 2, '点击已经成功获取奖励')

    c(360, 900, 60, '点击再看一个的页面下的领取奖励 5')

    d.app_stop(package_name)


def qiyi_get_money():
    package_name = 'com.qiyi.video.lite'
    d.app_start(package_name)
    time.sleep(10)

    # 点击赚钱
    d.click(363, 1519)
    time.sleep(10)

    # 点击提现
    d.click(610, 180)
    time.sleep(5)

    # 点击微信0.3元提现
    d.click(140, 500)
    time.sleep(5)

    # 关闭
    d.app_stop(package_name)


jin_ri_toutiao_make_money()   # 今日头条

# pinduoduo_make_money()        # 拼多多

# dou_yin_huo_shan_make_money() # 抖音火山版
# pinduoduo_make_money()        # 拼多多
# kuaishou_make_money()         # 快手
# dou_yin_ji_su_make_money()    # 抖音极速版

# total_time = 3600
# while total_time > 0:
#     total_time -= s_up(6)
#     print('剩余时间：' + str(total_time))
