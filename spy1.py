import scrapy
import re
import string

f = open("plantslist.txt", "r")
lines = f.readlines()
doc = []
for l in lines:
    doc.append(l.split('\n')[0])
# print(doc)
class QuotesSpider(scrapy.Spider):
    name = "plantspy2"
    start_urls = doc

    def parse(self, response):
        r = response.xpath('//p/text()').extract()
        # print(r)
        name = response.url.split('/')[-1]
        name = name+".txt"
        for s in r:
            file = open(name, "a")
            file.write(s)
            file.close()
