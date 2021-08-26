#!/usr/bin/env python3

import jaydebeapi
from typing import List

class DatabaseActioner:
    def __init__(self,
                 h2_jar : str,
                 jclassname : str = "org.h2.Driver",
                 url : str = "jdbc:h2:tcp://localhost:8091/mem:personDB",
                 credentials : List[str] = ["testDBUsername", "testDatabasePassword"]):
        """!
        @brief  Creates a connection to the database.
        @param  h2_jar The absolute path to the H2 Jar file, e.g. "/home/mdreisinger/src/testAutomation/target/h2-1.4.200.jar"
        @param  jclassname The jclassname.
        @param  url The JDBC URL.
        @param  credentials A list containing the database credentials.
        """
        self.h2_jar = h2_jar
        self.jclassname = jclassname
        self.url = url
        self.credentials = credentials
        self.conn = jaydebeapi.connect(jclassname, url, credentials, h2_jar)
        self.curs = self.conn.cursor()
        
    def execute(self, sql_statement):
        """!
        @brief  Executes the sql_statement and returns the result.
        @param  sql_statement The sql_statement to execute, e.g. "select * from PERSON"
        @return The sql response. 
        """
        return self.curs.execute(sql_statement)


if __name__ == "__main__":
    dba = DatabaseActioner("org.h2.Driver", 
                           "jdbc:h2:tcp://localhost:8091/mem:personDB", 
                           ["testDBUsername", "testDBPassword"], 
                           "/home/mdreisinger/src/testAutomation/target/h2-1.4.200.jar")

    print(dba.execute("select * from PERSON"))
