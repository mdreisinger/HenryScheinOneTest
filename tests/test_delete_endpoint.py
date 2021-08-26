#!/usr/bin/env python3

from helpers.database_actioner import DatabaseActioner
from helpers.delete_endpoint import DeleteEndpoint

H2_JAR = "/home/mdreisinger/src/testAutomation/target/h2-1.4.200.jar"
UNIQUE_GUY_0 = (0,'Mike0','D','0000000000')
UNIQUE_GUY_1 = (1,'Mike1','Dre','1111111111')
UNIQUE_GUY_2 = (2,'Mike2','Dr. Dre','2222222222')


def setup():
    # Delete everything from the database and then add one unique guy
    dba = DatabaseActioner(H2_JAR)
    dba.execute("delete from PERSON")
    dba.execute("select * from PERSON")
    pretest_data = dba.fetchall()
    assert pretest_data == [], "Failed to clear database before running test."
    dba.execute(f"insert into PERSON values ('{UNIQUE_GUY_0[0]}','{UNIQUE_GUY_0[1]}','{UNIQUE_GUY_0[2]}','{UNIQUE_GUY_0[3]}')")
    dba.execute(f"insert into PERSON values ('{UNIQUE_GUY_1[0]}','{UNIQUE_GUY_1[1]}','{UNIQUE_GUY_1[2]}','{UNIQUE_GUY_1[3]}')")
    dba.execute(f"insert into PERSON values ('{UNIQUE_GUY_2[0]}','{UNIQUE_GUY_2[1]}','{UNIQUE_GUY_2[2]}','{UNIQUE_GUY_2[3]}')")
    dba.execute("select * from PERSON")
    pretest_data = dba.fetchall()
    assert pretest_data == [UNIQUE_GUY_0, UNIQUE_GUY_1, UNIQUE_GUY_2], "Failed to insert unique people into database before running test."
    dba.close()

def test_deleteEndpointShouldReturn200GivenValidIdAndCredentials():
    # Arrange
    setup()
    delete_endpoint = DeleteEndpoint()
    
    # Act
    actual_response = delete_endpoint.delete(UNIQUE_GUY_0[0], write_access=True)
    
    # Assert
    assert actual_response.status_code == 200

def test_deleteEndpointShouldReturn401GivenValidIdAndInvalidCredentials():
    # Arrange
    setup()
    delete_endpoint = DeleteEndpoint()
    delete_endpoint.write_credentials = ("not", "arealguy")
    
    # Act
    actual_response = delete_endpoint.delete(UNIQUE_GUY_0[0], write_access=True)
    
    # Assert
    assert actual_response.status_code == 401

def test_deleteEndpointShouldReturn403GivenValidIdAndReadOnlyCredentials():
    # Arrange
    setup()
    delete_endpoint = DeleteEndpoint()
def test_deleteEndpointShouldReturn403GivenValidIdAndReadOnlyCredentials():
    # Arrange
    setup()
    delete_endpoint = DeleteEndpoint()
    
    # Act
    actual_response = delete_endpoint.delete(UNIQUE_GUY_0[0], write_access=False)
    
    # Assert
    assert actual_response.status_code == 403

def test_deleteEndpointShouldDeleteTheCorrectPersonGivenValidIdAndCredentials_0():
    # Arrange
    setup()
    delete_endpoint = DeleteEndpoint()
    
    # Act
    actual_response = delete_endpoint.delete(UNIQUE_GUY_0[0], write_access=True)
    
    # Assert
    dba = DatabaseActioner(H2_JAR)
    dba.execute("select * from PERSON")
    data = dba.fetchall()
    assert data == [UNIQUE_GUY_1, UNIQUE_GUY_2]
    dba.close()

def test_deleteEndpointShouldDeleteTheCorrectPersonGivenValidIdAndCredentials_1():
    # Arrange
    setup()
    delete_endpoint = DeleteEndpoint()
    
    # Act
    actual_response = delete_endpoint.delete(UNIQUE_GUY_0[1], write_access=True)
    
    # Assert
    dba = DatabaseActioner(H2_JAR)
    dba.execute("select * from PERSON")
    data = dba.fetchall()
    assert data == [UNIQUE_GUY_0, UNIQUE_GUY_2]
    dba.close()

def test_deleteEndpointShouldDeleteTheCorrectPersonGivenValidIdAndCredentials_2():
    # Arrange
    setup()
    delete_endpoint = DeleteEndpoint()
    
    # Act
    actual_response = delete_endpoint.delete(UNIQUE_GUY_2[0], write_access=True)
    
    # Assert
    dba = DatabaseActioner(H2_JAR)
    dba.execute("select * from PERSON")
    data = dba.fetchall()
    assert data == [UNIQUE_GUY_0, UNIQUE_GUY_1]
    dba.close()
