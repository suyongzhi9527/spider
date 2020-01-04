import requests
import re


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    resp = requests.get(url,headers = headers)
    text = resp.text
    titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>',text,re.DOTALL) # 列表类型
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall(r'<p class="source">.*?<span>.*?</span>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    content_tags = re.findall(r'<div class="contson".*?>(.*?)</div>',text,re.DOTALL)
    contents = []
    for content in content_tags:
        content = re.sub('<.*?>','',content)
        contents.append(content.strip())

    poems = []
    for value in zip(titles,dynasties,authors,contents):
        titles,dynasties,authors,contents = value
        poem = {
            'title':titles,
            'dynasties':dynasties,
            'authors':authors,
            'contents':contents
        }
        poems.append(poem)

    for poem in poems:
        print(poem)
        print("="*50)


def main():
    url = 'https://www.gushiwen.org/default_{}.aspx'
    # for i in range(1,11):
    #     url = 'https://www.gushiwen.org/default_%s.aspx' % i
    #     parse_page(url)
    for i in range(1,11):
        url = url.format(i)
        parse_page(url)


if __name__ == "__main__":
    main()
