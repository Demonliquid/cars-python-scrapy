import scrapy
import pandas as pd

from scrapy.loader import ItemLoader
from BMW.items import QuoteItem

chasis = pd.read_csv(r"C:\Users\Martin\Desktop\bot\lista.csv")
lista = []
for vin in chasis["CHASIS"]:
    lista.append(f"https://www.bmwsections.com/vin-check/result/?vin={vin}")




class BMWSpider(scrapy.Spider):
    #Identity
    name="BMW"


    #Request

    start_urls= lista

    #Response
    def parse(self, response):
        for quote in response.xpath('//*[@id="vcresbox"]'):
            loader= ItemLoader(item=QuoteItem(), selector=quote, response=response)
            loader.add_xpath('VIN', '//*[@id="vcresbox"]/p[1]/text()')
            loader.add_xpath('MARCA', '//*[@id="vcresbox"]/p[6]/text()')
            loader.add_xpath('ORIGEN', '//*[@id="vcresbox"]/p[10]/text()')
            loader.add_xpath('TIPO_VEHICULO', '//*[@id="vcresbox"]/p[12]/text()')
            loader.add_xpath('MODELO', '//*[@id="vcresbox"]/p[13]/text()')
            loader.add_xpath('VERSION', '//*[@id="vcresbox"]/p[14]/text()')
            loader.add_xpath('MOTOR', '//*[@id="vcresbox"]/p[19]/text()')
            loader.add_xpath('CILINDRADA', '//*[@id="vcresbox"]/p[20]/text()')
            loader.add_xpath('CILINDROS', '//*[@id="vcresbox"]/p[24]/text()')
            loader.add_xpath('COMBUSTIBLE', '//*[@id="vcresbox"]/p[25]/text()')
            loader.add_xpath('TRACCION', '//*[@id="vcresbox"]/p[26]/text()')
            loader.add_xpath('CARROCERIA', '//*[@id="vcresbox"]/p[27]/text()')
            loader.add_xpath('FABRICACION', '//*[@id="vcresbox"]/p[33]/text()')
            yield loader.load_item()
