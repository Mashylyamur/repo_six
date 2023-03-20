import requests
from threading import Thread
import time

def get_html(link):
    sess = requests.get(link)
    print(sess.text)
links = ['https://www.google.ru/', 'https://www.youtube.com/', 'https://ru.wikipedia.org/', 'https://dzen.ru/', 'https://ria.ru/']
t1 = time.time()
for i in links:
    get_html(i)
print(f'Время последовательного выполнения: {time.time() - t1}')
threads = [Thread(target = get_html, args=(i, )) for i in links]
t2 = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f'Время паралелльного выполнения: {time.time() - t2}')
