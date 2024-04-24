import pytest
import sys
sys.path.insert(0, './')
from bson.json_util import dumps
import dbClasses as db
import grabInfo as grab
import updateInfo as update
import addInfo as add

connector = db.Connections()

# create class for testing add info
class TestAddInfo:
    def __init__(self):
        self.connection = connector

    # function to test the add ticket function
    def test_add_ticket():
        # set the ticket cursor
        ticket_cursor = add.add_ticket(0, 
                                       'test file', 
                                       'test ticket', 
                                       'test type', 
                                       'tester', 
                                       'test device', 
                                       'test client', 
                                       'test team')
        
        # test that the actual and expected values are the same
        assert ticket_cursor != None
    #
    def test_add_client():
        # set the client cursor
        client_cursor = add.add_client(0, 
                                       'test email', 
                                       'test phone number', 
                                       '000', 
                                       '000', 
                                       'test contact')
        # check client was added
        assert client_cursor != None

    
    def test_add_device():
        # set the device cursor
        device_cursor = add.add_device(0, 
                                       'test worker', 
                                       'test type', 
                                       [], 
                                       True)

        # test the actual values match expected values
        assert device_cursor != None
    
    def test_add_worker():
        # set the worker cursor
        worker_cursor = add.add_worker(0, 
                                       'test worker', 
                                       'test email', 
                                       'test team', 
                                       [])
        # check the actual values match the expected values
        assert worker_cursor != None

    def test_add_team():
        # set the team cursor
        team_cursor = add.add_team(0, [], [], 'test team')
        # get list of actual values
    
        assert team_cursor != None

    
# create class for testing grab info
class TestGrabInfo:
    def __init__(self):
        self.connection = connector
    def test_grab_client_tickets(email, expected_tickets):
        # set the ticket value
        tickets_actual = grab.client_email_find_tickets(email)
        # check the actual tickets match expected tickets
        assert tickets_actual == expected_tickets
    def test_find_ticket(ticket_id):
        # set the actual ticket value
        ticket_actual = grab.ticket_id_find_ticket(ticket_id)
        # check the cursor is not none and a ticket was found
        assert ticket_actual != None
    def test_worker_tickets(worker_id, expected_tickets):
        # set the actual worker ticket value
        tickets_actual = grab.worker_id_find_tickets(worker_id)
        print(tickets_actual)
        # check if the actual matches the expected values
        assert tickets_actual == expected_tickets
    def test_worker_email_tickets(email, expected_tickets):
        # set the actual tickets value
        actual_tickets = grab.worker_email_find_tickets(email)
        # check if the actual values matches the expected
        assert actual_tickets == expected_tickets
    def test_team_tickets(team_id, expected_tickets):
        # set the value for the actul tickets
        tickets_actual = grab.find_team_tickets(team_id)
        # check if the actual values match the expected values
        assert tickets_actual == expected_tickets
    def test_find_worker(worker_id):
        # get the actual value
        worker_actual = grab.find_worker(worker_id)
        # check the actual value is not none
        assert worker_actual != None
    def test_find_worker_with_email(email):
        # get the actual value
        worker_actual = grab.find_worker_with_email(email)
        # check actual value not none
        assert worker_actual != None
    def test_find_device(device_id):
        # get actal device value
        device_actual = grab.find_device(device_id)
        # check the actual value not none
        assert device_actual != None
    def test_find_client(client_id):
        # get actual client value
        client_actual = grab.find_client(client_id)
        # check the value is not none
        assert client_actual != None
    

# create class for testing update info
class TestUpdateInfo:
    def __init__(self):
        self.connection = connector
    def test_ticket_worker(email, ticket_id):
        # get the cursor 
        ticket_cursor = update.update_ticket_worker(email, ticket_id)
        # check if expected matches actual
        assert ticket_cursor != None
    def test_ticket_team(new_team_id, ticket_id):
        # get the ticket cursor
        ticket_cursor = update.update_ticket_team(new_team_id, ticket_id)
        # check that the actual value matches the expected value
        assert ticket_cursor != None


def testBackend():
    # test add info
    TestAddInfo.test_add_ticket()
    TestAddInfo.test_add_worker()
    TestAddInfo.test_add_client()
    TestAddInfo.test_add_team()
    TestAddInfo.test_add_device()
    print('add info test passed')
    # test grab info
    TestGrabInfo.test_find_client('c1')
    TestGrabInfo.test_find_device('d-000')
    TestGrabInfo.test_find_ticket('t1')
    TestGrabInfo.test_find_worker('w0')
    TestGrabInfo.test_find_worker_with_email('jdoe@company.com')
    TestGrabInfo.test_grab_client_tickets('test@email.com', ['t-000'])
    TestGrabInfo.test_team_tickets('g0', [])
    TestGrabInfo.test_worker_email_tickets('jdoe@company.com', ['t-000'])
    TestGrabInfo.test_worker_tickets('w0', 'test ticket')
    print('grab info tests passed')
    # test update info
    TestUpdateInfo.test_ticket_team('g0', 't0')
    TestUpdateInfo.test_ticket_worker('jdoe@company.com', ['t0'])
    print('update info tests passed')

testBackend()