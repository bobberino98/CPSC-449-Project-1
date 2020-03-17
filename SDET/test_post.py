import requests
import time
import datetime
import app, model, service

class TestPosts:
    def test_createPosts(**arg):
        URL = 'http://127.0.0.1:5500/create-post'

        resp = requests.post(URL, data = arg)

        if resp.status_code == 201:
            return True, resp.text

        else:
            return False, -1

    def test_listRecents(community, n):
        URL = 'http://127.0.0.1:5500/list-recents/' + f'{community}?n={n}'

        resp = requests.get(URL)

        if resp.status_code == 200:
            obj = resp.obj
            return True,obj
        else:
            print (F'Recent post {n} for {community} fail to retrieve')
            return False, -1

        
    def test_listnParticular(n):
        URL = 'http://127.0.0.1:5500/list-n-particular?=' + f'{n}'
        
        resp = requests.get(URL)

        if resp.status_code == 200:
            obj = resp.json()
            return True, obj
        else: 
    
            return False, -1
        print()

    def test_deletePosts(title):
        URL = 'http://127.0.0.1:5500/delete/' + f'{title}'
        resp = requests.delete(URL)

        if resp.status_code == 204:
            return True
        else:
            return False


    def _addPosts():

        addInData = [
            {
                "title": "title1",
                "text": "text1",
                "community": "community1",
                "URL": "www.urlresource1.com",
                "username": "user1",
                "postDate": "02/28/2020"
            }, 
            {
                "title": "title2",
                "text": "text2",
                "community": "community2",
                "URL": "www.urlresource2.com",
                "username": "user2",
                "postDate": "02/27/2020"
            }, 
            {
                "title": "title3",
                "text": "text3",
                "community": "community3",
                "URL": "www.urlresource3.com",
                "username": "user3",
                "postDate": "02/28/2020"
            }, 
            {
                "title": "title4",
                "text": "text4",
                "community": "community4",
                "URL": "www.urlresource4.com",
                "username": "user4",
                "postDate": "02/28/2020"
            }, 
            {
                "title": "title5",
                "text": "text5",
                "community": "community5",
                "URL": "www.urlresource5.com",
                "username": "user5",
                "postDate": "02/28/2020"
            }, 
            {
                "title": "title6",
                "text": "text6",
                "community": "community6",
                "URL": "www.urlresource6.com",
                "username": "user6",
                "postDate": "02/28/2020"
            }, 
            {
                "title": "title7",
                "text": "text7",
                "community": "community7",
                "URL": "www.urlresource7.com",
                "username": "user7",
                "postDate": "02/28/2020"
            }, 
            {
                "title": "title8",
                "text": "text8",
                "community": "community8",
                "URL": "www.urlresource8.com",
                "username": "user8",
                "postDate": "02/28/2020"
            }, 
            {
                "title": "title9",
                "text": "text9",
                "community": "community9",
                "URL": "www.urlresource9.com",
                "username": "user9",
                "postDate": "02/28/2020"
            }, 
        ]

        for i in addInData:
            passed, resp = test_createPosts(**i)
            time.sleep(1)

        return passed, resp
def main():
    _addPosts()