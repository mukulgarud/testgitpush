import pymongo

client = pymongo.MongoClient("mongodb+srv://mukulgarud28:mukulgarud28@cluster0.gjoxaru.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "mukul",
    "surname": "garud",
    "email": "mukulgarud28@gmail.com"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)