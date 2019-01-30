import requests
from lxml import etree
import os

class Spider():
    def start_request(self):
        #请求拿到一级页面数据，小说名称创建文件夹
        response = requests.get("https://www.qidian.com/all")
        html = etree.HTML(response.text)
        #通过xpath获取小说名称text()为获取文本内容，@href为获取超链接
        Bigtit_list = html.xpath('//div[@class="book-mid-info"]/h4/a/text()')
        Bigsrc_list = html.xpath('//div[@class="book-mid-info"]/h4/a/@href')
        #提取列表内容
        for Bigtit,Bigsrc in zip(Bigtit_list,Bigsrc_list):
            if os.path.exists(Bigtit) == False:
                os.mkdir(Bigtit)
            self.file_data(Bigtit, Bigsrc)

    def file_data(self, Bigtit, Bigsrc):
        #请求拿到二级页面数据，抽取小说章节名及章节链接
        response = requests.get("http:"+Bigsrc)
        html = etree.HTML(response.text)
        Littit_list = html.xpath('//ul[@class="cf"]/li/a/text()')
        Litsrc_list = html.xpath('//ul[@class="cf"]/li/a/@href')
        #print(Littit_list, Litsrc_list)
        for name, src in zip(Littit_list, Litsrc_list):
            #if os.path.exists(Bigtit) == False:
            self.save(Bigtit, name, src)

    def save(self,Bigtit,name,src):
        #请求拿到三级页面数据，抽取文章内容，写入文件并保存到小说文件夹
        name = name.replace("\\", "").replace("?", "").replace("/", "").replace(":", "")
        path = os.path.join(Bigtit, name) + ".txt"
        response = requests.get("http:" + src)
        html = etree.HTML(response.text)
        tit_list = html.xpath('//div[@class="read-content j_readContent"]/p/text()')
        message = ''
        if os.path.exists(path):
            print(path + " is exists")
        else:
            for line in tit_list:
                message = message + line + "\n"
                #message.replace(r"　　", "")
            try:
                f = open(path, "w", encoding="utf-8")
                f.write(message)
                f.close()
            except Exception as e:
                print(e)


if __name__ == "__main__":
    #防止出现Max retries exceeded with url错误
    #增加重试连接次数
    requests.adapters.DEFAULT_RETRIES = 5
    #关闭多余的连接,requests使用了urllib3库，默认的http connection是keep-alive的，requests设置False关闭。
    s = requests.session()
    s.keep_alive = False

    spider = Spider()
    spider.start_request()
