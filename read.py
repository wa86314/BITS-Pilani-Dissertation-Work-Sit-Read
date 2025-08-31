from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "INFO: This Microservice is use for reading record from DB"

@app.route('/read', methods=['GET'])
def read():

    from connection import db_conn
    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT * FROM student")
    records = db_cursor.fetchall()

    html_body = "<title> Student Record </title>"
    html_body += "<h2>Student Table</h2><table border='1'>"
    html_body += "<tr><th>ID</th><th>Name</th></tr>"
    for record in records:
        html_body += f"<tr><td>{record[0]}</td><td>{record[1]}</td></tr>"
    html_body += "</table>"
    
    db_conn.commit()
    return html_body

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

