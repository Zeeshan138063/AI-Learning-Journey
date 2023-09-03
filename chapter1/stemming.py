"""
Natural Language Tool Kit (NLTK) is a Python library used to build programs capable of processing natural language.
The library can perform different operations such as
tokenizing, stemming, classification, parsing, tagging, semantic reasoning, sentiment analysis, and more.
"""
import string

import nltk

nltk.download('punkt')
from nltk.tokenize import word_tokenize

"""
Python Stemming example
One of the most popular stemming algorithms is called the “Porter stemmer.” 
The porter stemmer was first proposed by Martin Porter in a 1980 paper titled "An algorithm for suffix stripping." 
The paper has become one of the most common algorithms for stemming in English.
"""
from nltk.stem import PorterStemmer

# Initialize Python porter stemmer
ps = PorterStemmer()


def basic_example():
    # Example inflections to reduce
    example_words = ["program", "programming", "programer", "programs", "programmed"]
    # Perform stemming
    print("{0:20}{1:20}".format("--Word--", "--Stem--"))
    for word in example_words:
        print("{0:20}{1:20}".format(word, ps.stem(word)))

    """
    --Word--            --Stem--            
    program             program             
    programming         program             
    programer           program             
    programs            program             
    programmed          program

    """


def token_stemmer_example():
    example_sentence = "Python programmers often tend like programming in python because it's like english. We call people who program in python pythonistas."

    # Remove punctuation
    example_sentence_no_punct = example_sentence.translate(str.maketrans("", "", string.punctuation))

    # Create tokens
    word_tokens = word_tokenize(example_sentence_no_punct)

    # Perform stemming
    print("{0:20}{1:20}".format("--Word--", "--Stem--"))
    for word in word_tokens:
        print("{0:20}{1:20}".format(word, ps.stem(word)))

    """
    --Word--            --Stem--            
    Python              python              
    programmers         programm            
    often               often               
    tend                tend                
    like                like                
    programming         program             
    in                  in                  
    python              python              
    because             becaus              
    its                 it                  
    like                like                
    english             english             
    We                  we                  
    call                call                
    people              peopl               
    who                 who                 
    program             program             
    in                  in                  
    python              python              
    pythonistas         pythonista
    """


if __name__ == '__main__':
    # basic_example()
    token_stemmer_example()
