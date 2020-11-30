
import pandas as pd
import gc
import warnings
warnings.filterwarnings('ignore')
import memory_profiler

@pro
def main():
    # 导入数据集
    df_orginal = pd.read_csv('./taobao_persona.csv')
    df = df_orginal.sample(frac=0.2,random_state=None)
    # #回收内存
    # # del df_orginal
    # # gc.collect()

if __name__ == "__main__":
    main()