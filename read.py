from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "INFO: This microservices is use for reading record from Database"
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

