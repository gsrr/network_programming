import nltk
import os
import string

from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize


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

def getIndexContent(index_path , idList):
    index_content = {}
    fr = open(index_path , 'r')
    while True:
        line = fr.readline()
        if not line: break
        key = line.split()[0]
        file_num = int(line.split()[1])
        file_dic = {}
        for i in range(0 , file_num):
            file_line = fr.readline()
            file_id = file_line.split()[0]
            if file_id in idList:
                file_dic[file_id] = 0
            else:
                file_dic[file_id] = int(file_line.split()[1])
        index_content[key] = file_dic
    return index_content
    

def createInvertedIndex(path , file_id , index_content):
    fd = open(path , 'r')
    for line in fd.readlines():
        tokens = getTokens(line)
        index_content = combineTokens(index_content , tokens , file_id)
    fd.close()
    return index_content

def outputIndexFile(index_content , output_path):
    fw = open(output_path , 'w')
    for key in index_content.keys():
        file_list = index_content[key]
        fw.write(key + " " + str(len(file_list)) + "\n")
        for id in file_list.keys():
            fw.write(id + " " + str(file_list[id]) + "\n")
    fw.close()

if __name__ == "__main__":
    path = "C:\\Python27\\test.txt"
    output_path = "C:\\Python27\\invertedIndex"
    file_id = "1"
    index_content = {}
    if os.path.exists(output_path):
        index_content = getIndexContent(output_path , file_id)
    
    index_content = createInvertedIndex(path , file_id , index_content)
    outputIndexFile(index_content , output_path)
    