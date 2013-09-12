import nltk
import os
import string

from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

def outputIndexFile(index_content , output_path):
    pass

def combineTokens(index_content , tokens , file_id):
    for token in tokens.keys():
        if index_content.get(token) == None:
            file_dict = {}
            file_dict[file_id] = tokens.get(token)
        else:
            file_dict = index_content.get(token)
            file_dict[file_id] += tokens.get(token)
        index_content[token] = file_dict
        
    return index_content
        
def data_stem(tokens):
    tokens_stem = {}
    pStemmer = PorterStemmer()
    for word in tokens:
        try:
            if tokens_stem[word]:
                tokens_stem[word] += 1
        except:
            tokens_stem[word] = 1
    return tokens_stem

def data_token(line_clean):
    return word_tokenize(line_clean)
    
def data_clean(line):
    tmp_line = filter(lambda x: x in string.printable , line)
    return tmp_line.translate(None , string.punctuation + string.digits).strip()

def getTokens(line):
    line_clean = data_clean(line)
    tokens = data_token(line_clean)
    tokens_stem = data_stem(tokens)
    return tokens_stem
    
def createInvertedIndex(path , file_id):
    index_content = {}
    if os.path.exists(output_path):
        index_content = getIndexContent(output_path)
        
    fd = open(path , 'r')
    for line in fd.readlines():
        tokens = getTokens(line)
        index_content = combineTokens(index_content , tokens , file_id)
    fd.close()
    print index_content
    
if __name__ == "__main__":
    path = "C:\\Python27\\test.txt"
    output_path = "C:\\Python27\\invertedIndex"
    file_id = "1"
    index_content = createInvertedIndex(path , file_id)
    outputIndexFile(index_content , output_path)
    