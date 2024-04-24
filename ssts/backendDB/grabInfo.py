# import libraries
from bson.json_util import dumps
import sys
sys.path.insert(0, './')
import dbClasses as db


# set up connector to database and collections
connector = db.Connections()

# doing a dump(cursor) will return the information from the query, the first
# element in the dictionary is just mongoDBs object id that different for
# every element
# this will be the file that has all the functions for grabbing information from the
# mongo databases that can be passed back to mid

# connect collections as global variables
    # connect a tickets collection
ticket_collection = connector.ticket_collection

    # connect a workers collection
worker_collection = connector.worker_collection

    # connect a teams collection
team_collection = connector.team_collection

    # connect a device collection
device_collection = connector.device_collection

    # connect client collection
client_collection = connector.client_collection

    # conntect id tracker collection
id_tracker_collection = connector.id_tracker_collection

# create function to get current id count of collection 
def get_current_id(collection_name):
    # go through id tracker collection and only get ticket id count
    id_count = id_tracker_collection.find_one({'collection' : collection_name}, {'count' : 1})
    # get the str version of the id count
    id_count = dumps(id_count['count'])
    # convert the str to an int
    id_count = int(id_count)
    # return the id count integer value
    return id_count

# create function to find tickets with client email
def client_email_find_tickets(client_email):
    # need to go through client database first
        # functions: find_one
    client = client_collection.find_one({'email' : client_email})
    # get the str version of the tickets 
        # functions: dumps)
    # return the list of tickets
    return client['tickets']

# create functiont to finf ticket with ticket id
def ticket_id_find_ticket(ticket_id):
    # make a search on the database (query) to find the ticket from ticket id
        # functions: find_one
    ticket = ticket_collection.find_one({'ticket id' : ticket_id})

    # return the ticket object
    return ticket


# create function to find tickets with worker id
def worker_id_find_tickets(worker_id):
    # find the worker and only grab the tickets list
        # functions: find_one
    worker = worker_collection.find_one({'worker id' : worker_id})
    # return the list of tickets assigned to the worker
    return worker['tickets']

# create function to find tickets with worker email
def worker_email_find_tickets(worker_email):
    # find the worker with email and grab the tickets list
        # functions: find_one
    worker = worker_collection.find_one({'email' : worker_email})
    # get the str version of the tickets 
        # functions: dumps
    # return the tickets list cursor
    return worker['tickets']

# create function to find tickets with team id
def find_team_tickets(team_id):
    # find the tickets the team has by grabbing the team with matchin id
        # functions: find_one
    team = team_collection.find_one({'team id' : team_id})
    # get the str version of the tickets 
        # functions: dumps
    # return the list of tickets to the user
    return team['tickets']

# create function to find a worker given id
def find_worker(worker_id):
    # grab the worker with worker id and set the worker var to worker
    # document
        # functions: find_one
    worker = worker_collection.find_one({'worker id': worker_id})
    # return the worker mongodb cursor doc
    return worker
# create function to find a worker given email
def find_worker_with_email(worker_email):
    # get the worker with the worker email
        # functions: find_one
    worker = worker_collection.find_one({'email' : worker_email})
    # return the worker pymongo cursor doc 
    return worker

# create function to look for device given device id
def find_device(device_id):
    # get the device with the device id using the query function
        # functions: find_one
    device = device_collection.find_one({'device id' : device_id})
    # return the device pymongo cursor doc
    return device

# create function to look for device given device owner email
    # need to return multiple devices since there can be many
    # devices to one owner
        # grab the device list from the client collection

        # return the possible devices that the owner is
        # connected to

# create function to look for device given devices ticket id
    # need to update the adding info functions to accomidate for this
    # need to have an active tickets attribute we can look at for 
    # each device

# create search function to find a client given client id
def find_client(client_id):
    # grab the pymongo cursor from querying the client id
        # functions: find_one
    client = client_collection.find_one({'client id' : client_id})
    # return the pymongo cursor
    return client

# create search function to find a client given client email
    # grab the pymongo cursor from querying the client id
        # functions: find_one
    # return the pymongo cursor document

# create search function to find a client given client phone number
    # grab the pymongo cursor from querying the client id
        # functions: find_one
    # return the pymongo cursor document

# create search function to find a client given client name
    # grab the pymongo cursor from querying the client id
        # functions: find
    # return the pymongo cursor document




# example of code using search functions
# this sets ticket to be the search query cursor from mongoDB
ticket = ticket_id_find_ticket('t1')
# you can use the dumps function to convert from the pymongo
# cursor object type into a string of what key you want to 
# see, or just return a string of the dictionary with no key
# attribute attatched
ticket_description = dumps(ticket['description'])
# this prints out what its giving, so you can visualize it
#print((ticket_description))


