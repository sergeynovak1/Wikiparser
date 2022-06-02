import requests


def User(username):
    response = requests.get('https://jsonplaceholder.typicode.com/users', params={'username': username})
    return response.json()[0]['id']


def Posts(userId):
    list = []
    response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': userId})
    for i in range(len(response.json())):
        list.append(response.json()[i]['id'])
    return list


def Comments(postId):
    list = []
    response = requests.get('https://jsonplaceholder.typicode.com/comments', params={'postId': postId})
    for i in range(len(response.json())):
        list.append(response.json()[i]['email'])
    return list


def GetEmail(username):
    a = []
    for i in Posts(User(username)):
        for x in i:
            a.append(Comments(x))
    return a


