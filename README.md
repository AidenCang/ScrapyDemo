
###使用系统默认的类来构造类扩展
scrapy genspider -t crawl tencentcrawl  tencent.com


scrapy输出格式:




#新浪微博抓取
https://www.cnblogs.com/xinyangsdut/p/7631163.html

1.创建工程

    scrapy startproject sinaNews  #scrapy/templates/project 使用的创建模板

切换到工程里面创建一个爬虫类

    cd sinaNews
    scrapy genspider example example.com


文件里面设置运行环境编码:

    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    
#数据保存到Mogodb
https://www.cnblogs.com/xinyangsdut/p/7688130.html

##爬虫模拟网站登录:

