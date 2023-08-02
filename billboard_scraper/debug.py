import sys

from scrapy import cmdline

cmdline.execute(("scrapy crawl " + sys.argv[1]).split())