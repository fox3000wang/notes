import uiautomator2 as u2
import time

device = u2.connect('192.168.0.106')

# 打开淘宝app
# d.app_start('com.taobao.taobao')

# 打开抖音app
app = device.app_start("com.ss.android.ugc.aweme.lite")


# 等待10秒钟 A10环境下经验值
time.sleep(10)


# 点击坐标100，100
app.click(100, 100)

# 关闭淘宝app
app.app_stop('com.ss.android.ugc.aweme.lite')
