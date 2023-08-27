from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://phanibussa:CPgXHbJiHunRudH8@cluster0.b3vlwqb.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
 
 ## creating a DB   
 mydb=client["MyDatabse"]    
 
mycol =  mydb["myfirstcollection"]
myfirstrecord = {"fname":"Phani", "lname":"Bussa", "address":"Concord"}

mycol.insert_one(myfirstrecord)
 
 ## list all the DB names
client.list_database_name()