import scrapy


class QuotesSpider(scrapy.Spider):
    name = "plantspy"
    start_urls = ['https://www.southernliving.com/plants/a', 'https://www.southernliving.com/plants/b', 'https://www.southernliving.com/plants/c', 'https://www.southernliving.com/plants/d', 'https://www.southernliving.com/plants/e', 'https://www.southernliving.com/plants/f', 'https://www.southernliving.com/plants/g', 'https://www.southernliving.com/plants/h', 'https://www.southernliving.com/plants/i', 'https://www.southernliving.com/plants/j', 'https://www.southernliving.com/plants/k', 'https://www.southernliving.com/plants/l', 'https://www.southernliving.com/plants/m', 'https://www.southernliving.com/plants/n', 'https://www.southernliving.com/plants/o', 'https://www.southernliving.com/plants/p', 'https://www.southernliving.com/plants/q', 'https://www.southernliving.com/plants/r', 'https://www.southernliving.com/plants/s', 'https://www.southernliving.com/plants/t', 'https://www.southernliving.com/plants/u', 'https://www.southernliving.com/plants/v', 'https://www.southernliving.com/plants/w', 'https://www.southernliving.com/plants/x', 'https://www.southernliving.com/plants/y', 'https://www.southernliving.com/plants/z']


    def parse(self, response):
        temp = []
        # print(response.url)
        links = response.xpath("//li/a/@href").extract()
        # print(links)
        # print(type(response.url))

        for l in links:
            if  l[:len(response.url)] == response.url :
                # print(l)
                temp.append(l)
        print(temp)
