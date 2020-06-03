import os
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import spacy
import textract

nlp = spacy.load("en_core_web_sm")

def creat_emb(path,id,embeddings):

# Text preprocessing
    import re
    text = textract.process(path)
    text = str(text)
    text = text.lower().replace('\n', ' ').replace('\t', ' ').replace('\xa0',' ')
    text = ' '.join(text.split())
    text = text.split("test id : ")
    text = text[1:]
    lst = {}
    for i in text:
        temp = ""
        for j in i:
            if j==" ":
                break
            else:
                temp+=j
        lst[int(temp)] = i

# lst -> a dictionary containing the test ids
# loading the Universal Sentence Encoder (USE) pre-trained model 
    embed = hub.KerasLayer(r'model_use')
# Creating embeddings of each test case seaparately and storing it in the list of lists - embeddings
    print("Creating...")
    for j in lst:
        t=[]
        id.append(int(j))
        doc = nlp(lst[j])
        t.append(str(doc))
        temprary = embed(t)
        embeddings.append(temprary[0])
    # print(id)
    # print(embeddings)
    print("Embeddings Created!!")
    np.savetxt('embeddings.npz',embeddings)                     # an npz file for storing the embeddings
    np.savetxt('id.npz',id)                                     # an npz file to store the corresponding test ids    
    print(" Embeddings Saved")
    # print(embeddings)

if __name__ == "__main__":
    print("Hi")
    creat_emb("SampleTests.docx")
