# django-mysite
django 日常笔记，练习
# django-admin startproject py_mysit 创建py_site 项目
# python manage.py runserver 运行项目
# pip install mysqlclient==1.3.10 按照mysqldb，支持py3.3+
 

## python manage.py startapp polls 创建一个polls 应用
项目中可以包含多个应用

##生成数据sql 步骤

> python manage.py makemigrations polls #用来检测数据库变更和生成数据库迁移文件
> python manage.py sqlmigrate polls 0001 # 可以查看把数据库迁移文件转换成数据库语言
> python manage.py migrate polls #创建表结构 自动执行数据库迁移并同步管理你的数据库结构的命令migrate


> 生成的sql 可以放到数据库执行

> python manage.py createsuperuser
admin /django123

> python manage.py shell 