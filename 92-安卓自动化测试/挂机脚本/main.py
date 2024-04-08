import uiautomator2 as u2
import time
import random
import util as u

import baidu_ct as bdct
import baidu_js as bdjs

import douyin_js as dyjs


ds = []
ds.append(u2.connect('192.168.0.200'))
ds.append(u2.connect('192.168.0.201'))

# print(ds[0].info)
# print(ds[0].window_size())  # 获取屏幕大小

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
        total_time -= s_up(10)
        print('剩余时间：' + str(total_time))
    app_stop(package_name)

    app_start(package_name)
    total_time = 1900
    while total_time > 0:
        total_time -= s_up(10)
        print('剩余时间：' + str(total_time))
    app_stop(package_name)


def dou_yin_ji_su_make_money():  # 抖音极速版本挂机, 30分钟
    print('启动抖音极速版本挂机')
    package_name = 'com.ss.android.ugc.aweme.lite'
    app_start(package_name, 10)

    total_time = 1900
    while total_time > 0:
        total_time -= s_up(10)
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
        total_time -= s_up(10)
        print('剩余时间：' + str(total_time))
    app_stop(package_name)


###############################################################################

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


def daily():
    """
    bdct.sgin(ds)
    bdct.sgin(ds)
    bdct.get_money(ds)
    bdct.get_money(ds)

    bdjs.sgin(ds)
    bdjs.sgin(ds)
    bdjs.get_money(ds)
    bdjs.get_money(ds)


    dyjs.sgin(ds)
    dyjs.sgin(ds)
    """
    dyjs.get_money(ds)
    dyjs.get_money(ds)

    # bdct.get_box(ds)
    # bdjs.get_box(ds)


try:
    daily()

    # bdct.get_box(ds)
    # bdjs.get_box(ds)

    # dou_yin_ji_su_make_money()
    # pinduoduo_make_money()
    # jin_ri_toutiao_make_money()
    # kuaishou_make_money()

    # kuaishou_make_money()
    # dou_yin_ji_su_make_money()

    # total_time = 1900 * 6
    # while total_time > 0:
    #     # total_time -= s_up(15)
    #     total_time -= s_left(10)

    #     print('剩余时间：' + str(total_time))


except:
    u.send_notice('出错了!')
finally:
    # u.send_notice('完成!')
    pass
u.send_notice('完成!')
