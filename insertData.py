#!/usr/bin/python

import sqlite3

# conn = sqlite3.connect('test.db')
conn = sqlite3.connect('Data.db')
print "Opened database successfully";

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )");
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO LOC (NAME,X,Y,INFO) \
      VALUES ( 'Mark', 121, 23.456, 'Hello' )");

conn.commit()
print "Records created successfully";
conn.close()