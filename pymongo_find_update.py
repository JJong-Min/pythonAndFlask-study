from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbratel

same_ages = db.movies.find_one({'title':'매트릭스'})

comp_star = same_ages['star']

same_stars = list(db.movies.find({'star':comp_star}))

for same_star in same_stars:
    print(same_star['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':0}})
same_ages = db.movies.find_one({'title':'매트릭스'})

comp_star = same_ages['star']
print(comp_star)