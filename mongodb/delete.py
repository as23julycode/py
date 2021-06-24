import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["lib"]
books = db["books"]

# books.delete_one({
#     "year" : 2015
# })

books.delete_many({
    "year" : 1535
})
print([*books.find()])