import requests
import re
import traceback
import json

midlist = []


def write_filetitle(file_name):
    with open(file_name, "a", encoding="utf-8-sig") as f:
        f.write("up_id" + "," + "up_name" + "," + "video_title" + "," + "video_av" + "," + "up_date" + "," + \
                "watch_num" + "," + "subtitle_num" + "," + "comment_num" + "," + "up_type" + "," + "\n")


def get_html(url):
    """
    请求html文本数据
    """
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '返回异常!'


def parse_page(html):
    try:
        up_links = re.findall(r'a href=\"//space.bilibili.com/.*?\"', html)  # up主 主页链接
        up_names = re.findall(r'up-name\">.*?</a>', html)  # up主名字
        video_titles = re.findall(r'<a title=\".*?\"', html)  # 视频标题
        video_links = re.findall(r'a href=\"//www.bilibili.com/video/av.*?\"', html)  # 视频链接
        up_dates = re.findall(r'icon-date\"></i>.*?</span>', html, re.S)  # 视频上传日期
        watch_nums = re.findall(r'icon-playtime\"></i>.*?</span>', html, re.S)  # 观看人数
        subtitle_nums = re.findall(r'icon-subtitle\"></i>.*?</span>', html, re.S)  # 弹幕数
        for i in range(len(video_titles)):
            up_id = re.split(r'com/|\?from=search"', up_links[i])[1]  # 以ID前后字符分割
            up_name = re.split(r'">|</', up_names[i])[1]
            video_title = video_titles[i].split('"')[1]
            video_av = re.split(r'video/|\?from=search"', video_links[i])[1]
            up_date = re.split(r'\n', up_dates[i])[1]
            watch_num = re.split(r'\n', watch_nums[i])[1]
            subtitle_num = re.split(r'\n', subtitle_nums[i])[1]
            comment_num = "unknown"
            up_type = "A"
            with open("doctor_key_search.csv", "a", encoding='utf-8-sig') as f:
                f.write(
                    str(up_id) + "," + up_name + "," + video_title + "," + str(video_av) + "," + up_date + "," + str(
                        watch_num) + "," + str(subtitle_num) + "," + comment_num + "," + up_type + "\n")
            midlist.append(str(up_id))
        return midlist
        # print(midlist)
    except:
        print("解析数据异常")


def main():
    """
    以博士为关键词，请求50页的数据，print打印页面抓取速度
    """
    kw = 'Python'
    page = 5
    count = 0
    start_url = "https://search.bilibili.com/all?keyword=" + str(kw) + "&from_source=nav_search_new&page="
    for i in range(page):
        try:
            url = start_url + str(i + 1)
            html = get_html(url)
            parse_page(html)
            count += 1
            print('\r程序正在进行:{:.2f}%'.format(count * 100 / page), end="")
        except:
            count += 1
            print('\r程序正在进行:{:.2f}%'.format(count * 100 / page), end="")
            traceback.print_exc
            continue
    print("\n下载完成!\n")


if __name__ == '__main__':
    write_filetitle("doctor_key_search.csv")
    main()
