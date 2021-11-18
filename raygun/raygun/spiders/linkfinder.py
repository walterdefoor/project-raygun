import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider

class RaygunItem(scrapy.Item):
    url_from = scrapy.Field()
    url_to = scrapy.Field()
    link_text = scrapy.Field()
    pass


class LinkSpider(CrawlSpider):
    name = "links"
    start_urls = ['http://books.toscrape.com/']
    allowed_domains = ['books.toscrape.com']
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]
    seen_urls = []
    f = open("seen_urls.txt", 'w')

    def parse_items(self, response):
        items = []
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)

        for link in links:
            if link.url not in self.seen_urls:
                self.seen_urls.append(link.url)
                is_allowed = False
                for allowed_domain in self.allowed_domains:
                    if allowed_domain in link.url:
                        is_allowed = True
                if is_allowed:
                    item = RaygunItem()
                    item['url_from'] = response.url
                    item['url_to'] = link.url
                    item['link_text'] = link.text
                    items.append(item)
                self.f.write(str(link.url) + "\n")
        return items
