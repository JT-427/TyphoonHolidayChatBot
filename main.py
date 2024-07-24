import ollama
import requests
from bs4 import BeautifulSoup
import datetime as dt

url = "https://www.dgpa.gov.tw/typh/daily/nds.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Example: Finding the table
table = soup.find('table')

# Extracting data
data = []
for row in table.find_all('tr'):
    cells = row.find_all('td')
    row_data = [cell.text.strip() for cell in cells]
    data.append(row_data)

# data to string
prompt = ''
for i in data:
    # 確認i[1]這個字串裡有幾個'。'
    count = i[1].count('。')
    if count > 1:
        # 如果有兩個以上的'。'，將第一個'。'換成'，'
        i[1] = i[1].replace('。', '，', 1)
    else:
        # 如果只有一個'。'，將'。'換成'，'
        i[1] = i[1].replace('。', '，  明天尚未公布。')
    prompt += f'{i[0]}:{i[1]}\n'

all_q = [
  {
    'role': 'system',
    'content': f'以下是台灣時間{dt.datetime.now()}取得之颱風假資訊\n\n{prompt}\n\n你是一個只根據上述資訊回答問題的機器人，若有超出資料範圍的問題，以不清楚回答。',
  }
]

while True:
    Q = input('Q: ')
    all_q.append({
        'role': 'user',
        'content': Q
    })

    response = ollama.chat(model='mistral', messages=all_q)

    all_q.append(response['message'])
    print(' '*15, response['message']['content'], '\n')
    print(f"\n{'==='*20}\n")