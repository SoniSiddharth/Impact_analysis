import os
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
from sklearn import preprocessing
import spacy
from spacy.lang.en import English
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
from sklearn.metrics.pairwise import cosine_similarity
from convert_to_csv import To_csv

embed = hub.KerasLayer(r'C:\\Users\\Janvi Thakkar\\Desktop\\projects\\nlp_example')

embeddings=np.loadtxt('embeddings.npz')
id=np.loadtxt('id.npz')
l = len(id)

while True:
    print("Enter some keywords or a test ID number")
    search_string = input()

    try:
        no = float(search_string)
        if no in id:
            for k in range(0,l):
                if(no == id[k]):
                    index = k
                    break
            embeddings2 = [embeddings[index]]                     # embeddings of already existing test case
        else:
            print("You entered an invalid test ID")
            continue
    except:
	    embeddings2 = embed([search_string])                      # making the embeddings of the input string

    output = []                                                   # Storing all the test ids in decreasing order of similarity
    final_output = []                                             # Storing the test ids which are sufficiently similar


# comparing the test cases by using the embeddings and cosine similarity scores
    cosine_similarities = pd.Series(cosine_similarity(embeddings2, embeddings).flatten())
    for i,j in cosine_similarities.nlargest(l).iteritems():
        output.append(int(id[int(i)]))
        if (j>0.4):
            final_output.append(int(id[int(i)]))


# cases when there are no matching test cases and whether user wants to search more or not
    if final_output==[]:
        print("No match found")
        further = input("Do you want to get the test cases that are quite similar? y/n: ")
        
        if further=="y" or further=="Y":
            print("Enter the number of results expected")
            results_returned = int(input())
            
            if results_returned >= l:
                results_returned = l
            temp = output[:results_returned]
            print(temp)
            To_csv(temp, search_string, len(temp))
    else:
        print(final_output)
        To_csv(final_output, search_string, len(final_output))           # storing the results in a .csv/excel file       

    value = input("Want to search next? y/n : ")                            # to continue your search
    
    if value=="Y" or value=="y":
        continue
    else:
        break










# while True:

#     search_string = input('Type your search:')

#     results_returned = "6" 
#     try:
#         no = float(search_string)
#         if no in id:
#             print('yes')
#             index=0
#             for k in range(0,len(id)):
#                 if(no == id[k]):
#                     index = k
#                     break
#             embeddings2 = [embeddings[index]]
#         else:
#             print("You entered an invalid test ID")
#     except:
# 	    embeddings2 = embed([search_string])


#     cosine_similarities = pd.Series(cosine_similarity(embeddings2, embeddings).flatten())
#     for i,j in cosine_similarities.nlargest(int(results_returned)).iteritems():
#         print(id[int(i)])
#     value = input("Want to search next? \n Y/N : ")
#     if(value == 'N'):
#         break 
    
