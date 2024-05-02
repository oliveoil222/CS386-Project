import mongomock
import pytest
import pymongo


# create database class
class Database:
    # create init function
    def __init__(self):
        # get mongomock database
        self.client = mongomock.MongoClient()
        # create mock database to test
        self.db = self.client['ssts']

# create class for user
class UserCollection:
    # create init function
    def __init__(self):
        # connect to user database
        database = Database()
        self.collection = database.db['users']
    # function to add user to database collection
    # the user variable to input is a Worker/Client object
    def add_user(self, user):
        print("USER", user)
        collection = self.collection
        new_user = {
            'name' : user.name,
            'email': user.email,
            'password': user.password,
            'type' : user.user_type
        }
        return collection.insert_one(new_user)
    # the user variable to input is a Worker/Client object
    def find_user(self, email):
        collection = self.collection
        found_user = collection.find_one({'email': email})
        if found_user == None:
            return None
        found_user = User(found_user['name'],
                          found_user['email'],
                          found_user['type'],
                          found_user['password'])
        # query to find a user in the user collection
        return found_user

class User:
    def __init__(self, name, email, type, password):
        self.collection_name = 'users'
        self.name = name
        self.user_type = type
        self.email = email
        self.password = password

# create subclass of users for clients
class ClientCollection:
    # create init function 
    def __init__(self):
        database = Database()
        # connect to client collection
        self.collection = database.db['clients']
    
    def add_client_to_users(self, client):
        users = UserCollection()
        user = User(client.name, 
                    client.email, 
                    client.user_type,
                    client.password)
        user_added = users.add_user(user)
        print("USER ADDED", user_added)
        return user_added
    # add client method
    def add_client(self, client):
        # add client to users
        self.add_client_to_users(client)
        # set up client collection connection
        clients = self.collection
        # create a new document for the new client
        new_client = {
            'email' : client.email,
            'name': client.name,
            'phone number' : client.phone_num,
            'contact method' : client.contact_method,
            'password': client.password
        }
        # return the new added client pymongo id
        return clients.insert_one(new_client)
    
    def get_client(self, email):
        # add client to the user collection
        collection = self.collection
        client = collection.find_one({'email':email})
        client = Client(client['email'],
                        client['name'],
                        client['phone number'],
                        client['contact method'],
                        client['password'])
        return client
    
        
class Client:
    def __init__(self, email, name, phone_num, contact_method, password):
        self.email = email
        self.name = name
        self.phone_num = phone_num
        self.contact_method = contact_method
        self.collection_name = 'clients'
        self.user_type = 'client'
        self.password = password


# create subclass of users for workers
class WorkerCollection:
    def __init__(self):
    # collection connection
        database = Database()
        self.collection = database.db['workers']

    def add_worker_to_users(self, worker):
        users = UserCollection()
        user = User(worker.name,
                    worker.email,
                    worker.user_type,
                    worker.password)
        users.add_user(user)
        return user
    # add worker to collection
    def add_worker(self, worker):
        # add worker to user collection
        self.add_worker_to_users(worker)
        # add worker to worker collection
        worker_collection = self.collection
        # create new document for the new worker
        new_worker = {
            'name' : worker.name,
            'email' : worker.email,
            'team' : worker.team,
            'password': worker.password
        }
        # return the new worker added to the collection
        return worker_collection.insert_one(new_worker)
    
    
    def get_worker(self, worker_email):
        collection = self.collection
        worker = collection.find_one({'email': worker_email})
        if worker != None:
            worker = Worker(worker['name'],
                            worker['email'], 
                            worker['team'], 
                            worker['password'])
            return worker
        else:
            return None
    

class Worker:
    def __init__(self, name, email, team_name, password):
        self.name = name
        self.email = email
        self.team = team_name
        self.collection_name = 'workers'
        self.user_type = 'worker'
        self.password = password


# collection variables
WORKERS = WorkerCollection()
USERS = UserCollection()
CLIENTS = ClientCollection()

# test if new worker is able to be added to both user collection 
# and worker collection
def test_add_worker():
    # create and add new worker to mock collection
    worker = Worker('Mock Test', 'mock.worker@test.com', 'mockmongo', 'password')
    print(WORKERS.add_worker(worker))
    # test to see if the worker was added to the mock users collection
    in_users = USERS.find_user('mock.worker@test.com')
    print("USER", in_users)
    in_workers = WORKERS.get_worker('mock.worker@test.com')
    print("WORKER", in_workers)
    assert in_users != None and in_workers != None


# test if new client is able to be added to both user collection
# and client collection
def test_add_client():
    client = Client('mock.client@test.com', 'Mongo Mock', '5558888', 'phone', 'password')
    print(CLIENTS.add_client(client))
    # test to see if client was added to both client and user collections
    in_users = USERS.find_user('mock.client@test.com')
    print("USERS", in_users)
    in_clients = CLIENTS.get_client('mock.client@test.com')
    print("CLIENTS", in_clients)
    assert in_users != None and in_clients != None

db = Database()
users = DB['users']
print(users.find())

test_add_client()
test_add_worker()

