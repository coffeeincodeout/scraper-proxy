import scrapy

class FreeSpider(scrapy.Spider):
    name = 'free'
    start_urls = [
        'https://free-proxy-list.net/'
    ]

    def parse(self, response):

        ip_list = response.css('tr > td:nth-child(1)::text').extract()
        port_list = response.css('tr > td:nth-child(2)::text').extract()
        for ip, port in zip(ip_list, port_list):
            proxy = ip + ':' + port
            yield {
                'ip': proxy
            }