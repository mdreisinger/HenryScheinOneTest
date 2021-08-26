#!/usr/bin/env python3

import jaydebeapi
from typing import List

class DatabaseActioner:
    def __init__(self, jclassname : str, url : str, credentials : List[str]=None, h2_jar : str=None):
        """!
        @brief Creates a connection to the database.
        @param jclassname The jclassname, e.g. "org.h2.Driver"
        @param url The JDBC URL, e.g. "jdbc:h2:tcp://localhost:8091/mem:personDB"
        @param credentials A list containing the database credentials, e.g. ["testDBUsername", "testDBPassword"]
        @param h2_jar The absolute path to the H2 Jar file, e.g. "/home/mdreisinger/src/testAutomation/target/h2-1.4.200.jar"
        """
        self.jclassname = jclassname
        self.url = url
        self.credentials = credentials
        self.h2_jar = h2_jar
        self.conn = jaydebeapi.connect(jclassname, url, credentials, h2_jar)
        self.curs = self.conn.cursor()
        
    def execute(self, sql_statement):
        """!
        @brief Executes the sql_statement and returns the result.
        @param sql_statement The sql_statement to execute, e.g. "select * from PERSON"
        """
        return self.curs.execute(sql_statement)


if __name__ == "__main__":
    dba = DatabaseActioner("org.h2.Driver", 
                           "jdbc:h2:tcp://localhost:8091/mem:personDB", 
                           ["testDBUsername", "testDBPassword"], 
                           "/home/mdreisinger/src/testAutomation/target/h2-1.4.200.jar")

    print(dba.execute("select * from PERSON"))
