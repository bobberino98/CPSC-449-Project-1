from locust import HttpLocust, TaskSet, task, between
import json
import requests
from faker import Faker
from faker.providers import internet

fake = Faker()

username = fake.user_name()
email = fake.email()
karma = fake.random_int(min=1, max=1000,step=1)

dataCreateUser = {"user_name": username, "email": email, "karma": karma}
dataUsername = {"user_name": username}
dataEmail = {"user_name": username, "email": email}


class userTask(TaskSet):
    @task(1)
    def create_user(self):
        self.client.put("/accounts/create-user", json=dataCreateUser)

    @task(2)
    def update_email(self):
        self.client.post("/accounts/update-email", json=dataEmail)

    @task(3)
    def increment_karma(self):
        self.client.post("/accounts/increment-karma", json=dataUsername)

    @task(3)
    def decrement_karma(self):
        self.client.post("/accounts/decrement-karma", json=dataUsername)

    @task(4)
    def deactivate_account(self):
        self.client.post("/accounts/deactivate-account", json=dataUsername)


class websiteUser(HttpLocust):
    task_set = userTask
    wait_time = between(2, 5)