import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        products= response.xpath("//div[@id='product-lists']/div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']")
        for p in products:
            yield{
                    'product-url':p.xpath("./div[@class='product-img-outer']/a[1]/@href").get(),
                    'product-image-link':p.xpath("./div[@class='product-img-outer']/a[1]/img[1]/@src").get(),
                    'product-name':p.xpath(".//div[@class='p-title']/a[1]/text()").get() ,
                    'price': p.xpath(".//div[@class='p-price']//span/text()").get()
                    
            }
        next_page=response.xpath("//ul[@class='pagination']/li[position() = last()]/a/@href").get()
        #"//ul[@class='pagination']/li[position() = last()]/a/@href").get()
        yield scrapy.Request(url=next_page,callback=self.parse)    
