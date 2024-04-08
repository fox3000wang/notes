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
    """
    bdct.sgin(ds)
    bdct.sgin(ds)
    bdct.get_money(ds)
    bdct.get_money(ds)

    bdjs.sgin(ds)
    bdjs.sgin(ds)
    bdjs.get_money(ds)
    bdjs.get_money(ds)

    dyjs.sgin(ds)
    dyjs.sgin(ds)
    dyjs.get_money(ds)
    dyjs.get_money(ds)

    ys.sgin(ds)
    ys.get_money(ds)

    wk.sgin(ds)
    wk.get_money(ds)
    #wk.get_box(ds)

    fqxs.sgin(ds)
    fqxs.get_money(ds)
    """

    bdct.get_box(ds)
    bdjs.get_box(ds)


try:
    # daily()

    # aqy.watch_video(ds)
    # pdd.watch_video(ds)
    # ks.watch_video(ds)

    # bdct.get_box(ds)
    # bdjs.get_box(ds)

    # dou_yin_ji_su_make_money()
    # pinduoduo_make_money()
    # jin_ri_toutiao_make_money()
    # kuaishou_make_money()

    # kuaishou_make_money()
    # dou_yin_ji_su_make_money()

except:
    u.send_notice('出错了!')
finally:
    # u.send_notice('完成!')
    pass
u.send_notice('完成!')
