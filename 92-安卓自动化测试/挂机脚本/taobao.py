import uiautomator2 as u2
import util as u

__package_name = 'com.taobao.taobao'


def sgin(ds):
    u.app_stop(ds, __package_name)
    u.app_start(ds, __package_name)
    u.click(ds, 90, 100, 10, "点签到")
    u.click(ds, 640, 700, 1, "点元宝")
    u.click(ds, 360, 700, 1, "立即签到")
    u.app_stop(ds, __package_name)


def sgin2(ds):
    u.app_stop(ds, __package_name)
    u.app_start(ds, __package_name)

    for d in ds:
        btn = d(className='android.view.View', descriptionContains='领淘金币')
        if (btn.exists()):
            bs = btn.bounds()
            d.click(bs[0] + 20, bs[1] + 20)
        btn = d(className='android.widget.TextView', text='领淘金币')
        if (btn.exists()):
            bs = btn.bounds()
            d.click(bs[0] + 20, bs[1] + 20)
    time.sleep(5)

    for d in ds:
        btn = d(className='android.widget.Button', text='领取金币')
        if (btn.exists()):
            btn.click()

    for i in range(0, 30):
        u.click(ds, 360, 800, 2, "点推币领现金")

    u.app_stop(ds, __package_name)


def sign3(ds):
    u.app_stop(ds, __package_name)
    u.app_start(ds, __package_name)
    u.click(ds, 220, 1520, 10, "点视频")
    u.hang_up(ds, 60, 10, 5)

    # u.app_stop(ds, __package_name)
    # u.app_start(ds, __package_name)
    # u.click(ds, 220, 1520, 10, "点视频")
    # u.hang_up(ds, 600, 10, 5)

    for d in ds:
        t = 'com.taobao.taobao:id/tbvideo_interact_badge_center_component_circle_progress_view'
        btn = d(className='android.view.View', resourceId=t)

        if (btn.exists()):
            bs = btn.bounds()
            u.click([d], bs[0] + 20, bs[1] + 20, 2, '点击钱包')

    for d in ds:
        btn = d(className='android.widget.TextView', text='换现金')
        if (btn.exists()):
            bs = btn.bounds()
            u.click([d], bs[0] + 20, bs[1] + 20, 1, '点击换现金')

    for d in ds:
        btn = d(className='android.widget.TextView', text='提现')
        if (btn.exists()):
            bs = btn.bounds()
            u.click([d], bs[0] + 20, bs[1] + 20, 1, '点击提现')

    for d in ds:
        btn = d(className='android.widget.TextView', text='0.3元')
        if (btn.exists()):
            bs = btn.bounds()
            u.click([d], bs[0] + 20, bs[1] + 20)

    for d in ds:
        btn = d(className='android.widget.TextView', text='立即提现到支付宝')
        if (btn.exists()):
            bs = btn.bounds()
            u.click([d], bs[0] + 20, bs[1] + 20)

    u.click(ds, 360, 1450, 1, '点击立即提现到支付宝')
    u.app_stop(ds, __package_name)


ds = []
ds.append(u2.connect('192.168.0.200'))
ds.append(u2.connect('192.168.0.201'))
u.app_stop(ds, __package_name)
