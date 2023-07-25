import re
import time

import requests
from bs4 import BeautifulSoup
import pickle

def spider_it_daily():

    url = "https://next.ithome.com/"

    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'Hm_lvt_cfebe79b2c367c4b89b285f412bf9867=1689445927; Hm_lvt_f2d5cbe611513efcf95b7f62b934c619=1689445988; Hm_lpvt_f2d5cbe611513efcf95b7f62b934c619=1689800967; Hm_lpvt_cfebe79b2c367c4b89b285f412bf9867=1689800967',
        'Pragma': 'no-cache',
        'Referer': 'https://www.ithome.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except:
        return None
    res = response.text
    soup = BeautifulSoup(res, 'lxml')
    soups = soup.find_all(name='div', attrs={'class': 'c'})
    news_li = []

    for s in soups:
        # print(s)
        # break
        # print(s.a["href"])
        # print(s.text)
        news_li.append(s.h2.a.text+ "\n"+s.h2.a.get("href"))
    # print(news_li)
    try:
        with open('spider_it_daily.txt', 'rb') as f:
            cjb = pickle.load(f)
    except:
        cjb = {}
        # print(cjb)

    news = []
    for item in news_li:
        if item not in cjb:
            news.append(item)
    with open('spider_it_daily.txt', 'wb') as f:
        pickle.dump(news_li, f)
    news_message = ""
    if news == []:
        return None
    for i in range(len(news)):
        if len(news) > 1:
            add_string = str(i+1)+"."
        else:
            add_string = ""
        news_message += f"{add_string}{news[i]}\n"
    news_message += "from :https://www.ithome.com/"
    return news_message


