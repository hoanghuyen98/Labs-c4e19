from pymongo import MongoClient

uri = "mongodb://admin:admin123@ds235411.mlab.com:35411/c4e19-lab"

# 1. Connect to database
client = MongoClient(uri)
client = MongoClient(uri)
# 2. Get database
db = client.get_default_database()
db1 = client.get_default_database()
# 3. Create Collection
games = db['games']
data_game = db1['data game']
# 4. Create Document
# new_game = {
#     "name": " Chú cuội tìm trâu ",
#     "description": "League of Legend"
# }
# new_datagame = {
#     "name" : " code python ",
#     "description": " print('hello C4E 19')"
# }
# # 5. Insert doc into collection 

# games.insert_one(new_game)
# data_game.insert_one(new_datagame)


# get all document 
all_games = games.find()

print(all_games[1]['name'])