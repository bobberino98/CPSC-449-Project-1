#!/bin/sh

curl --verbose \
     -X PUT \
     --header 'Content-Type: application/json' \
     --data @post.json \
     http://localhost:5000/posts/create-post


curl --verbose \
     -X GET \
     --header 'Content-Type: application/json' \
     --data @title.json \
     http://localhost:5000/posts/retrieve


curl --verbose \
     -X POST \
     --header 'Content-Type: application/json' \
     --data @title.json \
     http://localhost:5000/posts/delete 


curl --verbose \
     -X GET \
     --header 'Content-Type: application/json' \
     --data @list_particular.json \
     http://localhost:5000/posts/list-n-particular


curl --verbose \
     -X GET \
     --header 'Content-Type: application/json' \
     --data @list_recent.json \
     http://localhost:5000/posts/list-recent