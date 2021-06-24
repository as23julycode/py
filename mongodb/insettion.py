import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["lib"]
books = db["books"]
books.insert_one({
    "name" : "aditya",
    "father" : "S N Singh"

})
books.insert_many([
    {
    "name" : "aditya",
    "father" : "S N Singh",
    "year": "1999"

},
{   "name" : "ayushi",
    "father" : "S N Singh",
    "year": "2001"
    
},
{
    "name" : "anyo",
    "father" : "dddddd",
    "year": "2005"
}
])
