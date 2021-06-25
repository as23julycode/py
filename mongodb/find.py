import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["lib"]
books = db["books"]
query = {
    "name" : "ayushi"
}
# print([*books.find({
#     "name" : "ayushi"
# },{
#     "_id": 0
# })])
print([*books.find().sort("year",-1).limit(1)])