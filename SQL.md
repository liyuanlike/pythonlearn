SQL
=======


基本类型：
-----
>char(N)
varchar(N)
int
smallint
numeric(p,d)
float(N)

----
基本模式定义


	creat table department
		(dept_name varchar(20),
		building varchar(15),
		budget numeric(12, 2),
		primary key (dept_name))
		foreign key (budget)
		references setion);
>####creat table 要用分号结束
####null not 表示不允许为空值

自然连接
---
自然连接运算作用了两个关系，并产生一个关系作为结果（只考虑在共同属性上取值相同的元组）

	
	join...using(),只考虑指定的属性名
更名运算
----
>如果我们在select子句中使用算术表达式，那么结果属性就没有名字了
	
	old-name as new-name
字符串运算
---
>百分号（%）：匹配任意子串
下划线 :匹配任意一个字符
like:表达比较运算符
escape '\':转义

集合运算
--------
>union
intersect
except

空值
-----

分组聚集
---
>当SQL查询使用分组时，一个很重要的事情是需要保证出现在select语句中但没有被聚集的属性只能是出现在group by子句的属性
任何出现在having子句中，但没有被聚集的属性必须出现在group by中

对空值和布尔值的聚集
---------------------
除了count(*)外所有的聚集函数都忽略输入集合中的空值。*

集合的成员运算
----------------
	in, not in, some, not some, all, not all, exists, not exists

重复元素存在性测试
----------------
unique:没有重复元组返回true

数据库修改
---------
删除

	delete from r
	where p
插入
	
	insert into r
		value(....)
更新
	
	update r
	set ...
	where ....


总结
------

