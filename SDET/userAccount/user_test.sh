#test script for user

curl --verbose \
    -X PUT \
    --header 'Content-Type: application/json' \
    --data @user_test.json \
    http://localhost:2015/accounts/create-user 

curl --verbose \
    -X POST \
    --header 'Content-Type: application/json' \
    --data @update_email.json \
    http://localhost:2015/accounts/update-email

curl --verbose \
    -X POST \
    --header 'Content-Type: application/json' \
    --data @increment_karma.json \
    http://localhost:2015/accounts/increment-karma

curl --verbose \
    -X POST \
    --header 'Content-Type: application/json' \
    --data @decrement_karma.json \
    http://localhost:2015/accounts/decrement-karma

curl --verbose \
    -X POST \
    --data @deactivate_account.json \
    http://localhost:2015/accounts/deactivate-account