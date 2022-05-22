# @Time : 2022/5/22 18:23 
# @Author : Jface 
# @coding: utf8

import json
import pandas as pd

path = r"/Users/jface/PycharmProjects/datas/2018record3.jsons"
data = []

############################################# 解析 json 数据文件 ##########################################################
with open(path, "r", encoding='utf-8') as f:
    for line in f.readlines():
        data += json.loads(line)['data']

data = pd.DataFrame(data)
# 调整字段顺序
columns = ['card_no', 'deal_date', 'deal_type', 'deal_money', 'deal_value', 'equ_no', 'company_name', 'station',
           'car_no', 'conn_mark', 'close_date']
data = data[columns]  # 调整字段顺序
data.info()

############################################# 输出处理 ##########################################################
# 全部都是 交通运输 的刷卡数据
print(data['company_name'].unique())

# 删除重复值
data.drop_duplicates(inplace=True)
data.reset_index(drop=True, inplace=True)

# 去除脏数据
data = data[data['deal_date'] > '2018-08-31']

# 数据保存为 csv
data.to_csv('SZTcard.csv', index=False, header=None)
