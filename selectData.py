#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('Data.db')
print "Opened database successfully";

cursor = conn.execute("SELECT id, name, x, y, info  from LOC")
for row in cursor:
   print row

print "Operation done successfully";
conn.close()

