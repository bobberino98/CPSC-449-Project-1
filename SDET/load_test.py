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
n = fake.random_int(min=1, max=200,step=1)
postDate = fake.date()
dataPost = {"title": title, "text": text,
            "username": username, "community": community, "URL": url, "postDate": postDate}
dataTitle = {"title": title}
dataListRecent = {"n": n}
dataListParticular = { "community": community,"n": n}
myheaders = {'Content Type': 'application/json', 'Accept': 'application/json'}


class userTask(TaskSet):
    @task(1)
    def post(self):
        self.client.put("/posts/create-post", json=dataPost)

    @task(2)
    def retrievePost(self):
        self.client.get("/posts/retrieve", json=dataTitle)

    @task(2)
    def deletePost(self):
        self.client.post("/posts/delete", json=dataTitle)  # title

    @task(4)
    def listnParticularPost(self):
        self.client.get("/posts/list-n-particular", json=dataListParticular)  # community and n

    @task(2)
    def listRecentPost(self):
        self.client.get("/posts/list-recent", json=dataListRecent)  # n


class websiteUser(HttpLocust):
    task_set = userTask
    wait_time = between(2, 5)
