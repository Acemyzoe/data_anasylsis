import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import gc
import warnings
warnings.filterwarnings('ignore')
from datetime import datetime

def main():
    # 导入数据集
    df_orginal = pd.read_csv('./taobao_persona_1%.csv')

    "数据预处理"
    """ 1.数据抽样"""
    # 数据集太大，为了提高运行效率，只随机抽取20%的数据
    df = df_orginal.sample(frac=0.2,random_state=None)
    # df.to_csv("./taobao_persona_1%.csv",index=0)
    #回收内存
    del df_orginal
    # gc.collect()
    print(gc.collect())
    # """2.缺失值处理"""
    # df.info()
    # # 查看各字段的缺失值数量
    # print(df.isnull().sum())
    # # 只有user_geohash有缺失值，且缺失的比例很高，无统计分析的意义，将此列删除
    # df.drop('user_geohash',axis=1,inplace=True)
    
    # """3.日期与时段处理"""
    # #将time字段拆分为日期和时段
    # df['date'] = df['time'].str[0:10]
    # df['date'] = pd.to_datetime(df['date'],format='%Y-%m-%d')
    # df['time'] = df['time'].str[11:]
    # df['time'] = df['time'].astype(int)
    # #将时段分为'凌晨'、'上午'、'中午'、'下午'、'晚上'
    # df['hour'] = pd.cut(df['time'],bins=[-1,5,10,13,18,24],labels=['凌晨','上午','中午','下午','晚上'])
   
    # """制作用户标签表"""
    # #生成用户标签表，制作好的标签都加入这个表中
    # users = df['user_id'].unique()
    # labels = pd.DataFrame(users,columns=['user_id'])

    # "用户行为标签"
    # """用户浏览活跃时间段"""
    # #对用户和时段分组，统计浏览次数
    # time_browse = df[df['behavior_type']==1].groupby(['user_id','hour']).item_id.count().reset_index()
    # time_browse.rename(columns={'item_id':'hour_counts'},inplace=True)

if __name__ == "__main__":
    main()

