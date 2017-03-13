
#安装环境说明
#root/OneOaaS#888
#内网:10.154.11.38
#公网:123.206.101.70

#内网: 10.154.9.6
#公网：123.206.105.107
https://paas.bking.com/engine/servers/

#修改主机名
hostname app_basic_online
hostname app_test

#同步数据
rsync -av -e ssh 10.154.31.192:/data/bkv2.0.1.tar.gz ./

#解压蓝鲸的安装包
tar zxf  bkv2.0.1.tar.gz
#拷贝证书
cp ssl_certificates.tar.gz  bkv2.0.1/
#进入安装目录
cd bkv2.0.0/
# 修改本机的配置
vi bk.conf
#启动一些服务，初始化环境
./bk.sh init  paas
# 安装集成平台
./bk.sh install paas

#安装paas agent 初始化
./bk.sh init paasagent
#安装paas agent 安装
./bk.sh install paasagent


curl -s http://123.206.101.70/download/direct/install_agent.sh | bash

#安装虚拟环境
pip install virtualenv
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





