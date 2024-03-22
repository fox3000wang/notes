import uiautomator2 as u2

d = u2.connect('192.168.0.106')  # alias for u2.connect_wifi('10.0.0.1')
print(d.info)
