import requests
import json
from pyecharts.charts import Map, Geo
from pyecharts import options as opt
from pyecharts.globals import GeoType, RenderType

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
# 模拟浏览器访问url
dict_data = json.loads(requests.get(url).json()['data'])
# print(resp.text)
china = dict_data['areaTree'][0]['children']
# print(china)

china_total = "确诊:" + str(dict_data['chinaTotal']['confirm']) + \
              "疑似:" + str(dict_data['chinaTotal']['suspect']) + \
              "死亡:" + str(dict_data['chinaTotal']['dead']) + \
              "治愈:" + str(dict_data['chinaTotal']['heal']) + \
              "更新日期:" + str(dict_data['lastUpdateTime'])

data = []
for i in range(len(dict_data)):
    data.append([china[i]['name'], china[i]['total']['confirm']])
print(data)

geo = Geo(init_opts=opt.InitOpts(width="1200px", height="600px", bg_color="#404a59", page_title="全国疫情实时报告",
                                 renderer=RenderType.SVG, theme="white"))  # 绘制尺寸，背景色
geo.add_schema(maptype="china", itemstyle_opts=opt.ItemStyleOpts(color="rgb(49,60,72)", border_color="rgb(0,0,0)"))
geo.add(series_name="geo", data_pair=data, type_=GeoType.EFFECT_SCATTER)  # 设置地图数据，动画方式为涟漪特效
geo.set_series_opts(label_opts=opt.LabelOpts(is_show=False), effect_opts=opt.EffectOpts(scale=6))
geo.set_global_opts(visualmap_opts=opt.VisualMapOpts(min_=0, max_=349),
                    title_opts=opt.TitleOpts(title="全国疫情地图", subtitle=china_total, pos_left="center", pos_top="10px"))
geo.render("render.html")
