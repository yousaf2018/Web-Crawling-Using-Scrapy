import pandas as pd 
import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
Port_Stemmer = PorterStemmer()
#Looping 57 times because we have 57 stemmed documents
All_Docs = []
for i in range(57):
    #Reading all stemmed data from csv files 
    data = pd.read_csv(f'Doc{i}_Stemmed_by_porter.csv')
    data = data.replace('#',np.nan,regex=True)
    data = data.replace('&',np.nan,regex=True)
    data = data.dropna()
    keys = data.keys()
    #Getting each document all terms for further processing
    All_Docs.append(data[keys[1]])
    print(f'Doc{i} data is obtained')
Inverted_Index = {}
counter = 0
for doc in All_Docs:
    for term in doc:
        temp_list = []
        keys = Inverted_Index.keys()
        if(term in keys):
            temp_list = Inverted_Index[term]
            if(f'Doc_{counter}' in temp_list):
                continue
            else:
                #Updating documneted frequency
                temp_list[0] = temp_list[0] + 1
                temp_list.append(f'Doc_{counter}')
                Inverted_Index[term] = temp_list
        else:
            temp_list.append(1)
            temp_list.append(f'Doc_{counter}')
            Inverted_Index[term] = temp_list
    print(counter)
    counter += 1
Posting_List = []
Doc_Freq = []
Term = []
All_Keys = Inverted_Index.keys()
for each_key in All_Keys:
        #Creating pandas dataframe for holding data in structured way
        Term.append(each_key)
        posting_list = Inverted_Index[each_key]
        doc_freq = posting_list[0]
        Doc_Freq.append(doc_freq)
        Posting_List.append(posting_list[1:])
df = pd.DataFrame(list(zip(Term,Doc_Freq,Posting_List)),
    columns = ['Term','Documented Frequency','Posting List'])        
df.to_csv('Inverted_Indexed_File.csv',mode = 'a')


