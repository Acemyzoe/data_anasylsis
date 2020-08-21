import json
import os

import openpyxl
import pandas as pd
import requests
from pyecharts.charts import Bar,Map
from pyecharts import options as opts


def get_data():
    china_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'  #爬取网页的ＵＲＬ
    header = {
        'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    response = requests.get(china_url,header).json()         
    '''
    有些网页采用了一些反爬措施，使用上述代码爬取网页可能会返回403的状态码
    可以通过设置header绕过
    header格式　header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    此时　response = requests.get(url,headers=header) 
    '''
    # print(response.encoding)              #查看网页编码格式
    # response.encoding = 'utf-8'           #网页编码格式设置为utf8
    # print(response.headers)               #查看网页头信息
    # print(response.url)                   #查看网页返回的地址
    # print(response.status_code)           #查看网页返回的状态码    
    # print(response.text)                  #查看网页内容  

    # 保存数据
    data = json.loads(response['data'])
    with open('./国内疫情.json','w') as f:
        f.write(json.dumps(data,indent=2,ensure_ascii=False))

def data2excel():
    with open('./国内疫情.json','r',encoding='utf-8') as f:
        data = f.read()
    data = json.loads(data)
    # 获取国内所有数据
    chinaAreaDict = data['areaTree'][0]
    # 获取所有省份数据
    provinceList = chinaAreaDict['children']
    # print(len(provinceList)) # >34
    chinacity_list = []
    for x in range(len(provinceList)):
        province = provinceList[x]['name']
        province_list = provinceList[x]['children'] # 每个市的数据
        for y in range(len(province_list)):
            city = province_list[y]['name']
            today = province_list[y]['today']
            total = province_list[y]['total']
            city_dict = {
                'province':province,
                'city':city,
                'today':today,
                'total':total
            }
            chinacity_list.append(city_dict)
    chinaTotalData = pd.DataFrame(chinacity_list)

    # 将chinaTotalData的total、today数据添加至DataFrame
    nowConfirmlist = []
    confirmlist = []
    suspectlist = []
    deadlist = []
    heallist = []
    deadRatelist = []
    healRatelist = []
    for value in chinaTotalData['total'].values.tolist():
        nowConfirmlist.append(value['nowConfirm'])
        confirmlist.append(value['confirm'])
        suspectlist.append(value['suspect'])
        deadlist.append(value['dead'])
        heallist.append(value['heal'])
        deadRatelist.append(value['deadRate'])
        healRatelist.append(value['healRate'])
    chinaTotalData['nowConfirm'] = nowConfirmlist
    chinaTotalData['confirm'] = confirmlist
    chinaTotalData['suspect'] = suspectlist
    chinaTotalData['dead'] = deadlist
    chinaTotalData['heal'] = heallist
    chinaTotalData['deadRate'] = deadRatelist
    chinaTotalData['healRate'] = healRatelist

    chinaTotalData.drop(['total','today'],axis=1,inplace=True)

    #保存至excel
    book = openpyxl.load_workbook('国内疫情.xlsx',read_only=False)
    writer = pd.ExcelWriter('国内疫情.xlsx',engine='openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title,ws) for ws in book.worksheets)
    chinaTotalData.to_excel(writer,index=False)
    writer.save()
    writer.close()

def drawmap():
    df = pd.read_excel('国内疫情.xlsx')
    data = df.groupby(by='province',as_index=False).sum()
    data_list = list(zip(data['province'].values.tolist(),data['confirm'].values.tolist()))
    def map_china() -> Map:
        c = (
            Map()
            .add(series_name='确诊病例',data_pair=data_list,maptype='china')
            .set_global_opts(
                title_opts=opts.TitleOpts(title='疫情地图'),
                visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                pieces=[
                    {"max":9,"min":0,"label":"0-9","color":"#FFE4E1"},
                    {"max":99,"min":10,"label":"10-99","color":"#FF7F50"},
                    {"max":499,"min":100,"label":"100-499","color":"#F08080"},
                    {"max":999,"min":500,"label":"500-999","color":"#CD5C5C"},
                    {"max":9999,"min":1000,"label":"1000-9999","color":"#990000"},
                    {"max":99999,"min":10000,"label":"10000-99999","color":"#660000"}
                ])

            )

        )
        return c

    d_map = map_china()
    d_map.render(path="./国内疫情地图.html")


if __name__ == "__main__":
    drawmap()
