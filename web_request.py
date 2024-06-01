import re
import requests

def spider(question):
    url = "http://127.0.0.1:1234/chat"
    headers = {
    'Cookie': 'csrftoken=LtaSPPy49QG60FoI0UZUcupKohvl9eCyBtWWS2qDkHYptDxAKU6x68sEjbshllHQ; 	_ga=GA1.1.1250225757.1715132751; _ga_R1FN4KJKJH=GS1.1.1715132751.1.1.1715132800.0.0.0',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
	}
    data = {
        "prompt": question
    }

    response = requests.post(url, headers=headers, json=data)
    reply = response.content.decode('utf-8')
    reply = re.sub(r'<eop>','',reply)
    return reply

print(spider("who are you"))
print(spider("hi"))
