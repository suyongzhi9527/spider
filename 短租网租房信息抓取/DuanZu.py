import requests


def main():
    url = 'https://www.airbnb.cn/api/v2/explore_tabs?_format=for_explore_search_web&auto_ib=true&client_' \
          'session_id=5e65a94b-923c-4164-9dc9-e49aba271bb5&currency=CNY&current_tab_id=all_tab&experiences_per' \
          '_grid=20&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&hide_dates_and_guests' \
          '_filters=false&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_per_grid=' \
          '18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=zh&metadata_only=false&query=Shenzhen%2C%20China&query_' \
          'understanding_enabled=true&refinement_paths%5B%5D=%2Ffor_you&satori_version=1.1.13&screen_height=150' \
          '&screen_size=large&screen_width=1366&selected_tab_id=all_tab&show_groupings=true&supports_for_you_v3=' \
          'true&timezone_offset=480&version=1.7.0'
    headers = {
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.117Safari / 537.36'
    }
    text = requests.get(url,headers=headers).json()
    data_list = text['explore_tabs'][0]['sections'][1]['listings']
    for data in data_list:
        data_item = {}
        data_item['name'] = data['listing']['name']  # 房源名称
        data_item['price'] = data['pricing_quote']['price_string']  # 价格
        data_item['preview'] = data['listing']['preview_tags'][0]['name']  # 评价数量
        data_item['guest_label'] = data['listing']['guest_label']  # 房客数量
        data_item['kicker_content'] = '-'.join(data['listing']['kicker_content']['messages'])  # 房屋类型

        print(data_item)


if __name__ == '__main__':
    main()