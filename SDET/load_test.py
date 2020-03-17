from locust import HttpLocust, TaskSet, task, between
import json
import requests
from faker import Faker

fake = Faker()

community_list = [
    'lollipop', 'poptart', 'icee',
    'waffle', 'popsicle', 'gummies',
    'Cookies', 'oatmeal', 'pie',
    'syrup', 'Beans', 'milk', 'cereals'
]
# posting
title = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
text = fake.sentence(nb_words=3, variable_nb_words=True, ext_word_list=None)
username = fake.user_name()
url = fake.image_url()
community = fake.word(ext_word_list=community_list)
n = fake.nID()

dataPost = {"title": title, "text": text,
            "username": username, "community": community, "url": url}
myheaders = {'Content Type': 'application/json', 'Accept': 'application/json'}


class userTask(TaskSet):
    @task(1)
    def post(self):
        self.client.post("/create-post", json=dataPost, headers=myheaders)

    @task(2)
    def retrievePost(self):
        self.client.get("/retrieve/get?title=%d" % {title})

    @task(2)
    def deletePost(self):
        self.client.post("/delete/post?title=%d" % {title})  # title

    @task(4)
    def listnParticularPost(self):
        self.client.get("/list-n-particular/get?=")  # community and n

    @task(2)
    def listRecentPost(self):
        self.client.get("/list-recent/get?n=%d" % (n))  # n


class websiteUser(HttpLocust):
    task_set = userTask
    wait_time = between(2, 5)
