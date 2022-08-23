import requests

if __name__ == "__main__":
    # 每个cookie对应一个formhash, formhash是在签到按钮链接上的一个8位字符串
    formhash = {'user_a': '00e267f5',
                'user_b': '924148f7',
                }
    cookies = {'user_a': '',
               'user_b': '',
               }

    for name in formhash.keys():
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-language': 'en-US,en;q=0.9',
                   'cache-control': 'max-age=0',
                   'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
                   'cookie': cookies[name],
                   'refer': 'https://www.4ksj.com/qiandao/',
                   }
        url = 'https://www.4ksj.com//qiandao/?mod=sign&operation=qiandao&formhash=' + \
            formhash[name]+'&format=empty'

        response = requests.session().get(url, headers=headers)

        if "非法" in response.text:
            title = "💔4K世界cookie失效!"
        elif "今日已签" in response.text:
            title = "😁4K世界今日已签到!"

        print(name+title)
