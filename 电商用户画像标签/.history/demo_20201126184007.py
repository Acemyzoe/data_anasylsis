import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import gc
import warnings
warnings.filterwarnings('ignore')
from datetime import datetime
# 导入数据集
df_orginal = pd.read_csv('./taobao_persona.csv')
#回收内存
del df_orginal
gc.collect()