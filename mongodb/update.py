import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["lib"]
books = db["books"]
# print(
#     books.update_one({
#         "name" : "Year got change"
#     }, {
#         "$set" : {
#             "name": "third"
#         }
#     }).modified_count
# )
books.update_many({"year" : 1535}, {
    "$set" : {
        "name" : "Year got change"
    }
})
print([*books.find()])