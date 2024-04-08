import uiautomator2 as u2
import util as u

__package_name = 'com.kuaishou.nebula'


def watch_video(ds):
    print("快手刷短视频")
    u.app_stop(ds, __package_name, 1)
    u.app_start(ds, __package_name, 10)
    u.app_stop(ds, __package_name, 1)
    u.app_start(ds, __package_name, 10)

    u.hang_up(ds, 1880, '快手刷短视频', 5, 10)
    u.app_stop(ds, __package_name, 1)
