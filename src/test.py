import pymongo

# connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# create a db called "mydatabase"

mydb = myclient["mydatabase"]
# even the above line is run, it hasn't created the db yet
# it will be created when we create a table with at least one document


# # create/retrieve collection = table 
mycol = mydb["customers"]


# # create a document = col in the table
# mydict = {"name": "John", "address": "Highway 15"}
# x = mycol.insert_one(mydict) # after running this line the db is created

# print("x auto generated id: {} ".format(x.inserted_id))

# #check if database exists
# print(myclient.list_database_names())
# #check if collection exists
# print(mydb.list_collection_names())

#----------------------------------------------------------------------------------------#
#
#               lets insert many cols at once
#----------------------------------------------------------------------------------------#

# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)


##print list of the _id values of the inserted documents:
# print(x.inserted_ids)

#----------------------------------------------------------------------------------------#
#
#               lets insert many cols at once but this time 
#               we submit the id to prevent mongodb to auto assign one
#----------------------------------------------------------------------------------------#

# mylist = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)


# # print list of the _id values of the inserted documents:
# print(x.inserted_ids)

# #----------------------------------------------------------------------------------------#
# #
# #               to find the first entry use the function find_one()
# #               
# #----------------------------------------------------------------------------------------#

# x = mycol.find_one()
# # print(x)

# #----------------------------------------------------------------------------------------#
# #
# #               to return all cols as if running SELECT *, use find() with no arguments
# #               
# #----------------------------------------------------------------------------------------#
# for x in mycol.find():
#     print(x)

#----------------------------------------------------------------------------------------#
#
#               Return only some fields
#               
#----------------------------------------------------------------------------------------#
for x in mycol.find({},{"name": 1, "address": 0 }):
    print(x)


# for x in mycol.find({},{ "address": 0 }):
#   print(x)