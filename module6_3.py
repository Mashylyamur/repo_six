import requests
from threading import Thread

def get_html(link):
    sess = requests.get(urls)
    print(sess.text)
urls = ['https://www.google.ru/', 'https://www.youtube.com/', 'https://ru.wikipedia.org/', 'https://dzen.ru/', 'https://ria.ru/']
#for i in urls:
#    get_html(i)
threads = [Thread(target = get_html, args=(i, )) for i in urls]

for t in threads:
    t.start()
for t in threads:
    t.join()

