# HenryScheinOneTest

## Objective
Run SQL commands from the Person Table to verify data is correctly inserted, and deleted

## Scope
* POST
  * Write access
* GET
  * Write access
  * Read access
* DELETE
  * Write access

## To run these tests:
* Make sure the application under test is running using these instructions: https://github.com/audiomojo/testAutomation/blob/master/Henry%20Schein%20One%20SET%20Test.docx
* You need to download this file: https://github.com/audiomojo/testAutomation/blob/master/target/h2-1.4.200.jar
  * Update the H2_JAR variable in following files with the absolute path to the above file:
    * tests/test_post_endpoint.py
    * tests/test_get_endpoint.py
    * tests/test_delete_endpoint.py
