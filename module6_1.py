import time
from threading import Thread
def get_thread(thread_name):
    time.sleep(1)
    print(f'Поток {thread_name}')
s = ['one', 'two', 'three', 'four', 'five']
#for i in s:
#    get_thread(i)
threads = [Thread(target = get_thread, args=(i, )) for i in s]

for t in threads:
    t.start()
for t in threads:
    t.join()
