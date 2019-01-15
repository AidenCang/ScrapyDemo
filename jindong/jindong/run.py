from scrapy import cmdline

# 方法 1
cmdline.execute('scrapy crawl jd'.split())

# # 方法 2
# sys.argv = ['scrapy', 'crawl', 'down_info_spider']
# cmdline.execute()
#
# # 方法 3, 创建子进程执行外部程序。方法仅仅返回外部程序的执行结果。0表示执行成功。
# os.system('scrapy crawl down_info_spider')
#
# # 方法 4
# import subprocess
# subprocess.Popen('scrapy crawl down_info_spider')
