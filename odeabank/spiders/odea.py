import scrapy
from scrapy.loader import ItemLoader
from odeabank.items import Article
from itemloaders.processors import TakeFirst


class OdeaSpider(scrapy.Spider):
    name = 'odea'
    allowed_domains = ['odeabank.com.tr']
    start_urls = ['https://www.odeabank.com.tr/hakkimizda/basin-bulteni']

    def parse(self, response):
        links = response.xpath('//li[@class="row"]//div[@class="col-sm-9"]/a/@href').getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        content = " ".join(response.xpath('//div[@id="contText"]//text()').getall()).strip()
        title = response.xpath('//h1/text()').get().strip()

        item.add_value('title', title)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
