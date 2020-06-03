# Impact_analysis
Impact analysis of software change leveraging ML, NLP models from huge number of test cases and requirement documents written in English – Python , Tensorflow / ElMo or equivalent model

Pre-Processing of Data - Data preprocessing is done to make the text in a form that can be used to analyze and predict the task. A task can be extracting text or keywords from the data file or sentiment analysis or checking sentence similarity. A large number of test cases written in english in a .docx file need to be pre-processed before feeding into the model.

#Steps to set up and search using the tool:

a) Downloading the model from the given link:
https://tfhub.dev/google/universal-sentence-encoder-large/5

b) Zip file name 5.tar will be downloaded (Please do not change this name)

c) Clone the Github Repository ( https://github.com/SoniSiddharth/Impact_analysis ) in your system (Download the zip folder and extract    it in a folder).

d) Create a new folder named "model_use" in 'code_files' and extract all the files of the 5.tar in "model_use".

e) Create two folders named: “separate_test_doc” & “main_document” in folder 'code_files'. 

f)To create the first embeddings of the test cases - 

  1) Run the “automate_cre.py” file.
  
  2) Place the document file containing the test cases (SampleTestCases.docx) in the “main_document” folder and terminate the process by selecting Ctrl+C, a file named “mainfile.data” will be created and then run "embeddings_update.py".
  
  3) After getting the message “saved”, check for the 2 “.npz files” (“embeddings.npz” and “id.npz”) in the folder where all the python files have been saved.
  
  4) Search through the document: run the file named ‘search_engine.py’.
  
  5) The console will ask for the user to enter either a keyword or a test-id.
  
  6) Then, it will ask the user to set up a threshold value. Enter the threshold value in the range of 0-1. 
If the given keyword is not found as per the threshold value, the tool will ask if the user still wants to search some similar matching test-cases (y/n). If yes, then type ‘y’ and enter. 

  7) After the search is completed, you will get the excel/.csv file containing the output of the search. The name of the file will be of the format: “Similar_to_SearchedString.csv”.
  
  8) To search for both test-id and keyword, you can run the "keyword+testid.py" file and enter the input values asked in the command line.

g) To search on the GUI, run the "main_GUI.py" file (it will take some time in the first time due to loading the model) then you can enter only keyword or only test-id or both. Provide the threshold value as per the need. You can also set the Default threshold value for all the three cases by editing the "threshold.csv" file.

h) To get a graph plot, run the "graph_plot.py". Enter the test-id for which you want to get the nearest test cases and press ENTER. The threshold value can be changed by editing the "threshold.csv" file. A new graph plot will be shown on the screen along with their test-ids. 

To update/modify the test cases:

If your test cases are in two or more .docx files then there are two steps you can follow:

  1. Delete the existing .docx file from the "main_document" and save it somewhere. Run the "automate_cre.py" and place all the .docx files ONE BY ONE (copying one file and pasting it and repeating the same procedure for all the files) in the "main_document" folder.
  
  2. Merge all the .docx files (along with the existing one) in a single doc file and after deleting the existing doc file from "main_document", run the "automate_cre.py" and place the Merged doc file in the "main_document" folder.

Now after doing any one of the above steps, terminate the "automate_cre.py" and run the "embeddings_update.py" file. You will get a message of embeddings getting saved.
