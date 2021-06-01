import scrapy
from urllib.parse import urljoin
import pandas as pd
from itertools import chain
class ProductsSpider(scrapy.Spider):
    #Counter for creating numbering the csv files for each document
    counter = 0
    name = "NamalWebCrawling"
    start_urls = [
        'https://www.namal.edu.pk/',
    ]
    def parse(self, response):
        products = response.css('a::attr(href)').extract()
        yield scrapy.Request('https://www.namal.edu.pk/', callback=self.parse_product)
        for p in products:
            url = urljoin(response.url, p)
            yield scrapy.Request(url, callback=self.parse_product)

    def parse_product(self, response):
        #Getting the current url 
        current_url = []
        current_url.append(response.request.url)
        #Extracting title of website 
        Title = []
        Title.append(response.xpath('//title/text()').get())
        #Extracting images from website
        Images_with_url = response.css('img').xpath('@src').getall()
        #Extracting all links from website
        Links = response.css('a::attr(href)').extract()
        #Extracting all paragraph text in website
        Paragraph = response.xpath('//p/text()').getall()
        #Extracting all div than look for h1
        divs = response.xpath('//div')
        #Extracting all div than look for Unorder list data
        UnorderList = response.xpath('//ul//text()').getall()
        print(UnorderList)
        #Extracting all div than look for Table data
        TableData = response.xpath('//table//text()').getall()
        print(TableData)
        Heading1 = []
        Heading2 = []
        Heading3 = []
        Heading4 = []
        Heading5 = []
        for h1 in divs.xpath('h1/text()'):
            Heading_1 = h1.getall()
            Heading1.append(Heading_1)
        Heading1 = [_ for i in range(len(Heading1)) for _ in Heading1[i]]
        #Extracting all div than look for h5
        for h5 in divs.xpath('h5/text()'):
            Heading_5 = h5.getall()
            Heading5.append(Heading_5)
        Heading5 = [_ for i in range(len(Heading5)) for _ in Heading5[i]]
        #Extracting all div than look for h4
        for h4 in divs.xpath('h4/text()'):
            Heading_4 = h4.getall()
            Heading4.append(Heading_4)
        Heading4 = [_ for i in range(len(Heading4)) for _ in Heading4[i]]

        #Extracting all div than look for h3
        for h3 in divs.xpath('h3/text()'):
            Heading_3 = h3.getall()
            Heading3.append(Heading_3)
        Heading3 = [_ for i in range(len(Heading3)) for _ in Heading3[i]]
        #Extracting all div than look for h2
        for h2 in divs.xpath('h2/text()'):
            Heading_2 = h2.getall()
            Heading2.append(Heading_2)
        Heading2 = [_ for i in range(len(Heading2)) for _ in Heading2[i]]

        #Setting same size of each list for pandas dataframe
        arrays = [current_url,Title,Links,Images_with_url,Paragraph,Heading1,Heading2,Heading3,Heading4,Heading5,UnorderList,TableData]
        max_length = 0
        for array in arrays:
            max_length = max(max_length, len(array))

        for array in arrays:
            array += [' '] * (max_length - len(array))
        #Creating pandas dataframe for holding data in structured way
        df = pd.DataFrame(list(zip(current_url,Title,Links,Images_with_url,Paragraph,Heading1,Heading2,Heading3,Heading4,Heading5,UnorderList,TableData)),
            columns = ['Current_Page_Url','Title','Links','Images_with_url','Paragraph','Heading1','Heading2','Heading3','Heading4','Heading5','UnorderList','TableData'])        
        df.to_csv(f'Doc{self.counter}.csv',mode = 'a')
        print(self.counter)
        self.counter = self.counter + 1