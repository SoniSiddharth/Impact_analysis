import textract
from Preprocess import Preprocess

pr = Preprocess()

text = textract.process("SampleTestCase.docx")
text = text.decode("utf-8")

"""
INDIVIDUAL TESTING
"""
lower_text = pr.text_lowercase(text)
sentence_tokens = pr.sentence_tokenize(lower_text)
for each_sent in sentence_tokens:
    lemmatizzed_sent = pr.lemmatize(each_sent)
    clean_text = pr.remove_numbers(lemmatizzed_sent)
    clean_text = pr.remove_punctuation(clean_text)
    clean_text = pr.remove_Tags(clean_text)
    clean_text = pr.remove_stopwords(clean_text)
    word_tokens = pr.word_tokenize(clean_text)
    # print(word_tokens)


"""
You can call the preprocess function directly
"""
# print()
arr = pr.preprocess(text)
print (arr)
print(len(arr))
