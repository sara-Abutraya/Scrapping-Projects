import scrapy;


class WomSpider(scrapy.Spider):
    name = 'wom'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries= response.xpath('//td/a')
        for country in countries :
            cou_name = country.xpath('.//text()').get()
            cou_link= country.xpath('.//@href').get()
            yield response.follow(url=cou_link,callback=self.parse_country,meta={'cou_name':cou_name})
  
    def parse_country(self,response):
        name=response.request.meta['cou_name']
        rows=response.xpath("//table[@class='table table-striped table-bordered table-hover table-condensed table-list']")
        for row in rows:
            year=row.xpath('.//td[1]/text()').get()
            population=row.xpath('.//td[2]/strong/text()').get()

            yield{
                'country_name':name,
                'year':year,
                'population':population,
            }

    