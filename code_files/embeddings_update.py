import pickle
from pre_process import creat_emb

id=[]
embeddings=[]

with open('mainfile.data','rb') as filehandler:
			main = pickle.load(filehandler)  
for j in range(len(main)):
    creat_emb(main[j],id,embeddings) 

 
