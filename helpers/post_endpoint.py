#!/usr/bin/env python3

import requests
from typing import Tuple

from helpers.base_endpoint import BaseEndpoint


class PostEndpoint(BaseEndpoint):
    def __init__(self, 
                 server : str = "http://localhost",
                 port : str = "8083",
                 credentials : Tuple[str, str] = ("admin", "testPassword"),
                 endpoint : str = "/v1/post-person"):
        """!
        @brief  A class which provides access to the Post Endpoint.
        @param  server The server address that the application is running on.
        @param  port The port that thte application is running on.
        @param  credentials A list containing the application credentials.
        @param  endpoint The url extension that provides access to the endpoint.
        """
        super().__init__(server, port)
        self.post_url = self.url + endpoint
        self.credentials = credentials

    def post(self, data : dict):
        """!
        @brief  Post the data to the endpoint.
        @param  data the data to Post to the endpoint.
        @return The request response.
        """
        return requests.post(self.post_url, data=data, auth=self.credentials)
