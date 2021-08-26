#!/usr/bin/env python3

from helpers.database_actioner import DatabaseActioner
from helpers.get_endpoint import GetEndpoint

H2_JAR = "/home/mdreisinger/src/testAutomation/target/h2-1.4.200.jar"
UNIQUE_GUY = (0,'Mike','D','6969696969')

def test_setup():
    # Delete everything from the database and then add one unique guy
    dba = DatabaseActioner(H2_JAR)
    dba.execute("delete from PERSON")
    dba.execute("select * from PERSON")
    pretest_data = dba.fetchall()
    assert pretest_data == [], "Failed to clear database before running test."
    dba.execute(f"insert into PERSON values ('{UNIQUE_GUY[0]}','{UNIQUE_GUY[1]}','{UNIQUE_GUY[2]}','{UNIQUE_GUY[3]}')")
    dba.execute("select * from PERSON")
    pretest_data = dba.fetchall()
    assert pretest_data == [UNIQUE_GUY], "Failed to insert unique person into database before running test."
    dba.close()

def test_getEndpointShouldReturn200GivenValidIdAndCredentials_read():
    # Arrange
    get_endpoint = GetEndpoint()
    
    # Act
    actual_response = get_endpoint.get(UNIQUE_GUY[0])
    
    # Assert
    assert actual_response.status_code == 200

def test_getEndpointShouldReturn200GivenValidIdAndCredentials_write():
    # Arrange
    get_endpoint = GetEndpoint()
    
    # Act
    actual_response = get_endpoint.get(UNIQUE_GUY[0], write_access=True)
    
    # Assert
    assert actual_response.status_code == 200

def test_getEndpointShouldGetCorrectData_read():
    # Arrange
    get_endpoint = GetEndpoint()
    
    # Act
    actual_response = get_endpoint.get(UNIQUE_GUY[0])
    
    # Assert
    # Usually only one assert per test but ¯\_(ツ)_/¯, teach me a better way code reviewers!
    assert actual_response.json()['id'] == UNIQUE_GUY[0]
    assert actual_response.json()['firstName'] == UNIQUE_GUY[1]
    assert actual_response.json()['lastName'] == UNIQUE_GUY[2]
    assert actual_response.json()['phoneNumber'] == UNIQUE_GUY[3]
    
def test_getEndpointShouldGetCorrectData_write():
    # Arrange
    get_endpoint = GetEndpoint()
    
    # Act
    actual_response = get_endpoint.get(UNIQUE_GUY[0], write_access=True)
    
    # Assert
    # Usually only one assert per test but ¯\_(ツ)_/¯, teach me a better way code reviewers!
    assert actual_response.json()['id'] == UNIQUE_GUY[0]
    assert actual_response.json()['firstName'] == UNIQUE_GUY[1]
    assert actual_response.json()['lastName'] == UNIQUE_GUY[2]
    assert actual_response.json()['phoneNumber'] == UNIQUE_GUY[3]
    
def test_getEndpointShouldReturn404GivenInvalidIdAndValidCredentials_read():
    # Arrange
    get_endpoint = GetEndpoint()
    
    # Act
    actual_response = get_endpoint.get(420)
    
    # Assert
    assert actual_response.status_code == 404

def test_getEndpointShouldReturn404GivenInvalidIdAndValidCredentials_write():
    # Arrange
    get_endpoint = GetEndpoint()
    
    # Act
    actual_response = get_endpoint.get(420, write_access=True)
    
    # Assert
    assert actual_response.status_code == 404

def test_getEndpointShouldReturn401GivenValidIdAndInvalidCredentials():
    # Arrange
    get_endpoint = GetEndpoint()
    get_endpoint.read_credentials = ("absolute","garbage")
    
    # Act
    actual_response = get_endpoint.get(UNIQUE_GUY[0])
    
    # Assert
    assert actual_response.status_code == 401
