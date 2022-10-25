#!/usr/bin/python3

import pymysql
import pandas as pd
from openpyxl import load_workbook


# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='user',
                     password='user',
                     database='gold')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


i = 1
while (i <= 38):

    workbook = load_workbook('./log.xlsx')
    sheet = workbook['Sheet' + str(i)]

    j = 8
    while (j <= 39):

        # print(sheet['B' + str(j)].value, sheet['D' + str(j)].value)
        if (sheet['B' + str(j)].value):
            types = sheet['B' + str(j)].value.split(' ')
            metal_type = types[0]
            money_type = types[1]
            is_buy = '1' if sheet['D' + str(j)].value == '买入' else '0'
            price = str(sheet['E' + str(j)].value)
            number = str(sheet['F' + str(j)].value)
            total_price = str(sheet['G' + str(j)].value)
            date = str(sheet['L' + str(j)].value).split('-')
            year = date[0]
            month = date[1]

            query = 'insert into record (metal_type, money_type, is_buy, price, number, total_price, year, month) values ("' + \
                metal_type + '","' + money_type + '",' + is_buy + ',' + \
                price + ',' + number + ',' + total_price + ',' + year + ',' + month + ' )'
            print(query)
            cursor.execute(query)
        else:
            print('----')  # .value.split(' '))
        j += 1

        # print(query)

        # cursor.execute(query)
    i += 1

# 关闭数据库连接
db.commit()
db.close()
