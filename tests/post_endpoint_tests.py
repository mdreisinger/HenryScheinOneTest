#!/usr/bin/env python3

import json

from helpers.database_actioner import DatabaseActioner
from helpers.post_endpoint import PostEndpoint

H2_JAR = "/home/mdreisinger/src/testAutomation/target/h2-1.4.200.jar"

VALID_DATA = {
        "firstName" : "Michael",
        "lastName" : "Dreisinger",
        "phoneNumber" : "4039093150"
}

INVALID_DATA = {
        "firstName" : "Michael",
        "lastName" : "Dreisinger",
        "phoneNumber" : "403"
}


def test_postEndpointShouldReturn201GivenValidDataAndCredentials():
    # Arrange
    post_endpoint = PostEndpoint()
    
    # Act
    actual_response = post_endpoint.post(json.dumps(VALID_DATA))
    
    # Assert
    assert actual_response.status_code == 201

def test_postEndpointShouldReturn403GivenValidDataAndReadOnlyCredentials():
    # Arrange
    post_endpoint = PostEndpoint()
    post_endpoint.credentials = ("testUsername", "testPassword")
    
    # Act
    actual_response = post_endpoint.post(json.dumps(VALID_DATA))
    
    # Assert
    assert actual_response.status_code == 403

def test_postEndpointShouldReturn401GivenValidDataAndInvalidCredentials():
    # Arrange
    post_endpoint = PostEndpoint()
    post_endpoint.credentials = ("fjriuea", "fnreaif")
    
    # Act
    actual_response = post_endpoint.post(json.dumps(VALID_DATA))
    
    # Assert
    assert actual_response.status_code == 401

def test_postEndpointShouldReturn400GivenInvalidDataAndValidCredentials():
    # Arrange
    post_endpoint = PostEndpoint()
    
    # Act
    actual_response = post_endpoint.post(json.dumps(INVALID_DATA))
    
    # Assert
    assert actual_response.status_code == 400

def test_postEndpointShouldProvideCorrectMsgGivenInvalidDataAndValidCredentials():
    # Arrange
    post_endpoint = PostEndpoint()
    expected_response = '["JSON Error: phoneNumber phoneNumber must be 10 digits."]'
    
    # Act
    actual_response = post_endpoint.post(json.dumps(INVALID_DATA))
    
    # Assert
    assert actual_response.text == expected_response

def test_postEndpointShouldCorrectlyPostToTheDatabase():
    # Arrange
    post_endpoint = PostEndpoint()
    dba = DatabaseActioner(H2_JAR)

    post_data = VALID_DATA
    unique_name = "yooo this is so uniqqqqqque"
    post_data["firstName"] = unique_name

    dba.execute("delete from PERSON")
    dba.execute("select * from PERSON")
    pretest_data = dba.fetchall()
    assert pretest_data == [], "Failed to clear database before running test."

    # Act
    post_endpoint.post(json.dumps(post_data))
    dba.execute("select * from PERSON")
    actual_data = dba.fetchall()
    dba.close()

    # Assert
    found_correct_data = False
    for person in actual_data:
        if person[1] == unique_name:
            if person[2] == post_data["lastName"] and person[3] == post_data["phoneNumber"]:
                print(f"found the data just posted: {person}")
                found_correct_data = True
    assert found_correct_data
