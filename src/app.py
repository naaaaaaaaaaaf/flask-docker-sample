import os
from flask import Flask, request
from sshtunnel import SSHTunnelForwarder
import pymysql.cursors

app = Flask(__name__)

dbConfigs = { "HOST_IP": os.environ.get("HOST_IP"), "HOST_PORT": os.environ.get("HOST_PORT"), "DB_PORT": os.environ.get("DB_PORT"), "DB_USER": os.environ.get("DB_USER"), "DB_PASS": os.environ.get("DB_PASS") }

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sample', methods=['GET'])
def sample_post():
    return "param1:{}".format(dbConfigs)

@app.route('/db', methods=['GET'])
def db_show():
    with SSHTunnelForwarder((dbConfigs["HOST_IP"], dbConfigs["HOST_PORT"]),ssh_host_key=None,ssh_pkey=None,ssh_username=dbConfigs["HOST_USER"],ssh_password=dbConfigs["HOST_PASS"],remote_bind_address=("localhost", dbConfigs["DB_PORT"]),allow_agent=False
        ) as ssh:
        ssh.start()
        conn = pymysql.connect(host='localhost',
            port = ssh.local_bind_port,
            user=dbConfigs["DB_USER"],
            password=dbConfigs["DB_PASS"],
            db=dbConfigs["DB_NAME"],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        sql = ""
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
    return "param1:{}".format(results)

if __name__ == "__main__":
    app.run(debug=True)