import requests


headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}


def get_json(url):
    params = {
        'page_size': 10,
        'next_offset':str(num),
        'tag': '今日热门',
        'platform': 'pc'
    }

    try:
        html = requests.get(url,params=params, headers=headers)
        return html.json()
    except Exception as e:
        print("flase")

def downloader(url,path):
    response = requests.get(url,headers=headers, stream=True)
    chunk_size = 1024

    #获取视频总大小
    content_size = int(response.headers['content-length'])
    print(content_size)

    if response.status_code == 200:
        print('[文件大小]:%0.2f MB'%(content_size/chunk_size/chunk_size))
        #文件操作
        with open(path,'wb') as f:
            for data in response.iter_content(chunk_size=chunk_size):
                f.write(data)
                #size += len(data)

if __name__ == '__main__':
    for i in range(12):
        url = 'http://api.vc.bilibili.com/board/v1/ranking/top?'
        num = i * 10 + 1
        html = get_json(url)
        infos = html['data']['items']
        for info in infos:
            title = info['item']['description']
            #
            video_url = info['item']['video_playurl']
            print(title)

            try:
                if 'high five' in title:
                    downloader(video_url,path='H:/BaiduNetdiskDownload/Bilibili/%s.mp4'%title)
                    print('下载成功')
            except Exception as e:
                print('下载失败')