#!/usr/bin/env python3

import requests
from typing import Tuple

from helpers.base_endpoint import BaseEndpoint


class DeleteEndpoint(BaseEndpoint):
    def __init__(self, 
                 server : str = "http://localhost",
                 port : str = "8083",
                 headers : str = {'Content-Type': 'application/json', 
                                  'Authorization': 'Basic YWRtaW46dGVzdFBhc3N3b3Jk'},
                 read_credentials : Tuple[str, str] = ("testUsername", "testPassword"),
                 write_credentials : Tuple[str, str] = ("admin", "testPassword"),
                 endpoint : str = "/v1/delete-person/"):
        """!
        @brief  A class which provides access to the Delete Endpoint.
        @param  server The server address that the application is running on.
        @param  port The port that thte application is running on.
        @param  headers The headers to send with the request.
        @param  read_credentials A list containing the application read credentials.
        @param  write_credentials A list containing the application write credentials.
        @param  endpoint The url extension that provides access to the endpoint.
        """
        super().__init__(server, port, headers)
        self.delete_url = self.url + endpoint
        self.read_credentials = read_credentials
        self.write_credentials = write_credentials

    def delete(self, id : int = 0, write_access = False):
        """!
        @brief  delete the data for the person with id from the endpoint.
        @param  id the id of the person to delete from the endpoint.
        @param  write_access True if you want to do a delete request with write access, 
                             False if you want to do the delete request with read access.
        @return The request response.
        """
        if write_access:
            return requests.request("DELETE", 
                                    f"{self.delete_url}{id}",
                                    headers=self.headers,
                                    auth=self.write_credentials)

        return requests.request("DELETE", 
                                f"{self.delete_url}{id}",
                                headers=self.headers,
                                auth=self.read_credentials)
