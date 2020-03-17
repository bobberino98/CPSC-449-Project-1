import requests
import datetime
import time


def case_retrievePosts(title):
    URL = 'http://localhost:5000/retrieve' + f'{title}'

    resp = requests.get(URL)

    if resp.status_code == 200:
        obj = resp.json()
        return True, obj

    else:
        print('Fail to retrieve the post title {title}!')
        return false, -1
    print()


def case_deletePosts(title):
    URL = 'http://localhost:5000/delete/' + f'{title}'

    resp = requests.delete(URL)

    if resp.status_code == 204:
        return True

    else:
        return False


def case_listRecentPosts(**arg):
    URL = 'http://localhost:5000/list-recent'
    resp = requests.get(URL, data=arg)

    if resp.status_code == 201:
        obj = resp.json()
        return True, obj

    else:
        return False, -1


def case_listnParticular(community, n):

    URL = 'http://localhost:5000/list-n-particular/' + f'{community}?n={n}'
    resp = requests.get(URL)

    if resp.status_code == 200:
        obj = resp.json()
        return True, obj

    else:
        print(f'Fail to retrieve post {n} from {community}!')


def _createPosts():

    addInData = [
        {
            "title": "title 1",
            "text": "text 1",
            "community": "community1",
            "URL": "www.urlresource1.com",
            "username": "user 1",
            "postDate": "02/28/2020"
        },
        {
            "title": "title 2",
            "text": "text 2",
            "community": "community2",
            "URL": "www.urlresource2.com",
            "username": "user 2",
            "postDate": "02/27/2020"
        },
        {
            "title": "title 3",
            "text": "text 3",
            "community": "community3",
            "URL": "www.urlresource3.com",
            "username": "user 3",
            "postDate": "02/28/2020"
        },
        {
            "title": "title 4",
            "text": "text 4",
            "community": "community4",
            "URL": "www.urlresource4.com",
            "username": "user 4",
            "postDate": "02/28/2020"
        },
        {
            "title": "title 5",
            "text": "text 5",
            "community": "community5",
            "URL": "www.urlresource5.com",
            "username": "user 5",
            "postDate": "02/29/2020"
        },
        {
            "title": "title 6",
            "text": "text 6",
            "community": "community6",
            "URL": "www.urlresource6.com",
            "username": "user 6",
            "postDate": "02/28/2020"
        },
        {
            "title": "title 7",
            "text": "text 7",
            "community": "community7",
            "URL": "www.urlresource7.com",
            "username": "user 7",
            "postDate": "02/28/2020"
        },
        {
            "title": "title 8",
            "text": "text 8",
            "community": "community8",
            "URL": "www.urlresource8.com",
            "username": "user 8",
            "postDate": "02/28/2020"
        },
        {
            "title": "title 9",
            "text": "text 9",
            "community": "community9",
            "URL": "www.urlresource9.com",
            "username": "user 9",
            "postDate": "02/28/2020"
        },
    ]
    for i in addInData:
       isPassed, resp = case_listRecentPosts(**i)
       time.sleep(1)

    return isPassed, resp

"""def main():
    delID = 1
    
    isPassed, resp = createPosts()

    delID = 17 
    print()
    print('*'*50)
    print(f'1. Get post by title at title = {title}')
    print('*'*50)
    print()

    Answer1 = []

    for i in myDB:
        if i['title'] == title:
            Answer1.append(i)

    print('Correct result from database:')
    print(f'Length = {len{Answer1}}')
    print('Post:')
    print(f'{Answer1}')

    print('-'*10 + '\n')

    isPassed, postbyTitle = case_listRecentPosts(delID)

    if isPassed and (postbyTitle in myDB):
        length = 1
        print('Result from test case\n')
        print(f'Length = {length}\n')
        print('Post:')
        print(f'{postbyTitle}')

        print('-'*10 + '\n')
        print('Test result : \n'.upprt())
        print('Test get post by title is successful')

    else:
        print(f'Fail to get post by title')

    myCommunity = 'community1'
    n = 3

    print()
    print('*'*50)
    print(f'2. Test get post {n} from {myCommunity}')
    print('*'*50)
    print()

    Answer=[]
    i = len(myDB) - 1
    
    while i > 0 and len(Answer) < n:
        if myDB[i]['Community'] == myCommunity:
            Answer.append(myDB[i])
            i -= 1

        else:
            i -= 1

    print('Correct Answer from database:\n')
    
"""


if __name__ == '__main__':
    print('test complete')
