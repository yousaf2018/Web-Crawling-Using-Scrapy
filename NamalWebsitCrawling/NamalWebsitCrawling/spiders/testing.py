import pandas as pd 
header_list = ['Title','Links','Images_with_url','Paragraph','Heading1','Heading2','Heading3','Heading4','Heading5']
df = pd.read_csv("NamalWebCrawling_by_Scrapy.csv", names=header_list)
df.to_csv("NamalWebCrawling_by_Scrapy.csv")