# import sys
import queue
import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# 从网路获取queue
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器
server_addr = '127.0.0.1'
print("connect to server %s..." % server_addr)

m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

# 从队列中获取
for i in range(10):
    try:
        n = task.get(timeout=1)
        print("run task %d*%d..." % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print("task is empty")
# end
print("worker exit.")
