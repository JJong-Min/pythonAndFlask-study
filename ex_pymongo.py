from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbratel
'''

db.users.insert_one({'name':'bobby','age':21})
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})
'''

all_users = list(db.users.find({}))
print(all_users)

same_ages = list(db.users.find({'age':21}))
print('---------')
print(same_ages)
print('---------')
print(all_users[0]) 
print('---------')       
print(all_users[0]['name'])
print('---------')
for user in all_users:      
    print(user)