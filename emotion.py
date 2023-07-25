import random
import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

def get_image(url):


  payload = {}
  headers = {
    'authority': 'img.soutula.com',
    'accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://fabiaoqing.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  if response.status_code == 200:
    # Create the "image" folder if it doesn't exist
    os.makedirs("image", exist_ok=True)

    # Save the image as a JPG file
    image_path = os.path.join("image", "image.jpg")
    with open(image_path, "wb") as f:
      f.write(response.content)
      print("Image saved successfully as 'image.jpg'")
  else:
    print("Failed to fetch the image.")


def get_emotion_img(word):

  encoded_text = urllib.parse.quote(word)
  # print(encoded_text)
  # "%E9%B8%A1%E4%BD%A0%E5%A4%AA%E7%BE%8E"
  url = f"https://fabiaoqing.com/search/bqb/keyword/{encoded_text}/type/bq/page/1.html"

  payload={}
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=cmk3og41p68hc556l7ortlu6rf; __gads=ID=3874d8193bfe8b09-22eaab2653e20052:T=1689169007:RT=1689810066:S=ALNI_MZ5KArKQLsYSLPNv3o0o8GqK0Ncsw; __gpi=UID=00000c202873e565:T=1689169007:RT=1689810066:S=ALNI_MbMVN2hb0qMeP0gyiFJnCNBJAaYJQ',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  res = response.text
  # print(res)
  soup = BeautifulSoup(res, 'lxml')
  soups = soup.find_all(name='img', attrs={'class': 'ui image bqppsearch lazy'})
  news_li = []
  for s in soups:
    # print(s)
    # print(s.a["href"])
    # print(s.text)
    news_li.append(s.get("data-original"))
  if len(news_li) == 0:
    return False

  image_url = random.choice(news_li)
  get_image(image_url)

  return True


if __name__ == '__main__':
    a = get_emotion_img("(都这样了还打我[狗头])")

    print(a)