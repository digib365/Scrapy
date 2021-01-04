import scrapy

class IMDbSpyder(scrapy.Spider):
    name='imdb_spyder'
    start_urls=['http://www.imdb.com/search/title?country_of_origin=ru&page=1&ref_=adv_prv',]

