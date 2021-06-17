import time
from raygun.raygun.spiders import linkfinder
from scrapy.crawler import CrawlerProcess


def main():
    print('Initiating Crawl')
    process = CrawlerProcess(settings={
        "FEEDS": {"links.jsonl": {"format": "jsonlines"}},
        "AUTOTHROTTLE_ENABLED": False,
    })

    process.crawl(linkfinder.LinkSpider,
                  start_urls=["https://quotes.toscrape.com/"],
                  allowed_domains=["quotes.toscrape.com"])
    process.start()
    return


if __name__ == '__main__':
    start_time = time.time()
    print("Charging Raygun")
    main()
    elapsed_time = time.time() - start_time
    print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

