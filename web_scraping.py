import requests
from bs4 import BeautifulSoup
'''
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    rank_tag = movie.select_one('td:nth-child(1) > img')
    a_tag = movie.select_one('td.title > div > a')
    point_tag = movie.select_one('td.point')
    if a_tag is not None:
        print (rank_tag['alt'], a_tag.text, point_tag.text)
'''

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://comic.naver.com/webtoon/weekday.nhn', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
webtoons = soup.select('#content > div.list_area.daily_all > div.col')

for webtoon in webtoons:
    day_tag = webtoon.select_one('div > h4 > span')
    print(day_tag.text)
    title_tags = webtoon.select('div > ul > li > a')
    for title_tag in title_tags:
        if title_tag is not None:
            print(title_tag.text)
    print('------------------')

