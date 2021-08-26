#!/usr/bin/env python3

import requests
from typing import Tuple

from helpers.base_endpoint import BaseEndpoint


class GetEndpoint(BaseEndpoint):
    def __init__(self, 
                 server : str = "http://localhost",
                 port : str = "8083",
                 headers : str = {'Content-Type': 'application/json', 
                                  'Authorization': 'Basic YWRtaW46dGVzdFBhc3N3b3Jk'},
                 read_credentials : Tuple[str, str] = ("testUsername", "testPassword"),
                 write_credentials : Tuple[str, str] = ("admin", "testPassword"),
                 endpoint : str = "/v1/get-person/"):
        """!
        @brief  A class which provides access to the Post Endpoint.
        @param  server The server address that the application is running on.
        @param  port The port that thte application is running on.
        @param  headers The headers to send with the request.
        @param  read_credentials A list containing the application read credentials.
        @param  write_credentials A list containing the application write credentials.
        @param  endpoint The url extension that provides access to the endpoint.
        """
        super().__init__(server, port, headers)
        self.get_url = self.url + endpoint
        self.read_credentials = write_credentials
        self.write_credentials = write_credentials

    def get(self, id : int = 0, write_access = False):
        """!
        @brief  get the data for the person with id from the endpoint.
        @param  id the id of the person to get from the endpoint.
        @param  write_access True if you want to do a get request with write access, 
                             False if you want to do the get request with read access.
        @return The request response.
        """
        if write_access:
            return requests.request("GET", 
                                    f"{self.get_url}{id}",
                                    headers=self.headers,
                                    auth=self.write_credentials)

        return requests.request("GET", 
                                f"{self.get_url}{id}",
                                headers=self.headers,
                                auth=self.read_credentials)
