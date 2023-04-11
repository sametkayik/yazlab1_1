import scrapy
import random
from dbinsert import *
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import time
import scraper_helper as sh
import threading

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    # 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
]


class VatanSpider(scrapy.Spider):
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEEDS': {'vatan.json': {'format': 'json', 'overwrite': True}},
        'LOG_LEVEL': 'INFO',
    }
    name = 'vatan'
    start_urls = ['https://www.vatanbilgisayar.com/notebook']
    base_url = 'https://www.vatanbilgisayar.com/notebook'

    def parse(self, response):

        for products in response.css('div.product-list.product-list--list-page'):
            notebook_url = self.base_url + products.css('a[class="product-list__link"]::attr(href)').extract()[0]
            title = products.css('div.product-list__content > a > div.product-list__product-name > h3 ::text').extract()[0]
            print(str(title))
            yield scrapy.Request(notebook_url, callback=self.parse_vatan,
                                 headers={"User-Agent": user_agent_list[random.randint(0, len(user_agent_list) - 1)]})

        for a in range(1, 20):
            next_page_url = self.base_url + "?stk=false&page=" + str(a)
            yield scrapy.Request(next_page_url, callback=self.parse,
                                 headers={"User-Agent": user_agent_list[random.randint(0, len(user_agent_list) - 1)]})

    def parse_vatan(self, response):
        features = []
        feature = {}

        model_name = response.css('div.product-list__product-code.pull-left.product-id::attr(data-productcode)').get()
        title = response.css('h1.product-list__product-name::text').get().replace('\n', '').upper()
        price = response.css('span.product-list__price::text').get()
        notebook_url = 'https://www.vatanbilgisayar.com/' + response.css(' div.wrapper-breadcrumb > div > div > div > ul > li:nth-child(5) > a::attr(href)').get()
        image_url = response.css(
            '#genel-bakis > div > div.general-features-head.row > div:nth-child(2) > img ::attr(data-src)').get()

        feature['Model Adı'] = model_name
        feature['Marka'] = title.split()[0].upper()
        feature['Başlık'] = title
        feature['Fiyat'] = price.rsplit(',', 1)[0]
        feature['Ürün URL'] = notebook_url
        feature['Görsel URL'] = image_url

        for tables in response.css('div.product-info-content'):
            head = tables.css('div.product-feature > table.product-table > tr > td:nth-child(1) ::text').extract()
            value = tables.css('div.product-feature > table.product-table > tr > td > p:nth-child(1) ::text').extract()

        for i in range(len(head)):
            feature[head[i]] = value[i]

        features.append(feature)
        insertData(features, 'vatan')
        return features


class TeknosaSpider(scrapy.Spider):
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEEDS': {'teknosa.json': {'format': 'json', 'overwrite': True}},
        'LOG_LEVEL': 'INFO',
    }
    name = 'teknosa'
    start_urls = ['https://www.teknosa.com/laptop-notebook-c-116004']
    base_url = 'https://www.teknosa.com'

    def parse(self, response):
        for products in response.css('#product-item'):
            link = products.css('a[class="prd-link"]::attr(href)').extract()[0]
            title = products.css('a[class="prd-link"]::attr(title)').extract()[0]
            print(title)
            notebook_url = self.base_url + link
            yield scrapy.Request(notebook_url, callback=self.parse_teknosa, headers={
                    "User-Agent": user_agent_list[random.randint(0, len(user_agent_list) - 1)]})

        for a in range(1, 50):
            next_page_url = self.base_url + "/laptop-notebook-c-116004?s=%3Arelevance&page=" + str(a)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_teknosa(self, response):
        features = []
        feature = {}

        title = response.css('h2.name::text').get().upper()
        price = response.css('span.prc.prc-last::text').get().split(' ')[0]
        image_url = response.css('div.swiper-slide ::attr(data-zoom)').extract()[0]
        notebook_url = response.css('#js-psh-btn ::attr(data-origin-url)').get()
        #feature['Model Adı'] = model_name
        feature['Marka'] = title.split()[0].upper()
        feature['Başlık'] = title
        feature['Fiyat'] = price.rsplit(',', 1)[0]
        feature['Ürün URL'] = notebook_url
        feature['Görsel URL'] = image_url

        for a in response.css('div.ptf-body'):
            head = a.css('tr > th::text').extract()
            value = a.css('tr > td::text').extract()

        for i in range(len(head)):
            feature[head[i]] = value[i]
        
        features.append(feature)
        insertData(features, 'teknosa')
        return features


class N11Spider(scrapy.Spider):
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEEDS': {'n11.json': {'format': 'json', 'overwrite': True}},
        'LOG_LEVEL': 'INFO',
    }
    name = 'n11'
    start_urls = ['https://m.n11.com/bilgisayar/dizustu-bilgisayar']
    base_next_url = 'https://m.n11.com/bilgisayar/dizustu-bilgisayar'
    base_notebook_url = 'https://www.n11.com/urun'

    def parse(self, response):
        for products in response.css('div.searchResultContainer'):
            title = products.css('div.product-text-area > div.product-item-title.two-lines ::text').extract()[0]
            print(title)
            links = products.css('a::attr(href)').extract()
            for link in links:
                notebook_url = self.base_notebook_url + link
                yield scrapy.Request(notebook_url, callback=self.parse_n11, headers={
                    "User-Agent": user_agent_list[random.randint(0, len(user_agent_list) - 1)]})

        for a in range(1, 50):
            next_page_url = self.base_next_url + "?&pg=" + str(a)
            yield scrapy.Request(next_page_url, callback=self.parse,
                                 headers={"User-Agent": user_agent_list[random.randint(0, len(user_agent_list) - 1)]})

    def parse_n11(self, response):
        features = []
        feature = {}

        #model_name = response.css('div.product-list__product-code.pull-left.product-id::attr(data-productcode)').get()
        title = response.css('div.nameHolder > h1 ::text').get().replace('\n        \n            ', '').replace('\n            ', '').upper()
        marka = title.split()[0]
        price = response.css('#unfSummary > div > div.unf-p-summary-right > div.unf-p-summary-price ::text').get()
        notebook_url = 'https://www.n11.com' + response.css(' div.unf-bottom-detail > div > input.returnUrl ::attr(value)').get()
        image_url = response.css('div.unf-p-thumbs-item ::attr(data-full)').extract()[0]
        #feature['Model Adı'] = model_name
        feature['Marka'] = marka
        feature['Başlık'] = title
        feature['Fiyat'] = price.rsplit(',', 1)[0]
        feature['Ürün URL'] = notebook_url
        feature['Görsel URL'] = image_url

        for tables in response.css('div.unf-prop'):
            head = tables.css('#unf-prop > div > ul > li > p.unf-prop-list-title ::text').extract()
            value = tables.css('#unf-prop > div > ul > li > p.unf-prop-list-prop ::text').extract()
        
        for i in range(len(head)):
            feature[head[i]] = value[i]

        features.append(feature)
        insertData(features, 'n11') 
        return features


def crawlAll():
    start_time = time.time()
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    runner.crawl(VatanSpider)
    runner.crawl(TeknosaSpider)
    runner.crawl(N11Spider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run() # the script will block here until all crawling jobs are finished
    print("\n\n{:.2f} Seconds".format(time.time() - start_time))

crawlAll()

#sh.run_spider(VatanSpider)






