import random
import time
import queue
from multiprocessing.managers import BaseManager

# 发生队列
task_queue = queue.Queue()
# 接受队列
result_queue = queue.Queue()


# 从basemanager继承queuemanager
class QueueManager(BaseManager):
    pass


# 把两个接口注册到网络，callable关联queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000，设置验证码abc
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动
manager.start()
# 获得通过网络访问的queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 任务，测试
for i in range(10):
    time.sleep(1)
    n = random.randint(0, 10000)
    print("put task %d..." % n)
    task.put(n)

# 读取
print("try to get queue...\n")
for i in range(10):
    r = result.get(timeout=10)
    print("get task %d..." % n)
# close
manager.shutdown()
print("master exit")
