import jieba.analyse
import re
from urllib import request
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}


# 分析网页函数
def getNowPlayingMovie_list():
    res = request.Request("https://movie.douban.com/nowplaying/hangzhou/", headers=headers)
    resp = request.urlopen(res)
    html_data = resp.read().decode("utf-8")

    # 解析网页
    soup = BeautifulSoup(html_data, "html.parser")

    nowplaying = soup.find_all("div", id="nowplaying")
    nowplaying_movie_list = nowplaying[0].find_all("li", class_="list-item")

    movie_list = list()

    for item in nowplaying_movie_list:
        movie_dict = {}  # 以字典形式存储每部电影的ID和名称
        movie_dict["id"] = item["data-subject"]
        for tag_img_item in item.find_all("img"):
            movie_dict["name"] = tag_img_item["alt"]
            movie_list.append(movie_dict)
    return movie_list


# 抓取电影评论函数
def getCommentById(movieId, page_num):
    if page_num > 0:
        start = (page_num - 1) * 20
    else:
        return False
    sub_url = "https://movie.douban.com/subject/" + movieId + "/comments?start=" + str(start) + "&limit=20"
    sub_res = request.Request(sub_url, headers=headers)
    sub_res_ = request.urlopen(sub_res)
    comment_data = sub_res_.read().decode("utf-8")
    soup = BeautifulSoup(comment_data, "html.parser")
    comment_div_list = soup.find_all("div", class_="comment")
    eachCommentList = list()
    for item in comment_div_list:
        if item.find_all("p")[0].find("span").string is not None:
            eachCommentList.append(item.find_all("p")[0].find("span").string)
    return eachCommentList


if __name__ == '__main__':
    commentList = list()
    movie_list = getNowPlayingMovie_list()
    for i in range(10):  # 前10页
        num = i + 1
        commentList_temp = getCommentById(movie_list[2]["id"], num)
        commentList.append(commentList_temp)

    # 将列表中的数据转换为字符串
    comments = ""
    for k in range(len(commentList)):
        comments = comments + (str(commentList[k])).strip()

    # 使用正则表达式去除标点符号
    pattern = re.compile(r"[\u4e00-\u9fa5]+")
    filterdata = re.findall(pattern, comments)
    cleaned_comments = "".join(filterdata)

    # 使用jieba分词进行中文分词
    results = jieba.analyse.textrank(cleaned_comments, topK=50, withWeight=True)
    keyword = dict()
    for i in results:
        keyword[i[0]] = i[1]
    print("删除停用词前:", keyword)

    # 用词云进行显示
    wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)
    word_frequence = keyword
    myword = wordcloud.fit_words(word_frequence)
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
