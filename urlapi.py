
from flask import Flask, jsonify

app = Flask(__name__)

import sqlite3
conn = sqlite3.connect('./url_data.db', check_same_thread=False)
c = conn.cursor()

hostname_port = list()
strig = list()

query = c.execute("select * from malware") # This line performs query and returns json result
for i in  query.fetchall():
    hostname_port.append(i[0])
    strig.append(i[1])



@app.route('/urlinfo/1/', methods=['GET'])
def get_all():
    return jsonify({'IP and port' : hostname_port ,'String' : strig})



@app.route('/urlinfo/1/<ip_port>/<st>', methods=['GET'])
def get_tasks(ip_port,st):
    if ip_port not in hostname_port:
        statIP = 'hostname and port are Safe!'
    else:
        statIP = "BLOCKED!, hostname and port are listed in the database."
    for i in strig:
        if i in st:
            statS = "BLOCKED, string listed in the database."
            break
        else:
            statS = "String Safe as its not listed in database."
    return jsonify({'url':'http://'+ ip_port + '/'+ st,
                    'IP and port Safety':statIP,
                    'string safety': statS})


if __name__ == '__main__':
    app.run(host='localhost', port=51, debug=True)