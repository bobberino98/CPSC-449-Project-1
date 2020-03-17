#!/bin/sh

curl --verbose \
     -X PUT \
     --header 'Content-Type: application/json' \
     --data @post.json \
     http://localhost:5000/create-post


curl --verbose \
     -X GET \
     --header 'Content-Type: application/json' \
     --data @post.json \
     http://localhost:5000/retrieve


curl --verbose \
     -X DELETE
     http://localhost:5000/delete 


curl --verbose \
     -X GET
     --header 'Content-Type: application/json' \
     --data @post.json \
     http://localhost:5000/list-n-particular


curl --verbose \
     -X GET
     --header 'Content-Type: application/json' \
     --data @post.json \
     http://localhost:5000/list-recent