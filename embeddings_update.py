import pickle
from update_emb import update_emb,embed
from pre_process import creat_emb

with open('mainfile.data','rb') as filehandler:
			main = pickle.load(filehandler)  
for j in range(len(main)):
    creat_emb(main[j]) 

with open('listfile.data','rb') as filehandle:
			paths = pickle.load(filehandle)
for i in range(len(paths)):
    update_emb(paths[i])

 
