import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient          
client = MongoClient('localhost', 27017) 
db = client.dbratel                 
'''

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')


movies = soup.select('#old_content > table > tbody > tr')


for movie in movies:
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None:
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text                                      
        star = movie.select_one('td.point').text                
        doc = {
            'rank' : rank,
            'title' : title,
            'star' : star
        }
        db.movies.insert_one(doc)
'''

all_users = list(db.movies.find({}))
print(all_users)