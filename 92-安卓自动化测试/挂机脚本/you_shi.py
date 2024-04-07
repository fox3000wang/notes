import uiautomator2 as u2
import time
import util as u

__package_name = 'com.ss.android.article.search'


def sgin(ds):
    print("有柿签到")
    u.app_start(ds, __package_name, 10)
    u.click_btn_text(ds, '开宝箱', 5, '点击“开宝箱”', 0, 0)
    u.click_btn_text(ds, '签到领金币', 5, '点击“签到领金币”', 0, 0)
    u.app_stop(ds, __package_name, 1)


def get_money(ds):
    print("有柿签到")
    u.app_start(ds, __package_name, 10)
    u.click_btn_text(ds, '任务', 5, '点击“任务”', 0, 0)
    u.click(ds, 190, 300, 5, '点击现金数字')
    u.click(ds, 600, 250, 5, '去提现')
    u.click_btn_text(ds, '0.5元', 5, '点击“0.5元”', 0, 0)

    # u.app_stop(ds, __package_name, 1)


ds = []
ds.append(u2.connect('192.168.0.200'))
# ds.append(u2.connect('192.168.0.201'))

#
#
# u.click_btn_text(ds, '0.5元', 5, '点击“0.5元”', 0, 0)


u.click_btn_text(ds, '0.5元', 5, '点击“0.5元”', 0, 0)
