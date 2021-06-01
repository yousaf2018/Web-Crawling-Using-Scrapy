import pandas as pd 
import numpy as np
from nltk.tokenize import word_tokenize
#Looping 57 times because we have 57 documents in csv format
for i in range(57):
    #Reading all crawled data from csv files 
    data = pd.read_csv(f'Doc{i}.csv')
    #Cleaning data from \n\t\r by using pandas 
    Paragraph = data['Paragraph'].replace('\n',' ',regex=True)
    Paragraph = Paragraph.replace('\t',' ',regex=True)
    Paragraph = Paragraph.replace('\r',' ',regex=True)

    Heading1 = data['Heading1'].replace('\n',' ',regex=True)
    Heading1 = Heading1.replace('\t',' ',regex=True)
    Heading1 = Heading1.replace('\r',' ',regex=True)

    Heading2 = data['Heading2'].replace('\n',' ',regex=True)
    Heading2 = Heading2.replace('\t',' ',regex=True)
    Heading2 = Heading2.replace('\r',' ',regex=True)

    Heading3 = data['Heading3'].replace('\n',' ',regex=True)
    Heading3 = Heading3.replace('\t',' ',regex=True)
    Heading3 = Heading3.replace('\r',' ',regex=True)

    Heading4 = data['Heading4'].replace('\n',' ',regex=True)
    Heading4 = Heading4.replace('\t',' ',regex=True)
    Heading4 = Heading4.replace('\r',' ',regex=True)

    Heading5 = data['Heading5'].replace('\n',' ',regex=True)
    Heading5 = Heading5.replace('\t',' ',regex=True)
    Heading5 = Heading5.replace('\r',' ',regex=True)
    print(Heading5)

    UnorderList = data['UnorderList'].replace('\n',' ',regex=True)
    UnorderList = UnorderList.replace('\t',' ',regex=True)
    UnorderList = UnorderList.replace('\r',' ',regex=True)

    TableData = data['TableData'].replace('\n',' ',regex=True)
    TableData = TableData.replace('\t',' ',regex=True)
    TableData = TableData.replace('\r',' ',regex=True)

    #Converting links to text for tokenization
    Links = data['Links'].replace('https://namal.edu.pk/',' ',regex=True)
    Links = Links.replace('https:','',regex=True)
    Links = Links.replace('/',' ',regex=True)
    Links = Links.replace('www.',' ',regex=True)
    Links = Links.replace('.com',' ',regex=True)
    Links = Links.replace(np.nan,' ',regex=True)

    #Tokenization using NLTK Library

    Link_tokens = []
    for text in Links:
        tokenize_text = word_tokenize(text)
        Link_tokens.append(tokenize_text)
    Link_tokens = [_ for i in range(len(Link_tokens)) for _ in Link_tokens[i]]

    Paragraph_tokens = []
    for text in Paragraph:
        tokenize_text = word_tokenize(text)
        Paragraph_tokens.append(tokenize_text)
    Paragraph_tokens = [_ for i in range(len(Paragraph_tokens)) for _ in Paragraph_tokens[i]]


    Heading1_tokens = []
    for text in Heading1:
        tokenize_text = word_tokenize(text)
        Heading1_tokens.append(tokenize_text)
    Heading1_tokens = [_ for i in range(len(Heading1_tokens)) for _ in Heading1_tokens[i]]
    print(Heading1_tokens)

    Heading2_tokens = []
    for text in Heading2:
        tokenize_text = word_tokenize(text)
        Heading2_tokens.append(tokenize_text)
    Heading2_tokens = [_ for i in range(len(Heading2_tokens)) for _ in Heading2_tokens[i]]

    Heading3_tokens = []
    for text in Heading3:
        tokenize_text = word_tokenize(text)
        Heading3_tokens.append(tokenize_text)
    Heading3_tokens = [_ for i in range(len(Heading3_tokens)) for _ in Heading3_tokens[i]]

    Heading4_tokens = []
    for text in Heading4:
        tokenize_text = word_tokenize(text)
        Heading4_tokens.append(tokenize_text)
    Heading4_tokens = [_ for i in range(len(Heading4_tokens)) for _ in Heading4_tokens[i]]

    Heading5_tokens = []
    for text in Heading5:
        tokenize_text = word_tokenize(text)
        Heading5_tokens.append(tokenize_text)
    Heading5_tokens = [_ for i in range(len(Heading5_tokens)) for _ in Heading5_tokens[i]]

    UnorderList_tokens = []
    for text in UnorderList:
        tokenize_text = word_tokenize(text)
        UnorderList_tokens.append(tokenize_text)
    UnorderList_tokens = [_ for i in range(len(UnorderList_tokens)) for _ in UnorderList_tokens[i]]

    TableData_tokens = []
    for text in UnorderList:
        tokenize_text = word_tokenize(text)
        TableData_tokens.append(tokenize_text)
    TableData_tokens = [_ for i in range(len(TableData_tokens)) for _ in TableData_tokens[i]]
    print(TableData_tokens)


    #Setting same size of each list for pandas dataframe
    arrays = [Link_tokens,Paragraph_tokens,Heading1_tokens,Heading2_tokens,Heading3_tokens,Heading4_tokens,Heading5_tokens,UnorderList_tokens,TableData_tokens]
    max_length = 0
    for array in arrays:
        max_length = max(max_length, len(array))

    for array in arrays:
        array += [' '] * (max_length - len(array))

    #Creating pandas dataframe for holding data in structured way
    df = pd.DataFrame(list(zip(Link_tokens,Paragraph_tokens,Heading1_tokens,Heading2_tokens,Heading3_tokens,Heading4_tokens,Heading5_tokens,UnorderList_tokens,TableData_tokens)),
        columns = ['Links Tokens','Paragraph Tokens','Heading1 Tokens','Heading2 Tokens','Heading3 Tokens','Heading4 Tokens','Heading5 Tokens','UnorderList Tokens','TableData Tokens'])        
    df.to_csv(f'Doc{i}_Tokens.csv',mode = 'a')
