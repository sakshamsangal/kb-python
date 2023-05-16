```sql
# create database
use <databaseName>

#delete database
db.dropDatabase()

#display database
show dbs

# display collection
show collections

# create collection
db.createCollection(<collectionName>)

#find
db.<collectionName>.find()
db.<collectionName>.findOne()

condition = {
	"age": {$lt: "30"}
}

db.<collectionName>.find(<condition>)

#insert
obj = {
	"email": "sak",
	"password": "123"
} 
OR 
arr = [
	obj1,
	obj2,...
]
db.<collectionName>.insert(<obj> OR <arr>)


