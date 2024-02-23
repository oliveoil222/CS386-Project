# import libraries
import pymongo


# 'connect to client' aka connecting to our server
    # everything but the url in there since this is private
client =  pymongo.MongoClient('server url') # keep empty for now

# connect to help desk ticket database
db = client['Ticket Tracker']
# create collections
    # create a tickets collection
ticket_collection = db['Tickets']
    # add to collections list
        
    # create a workers collection
worker_collection = db['Workers']

    # create a teams collection
team_collection = db['Teams']

    # create a device collection
device_collection = db['Devices']

    # create client collection
client_collection = db['Clients']

def add_ticket(description, worker_id, device_id, client_id, team_id):
    # create document dictionary to add to the collection
        # the id is made by pymongo so we dont have to do that
    new_ticket = {
        'description': description,
        'worker' : worker_id,
        'device' : device_id,
        'client' : client_id,
        'team' : team_id
    }
    # return the document inserted into the ticket collection
    return ticket_collection.insert_one(new_ticket)

# then can get a ticket id as follows
new_ticket = add_ticket(...)
# next is getting the id from the recently added ticket
new_ticket_id = new_ticket.inserted_id

def add_client(email, ticket_id, device_id, worker_id):
    # create a new document for the new client
    new_client = {
        'email' : email,
        'tickets' : [ticket_id],
        'devices' : [device_id],
        'workers' : [worker_id]
    }
    # return the new inserted document in the collection
    return client_collection.insert_one(new_client)

def add_worker(name, email, team, ticket):
    # create new document for the new worker
    new_worker = {
        'name' : name,
        'email' : email,
        'team' : team,
        'tickets' : [ticket]
    }
    # return the new worker added to the collection
    return worker_collection.insert_one(new_worker)

def add_team(workers, tickets, name):
    # create new document for the new team
    new_team = {
        'name' : name,
        'workers' : [workers],
        'tickets': [tickets]
    }
    # return the new team inserted into the team collection
    return team_collection.insert_one(new_team)




