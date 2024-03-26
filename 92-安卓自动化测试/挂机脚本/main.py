import uiautomator2 as u2
import time

d = u2.connect('192.168.0.109')

d.info
# 得出设备链接信息
print(d.window_size())
# 获取屏幕大小
print(d.current_app())
# 获取当前应用的信息
print(d.serial)
# 获取设备序列号
print(d.wlan_ip)
# 获取WIFI IP
print(d.device_info)
# 获取详细的设备信息


#
package_name = 'com.taobao.taobao'

# 打开淘宝app
d.app_start(package_name)

# 等待10秒钟 A10环境下经验值
time.sleep(10)

# 点击坐标100，100
# d.click(100, 100)

# 关闭淘宝
d.app_stop(package_name)
