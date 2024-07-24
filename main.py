import requests
import ollama
from bs4 import BeautifulSoup
import datetime as dt

def fetch_html(url):
    response = requests.get(url)
    return response.content

def process_data(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find('table')
    data = []
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        row_data = [cell.text.strip() for cell in cells]
        data.append(row_data)
    data = data[1:-1]
    prompt = ''
    for i in data:
        count = i[1].count('。')
        if count > 1:
            i[1] = i[1].replace('。', '，', 1)
        else:
            i[1] = i[1].replace('。', '，  明天尚未公布。')
        prompt += f'{i[0]}:{i[1]}\n'
    return prompt

def ollama_chat(prompt):
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

if __name__ == "__main__":
    url = "https://www.dgpa.gov.tw/typh/daily/nds.html"
    html_content = fetch_html(url)
    prompt = process_data(html_content)

    ollama_chat(prompt)