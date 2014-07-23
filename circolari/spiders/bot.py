# -*- coding: utf-8 -*-
import scrapy
import urllib
from circolari.items import CircolariItem


class BotSpider(scrapy.Spider):
    name = "bot"
    allowed_domains = ["avolta.pg.it"]
    start_urls = (
        'http://www.avolta.pg.it/circolari/?titolo=&select=5&numero=25&DataIn=2%2F9%2F2013&DataOut=16%2F6%2F2014',
    )

    def parse(self, response):
        link ='http://www.avolta.pg.it/circolari/'
        table = response.css(".tabelle.pippo")
        nodes = table.xpath(".//a/@href").extract()
        circular = CircolariItem()
        for node in nodes:
            quoted = urllib.quote(node)
            circular['pdflink'] = "%s%s" % (link, quoted)
            yield circular
