import pytest
import sys
sys.path.insert(0, './')
from bson.json_util import dumps
import dbClasses as db


# GLOBAL VARIABLES
    # team test variables
TEAM_NAME_1 = 'Test Team 1'
TEAM_NAME_2 = 'Test Team 2'

    # worker test variables
WORKER_EMAIL_1 = 'testWorker1@test.com'
WORKER_NAME_1 = 'Worker 1 Test'
WORKER_EMAIL_2 = 'testWorker2@test.com'
WORKER_NAME_2 = 'Worker 2 Test'

    # client test variables
CLIENT_EMAIL_1 = 'testClient1@test.com'
CLIENT_NAME_1 = 'Client 1 Test'
CLIENT_PHONE_1 = '555-0001'
CLIENT_CONTACT_1 = 'Email'
CLIENT_EMAIL_2 = 'testClient2@test.com'
CLIENT_NAME_2 = 'Client 2 Test'
CLIENT_PHONE_2 = '555-0002'
CLIENT_CONTACT_2 = 'Phone'

# device test variables
DEVICE_OP_SYS_1 = 'MacOS'
DEVICE_PROBLEMS_1 = True
DEVICE_OP_SYS_2 = 'Windows'
DEVICE_PROBLEMS_2 = False
DEVICE_OP_SYS_3 = 'Linux'
DEVICE_PROBLEMS_3 = True


# ticket test variables
TICKET_DESC_1 = 'Test description 1'
TICKET_TITLE_1 = 'Test ticket 1'
TICKET_STATUS_1 = 'open'
TICKET_DESC_2 = 'Test description 2'
TICKET_TITLE_2 = 'Test ticket 2'
TICKET_STATUS_2 = 'open'
TICKET_DESC_3 = 'Test description 3'
TICKET_TITLE_3 = 'Test ticket 3'
TICKET_STATUS_3 = 'open'
TICKET_DESC_4 = 'Test description 4'
TICKET_TITLE_4 = 'Test ticket 4'
TICKET_STATUS_4 = 'open'
TICKET_DESC_5 = 'Test description 5'
TICKET_TITLE_5 = 'Test ticket 5'
TICKET_STATUS_5 = 'open'

# solution variables
SOLUTION_PROGRESS_1 = ['progress 1 test 1', 'progress 2 test 1']
SOLUTION_KEYWORDS_1 = ['Test 1']
SOLUTION_PROGRESS_2 = ['progress 1 test 2', 'progress 2 test 2']
SOLUTION_KEYWORDS_2 = ['Test 2']
# test database class

class DatabaseTests:
    def test_connection():
        connection = db.Database()
        assert connection != None

# test client collection and client class
class ClientTests:
    def __init__(self):
        self.collection = db.ClientCollection()
    def test_add_client(self, client):
        collection = self.collection
        # add new client with client collection
        new_client_1 = collection.add_client(client)
        print('ADDED CLIENT:', new_client_1)
        assert new_client_1 != None 

    def test_get_devices():
        return None
    def test_get_tickets():
        return None
    def test_get_workers():
        return None
    
# test worker collection and worker class
class WorkerTests:
    def __init__(self):
        self.collection = db.WorkerCollection()
    def test_add_worker(self, worker):
        collection = self.collection
        new_worker = collection.add_worker(worker)
        print('WORKER ADDED:', new_worker)
        assert new_worker != None

    def test_get_team_workers(self, team):
        collection = self.collection
        workers = collection.get_team_workers(team)
        print('WORKERS IN TEAM', workers)
        if len(workers) > 0:
            worker = workers[0]
        else:
            worker = None
        assert worker.email == WORKER_EMAIL_1
    
    def test_get_worker(self, worker_email):
        collection = self.collection
        worker = collection.get_worker(worker_email)
        print('WORKER:', worker.email)
        assert worker.email == worker_email


# test user collection and user class
class UserTests:
    def __init__(self):
        self.collection = db.UserCollection()
    def test_add_user(self, user):
        collection = self.collection
        new_user = collection.add_user(user)
        print('USER:', user)
        assert new_user != None

# test device collection and device class

# test ticket collection and ticket class
class TicketTests:
    def __init__(self):
        self.collection = db.TicketCollection()
    def test_add_ticket(self, ticket):
        collection = self.collection
        new_ticket = collection.add_ticket(ticket)
        print('NEW TICKET', new_ticket)
        assert new_ticket != None

# test solution collection and solution class
class SolutionTests:
    def __init__(self):
        self.collection = db.SolutionCollection()
    def test_add_solution(self, solution):
        collection = self.collection
        new_solution = collection.add_solution(solution)
        print('NEW SOLUTION', new_solution)
        assert new_solution != None

# test team collection and team class
class TeamTests:
    def __init__(self):
        self.collection = db.TeamCollection()
    def test_add_team(self, team):
        collection = self.collection
        new_team_1 = collection.add_team(team)
        print('NEW TEAM', new_team_1)
        assert new_team_1 != None 

    def test_get_workers(self, team):
        collection = self.collection
        workers = collection.get_workers(team)
        print('TEAM WORKERS:', workers)
        assert len(workers) > 0
    
    def test_get_tickets(self, team):
        collection = self.collection
        tickets = collection.get_tickets(team)
        print('TEAM TICKETS:', tickets)
        assert len(tickets) > 0
    


