from locust import HttpLocust, TaskSet, task, between
import json
import requests
from faker import Faker

fake = Faker()

username = fake.username()
email = fake.email()
karma = fake.karma()

dataUser = {"username":username, "email":email, "karma":karma}

class userTask(TaskSet):
    @task(1)
    def create_user():
        self.client.post("/accounts/create-user", json=dataUser)

    @task(2)
    def update_email():
        self.client.post("/accounts/update-email/post?user_name=%d" %{username})

    @task(3)
    def increment_karma():
        self.client.post("/accounts/increment-karma/post?user_name=%d" %{username})

    @task(3)
    def decrement_karma():
        self.client.post("/accounts/decrement-karma/post?user_name=%d" %{username})

    @task(4)
    def deactivate_account():
        self.client.post("/accounts/deactivate-account/post?user_name=%d" %{username})


class websiteUser(HttpLocust):
    task_set = userTask
    min_wait = 1000
    max_wait = 2000