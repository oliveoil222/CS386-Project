# import libraries
import pymongo
import createDatabases

# this will be the file that has all the functions for grabbing information from the
# mongo databases that can be passed back to mid

# connect to database
# 'connect to client' aka connecting to our server
    # everything but the url in there since this is private
client =  pymongo.MongoClient('server url') # keep empty for now

# connect to help desk ticket database
db = client['Ticket Tracker']

# connect collections
    # connect a tickets collection
ticket_collection = db['Tickets']

    # connect a workers collection
worker_collection = db['Workers']

    # connect a teams collection
team_collection = db['Teams']

    # connect a device collection
device_collection = db['Devices']

    # connect client collection
client_collection = db['Clients']


def client_email_find_tickets(client_email):
    # need to go through client database first
    tickets = client_collection.find({'email' : client_email}, {'tickets' : 1})
    # return the list of ticket ids
    return tickets

def ticket_id_find_ticket(ticket_id):
    # make a search on the database (query) to find the ticket from ticket id
    ticket = ticket_collection.find({'_id' : ticket_id})
    # return the ticket object
    return ticket