import datetime
import requests

def get_weather():
    api_url = "https://v0.yiketianqi.com/api"
    params = {
        "unescape": "1",
        "version": "v91",
        "appid": "43656176",
        "appsecret": "I42og6Lm",
        "ext": "",
        "cityid": "",
        "city": "福安"
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    # 提取当天和第二天的天气信息
    print(data)
    today_weather = data["data"][0]
    tomorrow_weather = data["data"][1]

    # 解析当天天气信息
    today_date = today_weather["date"]
    today_week = today_weather["week"]
    today_weather_condition = today_weather["wea"]
    today_temperature = today_weather["tem"]
    today_humidity = today_weather["humidity"]
    today_wind = today_weather["win"][0]
    today_wind_speed = today_weather["win_speed"]

    # 解析第二天天气信息
    tomorrow_date = tomorrow_weather["date"]
    tomorrow_week = tomorrow_weather["week"]
    tomorrow_weather_condition = tomorrow_weather["wea"]
    tomorrow_temperature = tomorrow_weather["tem"]
    tomorrow_humidity = tomorrow_weather["humidity"]
    tomorrow_wind = tomorrow_weather["win"][0]
    tomorrow_wind_speed = tomorrow_weather["win_speed"]
    # 提取当天和第二天的天气数据
    today_weather = data['data'][0]
    tomorrow_weather = data['data'][1]

    # 获取当天和第二天的日期、天气和温度
    today_date = today_weather['date']
    today_wea = today_weather['wea']
    today_tem = today_weather['tem2']
    today_tem1 = today_weather['tem1']

    tomorrow_date = tomorrow_weather['date']
    tomorrow_wea = tomorrow_weather['wea']
    tomorrow_tem = tomorrow_weather['tem2']
    tomorrow_tem1 = tomorrow_weather['tem1']

    if '大雨' in today_wea or '大雨' in tomorrow_wea:
        tips = '今天和明天有大雨，请注意出行安全，记得带好雨具。'
    elif '小雨' in today_wea or '小雨' in tomorrow_wea:
        tips = '今天和明天有小雨，记得带好雨具，注意防雨滑。'
    elif '雷暴' in today_wea or '雷暴' in tomorrow_wea:
        tips = '今天和明天可能有雷暴天气，请尽量减少户外活动，注意安全。'
    elif '阴' in today_wea or '阴' in tomorrow_wea:
        tips = '今天和明天阴天，心情可能会有些低落，记得调节心态，保持愉快心情。'
    else:
        tips = '今天和明天的天气情况较为平稳，请合理安排活动，享受美好时光。'

    weather_emotions = {
        "晴": ("天气晴朗", "(*^ω^*)"),
        "阴": ("天气阴沉", "(=^-ω-^=)"),
        "多云": ("天空有些多云", "(=^･ｪ･^=)"),
        "雨": ("下雨了", "╮(╯_╰)╭"),
        "雪": ("下雪了", "ฅ(＾・ω・＾ฅ)"),
        "雾": ("有雾气弥漫", "≧ω≦"),
        "霾": ("有霾天气", "(๑•̀ㅂ•́)و✧"),
        "雷阵雨": ("有雷阵雨", "(≧▽≦)"),
        "小雨": ("有小雨", "⊂((・▽・))⊃"),
        "中雨": ("有中雨", "(/ω＼)"),
        "大雨": ("有大雨", "Σ( ° △ °|||)"),
        "暴雨": ("有暴雨", "(」°ロ°)」"),
    }
    # 根据天气选择对应的语气词和表情
    if "转" in today_wea:
        today_wea = today_wea.split("转")[0]
    if "转" in tomorrow_wea:
        today_wea= tomorrow_wea.split("转")[0]
    today_emotion = weather_emotions.get(today_wea, ("天气", "(=^-ω-^=)"))
    tomorrow_emotion = weather_emotions.get(tomorrow_wea, ("天气", "(=^･ｪ･^=)"))


    # 获取当前日期
    current_date = datetime.date.today()


    # 星期几对应的中文名称
    weekday_dict = {
        0: "星期一",
        1: "星期二",
        2: "星期三",
        3: "星期四",
        4: "星期五",
        5: "星期六",
        6: "星期日",
    }

    # 获取当前日期对应的星期几
    weekday = weekday_dict[current_date.weekday()]


    # 输出天气信息和温馨提示
    result = f'今天是{today_date}, {weekday}，天气{today_wea}，温度{today_tem}~{today_tem1}℃。{today_emotion[1]}\n' +  f'明天天气{tomorrow_wea}，温度{tomorrow_tem}~{tomorrow_tem1}℃。{tomorrow_emotion[1]}'
    result += "\n温馨提示：{}".format(tips)
    return result

if __name__ == '__main__':
    a = get_weather()
    print(a)

