import requests
import parsel
import tomd
import re


def download_article(article_url):
    response = requests.get(article_url)
    html = response.text
    sel = parsel.Selector(html)
    title = sel.css('.title-article::text').get()
    content = sel.css('article').get()

    md_text = tomd.Tomd(content).markdown
    md_text = re.sub(r'<a.*?a>', '', md_text)
    print(title)
    # print(md_text)

    with open(title + '.md', 'w', encoding='utf-8') as f:
        f.write('#' + title)
        f.write(md_text)


# article_url = 'https://blog.csdn.net/fei347795790/article/details/103744586'
# download_article(article_url)

def down_user():
    user_name = 'fei347795790'
    page = 1
    while True:
        index_url = 'https://blog.csdn.net/{}/article/list/{}'.format(user_name, page)
        response = requests.get(index_url)
        html = response.text
        sel = parsel.Selector(html)
        urls = sel.css('.article-list a::attr(href)').getall()
        # print(urls)
        if not urls:
            break
        for url in urls:
            print(url)
            # download_article(url)
        page += 1
        print("第",page,"页")


down_user()
