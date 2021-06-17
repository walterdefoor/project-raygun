# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RaygunItem(scrapy.Item):
    url_from = scrapy.Field()
    url_to = scrapy.Field()
    pass
