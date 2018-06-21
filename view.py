# to view the table
import sqlite3
conn = sqlite3.connect('url_data.db')
c = conn.cursor()

query = c.execute("select * from malware") # This line performs query and returns json result
print query.fetchall()
