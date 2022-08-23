import requests

if __name__ == "__main__":
    url = 'https://www.latexstudio.net/api/Sign/Sign'
    cookie = ''
    header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
              'Cookie': cookie, }

    response = requests.post(url, headers=header)
    print(response.text)

    if "已签到" or "积分" in response.text:
        title = "latex-studio今日签到成功!"
    else:
        title = "latex-studio今日签到失败!"
