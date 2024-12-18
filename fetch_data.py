from pymongo import MongoClient
connection_string= "mongodb+srv://sutharkk22:KFqXsDW2debzBqj2@cluster0.bx9by.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string) #client == conn
database = client['Farmer']
collection = database['FarmerDetail']

documents = collection.find()  # select * from table;
for document in documents: 
    print(document) 
print("thank you!")
