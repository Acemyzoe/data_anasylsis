'''def is_edu_id(ip: str) -> bool:
"""判断 ip 是否是教育网ip"""
# 1. 从 http://ipcn.chacuo.net/view/i_CERNET 获取教育网ip列表
# code
# 2. 判断 ip 是否是 教育网 ip
# code
pass
注：请注意是要实现该功能，完成后将py文件发送至luo.ziyang@ricequant.com（请备注名字）'''

#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: guojun
@datetime:2020/8/25 11：00
@software: Vscode
"""

import unittest

import requests
from fake_useragent import UserAgent
from lxml import etree


class Testlist(unittest.TestCase):
    ''' 功能测试'''
    def test_case1(self):
        self.assertEqual(is_edu_id('59.192.0.0'),True)

    def test_case2(self):
        self.assertEqual(is_edu_id('59.192.233.233'),True)

def is_edu_id(ip: str) -> bool:
    """判断 ip 是否是教育网ip"""
    # 1. 从 http://ipcn.chacuo.net/view/i_CERNET 获取教育网ip列表
    url = 'http://ipcn.chacuo.net/down/t_txt=c_CERNET'
    headers = {
        'User-Agent': UserAgent().random
    }
    resp = requests.get(url=url, headers=headers).content.decode('utf8')

    html = etree.HTML(resp)
    ips = html.xpath('/html/body/pre//text()')
    # ip_dict = [(ip.split('\t')[0],ip.split('\t')[1]) for ip in ips[0].split('\r\n') if ip ]
    ip_tuple = [(int(ip.split('\t')[0].split('.')[0])* 256 * 256 * 256+
                int(ip.split('\t')[0].split('.')[1])* 256 * 256+
                int(ip.split('\t')[0].split('.')[2])* 256+
                int(ip.split('\t')[0].split('.')[3]),
                int(ip.split('\t')[1].split('.')[0])* 256 * 256 * 256+
                int(ip.split('\t')[1].split('.')[1])* 256 * 256+
                int(ip.split('\t')[1].split('.')[2])* 256+
                int(ip.split('\t')[1].split('.')[3])
                )
               for ip in ips[0].split('\r\n') if ip]

    # 2. 判断 ip 是否是 教育网 ip

    # for iplist in ip_dict:
    #     if ip in IPy.IP('{}-{}'.format(iplist[0], iplist[1])):
    #         return True
    #     else:
    #         continue
    # return False

    ip_target = int(ip.split('.')[0])* 256 * 256 * 256+int(ip.split('.')[1])* 256 * 256 + int(ip.split('.')[2])* 256+int(ip.split('.')[3])
    for x,y in ip_tuple:
        if ip_target >= x and ip_target <= y:
            return True
        else:
            continue
    return False

if __name__ == '__main__':
    unittest.main()
