# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags

def remove_quotations(value):
    return value.replace(u"\u201d", '').replace(u"\u201c", '')


class QuoteItem(scrapy.Item):
    VIN= scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quotations),
        output_processor= TakeFirst()
    )
    MARCA= scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quotations),
        output_processor= TakeFirst()
    )
    ORIGEN= scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quotations),
        output_processor= TakeFirst()
    )
    MODELO= scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quotations),
        output_processor= TakeFirst()
    )
    MOTOR= scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quotations),
        output_processor= TakeFirst()
    )
    CILINDROS= scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quotations),
        output_processor= TakeFirst()
    )
    COMBUSTIBLE= scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quotations),
        output_processor= TakeFirst()
    )
    TRACCION= scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quotations),
        output_processor= TakeFirst()
    )
    CARROCERIA= scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quotations),
        output_processor= TakeFirst()
    )
    FABRICACION= scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quotations),
        output_processor= TakeFirst()
    )
    TRANSMISION= scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quotations),
        output_processor= TakeFirst()
    )