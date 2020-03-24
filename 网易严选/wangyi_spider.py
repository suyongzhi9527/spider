import requests
import time


def search_keyword(keyword):
    """
    获取商品ID
    """
    url = 'http://you.163.com/xhr/search/search.json'
    headers = {
        'Host': 'you.163.com',
        # 'Referer': 'http://you.163.com/search?keyword=%E6%96%87%E8%83%B8&timestamp=1585036172078&_stat_search=userhand&searchWordSource=1',
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/79.0.3945.117Safari/537.36'
    }
    query = {
        'page': 1,
        'keyword': keyword
    }
    try:
        response = requests.get(url, headers=headers, params=query).json()
        result = response['data']['directly']['searcherResult']['result']
        product_id = list()
        for i in result:
            product_id.append(i['id'])
        return product_id
    except Exception as e:
        print("出错了:%s" % e)


def details(product_id):
    """
    抓取商品评论数据
    """
    url = 'http://you.163.com/xhr/comment/listByItemByTag.json'
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/79.0.3945.117Safari/537.36'
    }
    try:
        comment_list = list()
        for i in range(1, 3):
            query = {
                'page': i,
                'itemId': product_id
            }
            response = requests.get(url, headers=headers, params=query).json()
            # print(response['data']['commentList'])
            if not response['data']['commentList'][0]:
                break
            print('正在抓取第 %s 页评论' % i)
            commentList = response['data']['commentList'][0]
            comment_list.append(commentList)
            time.sleep(1)
        return comment_list
    except Exception as e:
        print('出错了%s' % e)


def main():
    product_id = search_keyword("文胸")
    # print(product_id)
    comment_list = details(product_id)
    print(comment_list)


if __name__ == '__main__':
    main()
