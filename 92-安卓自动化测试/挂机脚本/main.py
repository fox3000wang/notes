import uiautomator2 as u2
import time
import random

d = u2.connect('192.168.0.109')

d.info
# 得出设备链接信息
print(d.window_size())
# 获取屏幕大小

# 关闭所有app 千万不要用啊，会杀掉后台进程
# d.app_stop_all()


def c(x, y, delay, comment):
    print('click ' + str(x) + ',' + str(y) + comment + ' wait ' + str(delay))
    d.click(x, y)
    time.sleep(delay + random.randint(-3, 3))


def s(sx, sy, ex, ey, delay):
    print('swipe ' + str(sx) + ',' + str(sy) + ' to ' +
          str(ex) + ',' + str(ey) + ' wait ' + str(delay))
    d.swipe(sx, sy, ex, ey, 0.1)
    time.sleep(delay + random.randint(-3, 3))


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


def pinduoduo_make_money():
    print('启动拼多多刷短视频')
    package_name = 'com.xunmeng.pinduoduo'
    d.app_start(package_name)
    time.sleep(5)
    c(234, 1500, 5, '点击多多视频')
    for i in range(100):
        s(360, 1200, 360, 500, 6)
    d.app_stop(package_name)


def kuaishou_make_money():
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


pinduoduo_make_money()
# kuaishou_make_money()
