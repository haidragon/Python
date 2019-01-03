import requests
import json
import csv
from urllib.parse import urlencode
import time


def saveHtml(file_name, file_content):  # 保存conten对象为html文件
    with open(file_name.replace('/', '_') + '.html', 'wb') as f:
        f.write(file_content)


def GetData(url, writer):  # 解析并将数据保存为CSV文件
    response = requests.get(url)
    data = response.content
    saveHtml('zlzp', data)  # 保存html文件
    jsondata = json.loads(data)
    dataList = jsondata['data']['results']
    # print(jsondata)
    for dic in dataList:
        jobName = dic['jobName']  # 岗位名称
        company = dic['company']['name']  # 公司名称
        salary = dic['salary']  # 薪水
        city = dic['city']['display']  # 城市
        jobtype = dic['jobType']['display']  # 所属行业
        eduLevel = dic['eduLevel']['name']  # 学历要求
        workingExp = dic['workingExp']['name']  # 工作经验
        print(jobName, company, salary, city, jobtype, eduLevel, workingExp)
        writer.writerow([jobName, company, salary, city, jobtype, eduLevel, workingExp])


param = {'start': 0,
         'pageSize': 60,
         'cityId': 489,
         'workExperience': -1,
         'education': -1,
         'companyType': -1,
         'employmentType': -1,
         'jobWelfareTag': -1,
         'kw': '软件测试工程师',  # 搜索关键词，可以根据你需要爬取的岗位信息进行更换
         'kt': 3,
         'lastUrlQuery': {"p": 1, "pageSize": "60", "jl": "681", "kw": "python", "kt": "3"}
         }  # 参数配置
pages = range(1, 31)  # 爬取1-30页数据
out_f = open('test.csv', 'w', newline='')
writer = csv.writer(out_f)
writer.writerow(['jobName', 'company', 'salary', 'city', 'jobtype', 'eduLevel', 'workingExp'])
for p in pages:  # 自动翻页
    param['start'] = (p - 1) * 60
    param['lastUrlQuery']['p'] = p
    url = 'https://fe-api.zhaopin.com/c/i/sou?' + urlencode(param)
    print(url)
    GetData(url, writer)
    time.sleep(3)  # 间隔休眠3秒，防止IP被封
    print(p)
out_f.close()