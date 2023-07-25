# import openai
#
# openai.proxy = 'http://127.0.0.1:33210'
# openai.api_key = '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'
# # 通过 `系统(system)` 角色给 `助手(assistant)` 角色赋予一个人设
# messages = [{'role': 'system', 'content': '你是一个乐于助人的诗人。'}]
# # 在 messages 中加入 `用户(user)` 角色提出第 1 个问题
# messages.append({'role': 'user', 'content': '作一首诗，要有风、要有肉，要有火锅、要有雾，要有美女、要有驴！'})
# # 调用 API 接口
#
# response = openai.ChatCompletion.create(
#     model='gpt-3.5-turbo',
#     messages=messages,
# )
# # 在 messages 中加入 `助手(assistant)` 的回答
# messages.append({
#     'role': response['choices'][0]['message']['role'],
#     'content': response['choices'][0]['message']['content'],
# })
# # 在 messages 中加入 `用户(user)` 角色提出第 2 个问题
# messages.append({'role': 'user', 'content': '好诗！好诗！'})
# # 调用 API 接口
# response = openai.ChatCompletion.create(
#     model='gpt-3.5-turbo',
#     messages=messages,
# )
# # 在 messages 中加入 `助手(assistant)` 的回答
# messages.append({
#     'role': response['choices'][0]['message']['role'],
#     'content': response['choices'][0]['message']['content'],
# })
# # 查看整个对话
# print(messages)

def api_self():
    import requests

    url = "https://openai.api2d.net/v1/chat/completions"

    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer fk207212-lZpwH6JtpGbuwU0rEsiH34vazDTy1Cj7' # <-- 把 fkxxxxx 替换成你自己的 Forward Key，注意前面的 Bearer 要保留，并且和 Key 中间有一个空格。
    }

    data = {
      "model": "gpt-4-0613",
      "messages": [{"role": "user", "content": "今天是星期几"}],
      "max_tokens": 100,
    }

    response = requests.post(url, headers=headers, json=data)
    if "200" not in str(response.status_code):
        return False

    # print("Status Code", response.status_code)
    # print("JSON Response ", response.json())
    return response.json()["choices"][0]["message"]["content"]

if __name__ == '__main__':

    a = api_self()
    print(a)