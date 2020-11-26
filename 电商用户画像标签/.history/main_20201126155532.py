import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import gc
import warnings
warnings.filterwarnings('ignore')
from datetime import datetime

def main():
    # 导入数据集
    df_orginal = pd.read_csv('./taobao_persona.csv')

    ### 数据预处理
    # 数据抽样
    # 数据集太大，为了提高运行效率，只随机抽取20%的数据
    df = df_orginal.sample(frac=0.2,random_state=None)

