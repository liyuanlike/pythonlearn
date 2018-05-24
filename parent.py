import os


print("Process (%s) start..." % os.getpid())

for i in range(0, 2):
    pid = os.fork()
    print(pid)
    if pid == 0:
        print("i am child Process (%s) and my parent is %s." % (os.getpid(),
              os.getppid()))
    else:
        print("i (%s) just created a child Process(%s)." % (os.getpid(), pid))
