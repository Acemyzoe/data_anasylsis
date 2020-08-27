import http.client
import re
import IPy


def get_html(host, path):
    conn = http.client.HTTPConnection('ipcn.chacuo.net')
    conn.request("GET", '/view/i_CERNET')
    res = conn.getresponse()
    return res.read().decode("utf-8")


def is_edu_ip(ip: str) -> bool:
    # 1. 获取教育网IP列表
    html = get_html('ipcn.chacuo.net', '/view/i_CERNET')
    res = re.findall(r'<span class="v_l">(.*)</span><span class="v_r">(.*)</span>', html)
    # 2. 判断当前ip是否在教育网IP中
    for iplist in res:
        if ip in IPy.IP('{}-{}'.format(iplist[0], iplist[1])):
            return True
        else:
            continue
    return False


if __name__ == '__main__':
    print(is_edu_ip('22.38.65.21'))
    print(is_edu_ip('202.38.65.21'))
    print(is_edu_ip('202.38.65.21'))