from model import Schema
from service import PostService
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/create-post", methods=['PUT'])
def create_post():
    #create new posts
    return PostService().create_post(request.get_json())


@app.route('/delete', methods=['POST'])
def delete_post():
    #delete post
    return PostService().delete_post(request.get_json())


@app.route('/retrieve', methods=['GET'])
def retrieve_post():
    #retrieve existing post
    return PostService().retrieve_post(request.get_json())


@app.route('/list-n-particular', methods=['GET'])
def list_particular():
    #list the n most recent post to a particular community
    return PostService().list_particular(request.get_json())


@app.route('/list-recent', methods=['GET'])
def list_recent():
    #list the n most recent posts to any community
    return PostService().list_recent(request.get_json())


if __name__ == "__main__":
    Schema()
    app.run(debug=True)
