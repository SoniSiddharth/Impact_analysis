import os
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from convert_to_csv import To_csv

import tkinter as tk
from tkinter import *
import requests

nlp = spacy.load("en_core_web_sm")
embed = hub.KerasLayer("model_use", trainable= True)

embeddings=np.loadtxt('embeddings.npz') # Loading the stored embeddings of all the test cases present
id=np.loadtxt('id.npz') # Loading a list containing the test ids
l = len(id)

def keytest(keyword,testid,thres):
     # Calling the downloaded USE model
    #print("Hi! Would like to search a keyword+test-id?")
    #print("Enter your keyword first: ")
    default_t = pd.read_csv('threshold.csv')
    X = default_t.iloc[:,:].values
    threshold_key = X[0][0]
    threshold_test = X[0][1]
    threshold_both = X[0][2]

    search_str=keyword # Input the keyword
    flag_word = 0
    flag_id = 0
    #print("Now enter the id of the test-id: ")
    try:
        search_id=float(testid) # Input the number of the test-id
    except:
        flag_id = 1

    if search_str=="":
        flag_word = 1
    
    output_1=[] # Total output for keyword
    final_output_1=[] # Output for keyword above the threshold

    output_2=[] # Total output for test-id
    final_output_2=[] # Output for test-id above the threshold
    # Some empty arrays are defined below:

    if (flag_id==0 and flag_word==0):

        embeddings2 = embed([search_str]) # Make the embeddings of the search string
        
        try:
            if search_id in id:
                for k in range(0,l):
                    if(search_id == id[k]):
                        index = k
                        break
            embeddings3 = [embeddings[index]] # Embeddings of already existing test case
        except:
            print("No such test-id available")
            return

        final_intersection_output=[] # Output containing the intersection of the two searches

        #threshold = float(input('Set the threshold (type in range of 0-1) :')) # Enter the threshold
        if thres=="":
            threshold = threshold_both                   # Default threshold
        else:
            threshold = float(thres)
        
        cosine_similarities = pd.Series(cosine_similarity(embeddings2, embeddings).flatten()) # Cosine similarity for the keyword
        #threshold = float(input('Set the threshold (type in range of 0-1) :'))
        for i,j in cosine_similarities.nlargest(l).iteritems():
            output_1.append(int(id[int(i)]))
            if (j>threshold):
                final_output_1.append(int(id[int(i)]))
        # print(output_1)
        # print(final_output_1)

        cosine_similarities = pd.Series(cosine_similarity(embeddings3, embeddings).flatten()) # Cosine similarity for the id number
        #threshold = float(input('Set the threshold (type in range of 0-1) :'))
        for i,j in cosine_similarities.nlargest(l).iteritems():
            output_2.append(int(id[int(i)]))
            if (j>threshold):
                final_output_2.append(int(id[int(i)]))
        # print(output_2)
        # print(final_output_2)

        for i in range(len(final_output_2)):
            for j in range(len(final_output_1)):
                if(final_output_1[j]==final_output_2[i]):
                    final_intersection_output.append(final_output_2[i])

        if final_intersection_output==[]:
            print("No match found above " + str(threshold) + " threshold. Try some lower value of threshold. However, here are some results in decreasing order of similarity which are quite similar to test-ids only:")
            print(final_output_2)
            search_string=search_str + str(search_id)
            To_csv(final_output_2, search_string, len(final_output_2),threshold) # Storing the results in a .csv/excel file
        else:    
            print(final_intersection_output)
            search_string=search_str + str(search_id)
            To_csv(final_intersection_output, search_string, len(final_intersection_output),threshold) # Storing the results in a .csv/excel file

    elif flag_word==0 and flag_id==1:
        
        embeddings2 = embed([search_str]) # Make the embeddings of the search string
        if thres=="":
            threshold = threshold_key                # Default threshold
        else:
            threshold = float(thres)
        
        cosine_similarities = pd.Series(cosine_similarity(embeddings2, embeddings).flatten()) # Cosine similarity for the keyword
        #threshold = float(input('Set the threshold (type in range of 0-1) :'))
        for i,j in cosine_similarities.nlargest(l).iteritems():
            output_1.append(int(id[int(i)]))
            print(j)
            if (j>threshold):
                final_output_1.append(int(id[int(i)]))
        # print(output_1)
        # print(final_output_1)

        if final_output_1==[]:
            print("No match found above " + str(threshold) + " threshold. Try some lower value of threshold. However, here are some results in decreasing order of similarity which are quite similar:")
            print(output_1)
            search_string=search_str
            To_csv(output_1, search_string, len(output_1),threshold) # Storing the results in a .csv/excel file
        else:
            search_string=search_str
            To_csv(final_output_1, search_string, len(final_output_1),threshold) # Storing the results in a .csv/excel file

    elif flag_word==1 and flag_id==0:
        try:
            if search_id in id:
                for k in range(0,l):
                    if(search_id == id[k]):
                        index = k
                        break
            embeddings3 = [embeddings[index]] # Embeddings of already existing test case
        except:
            print("No such test-id available")
            return
        
        if thres=="":
            threshold = threshold_test          # Default threshold
        else:
            threshold = float(thres)
        cosine_similarities = pd.Series(cosine_similarity(embeddings3, embeddings).flatten()) # Cosine similarity for the id number
        #threshold = float(input('Set the threshold (type in range of 0-1) :'))
        for i,j in cosine_similarities.nlargest(l).iteritems():
            output_2.append(int(id[int(i)]))
            if (j>threshold):
                final_output_2.append(int(id[int(i)]))
        # print(output_2)
        # print(final_output_2)
        if final_output_2==[]:
            print("No match found above " + str(threshold) + " threshold. Try some lower value of threshold. However, here are some results in decreasing order of similarity which are quite similar:")
            print(output_2)
            search_string = str(search_id)
            To_csv(output_2, search_string, len(output_2),threshold) # Storing the results in a .csv/excel file
        else:
            search_string = str(search_id)
            To_csv(final_output_2, search_string, len(final_output_2),threshold) # Storing the results in a .csv/excel file
    else:
        return

root=Tk()
root.geometry('500x500')
root.title("Search Engine")

#Keyword
label_1=Label(root, text="Enter Keyword", width= 25, font=("bold", 12), padx = 7)
label_1.place(x=30, y=100)

entry_1=tk.Entry(root, font=9)
entry_1.place(x=250,y=100)

# TestId 
label_2=Label(root, text="Enter Test-ID", width= 25, font=("bold", 12))
label_2.place(x=30, y=160)

entry_2=tk.Entry(root, font = 9)
entry_2.place(x=250,y=160)

# Threshold
label_3=Label(root, text="Enter Threshold", width= 25, font=("bold", 12), padx = 10)
label_3.place(x=30, y=220)

entry_3=tk.Entry(root, font = 9)
entry_3.place(x=250,y=220)

# Button
button1 = Button(root, text="Search", font=("arial", 15, "bold"), command = lambda: keytest(entry_1.get(),entry_2.get(),entry_3.get()))
button1.place(x = 200, y = 350)

root.mainloop()
