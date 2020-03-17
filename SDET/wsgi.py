from model import Schema
from service import PostService
from flask import Flask
from flask import request
from test_post import *

if __name__ == "__main__":
	test_post._addPosts()