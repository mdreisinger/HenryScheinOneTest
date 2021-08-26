#!/usr/bin/env python3

from helpers.database_actioner import DatabaseActioner
from helpers.post_endpoint import PostEndpoint

H2_JAR = "/home/mdreisinger/src/testAutomation/target/h2-1.4.200.jar"

def test_postEndpointShouldReturn200GivenValidDataAndCredentials():
    # Arrange
    #dba = DatabaseActioner(H2_JAR)
    post_endpoint = PostEndpoint()
    data = {
        "firstName" : "Michael",
        "lastName" : "Dreisinger",
        "phoneNumber" : "4039093150"
    }
    
    # Act
    actual_response = post_endpoint.post(data)
    
    # Assert
    assert actual_response.status_code == 200
