#!/usr/bin/env python3


class BaseEndpoint:
    def __init__(self, server : str, port : str, headers : str):
        """!
        @brief  a parent class for endpoint classes to inherit from.
        @param  server The server address that the application is running on, e.g. "http://localhost".
        @param  port The port that thte application is running on, e.g. "8083".
        @param  headers The headers to send with the request.
        """
        self.server = server
        self.port = port
        self.url = server+":"+port
        self.headers = headers
