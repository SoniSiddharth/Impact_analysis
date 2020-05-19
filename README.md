# Impact_analysis
Impact analysis of software change leveraging ML, NLP models from huge number of test cases and requirement documents written in English – Python , Tensorflow / ElMo or equivalent model

Pre-Processing of Data - Data preprocessing is done to make the text in a form that can be used to analyze and predict the task. A task can be extracting text or keywords from the data file or sentiment analysis or checking sentence similarity. A large number of test cases written in english in a .docx file need to be pre-processed before feeding into the model.

#Steps to set up and search using the tool:

a) Downloading the model from the given link:
https://tfhub.dev/google/universal-sentence-encoder-large/5
b) Zip file name 5.tar will be downloaded (Please do not change this name)
c) Extract all files in the project folder.
d) Create two folders named: “separate_test_doc” & “main_document”.
e) Download 8 python code files from the Github Repository ( https://github.com/SoniSiddharth/Impact_analysis ), the files are as follows: ( “automate_cre.py”, “automate_up.py”, “convert_to_csv.py”, “embeddings_update.py”, “graph_plot.py”, “pre_process.py”, “search_engine.py”, “update_emb.py” )
f) Make the changes in each file as mentioned below in step "8)".

g)To create the first embeddings of the test cases - 

  1) Run the “automate_cre.py” file after making the essential changes in each file as mentioned below.
  
  2) Place the document file containing the test cases (SampleTestCases.docx) in the “main_document” folder and terminate the process by selecting Ctrl+C, a file named “mainfile.data” will be created and then run embeddings_update.py.
  
  3) After getting the message “saved”, check for the 2 “.npz files” (“embeddings.npz” and “id.npz”) in the folder where all the python files have been saved.
  
  4) Search through the document: run the file named ‘search_engine.py’.
  
  5) The console will ask for the user to enter either a keyword or a test-id.
  
  6) Then, it will ask the user to set up a threshold value. Enter the threshold value in the range of 0-1. 
If the given keyword is not found as per the threshold value, the tool will ask if the user still wants to search some similar matching test-cases (y/n). If yes, then type ‘y’ and enter. 

  7) After the search is completed, you will get the excel/.csv file containing the output of the search. The name of the file will be of the format: “Similar_to_SearchedString.csv”.

  8) Make the following changes in the files mentioned below:

a) Changes required in pre_process.py: 
  1) Change path accordingly in the pre_process.py for variable embed (line 39)
  2) Change path for the “separate_test_doc”(line 42)

b) Changes required in automate_cre.py:
  1) Change the src_path (line 33) to the path of your main_document directory

c) Changes required in automate_up.py
  1) Change the src_path (line 33) to the path of your separate_test_doc directory

d) Changes required in update_emb.py
  1) Change the path of embed in (line 11) similar to pre_process.py.
  
e) Changes required in search_engine.py
  1) Specify the address of the directory where the USE model has been extracted (line 12) 

The rest of the files do not require any change.

To update/modify the test cases:

Run the “automate_up.py” file and do the required changes in the test cases (.txt files) from the folder “separate_test_doc” and then terminate the process running in “automate_up.py” by pressing Ctrl+C in the terminal window. A file named listfile.data will be created, you can go and check the time of the last modifications. And then run “embeddings_update.py”.
