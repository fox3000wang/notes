# -*- coding:utf-8 -*-
import cmath

if __name__ == "__main__":

    # 输入
    target = 100
    b = [30, 40, 40, 40, 100]
    l = len(b)

    sum = 0
    for v in b:
        sum += v
    print('sum', sum)

    # 平均值
    avg = sum / l
    print('avg', avg)

    # 方差
    ssum = 0
    for v in b:
        ssum += v * v
    va = ssum / l - (avg) * (avg)
    print('va', va)

    # 标准差
    sd = cmath.sqrt(va)
    print('sd', sd)

    # 偏差值
    dev = 50 + (target - avg) / sd * 10
    print('dev', dev)
