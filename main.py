import time
import os

# fix the path to accomodate a weird structure here
import sys
sys.path.insert(0, "raygun/")

from raygun.spiders import linkfinder
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def main():
    print('Initiating Crawl')
    settings_file_path = 'raygun.settings'  # The path seen from root, ie. from main.py
    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
    process = CrawlerProcess(settings=get_project_settings())

    process.crawl(linkfinder.LinkSpider,
                  start_urls=["https://rwalk.xyz/"],
                  allowed_domains=["rwalk.xyz"])
    process.start()
    return

if __name__ == '__main__':
    start_time = time.time()
    print("Charging Raygun")
    main()
    elapsed_time = time.time() - start_time
    print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

