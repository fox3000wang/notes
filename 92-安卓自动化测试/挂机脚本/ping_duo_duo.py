import uiautomator2 as u2
import util as u

__package_name = 'com.xunmeng.pinduoduo'


def watch_video(ds):
    print("拼多多刷短视频")
    u.app_stop(ds, __package_name)
    u.app_start(ds, __package_name, 10)

    u.click(ds, 234, 1500, 2, '点击多多视频')
    u.click(ds, 360, 1000, 2, '点击领取今日奖励')
    u.click_btn_text(ds, '领取今日现金', 1, '点击领取今日现金')
    u.click(ds, 360, 1000, 1, '点击确认领取今日奖励')
    u.click_btn_text(ds, '明日继续来领', 1, '点击明日继续来领')

    total_time = 1880
    while total_time > 0:
        total_time -= u.swipe_up(ds, 5, 5)
        print('拼多多刷短视频' + ' 剩余时间：' + str(total_time))
        u.click(ds, 600, 320, 1, '点击关闭红包')
    u.app_stop(ds, __package_name, 1)
