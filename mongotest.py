import pymongo

client = pymongo.MongoClient("mongodb+srv://mukulgarud28:mukulgarud28@cluster0.gjoxaru.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "mukul",
    "surname": "garud",
    "email": "mukulgarud28@gmail.com"
    "mobile_no": 9820610357
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)