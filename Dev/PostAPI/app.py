from model import Schema
from service import PostService
from flask import Flask      
from flask import request     


app = Flask(__name__)             

@app.route("/create-post", methods=['PUT'])                  
def create_post():                     
    return PostService().create_post(request.get_json())

@app.route('/delete', methods=['POST'])
def delete_post():
    return PostService().delete_post(request.get_json())

@app.route('/retrieve', methods=['GET'])
def retrieve_post():
    return PostService().retrieve_post(request.get_json())

@app.route('/list-n-particular', methods=['GET'])
def list_particular():
    return PostService().list_particular(request.get_json())

@app.route('/list-recent', methods=['GET'])
def list_recent():
    return PostService().list_recent(request.get_json())

if __name__ == "__main__":       
    Schema()
    app.run(debug=True)                    