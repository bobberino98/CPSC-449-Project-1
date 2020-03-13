#import json
#import unittest
#from unittest import TestCase
#import app
#import datetime
#from Scripts import requests
#from unittest.mock import patch

#class TestApp(TestCase):
#    @patch('request.post')
 #   def test_createPosts(self, mock_post):
  #      result = {"title": "value1", "text": "value2", "community":"value3", "URL": "value4", "username":"value5", "postDate": "value6"}
   #     resp = requests.post("http://127.0.0.1:5500/create-post", data=json.dumps(result), headers={'Content-Type': 'application/json'})
    #    mock_post.assert_called_with("http://127.0.0.1:5500/create-post", data=json.dumps(result), headers={'Content-Type': 'application/json'})
        
#if __name__ == '__main__':
 #   unittest.main()
