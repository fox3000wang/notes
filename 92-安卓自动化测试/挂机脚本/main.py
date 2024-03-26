import uiautomator2 as u2
import time

d = u2.connect('192.168.0.109')

d.info
# 得出设备链接信息
print(d.window_size())
# 获取屏幕大小

# 关闭所有app 千万不要用啊，会杀掉后台进程
# d.app_stop_all()


def taobao():
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


def qiyi():
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


qiyi()
