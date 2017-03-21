#!/usr/bin/python

import sqlite3

# conn = sqlite3.connect('test.db')
conn = sqlite3.connect('Data.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE LOC
       (ID INTEGER PRIMARY KEY      NOT NULL,
       NAME         CHAR(50)    NOT NULL,
       X            REAL     NOT NULL,
       Y            REAL     NOT NULL,
       INFO         TEXT);''')
print "Table created successfully";

conn.close()