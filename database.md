
数据库
=======

>调度(schedule):表示指令在系统中执行的时间顺序
串行的(serial):属于同一事务的指令在调度中紧挨在一起
并发控制(concurrency-control)
可串可行化调度(conflict serializable):若一个调度与一个串行调度冲突等价，则这个调度是冲突可串行化调度
冲突可串行化:(同上)
冲突等价(conflict equivalent):一个调度经过一系列非冲突指令转换成另一个调度，则他们两冲突等价
级联回滚(cascading rollback)
无级联调度(cascadeless schedule)
脏写(dirty write):如果一个数据项已经被另外一个尚未提交或中止的事务写入，则不允许对该数据项执行写操作

两阶段锁协议：
------------------------------
两阶段锁协议(two-phase locking protocol):级联回滚可能发生，保证可串行性,可能发生死锁
严格两阶段封锁协议(strict two-phase locking protocol):避免级联回滚，要求事务持有的所有排他锁必须在事务提交后方可释放。
强两阶段封锁协议(rigorous two-phase locking protocol):要求事务提交之前不得释放任何锁

锁转换(lock conversion):升级(upgrade)，降级(downgrade)

基于图的协议：
----------------------
>数据库图（database graph）：有向无环图
树形协议（tree protocol）：加锁指令只有lock-X，每个事务对一个数据项最多加一次锁。满足树形协议的调度是冲突可串行化的
树形协议不仅保证冲突可串行性，而且保证不会产生死锁，但不保证可恢复性和无级联回滚


死锁处理：
---------------
>死锁预防（deadlock prevention）
死锁检查（deadlock detection）
死锁恢复（deadlock recovery)

多粒度（granularity）：
---------------------
>多粒度封锁协议（multipe-granularity locking protocol）:保证了可串行性，协议要求加锁按照自顶向下的顺序，而锁的释放则按自底向上的顺序（叶到根）

End
======
