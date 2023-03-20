import time
from threading import Thread
def get_thread(thread_name):
    time.sleep(1)
    print(f'Поток {thread_name}')
s = ['one', 'two', 'three', 'four', 'five']
t1 = time.time()
for i in s:
    get_thread(i)
print(f'Время последовательного выполнения: {time.time() - t1}')
threads = [Thread(target = get_thread, args=(i, )) for i in s]
t2 = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f'Время параллельного выполнения: {time.time() - t2}')
