
"""database""""


调度(schedule):表示指令在系统中执行的时间顺序
串行的(serial):属于同一事务的指令在调度中紧挨在一起
并发控制(concurrency-control)
可串可行化调度(conflict serializable):若一个调度与一个串行调度冲突等价，则这个调度是冲突可串行化调度
冲突可串行化:(同上)
冲突等价(conflict equivalent):一个调度经过一系列非冲突指令转换成另一个调度，则他们两冲突等价
级联回滚(cascading rollback)
无级联调度(cascadeless schedule)



""""End"""""""
