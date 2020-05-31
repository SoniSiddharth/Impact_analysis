# importing some essential libraries
import os
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from convert_to_csv import To_csv


nlp = spacy.load("en_core_web_sm")
embed = hub.KerasLayer("model_use", trainable= True) # Calling the downloaded USE model

embeddings=np.loadtxt('embeddings.npz') # Loading the stored embeddings of all the test cases present
id=np.loadtxt('id.npz') # Loading a list containing the test ids
l = len(id)

while True:
    print("Hi! Would like to search a keyword+test-id?")
    print("Enter your keyword first: ")
    search_str=input() # Input the keyword

    print("Now enter the id of the test-id: ")
    search_id=float(input()) # Input the number of the test-id

    embeddings2 = embed([search_str]) # Make the embeddings of the search string

    if search_id in id:
        for k in range(0,l):
            if(search_id == id[k]):
                index = k
                break
        embeddings3 = [embeddings[index]] # Embeddings of already existing test case
    else:
        print("You entered an invalid test ID")
        continue


    # Some empty arrays are defined below:
    #1
    output_1=[] # Total output for keyword
    final_output_1=[] # Output for keyword above the threshold

    #2
    output_2=[] # Total output for test-id
    final_output_2=[] # Output for test-id above the threshold

    
    final_intersection_output=[] # Output containing the intersection of the two searches

    threshold = float(input('Set the threshold (type in range of 0-1) :')) # Enter the threshold

    cosine_similarities = pd.Series(cosine_similarity(embeddings2, embeddings).flatten()) # Cosine similarity for the keyword
    #threshold = float(input('Set the threshold (type in range of 0-1) :'))
    for i,j in cosine_similarities.nlargest(l).iteritems():
        output_1.append(int(id[int(i)]))
        if (j>threshold):
            final_output_1.append(int(id[int(i)]))
    print(final_output_1)

    cosine_similarities = pd.Series(cosine_similarity(embeddings3, embeddings).flatten()) # Cosine similarity for the id number
    #threshold = float(input('Set the threshold (type in range of 0-1) :'))
    for i,j in cosine_similarities.nlargest(l).iteritems():
        output_2.append(int(id[int(i)]))
        if (j>threshold):
            final_output_2.append(int(id[int(i)]))
    print(final_output_2)
    #set_intersection_output=set_output_1.intersection(set_output_2)

    #
    for i in range(len(final_output_2)):
        for j in range(len(final_output_1)):
            if(final_output_1[j]==final_output_2[i]):
                final_intersection_output.append(final_output_2[i])


    if final_intersection_output==[]:
        print("No match found")
        print("Do you want to get the test cases that are similar on basis of either the keyword or the test-id?")
        further = input("If you want matching test cases on the basis of test-id, then press 'i' and if you want on basis of keywords, then press 'k': ")
            
        if further=="i" or further=="I": #Press 'i' to search on basis of test-id
            temp = final_output_2
            print(temp) 
            search_string=str(search_id)
            To_csv(temp, search_string, len(temp),threshold)

        elif further=="k" or further=="K": # Press 'k' to search on basis of keyword
            temp=final_output_1
            print(temp)
            search_string=search_str
            To_csv(temp, search_string, len(temp),threshold)
            
    else:
        print(final_intersection_output)
        search_string=search_str + str(search_id)
        To_csv(final_intersection_output, search_string, len(final_intersection_output),threshold) # Storing the results in a .csv/excel file       

    value = input("Want to search next? y/n : ") # To continue your search
        
    if value=="Y" or value=="y":
        continue
    else:
        break