def spider_venturebeat():

    url = "https://venturebeat.com/"

    payload = {}
    headers = {
        'authority': 'venturebeat.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'cookie': 'lux_uid=168979767859713138; _gcl_au=1.1.1410204182.1689797685; _ga=GA1.2.1270589347.1689797686; _gid=GA1.2.1098377494.1689797688; _au_1d=AU1D-0100-001689797688-RSRVET9R-C7P7; _au_last_seen_pixels=eyJhcG4iOjE2ODk3OTc2ODgsInR0ZCI6MTY4OTc5NzY4OCwicHViIjoxNjg5Nzk3Njg4LCJydWIiOjE2ODk3OTc2ODgsInRhcGFkIjoxNjg5Nzk3Njg4LCJhZHgiOjE2ODk3OTc2ODgsImdvbyI6MTY4OTc5NzY4OCwiY29sb3NzdXMiOjE2ODk3OTc2ODgsInNtYXJ0IjoxNjg5Nzk3Njg4LCJhZG8iOjE2ODk3OTc2ODh9; _mkto_trk=id:673-PHK-948&token:_mch-venturebeat.com-1689797690430-56350; ln_or=eyIzMDg2OTgwLDQwMTA0MTgiOiJkIn0%3D; __qca=P0-1537604844-1689797684357; _fbp=fb.1.1689797692714.444382781; _ga_B8TDS1LEXQ=GS1.1.1689797686.1.0.1689797702.44.0.0',
        'pragma': 'no-cache',
        'referer': 'https://link.zhihu.com/?target=https%3A//venturebeat.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except:
        return None
    res = response.text
    soup = BeautifulSoup(res, 'lxml')
    soups = soup.find_all(name='a', attrs={'class': 'ArticleListing__title-link'})
    news_li = []

    for s in soups:
        # print(s)
        # break
        # print(s.a["href"])
        # print(s.text)
        news_li.append(s.get("title")+ "\n"+s.get("href"))
    # print(news_li)
    try:
        with open('venturebeat.txt', 'rb') as f:
            cjb = pickle.load(f)
    except:
        cjb = {}
        # print(cjb)


    news = []
    for item in news_li:
        if item not in cjb:
            news.append(item)
    with open('venturebeat.txt', 'wb') as f:
        pickle.dump(news_li, f)
    news_message = ""
    if news==[]:
        return None
    for i in range(len(news)):
        if len(news) > 1:
            add_string = str(i+1) + "."
        else:
            add_string = ""
        news_message += f"{add_string}{news[i]}\n"
    news_message += "from :https://www.venturebeat.com/"
    return news_message


def spider_techcruch():
    url = "https://techcrunch.com/category/artificial-intelligence/"

    payload={}
    headers = {
      'authority': 'techcrunch.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
      'cache-control': 'no-cache',
      'pragma': 'no-cache',
      'referer': 'https://www.bing.com/',
      'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    except Exception as file:
        return None
    res = response.text
    soup = BeautifulSoup(res, 'lxml')
    soups = soup.find_all(name='h2', attrs={'class': 'post-block__title'})
    news_li = []
    for s in soups:
        # print(s)
        # print(s.a["href"])
        # print(s.text)
        news_li.append(s.text.strip()+ "\n"+s.a.get("href"))
    # print(news_li)
    news_li = news_li[:7]
    news_message = ""
    for i in range(len(news_li)):
        news_message += f"{i+1},{news_li[i]}\n"
    news_message += "from :https://techcrunch.com/category/artificial-intelligence/"
    return news_message

def spider_inner():

    url = "https://www.ithome.com/block/rank.html?d=it"

    payload = {}
    headers = {
        'authority': 'www.ithome.com',
        'accept': 'text/html, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'origin': 'https://it.ithome.com',
        'pragma': 'no-cache',
        'referer': 'https://it.ithome.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79'
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except:
        return None
    res = response.text
    # print(res)

    soup = BeautifulSoup(res, 'lxml')
    soups = soup.find(name='ul', attrs={'id': 'd-2'}).find_all(name='a', attrs={'target': '_blank'})
    news_li = []
    for s in soups:

        # print(s.a["href"])
        # print(s.text)
        news_li.append(s.text.strip())
    # print(news_li)
    news_li = news_li[:7]
    news_message = ""
    for i in range(len(news_li)):
        news_message += f"{i+1},{news_li[i]}\n"
    news_message += "from :https://it.ithome.com/ 周榜"
    # print(news_message)
    return news_message

def spider_jiqizhixin():

    url = "https://www.jiqizhixin.com/"

    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'ahoy_visitor=91058804-91a7-48ad-b0c6-e591dc322ffd; ahoy_visit=e240accb-57d8-49fa-adf7-b7acea083cf8; _ga=GA1.2.1752699788.1689511312; _gid=GA1.2.1023103424.1689511312; _ga_R78HWX068N=GS1.2.1689511313.1.0.1689511313.60.0.0; _Synced_session=kGCPUMhUDGvNC%2F5Z0cXevLL2iNiw8qWribAo9CJ5sroNGrdetyWyBJgqGEZtO7T%2BnBZvUUB3hKC4o7dD%2B2lOtzI5kY6X43lTNkY%2B9Qk9VuSbUt%2FJw2h7NsIiFi9NdUUqx0IsWFdAt%2BpQ8vSXIdQkN8%2BToPk4oBeEimWJqG8H5n0xEi2GUOtAr1b6eDXhuxEOxBvPC352%2Btih8ULKuIHulYTp%2FKzUxZfPp77h4c3BiXkysEu5FXYwNPQXhCuNZk7gPt8QbLj6iOO8dbStjI2apQ1y1rhwxFS89q5ea6YhedZ4i%2Fq7YhPx95m%2FV5YWBMS%2FKRv4omtUdfgKVQU3kxVLn67jNvASUFv2zQXNUeccan2Jj5zY5g%3D%3D--LahHnHBQjFIJLV8I--Z6GZ%2BRDc5S9xOFHtXxyDJA%3D%3D; _Synced_session=LYZ9Hv4hBPP6jBKME9hAG6hV2OJpUUDRmXOozqv6gEUxaAzwLUhEoN5QG2K6ZKvP2c6xxRyjBf6JwVpe4VgCOIdFVYSgLBU6N4eu8x6Jl1AKS8eS5Usz5XUvTRzfPKszJbf15NRG9I6CbjHt%2BE3ZWISryESKAgWjHExxkr123nV2xEDcLrmuB8ayxh3dyPW6k6LuvKzDltfkXOo4icG1WLx%2BcpFf1L3CaeqQVNfK5VDImsE2eBc3beoaEncxE%2FF%2BgRhwyg6vU6xXcLXwmbJ7%2BW%2Fmf54n9nsQmB5Vzdx%2BokruhG4C8lK9DcYcUqxQ%2FswwaeBvbYxx4cYpZbobtTCpQV8z72u4H5rq011h08T0BnHltgjCiw%3D%3D--qX4HjAJK0%2BY2lETr--f9zoYphE%2B5CD2a2nAfEdYw%3D%3D; ahoy_visit=e240accb-57d8-49fa-adf7-b7acea083cf8',
        'Pragma': 'no-cache',
        'Referer': 'https://link.zhihu.com/?target=https%3A//www.jiqizhixin.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except:
        return None
    res = response.text

    soup = BeautifulSoup(res, 'lxml')
    soups = soup.find_all(name='a', attrs={'class': 'article-item__title t-strong js-open-modal'})
    news_li = []
    for s in soups:
        # print(s)
        news_li.append(s.text.strip()+"\n"+"https://www.jiqizhixin.com/"+s.get("href"))
    # print(news_li)
    try:
        with open('jiqizhixin.txt', 'rb') as f:
            cjb = pickle.load(f)
    except:
        cjb = {}
        # print(cjb)


    news = []
    for item in news_li:
        if item not in cjb:
            news.append(item)
    with open('jiqizhixin.txt', 'wb') as f:
        pickle.dump(news_li, f)
    news_message = ""
    if news==[]:
        return None
    for i in range(len(news)):
        if len(news) > 1:
            add_string = str(i+1) + "."
        else:
            add_string = ""
        news_message += f"{add_string}{news[i]}\n"
    news_message += "from :https://www.jiqizhixin.com/"
    return news_message
    # print(news_li)

def spider_scitechdaily():

    url = "https://scitechdaily.com/news/technology/"

    payload = {}
    headers = {
        'authority': 'scitechdaily.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'cookie': 'ezosuibasgeneris-1=ed927813-a843-46a7-6bb4-badcaaf3935a; ezds=ffid%3D1%2Cw%3D1920%2Ch%3D1080; ezouspvv=0; ezouspva=0; _pbjs_userid_consent_data=3524755945110770; __qca=P0-1217474810-1689510475977; _au_1d=AU1D-0100-001689510478-7HKL1LQM-31P5; cnx_userId=bd5f569cf528412eb445c87b076b9ae0; panoramaId_expiry=1690115284625; _cc_id=9a6c0a91fc897d6a23934367d061a221; panoramaId=545041eddc40e525ad15a49ea02316d5393812fc41ccf40654138b6a1d763f80; ezux_ifep_339447=true; ntv_as_us_privacy=1---; _gid=GA1.2.684020861.1689777181; _ntv_uid=7265b3a1-0712-4a78-9afb-17c0a04ed0db; _au_last_seen_pixels=eyJhcG4iOjE2ODk3NzcxOTAsInR0ZCI6MTY4OTc3NzE5MCwicHViIjoxNjg5Nzc3MTkwLCJydWIiOjE2ODk3NzcxOTAsInRhcGFkIjoxNjg5Nzc3MTkwLCJhZHgiOjE2ODk3NzcxOTAsImdvbyI6MTY4OTc3NzE5MCwic29uIjoxNjg5Nzc3MjE2LCJwcG50IjoxNjg5Nzc3MTkwLCJvcGVueCI6MTY4OTc3NzIxNiwidGFib29sYSI6MTY4OTc3NzIxNiwidW5ydWx5IjoxNjg5Nzc3MjE2LCJhZG8iOjE2ODk3NzcyMTYsImNvbG9zc3VzIjoxNjg5Nzc3MjE2LCJzbWFydCI6MTY4OTc3NzIxNiwiYmVlcyI6MTY4OTc3NzIxNiwiaW1wciI6MTY4OTc3NzE5MH0%3D; _tfpvi=OTUxZDExMDgtNTY4MC00NTU0LTgzMTEtOTBhYWYwZWJjNDEwIy02LTI%3D; __gads=ID=57d0e20b17edfccc-228d91ca67e20074:T=1689777441:RT=1689777441:S=ALNI_MbW3BU_IoVs8pD0TjSmU7Kfl5pwvw; __gpi=UID=00000c2254a99807:T=1689777441:RT=1689777441:S=ALNI_MYVVZYZ9zH-Rp9k0h7qQ60yNHzupA; ezoadgid_339447=-1; ezoref_339447=; ezoab_339447=mod58; ezovid_339447=1874853342; lp_339447=https://scitechdaily.com/?s=ocean; ezovuuid_339447=411a0bb4-3001-4f40-4155-0a0dd36e4349; ezohw=w%3D1865%2Ch%3D969; cto_bidid=ySPW2F94YyUyRnJPSXdqbW14MHBZdEFBOW44SlI3bXJuZUVRM2pub1haeFdVbzNMWk1BMHFTT3doSE9Sc1hOWlZvbk9ad0QyZTJQcCUyRkt0aHMxdTlKdmcyM1RjdXhDN0JBVmclMkJidklzeVY2Wnh3V1RVTnpPMDhkR3VGN2tGMXo5cFZBZkFWJTJGYmIzUk1ROEdPVHBpcVNkQUwlMkJoRjV3JTNEJTNE; cto_dna_bundle=-s1Gr180M0RITmhlJTJCZkMwOUJGQlhaMUN2czlsZ2xRJTJGdVBWTmFyT0JLeUdSQmRncEZseFkxMEVHcWJPcE5qdiUyRkZ4UXJZ; ntvSession={"id":1834232,"placementID":1203581,"lastInteraction":1689787961683,"sessionStart":1689787961683,"sessionEndDate":1689868800000,"experiment":""}; ezgwv=-1; cto_bundle=CryOZl9jbjdFNHJ1cHR1JTJCNSUyQkFtUWdHdGNYQm9oZHlweURqSmJ2NzAwWUtic0drdG9lVHdGdDdEUE0xWTJEVjRSVlNHamNFdyUyRlZrTW5PSiUyRk9BaFVFYUh6aDJOM09pJTJCNmdrTUIzMGpYUzRxJTJGZTRHTUNXdHVYS0RxTDNiRGRPSUh0VkllN0d4ZWQ0VHVVSHM2djYzUHhBR04xUVV2RGVCdFVJTXhXaVNPRzZKUndYbHMlM0Q; _pubcid=176c5711-8cd0-4d00-8f79-13f94057b8d3; _gat_gtag_UA_31488880_1=1; active_template::339447=pub_site.1689788145; ezopvc_339447=21; ezepvv=807; ezovuuidtime_339447=1689788145; _ga_W2V0N2TS2C=GS1.1.1689787730.4.1.1689788145.10.0.0; _sharedid=ae031389-1682-4e05-ac3b-cc833c6d2adf; _ga=GA1.2.1136116204.1689510476; ezux_lpl_339447=1689788158025|1cae760b-58b4-4e44-6e25-08501be3d05d|true; ezux_et_339447=171; ezux_tos_339447=96202; active_template::339447=pub_site.1689794200; ezepvv=807; ezoab_339447=mod58; ezoadgid_339447=-1; ezopvc_339447=1; ezoref_339447=; ezosuibasgeneris-1=ed927813-a843-46a7-6bb4-badcaaf3935a; ezovid_339447=1874853342; ezovuuid_339447=563b0c79-9c69-4a02-43b5-05b23e81d12d; ezovuuidtime_339447=1689794201; lp_339447=https://scitechdaily.com/?s=ocean',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except:
        return None
    res =response.text
    soup = BeautifulSoup(res, 'lxml')
    soups = soup.find_all(name='h3', attrs={'class':     "entry-title content-grid-title"})
    news_li = []
    for s in soups:
        # print(s)
        news_li.append(s.text.strip()+"\n"+s.a.get("href"))

    try:
        with open('scitechdaily.txt', 'rb') as f:
            cjb = pickle.load(f)
    except:
        cjb = {}
        # print(cjb)

    news = []
    for item in news_li:
        if item not in cjb:
            news.append(item)
    with open('scitechdaily.txt', 'wb') as f:
        pickle.dump(news_li, f)
    news_message = ""
    if news == []:
        return None
    for i in range(len(news)):
        if len(news) > 1:
            add_string = str(i+1) + "."
        else:
            add_string = ""
        news_message += f"{add_string}{news[i]}\n"
    news_message += "from :https://www.scitechdaily.com/"
    return news_message
    return None

if __name__ == '__main__':
    # spider_inner()
    # while True:

    a = spider_techcruch() + "\n\n" + spider_inner()
    # result = spider_scitechdaily()
    print(a)
    # time.sleep(5)
# news = spider_techcruch()
# print(news)
"""
<div class="post-block__content">OpenAI today announced the general availability of GPT-4, its latest text-generating model, through its API. Starting this afternoon, all existing OpenAI API developers &#8220;with a history of succes	</div>
                                <footer class="post-block__footer">
                                    <figure class="post-block__media">
                                        <a href="https://techcrunch.com/2023/07/06/openai-makes-gpt-4-generally-available/">
                                            <!-- Attaching the URL
"""