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
import textract
import nltk
from nltk.tokenize import word_tokenize

def creat_emb(path):
    try:
        embeddings=np.loadtxt('embeddings.npz')                     # loading the already existing embeddings and test ids
        id=np.loadtxt('id.npz')
    except:
        id=[]                                                       # initializing the lists if they do not exist
        embeddings=[]

    # embeddings=np.loadtxt('embeddings.npz')
    # id=np.loadtxt('id.npz')
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
    embed = hub.KerasLayer(r'C:\\Users\\Janvi Thakkar\\Desktop\\projects\\nlp_example')

    # id=[]
    # embeddings=[]
    path = r'C:\\Users\\Janvi Thakkar\\Desktop\\projects\\Capegemini\\separate_test_doc'
    for j in lst:
        # t = []
        # doc = nlp(lst[j])
        # t.append(str(doc))
        # lst[j] = t
        file = str(j)+'.txt'
        dir_list = os.listdir(path)
        if(file not in dir_list):
            with open(os.path.join(path, file), 'w') as fp:
                # id.append(j)
                # t=[]
                doc = nlp(lst[j])
                print(str(doc))
                # t.append(str(doc))
                # temprary = embed(t)
                # embeddings.append(temprary[0])
                fp.write(str(doc))

    for k in dir_list:
        with open(os.path.join(path, k), 'r') as fp:
            (file, ext) = os.path.splitext(k)
            # print(file)
            if(int(file) not in id):
                id.append(int(file))
                t=[]
                lines = fp.read()
                doc = nlp(lines)
                t.append(str(doc))
                temprary = embed(t)
                embeddings.append(temprary[0])
    # print(id)
    # print(embeddings)
    np.savetxt('embeddings.npz',embeddings)
    np.savetxt('id.npz',id)
    print("saved")
    # print(embeddings)

if __name__ == "__main__":
    print("Hi")
    creat_emb("SampleTests.docx")