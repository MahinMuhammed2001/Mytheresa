# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class MytheresaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

class BreadcrumbItem(scrapy.Item):
    breadcrumbs = scrapy.Field()
