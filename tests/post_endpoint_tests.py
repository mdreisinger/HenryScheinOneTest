#!/usr/bin/env python3

import json

from helpers.database_actioner import DatabaseActioner
from helpers.post_endpoint import PostEndpoint

H2_JAR = "/home/mdreisinger/src/testAutomation/target/h2-1.4.200.jar"

def test_postEndpointShouldReturn201GivenValidDataAndCredentials():
    # Arrange
    #dba = DatabaseActioner(H2_JAR)
    post_endpoint = PostEndpoint()
    data = {
        "firstName" : "Michael",
        "lastName" : "Dreisinger",
        "phoneNumber" : "4039093150"
    }
    
    # Act
    actual_response = post_endpoint.post(json.dumps(data))
    
    # Assert
    assert actual_response.status_code == 201
