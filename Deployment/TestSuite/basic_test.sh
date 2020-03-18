#test script for user
curl --verbose \
     -X PUT \
     --header 'Content-Type: application/json' \
     --data @./Data/post.json \
     http://localhost:2015/posts/create-post


curl --verbose \
     -X GET \
     --header 'Content-Type: application/json' \
     --data @./Data/title.json \
     http://localhost:2015/posts/retrieve


curl --verbose \
     -X POST \
     --header 'Content-Type: application/json' \
     --data @./Data/title.json \
     http://localhost:2015/posts/delete 


curl --verbose \
     -X GET \
     --header 'Content-Type: application/json' \
     --data @./Data/list_particular.json \
     http://localhost:2015/posts/list-n-particular


curl --verbose \
     -X GET \
     --header 'Content-Type: application/json' \
     --data @./Data/list_recent.json \
     http://localhost:2015/posts/list-recent

curl --verbose \
    -X PUT \
    --header 'Content-Type: application/json' \
    --data @./Data/user_test.json \
    http://localhost:2015/accounts/create-user 

curl --verbose \
    -X POST \
    --header 'Content-Type: application/json' \
    --data @./Data/update_email.json \
    http://localhost:2015/accounts/update-email

curl --verbose \
    -X POST \
    --header 'Content-Type: application/json' \
    --data @./Data/increment_karma.json \
    http://localhost:2015/accounts/increment-karma

curl --verbose \
    -X POST \
    --header 'Content-Type: application/json' \
    --data @./Data/decrement_karma.json \
    http://localhost:2015/accounts/decrement-karma

curl --verbose \
    -X DELETE \
    --header 'Content-Type: application/json' \
    --data @./Data/deactivate_account.json \
    http://localhost:2015/accounts/deactivate-account