import requests


with open('list_link_carmudi.txt') as f:
    list_link = f.readlines()
    for i in range(len(list_link)):
        list_link[i] = list_link[i].replace('\n', '')
    f.close()


# html = html.content.decode('utf-8').splitlines()
