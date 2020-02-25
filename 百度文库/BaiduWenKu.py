import requests
import re
import json
import os

session = requests.session()


def parse_url(url):
    # print(session.get(url).content.decode('gbk'))
    return session.get(url).content.decode('gbk')


def get_doc_id(url):
    # https://wenku.baidu.com/view/35b09185ba68a98271fe910ef12d2af90242a88d.html?from=search
    doc_id = re.findall(r'view/(.*).html', url)[0]
    return doc_id


def parser_type(content):
    type = re.findall(r'\'docType\'\: \'(.*?)\'\,', content)[0]
    return type


def parser_title(content):
    title = re.findall(r'\'title\'\: \'(.*?)\'\,', content)[0]
    return title


def parser_txt(doc_id):
    content_url = 'https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=' + doc_id
    content = parse_url(content_url)

    # print(content)
    md5 = re.findall(r'"md5sum":"(.*?)"', content)[0]
    pn = re.findall(r'"totalPageNum":"(.*?)"', content)[0]
    rsgin = re.findall(r'"rsign":"(.*?)"', content)[0]

    content_urls = 'https://wkretype.bdimg.com/retype/text/' + doc_id + '?rn=' + pn + '&type=txt' + md5 + '&rsign=' + rsgin
    content = json.loads(parse_url(content_urls))
    result = ''
    for item in content:
        for i in item['parags']:
            result += i['c'].replace('\\r', '\r').replace('\\n', '\n')
    return result


def save_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        print('已保存:' + filename)


def parser_other(doc_id):
    content_url = 'https://wenku.baidu.com/browse/getbcsurl?doc_id=' + doc_id + '&pn=1&rn=99999&type=ppt'
    content = parse_url(content_url)
    url_list = re.findall(r'{"zoom":"(.*?)","page"', content)
    url_list = [item.replace("\\", "") for item in url_list]
    if not os.path.exists(doc_id):
        os.mkdir(doc_id)
    for index, url in enumerate(url_list):
        content = session.get(url).content
        path = os.path.join(doc_id, str(index) + '.jpg')
        with open(path, 'wb') as f:
            f.write(content)
    print("图片保存在" + doc_id + "文件夹")


if __name__ == '__main__':
    url = input('请输入要下载的文库地址:')
    content = parse_url(url)
    doc_id = get_doc_id(url)
    type = parser_type(content)
    title = parser_title(content)
    if type == 'txt':
        result = parser_txt(doc_id)
        save_file(title + '.txt', result)
    else:
        parser_other(doc_id)
