#!/bin/sh

curl --verbose \
     --request POST \
     --header 'Content-Type: application/json' \
     --data @createpost.json \
     http://127.0.0.1:5500/