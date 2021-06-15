import pandas as pd 
import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
Port_Stemmer = PorterStemmer()
#Looping 57 times because we have 57 tokenized documents
for i in range(57):
    Stemming_List_For_Each_Document = []
    #Reading all tokenized data from csv files 
    data = pd.read_csv(f'Doc{i}_Tokens.csv')
    #Loading data into pandas dataframes    
    Links = data['Links Tokens']
    Paragraph = data['Paragraph Tokens']
    Heading1 = data['Heading1 Tokens']
    Heading2 = data['Heading2 Tokens']
    Heading3 = data['Heading3 Tokens']
    Heading4 = data['Heading4 Tokens']
    Heading5 = data['Heading5 Tokens']
    UnorderList = data['UnorderList Tokens']
    TableData = data['TableData Tokens']
    print(TableData)
    #Stemming by Porter Stemmer using NLTK Library

    for text in Links:
        Stemmed_Word = Port_Stemmer.stem(text)
        Stemming_List_For_Each_Document.append(Stemmed_Word)

    for text in Paragraph:
        Stemmed_Word = Port_Stemmer.stem(text)
        Stemming_List_For_Each_Document.append(Stemmed_Word)


    for text in Heading1:
        Stemmed_Word = Port_Stemmer.stem(text)
        Stemming_List_For_Each_Document.append(Stemmed_Word)

    for text in Heading2:
        Stemmed_Word = Port_Stemmer.stem(text)
        Stemming_List_For_Each_Document.append(Stemmed_Word)

    for text in Heading3:
        Stemmed_Word = Port_Stemmer.stem(text)
        Stemming_List_For_Each_Document.append(Stemmed_Word)

    for text in Heading4:
        Stemmed_Word = Port_Stemmer.stem(text)
        Stemming_List_For_Each_Document.append(Stemmed_Word)

    for text in Heading5:
        Stemmed_Word = Port_Stemmer.stem(text)
        Stemming_List_For_Each_Document.append(Stemmed_Word)

    for text in UnorderList:
        Stemmed_Word = Port_Stemmer.stem(text)
        Stemming_List_For_Each_Document.append(Stemmed_Word)

    for text in UnorderList:
        Stemmed_Word = Port_Stemmer.stem(text)
        Stemming_List_For_Each_Document.append(Stemmed_Word)
    #Creating pandas dataframe for holding data in structured way
    df = pd.DataFrame(Stemming_List_For_Each_Document,
        columns = ['Stemmed words'])
    df = df['Stemmed words'].replace(' ',np.nan,regex=True)
    df = df.dropna()
    print(df)
    df.to_csv(f'Doc{i}_Stemmed_by_porter.csv',mode = 'a')