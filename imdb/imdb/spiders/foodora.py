# -*- coding: utf-8 -*-
import scrapy


class FoodoraSpider(scrapy.Spider):
    name = 'foodora'
    allowed_domains = ['foodora.se']
    start_urls = ['https://www.foodora.se/en/city/stockholm?r=0']

    def parse(self, response):
        products = response.xpath(".//div[@class='search_items']/ul/li")
        for product in products:
            product_name = product.xpath(".//span[@class='name fn']/text()").get()
            product_rating = product.xpath(".//span[@class='rating']/strong/text()").get()
            product_count = product.xpath(".//span[@class='count']/text()").get()
            yield {
                'name': product_name,
                'url': product_rating,
                'price': product_count,
            }

# import scrapy


# class FoodoraSpider(scrapy.Spider):
#     name = 'foodora'
#     allowed_domains = ['foodora.se']
#     start_urls = ['https://www.foodora.se/en/city/stockholm?r=0']

#     def parse(self, response):
#         products = response.xpath("//div[@class='search_items']/ul/li")
#         for product in products:
#             product_name = product.xpath(".//div/a[@class='items_p']/text()").get()
#             product_url = product.xpath(".//div/a[@class='items_p']/@href").get()
#             product_price = product.xpath(".//div/span[@class='items_price']/text()").get()
#             promotion_ends = product.xpath(".//div/div[@class='favit_free']/div/span/text()").get()
#             yield {
#                 'name': product_name,
#                 'url': product_url,
#                 'price': product_price,
#                 'promotion': promotion_ends
#             }