import uiautomator2 as u2
import util as u

import baidu_ct as bdct
import baidu_js as bdjs
import douyin_js as dyjs
import you_shi as ys
import wu_kong as wk
import fan_qie_xiao_shuo as fqxs
import ai_qi_yi as aqy
import ping_duo_duo as pdd
import kuaishou as ks


ds = []
ds.append(u2.connect('192.168.0.200'))
ds.append(u2.connect('192.168.0.201'))
# 关闭所有app 千万不要用啊，会杀掉后台进程
# d.app_stop_all()


def daily():

    bdct.sgin(ds)
    bdct.sgin(ds)
    bdct.get_money(ds)
    bdct.get_money(ds)

    bdjs.sgin(ds)
    bdjs.sgin(ds)
    bdjs.get_money(ds)
    bdjs.get_money(ds)

    # dyjs.sgin(ds)
    # dyjs.sgin(ds)
    # dyjs.get_money(ds)
    # dyjs.get_money(ds)

    # ys.sgin(ds)
    # ys.get_money(ds)
    # wk.sgin(ds)
    # wk.get_money(ds)
    # wk.get_box(ds)
    # fqxs.sgin(ds)
    # fqxs.get_money(ds)


def get_box():
    bdct.get_box(ds)
    bdjs.get_box(ds)


# aqy.sgin(ds)
# aqy.sgin(ds)
# aqy.sgin(ds)


# daily()
# get_box()

# u.hang_left(ds, 4000, '', 5, 10)
# u.hang_left(ds, 1880 * 6, '', 15, 15)
u.hang_up(ds, 1880, '', 5, 10)
# u.hang_up(ds, 1880 * 2, '', 10, 20)


# dyjs.watch_video(ds)

for i in range(0, 3):
    # aqy.watch_video(ds)
    pdd.watch_video(ds)
    ks.watch_video(ds)
    dyjs.watch_video(ds)
    bdjs.watch_video(ds)

# dyjs.watch_video(ds
#
# )
# pdd.watch_video(ds)
# ks.watch_video(ds)

u.send_notice('挂机结束')
# daily()
# get_box()

# u.hang_left(ds)
# u.hang_up(ds)

# aqy.watch_video(ds)
# pdd.watch_video(ds)
# ks.watch_video(ds)
