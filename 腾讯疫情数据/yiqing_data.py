import requests
import json
import pymysql
import time
import traceback  # 跟踪异常


def get_conn():
    """
    :return 连接，游标
    """
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        database='cov',
        port=3306
    )
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def get_tencent_history_data():
    """
    :return 返回历史数据
    """
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'
    headers = {
        'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/79.0.3945.117Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    res = json.loads(r.text)
    data_all = json.loads(res['data'])
    history = {}  # 保存历史数据
    for i in data_all['chinaDayList']:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}
    for i in data_all["chinaDayAddList"]:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds].update({"confirm_add": confirm, "suspect_add": suspect, "heal_add": heal, "dead_add": dead})
    return history


def insert_history():
    """
    插入历史数据
    """
    cursor = None
    conn = None
    try:
        dic = get_tencent_history_data()
        print(f"{time.asctime()}开始插入数据")
        conn, cursor = get_conn()
        sql = "insert into history values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for k, v in dic.items():
            cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get("suspect"),
                                 v.get("suspect_add"),v.get("heal"), v.get("heal_add"),
                                 v.get("dead"), v.get("dead_add")])
        conn.commit()
        print(f"{time.asctime()}插入历史数据完成!")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def update_history():
    """
    更新历史数据
    """
    cursor = None
    conn = None
    try:
        dic = get_tencent_history_data()
        print(f"{time.asctime()}开始更新历史数据")
        conn, cursor = get_conn()
        sql = "insert into history values (%s,%s,%s,%s,%s,%s,%s,%s,%s,)"
        sql_query = "select confirm from history where ds = %s"
        for k, v in dic.items():
            if not cursor.execute(sql_query, k):
                cursor.execute(sql, [k, v.get("conffirm"), v.get("confirm_add"), v.get("suspect"), v.get("suspect_add"),
                                     v.get("heal"), v.get("heal_add"), v.get("dead"), v.get("dead_add")])
        conn.commit()
        print(f"{time.asctime()}历史数据更新完成!")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def get_tencent_data():
    """
    :return 返回当日详细数据
    """
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    headers = {
        'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/79.0.3945.117Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    json_data = json.loads(resp.text)
    all_data = json.loads(json_data['data'])
    detail = []  # 当日详细数据
    update_time = all_data['lastUpdateTime']
    data_country = all_data['areaTree']  # 所有国家列表
    data_province = data_country[0]['children']  # 中国所有省份
    for pro_infos in data_province:
        province = pro_infos['name']  # 省名
        for city_infos in pro_infos['children']:
            city = city_infos['name']  # 城市名
            confirm = city_infos['total']['confirm']
            confirm_add = city_infos['today']['confirm']
            heal = city_infos['total']['heal']
            dead = city_infos['total']['dead']
            detail.append([update_time, province, city, confirm, confirm_add, heal, dead])
    return detail


def update_detail():
    """
    更新 details表
    """
    cursor = None
    conn = None
    try:
        li = get_tencent_data()
        conn, cursor = get_conn()
        sql = "insert into details(update_time, province, city, confirm, confirm_add, heal, dead) values (%s, %s, %s, %s, %s, %s, %s)"
        sql_query = "select %s=(select update_time from details order by id desc limit 1)"
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新最新数据")
            for item in li:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}更新数据完成")
        else:
            print(f"{time.asctime()}已是最新数据")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == '__main__':
    # detail = get_tencent_data()
    # update_detail()
    # get_tencent_history_data()
    insert_history()
