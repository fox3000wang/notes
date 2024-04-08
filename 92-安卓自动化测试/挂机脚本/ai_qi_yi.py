import uiautomator2 as u2
import time
import util as u

__package_name = 'com.qiyi.video.lite'


def sgin(ds):
    print("爱奇艺签到")
    u.app_start(ds, __package_name, 12)

    u.app_stop(ds, __package_name, 1)


def get_money(ds):
    print("有柿签到")
    u.app_start(ds, __package_name, 10)
    u.click_btn_text(ds, '任务', 5, '点击“任务”', 0, 0)
    u.click(ds, 190, 300, 5, '点击现金数字')
    u.click(ds, 600, 250, 5, '去提现')
    # u.click_btn_text(ds, '0.5元', 5, '点击“0.5元”', 0, 0)
    u.click(ds, 130, 550, 5, '点击“0.5元”')
    # TODO: 这里要手动填写支付宝信息
    # u.app_stop(ds, __package_name, 1)


def get_box(ds):
    pass


def watch_video(ds):
    print("爱奇艺观看视频")
    u.app_start(ds, __package_name, 10)
    u.click(ds, 200, 1500, 3, '点击短视频')

    total_time = 1900
    while total_time > 0:
        total_time -= u.swipe_up(ds, 5, 10)
        print('爱奇艺观看视频 剩余时间：' + str(total_time))
    u.app_stop(ds, __package_name, 1)


# ds = []
# ds.append(u2.connect('192.168.0.200'))
# ds.append(u2.connect('192.168.0.201'))
