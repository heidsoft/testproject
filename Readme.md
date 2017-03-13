#虚拟开发环境的python 环境为2.7
virtualenv --python=/usr/bin/python dev-djdemo

#创建django 工程
/Users/heidsoft/work/dev-djdemo/bin/django-admin startproject testproject
#创建django APP
python manage.py startapp test1

#启动运行app
python manage.py runserver  127.0.0.1:8000

#生成模型到sql 的翻译文件
python manage.py makemigrations test1
#执行模型生成sql的翻译文件
python manage.py migrate test1

#创建用户
python manage.py createsuperuser
#用户名heidsoft
#密码:heidsoft
#进入管理控制台:http://127.0.0.1:8000/admin/

#对象操作
```
保存对象
>>> from test1.models import Author
>>> from test1.models import Book
>>> author1 = Author(name='heidsoft')
>>> author1.save()

查询
>>> from test1.models import Author
>>> Author.objects.create(name="zhangsan")
<Author: zhangsan>
>>> Author.objects.all()
[<Author: heidsoft>, <Author: zhangsan>]

过滤
>>> Author.objects.filter(name__contains="h")
[<Author: heidsoft>, <Author: zhangsan>]
>>> Author.objects.filter(name__contains="heidsoft")
[<Author: heidsoft>]

>>> Author.objects.get(name="liubin")
<Author: liubin>

更新
>>> Author.objects.filter(name="heidsoft").update(name="liubin")
1

删除
>>> Author.objects.get(name="liubin").delete()
>>> Author.objects.all()
[<Author: zhangsan>]

管理查询与创建
>>> zhangsan = Author.objects.get(name="zhangsan")
>>> Book.objects.create(name="java",author=zhangsan)
>>> zhangsan.book_set.create(name="C++")
>>> Author.objects.all()

```





