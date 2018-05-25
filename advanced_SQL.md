Advanced SQL
==========
连接条件
------------
>左外连接
右外连接
全连接
内连接
on

视图
------------
定义：
	
	create table v as <query expression>

物化视图(materialized view)：如果用于定义视图的实际关系改变，视图也跟着修改。

单个关系上的约束：
-------------
not null：声明属性不能插入空值
unique:声明属性a1, a2, a3...为候选码

	unique(a1, a2, a3, ...)

check子句:保证属性值满足指定的条件

	check(P)

默认值
-----------
>default

创建索引
-------
	create index ... on 
大对象类型
----------
	clob, blob
用户定义的类型
---------
	create type ... as ... final;
删除或者修改创建的类型
	
	drop type
	alter type

创建域
	
	create domain
>域上可以声明约束
域不是强类型的

check子句应用于域上

	create domain
	 constraint ... check(...)

授权
-----------
授权：

	grant <权限列表>
	on <关系名或视图名>
	to <用户/角色列表>
收回：
	revoke <权限列表>
	on <关系名或视图名>
	to <用户/角色列表>
角色
-------------
for example:

	create role instructor

总结
-----------------
