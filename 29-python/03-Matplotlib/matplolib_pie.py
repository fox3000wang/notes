# -*- coding:utf-8 -*-
import pymysql
import matplotlib.pyplot as plt
import numpy as np
import math


def getData():

    db = pymysql.connect(host='localhost',
                         user='user',
                         password='user',
                         database='gold')
    cursor = db.cursor()
    query = "select  money_type, metal_type, is_buy,  sum(total_price) from record group by metal_type, money_type, is_buy order by is_buy, money_type, metal_type;"
    result = cursor.execute(query)
    data = list(cursor.fetchall())
    db.close()
    return data
    # [('人民币', '白银', 0, Decimal('483541.05')), ('人民币', '黄金', 0, Decimal('223502.70')), ('美元', '白银', 0, Decimal('38914.39')), ('美元', '黄金', 0, Decimal('9554.67')), ('人民币', '白银', 1, Decimal('482443.00')), ('人民币', '黄金', 1, Decimal('218192.59')), ('美元', '白银', 1, Decimal('38676.89')), ('美元', '黄金', 1, Decimal('9463.31'))]


data = getData()

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('equal')

type = []
price = []
# ('人民币', '白银', 0, Decimal('483541.05'))
for d in data:
    if d[2] == 0:
        type.append("卖出" + d[0] + d[1])
        price.append(d[3])
    if d[2] == 1:
        type.append("买入" + d[0] + d[1])
        price.append(d[3])

ax.pie(price, labels=type, autopct='%1.2f%%')
plt.show()
