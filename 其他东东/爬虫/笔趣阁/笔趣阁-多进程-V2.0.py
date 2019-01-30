import requests
from lxml import etree
import os
from multiprocessing import Pool,freeze_support
import mul_process_package

class Spider():
    def start_request(self):
        #请求拿到一级页面数据，小说名称创建文件夹
        response = requests.get("http://www.xbiquge.la/paihangbang/####")
        html = etree.HTML(response.text)
        #通过xpath获取小说名称text()为获取文本内容，@href为获取超链接
        Bigtit_list = html.xpath('//div[@class="box b3"][2]/ul[1]/li/a/text()')
        Bigsrc_list = html.xpath('//div[@class="box b3"][2]/ul[1]/li/a/@href')
        #创建进程池
        pool = Pool(8)
        #提取列表内容
        for Bigtit,Bigsrc in zip(Bigtit_list,Bigsrc_list):
            if os.path.exists(Bigtit) == False:
                os.mkdir(Bigtit)
            else:
                print("%s已存在，不再重复创建文件夹"%Bigtit)
            pool.apply_async(self.file_data, args=(Bigtit, Bigsrc))
            #self.file_data(Bigtit, Bigsrc)
        pool.close()
        pool.join()

    def file_data(self, Bigtit, Bigsrc):
        #请求拿到二级页面数据，抽取小说章节名及章节链接
        response = requests.get(Bigsrc)
        #response.encoding = 'utf-8';response.content； parser=etree.HTMLParser(encoding='utf-8')
        #以上代码可以指定编码方式，防止出现乱码
        response.encoding = 'utf-8'
        response.content
        html = etree.HTML(response.text, parser=etree.HTMLParser(encoding='utf-8'))
        Littit_list = html.xpath('//div[@id="list"]/dl/dd/a/text()')
        Litsrc_list = html.xpath('//div[@id="list"]/dl/dd/a/@href')
        i = 0
        for name, src in zip(Littit_list, Litsrc_list):
            if i < 10:
                name = "000" + str(i) + "-" + name
                print("===小于10===%s"%name)
                self.save(Bigtit, name, src)
                i += 1
            elif i < 100:
                name = "00" + str(i) + "-" + name
                print("===10<X<100===%s" % name)
                self.save(Bigtit, name, src)
                i += 1
            elif i < 1000:
                name = "0" + str(i) + "-" + name
                print("===100<X<1000===%s" % name)
                self.save(Bigtit, name, src)
                i += 1
            else:
                name = str(i) + "-" + name
                print("===X>1000===%s" % name)
                self.save(Bigtit, name, src)
                i += 1

    def save(self,Bigtit,name,src):
        #请求拿到三级页面数据，抽取文章内容，写入文件并保存到小说文件夹
        name = name.replace("\\", "").replace("?", "").replace("/", "").replace(":", "")
        #拼接路径，按照拼接后的路径将章节写入以小说名命名的文件夹内
        path = os.path.join(Bigtit, name) + ".txt"
        response = requests.get("http://www.xbiquge.la" + src)
        response.encoding = 'utf-8'
        response.content
        html = etree.HTML(response.text, parser=etree.HTMLParser(encoding='utf-8'))
        tit_list = html.xpath('//div[@id="content"]/text()')
        message = ''
        if os.path.exists(path):
            print(path + " is exists")
        else:
            i = 0
            for line in tit_list:
                if len(line) > 5:
                    message = message + line + "\n"
                    message.replace("    ", "").replace("\r", "")
                    #print(message)
            try:
                f = open(path, "w", encoding="utf-8")
                f.write(message)
                f.close()
            except Exception as e:
                print(e)
if __name__ == "__main__":
    freeze_support()
    s = Spider()
    s.start_request()