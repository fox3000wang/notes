import uiautomator2 as u2
import time
import util as u

__package_name = 'com.ss.android.article.lite'


def sgin(ds):
    print("今日头条签到")
    u.app_start(ds, __package_name, 10)
    u.click_btn_text(ds, '开宝箱', 10, '点击“开宝箱”', 0, 0)
    # u.click(ds, 250, 990, 3, '点击中下方赚钱')
    # u.app_stop(ds, __package_name, 1)


def get_money(ds):
    print("今日头条提现")
    u.app_start(ds, __package_name, 10)
    u.click_btn_text(ds, '开宝箱', 10, '点击“开宝箱”', 0, 0)
    u.click(ds, 140, 230, 5, '点击现金数字')
    u.click(ds, 600, 250, 5, '去提现')
    u.click(ds, 140, 650, 3, '点击"0.5元"')
    u.click(ds, 360, 1500, 1, '点击"立即提现"')
    # u.app_stop(ds, __package_name, 1)


ds = []
ds.append(u2.connect('192.168.0.200'))
# ds.append(u2.connect('192.168.0.201'))


# sgin(ds)
get_money(ds)
# get_box(ds)
