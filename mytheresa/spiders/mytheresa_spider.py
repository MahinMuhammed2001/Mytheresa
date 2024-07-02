import scrapy

class MytheresaSpider(scrapy.Spider):
    name = 'mytheresa_spider'
    start_urls = ['https://www.mytheresa.com/int/en/men/shoes?rdr=mag']  

    def parse(self, response):
      
        product_links = response.xpath('//a[contains(@class, "item__link")]/@href').getall()

        for product_link in product_links:
            yield response.follow(product_link, callback=self.parse_product)

        
        next_page = response.xpath('//a[contains(@class, "pagination_item_text--active")]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response):
        product_name = response.xpath('//h1[@class="product_areabranding_name"]/text()').extract()
        product_brand = response.xpath('//a[@class="product_areabrandingdesigner_link"]/text()').extract()
        product_breadcrumbs = response.xpath('//ol[@class="breadcrumb"]//li//text()').extract()
        product_listing_price = response.xpath('//span[contains(@class, "pricing_pricesvalue--original")]/span[@class="pricingprices_price"]/text()').extract()
        product_offer_price = response.xpath('//span[contains(@class, "pricing_pricesvalue--discount")]/span[@class="pricingprices_price"]/text()').extract()
        product_discount = response.xpath('//span[@class="pricing_info_percentage"]/text()').extract()
        product_image_url = response.xpath('//img[@class="zoompro"]/@src').extract()
        product_id = response.xpath('//li[contains(text(), "Item No.")]/text()').extract()
        product_size = response.xpath('//div[@class="dropdown_select_content"]//span/text()').extract()
        product_description = response.xpath('//div[@class="productinfo_block"]//ul[@class="accordionbody_content"]//li/text()').extract()

        yield {
            'name': product_name,
            'brand': product_brand,
            'breadcrumbs': product_breadcrumbs,
            'listing_price': product_listing_price,
            'offer_price': product_offer_price,
            'discount': product_discount,
            'image': product_image_url,
            'id': product_id,
            'size': product_size,
            'description': product_description,
            'url': response.url,
        }
