from urllib.request import urlopen
from bs4 import BeautifulSoup

#네이버 인명사전 이름 구하기.

base_url = 'https://terms.naver.com/list.nhn?cid=43671&categoryId=43671&page={}'

name_list=[]
for index in range(1,500):

    get_url = base_url.format(index)
    web_page = urlopen(get_url)
    source = BeautifulSoup(web_page, 'html.parser')
    # get_name = source.find_all('div', class_='subject')
    get_name = source.select('div.subject')

    for name in get_name:

        get_name = name.get_text()
        erase_newline = get_name.replace('\n','$')
        last_name = erase_newline.split('$')

        for name_split in last_name:
            if len(name_split) == 0:
                continue

            if '[' in name_split:
                name_list.append(name_split)

with open ('D:/MY개발/00.비식별화/B사/TEST/사전/인명사전22.txt','w', encoding = 'utf-8') as file_write:

    for line in name_list:
        file_write.write(line+'\n')

file_write.close()


