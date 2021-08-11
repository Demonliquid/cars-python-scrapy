import scrapy
import pandas as pd

from scrapy.loader import ItemLoader
from vindecoder.items import QuoteItem

chasis = pd.read_csv(r"C:\Users\Martin\Desktop\bot\lista.csv")
lista = []
for vin in chasis["CHASIS"]:
    lista.append(f"https://en.vindecoder.pl/{vin}")




class VINDECODERSpider(scrapy.Spider):
    #Identity
    name="vindecoder"


    #Request

    start_urls= lista

    #Response
    def parse(self, response):
        for quote in response.xpath('//*[@id="vcresbox"]'):
            loader= ItemLoader(item=QuoteItem(), selector=quote, response=response)
            loader.add_xpath('VIN', '/html/body/div[4]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td')
            loader.add_xpath('MARCA', '/html/body/div[4]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td')
            loader.add_xpath('ORIGEN', '/html/body/div[4]/div/div[2]/div[3]/div/div/table/tbody/tr[8]/td')
            loader.add_xpath('MODELO', '/html/body/div[4]/div/div[2]/div[3]/div/div/table/tbody/tr[2]/td')
            loader.add_xpath('MOTOR', '/html/body/div[4]/div/div[2]/div[3]/div/div/table/tbody/tr[5]/td')
            loader.add_xpath('CILINDROS', '/html/body/div[4]/div/div[2]/div[5]/div/div/table/tbody/tr[6]/td')
            loader.add_xpath('COMBUSTIBLE', '/html/body/div[4]/div/div[2]/div[5]/div/div/table/tbody/tr[11]/td')
            loader.add_xpath('TRACCION', '/html/body/div[4]/div/div[2]/div[5]/div/div/table/tbody/tr[12]/td')
            loader.add_xpath('CARROCERIA', '/html/body/div[4]/div/div[2]/div[5]/div/div/table/tbody/tr[1]/td')
            loader.add_xpath('FABRICACION', '/html/body/div[4]/div/div[2]/div[3]/div/div/table/tbody/tr[3]/td')
            loader.add_xpath('TRANSMISION', '/html/body/div[4]/div/div[2]/div[3]/div/div/table/tbody/tr[7]/td')
            yield loader.load_item()