def testClasses():
    TEAM_1 = db.Team(TEAM_NAME_1)
    TEAM_2 = db.Team(TEAM_NAME_2)
    print('TEAMS', TEAM_1, TEAM_2)
    # create worker 1
    worker_1 = db.Worker(WORKER_NAME_1, 
                        WORKER_EMAIL_1, 
                        TEAM_NAME_1)
    # create worker 2
    worker_2 = db.Worker(WORKER_NAME_2, 
                        WORKER_EMAIL_2, 
                        TEAM_NAME_2)
    print('WORKERS', worker_1, worker_2)
    # create client 1
    client_1 = db.Client(CLIENT_EMAIL_1,
                         CLIENT_NAME_1,  
                         CLIENT_PHONE_1,
                         CLIENT_CONTACT_1)
    # create client 2
    client_2 = db.Client(CLIENT_EMAIL_2,
                        CLIENT_NAME_2,  
                        CLIENT_PHONE_2,
                        CLIENT_CONTACT_2)
    print('CLIENTS', client_1.email, client_2.email)

    # user test variables 
    # create user 1
    user_1 = db.User(worker_1.name, 
                    worker_1.email, 
                    worker_1.user_type)
    # create user 2
    user_2 = db.User(client_1.name, 
                    client_1.email, 
                    client_1.user_type)
    print('USERS', user_1, user_2)
    
    # create device objects
    device_1 = db.Device(client_1, 
                         DEVICE_OP_SYS_1, 
                         DEVICE_PROBLEMS_1)
    device_2 = db.Device(client_1, 
                         DEVICE_OP_SYS_2, 
                         DEVICE_PROBLEMS_2)
    device_3 = db.Device(client_2, 
                         DEVICE_OP_SYS_3, 
                         DEVICE_PROBLEMS_3)
    print('DEVICES', device_1, device_2, device_3)
    
    # create ticket objects
    ticket_1 = db.Ticket(TICKET_DESC_1, 
                         TICKET_TITLE_1,
                         worker_1, 
                         device_1, 
                         TICKET_STATUS_1)
    ticket_2 = db.Ticket(TICKET_DESC_2, 
                         TICKET_TITLE_2, 
                         worker_1, 
                         device_2, 
                         TICKET_STATUS_2)
    ticket_3 = db.Ticket(TICKET_DESC_3, 
                         TICKET_TITLE_3, 
                         worker_1, 
                         device_3, 
                         TICKET_STATUS_3)
    ticket_4 = db.Ticket(TICKET_DESC_4, 
                         TICKET_TITLE_4, 
                         worker_2, 
                         device_1, 
                         TICKET_STATUS_4)
    ticket_5 = db.Ticket(TICKET_DESC_5, 
                         TICKET_TITLE_5, 
                         worker_2, 
                         device_3, 
                         TICKET_STATUS_5)
    print('TICKETS', ticket_1, ticket_2, ticket_3, ticket_4, ticket_5)
    
    # solution onjects
    solution_1 = db.Solution(worker_1.email, 
                             SOLUTION_PROGRESS_1, 
                             SOLUTION_KEYWORDS_1,
                               device_1)
    solution_2 = db.Solution(worker_2.email, 
                             SOLUTION_PROGRESS_2, 
                             SOLUTION_KEYWORDS_2, 
                             device_2)
    print('SOLUTIONS:', solution_1, solution_2)

    # client tests
    print('CLIENT TESTS')
    
    client_test = ClientTests()
    client_test.test_add_client(client_1)
    client_test.test_add_client(client_2)

    # worker tests
    print('WORKER TESTS')
    worker_test = WorkerTests()
    #worker_test.test_add_worker(worker_1)
    #worker_test.test_add_worker(worker_2)
    worker_test.test_get_worker(worker_1.email)
    worker_test.test_get_team_workers(TEAM_1.name)

        # User tests
    print('USER TESTS')
    user_test = UserTests()
    user_test.test_add_user(user_1)
    user_test.test_add_user(user_2)

    # Ticket tests
    print('TICKET TESTS')
    ticket_tests = TicketTests()
    ticket_tests.test_add_ticket(ticket_1)
    ticket_tests.test_add_ticket(ticket_2)
    ticket_tests.test_add_ticket(ticket_3)
    ticket_tests.test_add_ticket(ticket_4)
    ticket_tests.test_add_ticket(ticket_5)

    # soltution tests
    print('SOLUTION TESTS')
    solution_tests = SolutionTests()
    solution_tests.test_add_solution(solution_1)
    solution_tests.test_add_solution(solution_2)

    # team tests
    print('TEAM TESTS')
    team_tests = TeamTests()
    team_tests.test_add_team(TEAM_1)
    team_tests.test_add_team(TEAM_2)

# test backend

testClasses()