import nltk 
import string 
import re
import inflect
from autocorrect import spell
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

p = inflect.engine()
snowball_stemmer = SnowballStemmer('english')
wordnet_lemmatizer = WordNetLemmatizer()

class Preprocess:
    def __init__(self):
        pass

    def text_lowercase(self,text): 
        return text.lower()

    def remove_numbers(self,text): 
        result = re.sub(r'\d+', '', text) 
        return result 

    def convert_number(self,text):  #convert number to test form
        temp_str = text.split() 
        new_string = [] 
    
        for word in temp_str: 
            if word.isdigit(): 
                temp = p.number_to_words(word) 
                new_string.append(temp) 
            else: 
                new_string.append(word) 
        temp_str = ' '.join(new_string) 
        return temp_str

    def remove_punctuation(self,text): 
        translator = str.maketrans('', '', string.punctuation) 
        return text.translate(translator)

    def remove_whitespace(self,text): 
        return  " ".join(text.split()) 
    
    def autospell(self,text):
        """
        correct the spelling of the word.
        """
        spells = [spell(w) for w in (nltk.word_tokenize(text))]
        return " ".join(spells)
    
    def remove_Tags(self,text):
        """
        take string input and clean string without tags.
        use regex to remove the html tags.
        """
        cleaned_text = re.sub('<[^<]+?>', '', text)
        return cleaned_text

    def remove_stopwords(self,sentence):
        """
        removes all the stop words like "is,the,a, etc."
        """
        stop_words = stopwords.words('english')
        return ' '.join([w for w in nltk.word_tokenize(sentence) if not w in stop_words])
    
    def sentence_tokenize(self,text):
        """
        take string input and return list of sentences.
        use nltk.sent_tokenize() to split the sentences.
        """
        sent_list = []
        for w in nltk.sent_tokenize(text):
            sent_list.append(w)
        return sent_list

    def word_tokenize(self,text):
        """
        :param text:
        :return: list of words
        """
        return [w for sent in nltk.sent_tokenize(text) for w in nltk.word_tokenize(sent)]

    def stem(self,text):
        """
        :param word_tokens:
        :return: list of words
        """
        stemmed_word = [snowball_stemmer.stem(word) for sent in nltk.sent_tokenize(text)for word in nltk.word_tokenize(sent)]
        return " ".join(stemmed_word)
    
    def lemmatize(self,text):
        lemmatized_word = [wordnet_lemmatizer.lemmatize(word)for sent in nltk.sent_tokenize(text)for word in nltk.word_tokenize(sent)]
        return " ".join(lemmatized_word)
    
    def preprocess(self,text):
        lower_text = self.text_lowercase(text)
        sentence_tokens = self.sentence_tokenize(lower_text)
        word_list = []
        for each_sent in sentence_tokens:
            lemmatizzed_sent = self.lemmatize(each_sent)
            clean_text = self.remove_numbers(lemmatizzed_sent)
            clean_text = self.remove_punctuation(clean_text)
            clean_text = self.remove_Tags(clean_text)
            clean_text = self.remove_stopwords(clean_text)
            word_tokens = self.word_tokenize(clean_text)
            for i in word_tokens:
                word_list.append(i)
        return word_list
