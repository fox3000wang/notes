import uiautomator2 as u2
import util as u

__package_name = 'com.xunmeng.pinduoduo'


def watch_video(ds):
    print("拼多痘刷短视频")
    u.app_start(ds, __package_name, 10)
    u.app_stop(ds, __package_name, 1)
    u.app_start(ds, __package_name, 10)

    c(234, 1500, 5, '点击多多视频')
    c(360, 1000, 5, '点击领取今日奖励')
    c(360, 1000, 5, '点击确认领取今日奖励')

    u.click(ds, 200, 1500, 3, '点击短视频')

    total_time = 1900
    while total_time > 0:
        total_time -= u.swipe_up(ds, 5, 10)
        print('拼多痘刷短视频 剩余时间：' + str(total_time))
    u.app_stop(ds, __package_name, 1)
