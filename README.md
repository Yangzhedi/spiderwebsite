# spiderwebsite

一个基于爬虫的展示网站，前后端暂时还未分离，前端只是用了html来完成模版，后端用django+mongoDB。（以后前端打算用react做到前后分离）

里面的数据主要是来自于：[58同城爬虫](https://github.com/Yangzhedi/pythonSpider/tree/master/bs4/58tongcheng)，并且用mongoDB存储。

下载zip的时候可以先用上面的爬虫爬下数据，然后才能用这个网站的模版来展示。（之后也会丰富模版，可以展示跟多样化的数据）

cd 到项目根目录下， `python manage.py runserver`之后，

输入`http://127.0.0.1:8000/index/`就可以看到展示的爬虫数据了。
