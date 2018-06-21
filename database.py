# This script is to create database
import sqlite3
conn = sqlite3.connect('url_data.db')
c = conn.cursor()
#Creating table with two fields
c.execute('''CREATE TABLE malware (ip_port text, strings text)''')

#inserting some values for testing
c.execute('''INSERT INTO MALWARE VALUES('1.1.1.0:80','xxx')''')
c.execute('''INSERT INTO MALWARE VALUES('1.1.1.1:81','!&*')''')
c.execute('''INSERT INTO MALWARE VALUES('test.domain:80','abc')''')
conn.commit()

conn.close()

