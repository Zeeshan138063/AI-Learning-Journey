"""
 In our lemmatization example, we will be using a popular lemmatizer called WordNet lemmatizer.

Wordnet is a large, free, and publicly available lexical database for the
English language aiming to establish structured semantic relationships between words.
"""

import nltk
import string
from nltk.tokenize import word_tokenize


nltk.download('punkt')

nltk.download("wordnet")
nltk.download("omw-1.4")

from nltk.stem import WordNetLemmatizer

# Initialize wordnet lemmatizer
wnl = WordNetLemmatizer()
def basic_lemmatizer_example():
    # Example inflections to reduce
    example_words = ["program", "programming", "programer", "programs", "programmed"]

    # Perform lemmatization
    print("{0:20}{1:20}".format("--Word--", "--Lemma--"))
    for word in example_words:
        print("{0:20}{1:20}".format(word, wnl.lemmatize(word, pos="v")))

    """
    --Word--            --Lemma--           
    program             program             
    programming         program             
    programer           programer           
    programs            program             
    programmed          program
    """


def lemmatizer_with_tokenizer():
    example_sentence = "Python programmers often tend like programming in python because it's like english. We call people who program in python pythonistas."

    # Remove punctuation
    example_sentence_no_punct = example_sentence.translate(str.maketrans("", "", string.punctuation))
    word_tokens = word_tokenize(example_sentence_no_punct)
    # Perform lemmatization
    print("{0:20}{1:20}".format("--Word--", "--Lemma--"))
    for word in word_tokens:
        print("{0:20}{1:20}".format(word, wnl.lemmatize(word, pos="v")))
    """
    --Word--            --Lemma--           
    Python              Python              
    programmers         programmers         
    often               often               
    tend                tend                
    like                like                
    programming         program             
    in                  in                  
    python              python              
    because             because             
    its                 its                 
    like                like                
    english             english             
    We                  We                  
    call                call                
    people              people              
    who                 who                 
    program             program             
    in                  in                  
    python              python              
    pythonistas         pythonistas 
    """


if __name__ == '__main__':
    # basic_lemmatizer_example()
    lemmatizer_with_tokenizer()