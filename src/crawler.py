import requests
import re
from pyvi import ViTokenizer, ViPosTagger
from bs4 import BeautifulSoup
import json
import logging
import os

BASE_DIR = os.getcwd().replace("src", "")
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;.""]')

TAG_2_KEY = {
    "kinh doanh": "1",
    "thời sự": "2",
    "thế giới": "3",
    "thể thao": "4",
    "pháp luật": "5",
    "giáo dục": "6",
    "số hóa": "7",
    "ý kiến": "8",
    "sức khỏe": "9",
    "xe": "10"
}

def cleaned_text(text):
    text = text.lower()
    return REPLACE_BY_SPACE_RE.sub('', text)


def get_content_vnexpress(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    category = soup.select('li.start h4 a')
    # print(category)
    # return {'content': 1}

    content_list = soup.select('article.content_detail p.Normal')
    # print(content_list)
    if not content_list:
        content_list = soup.select('div.fck_detail p.Normal')

    content = "".join([_.text for _ in content_list]) if content_list else None
    # print(category)
    return {
        'category': category[0].text if len(category) > 0 else None,
        'content': content
    }



def get_vnexpress_news():
    r = requests.get('https://vnexpress.net')
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.select('section.sidebar_home_1 article.list_news')
    data = []
    for n in news:
        n_data = {}
        n_data['description'] = cleaned_text(n.p.text).replace('\n',' ') if n.find(class_='description') else None
        url = n.h4.a.get('href')
        deep_data = get_content_vnexpress(url)
        n_data.update({
            'title': n.h4.text.replace('\n', ''),
            # 'img': n.div.a.img.get('src'),
            'url': url,
            'content': deep_data['content'],
            'category': TAG_2_KEY[deep_data['category'].lower()] if deep_data['category'] != None else None
        })
        data.append(n_data)

    return data


# print(get_vnexpress_news())

def save(data, file_name):
    with open(file_name + '.json', 'w') as f:
        json.dump(data, f, indent=4)

    with open(file_name + '.txt', 'w') as f:
        for i, d in enumerate(data):
            if d['description'] is not None and d['category'] is not None:
                f.write(str(d['description']) + ".	")
                # f.write("url: " + d['url'] + "\n")
                f.write(str(d['category']) + "\n")
                # f.write("content: " +str(d['content']) + "\n")
                # f.write("---------------------------------\n")

save(get_vnexpress_news(),BASE_DIR + "raw_data/vn_express_data/vn_express")
# data = get_thanhnien_news()
# with open("thanhnien.json", "W") as f:
    # json.dump(data, f, indent=4)
# save(get_thanhnien_news(), 'thanhnien')