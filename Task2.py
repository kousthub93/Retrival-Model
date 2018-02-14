import requests
from bs4 import BeautifulSoup
import os
import re
from string import maketrans
import operator

S_PATH = 'D:\\IR-6200\\hw3\\parsetextfiles'  #mention source path in which the cleaned corpus is present
# dictionaries to hold inverted indexes and tokens generated
dict_unigram ={}
dict_bigram ={}
dict_trigram ={}
dict_unigram_tokens ={}
dict_bigram_tokens ={}
dict_trigram_tokens={}

def unigram_index(data_list,formatted_fName):

    uni_temp = [] # for generating tokens,set is used to avoid duplicate  elements
    for each_word in data_list:
        uni_temp.append(each_word)
        if dict_unigram.has_key(each_word):
            if formatted_fName[0] not in dict_unigram[each_word]: #check whether the file is there in the dictionary
                dict_unigram[each_word].update({formatted_fName[0]: 1})
            else:
                dict_unigram[each_word][formatted_fName[0]] += 1  #updated the times of occurence if the file is already
                                                                  #in the dictionary
        else:
            dict_unigram[each_word] = {formatted_fName[0]: 1}

    num_tokens = len(uni_temp)
    dict_unigram_tokens.update({formatted_fName[0]:str(num_tokens)})


def bigram_index(data_list,formatted_fName):
    bi_temp = set()
    for index in range(len(data_list) - 1):
        each_bi_gram = data_list[index] + " " + data_list[index + 1] #to generate bi gram tokens
        bi_temp.add(each_bi_gram)
        if dict_bigram.has_key(each_bi_gram):
            if formatted_fName[0] not in dict_bigram[each_bi_gram]:
                dict_bigram[each_bi_gram].update({formatted_fName[0]: 1})
            else:
                dict_bigram[each_bi_gram][formatted_fName[0]] += 1

        else:
            dict_bigram[each_bi_gram] = {formatted_fName[0]: 1}

    num_tokens = len(bi_temp)
    dict_bigram_tokens.update({formatted_fName[0]:str(num_tokens)})


def trigram_index(data_list,formatted_fName):
    tri_temp = set()
    for index in range(len(data_list) - 2):
        #to generate tri gram tokens
        each_tri_gram = data_list[index] + " " + data_list[index + 1] + " " + data_list[index + 2]
        tri_temp.add(each_tri_gram)
        if dict_trigram.has_key(each_tri_gram):
            if formatted_fName[0] not in dict_trigram[each_tri_gram]:
                dict_trigram[each_tri_gram].update({formatted_fName[0]: 1})
            else:
                dict_trigram[each_tri_gram][formatted_fName[0]] += 1

        else:
            dict_trigram[each_tri_gram] = {formatted_fName[0]: 1}

    num_tokens = len(tri_temp)
    dict_trigram_tokens.update({formatted_fName[0]:str(num_tokens)})

def create_tf(dictAny,fileName):
    # to create term frequency table for uni,ni and tri grams
    dict_tf ={}
    for key in dictAny.keys():
        sum_tf = 0
        dict_temp = dictAny[key]
        for each_file in dict_temp.keys():
            sum_tf = sum_tf + dict_temp[each_file]

        dict_tf.update({key:sum_tf})

    dict_tf_temp = sorted(dict_tf.iteritems(), key=operator.itemgetter(1),reverse = True)

    f = open(fileName, 'w')
    write_to =''
    for key,value in dict_tf_temp:
        write_to+=key +'-------->' +str(value)+'\n'

    f.write(write_to)
    f.close()

def create_df(dictAny,fileName):

    #to create Df tables for uni,bi and tri grams
    dict_df = sorted(dictAny.iteritems(), key=operator.itemgetter(0))
    f = open(fileName, 'w')
    for key,value in dict_df:
        term = key
        docIds = ''
        df = len(value)
        k=0 #if k<df then append ',' else do not append
        for each_value in value.keys():
            k+=1
            if(k<df):
                docIds += each_value + ","
            else:
                docIds+=each_value

        f.write(term + "  " + "-------->" + " " + docIds +"," + str(df) + "\n")

    f.close()

def create_tokens_dict(dictAny,fileName):
    f = open(fileName,'w')
    keys = dictAny.keys()
    values= dictAny.values()
    for i in range(0,len(keys)):
        f.write(keys[i]+"----->" + " " +str(values[i]) + "\n")
    f.close()

def create_index_file(dictAny,fileName):
    sorted_x = sorted(dictAny.items(), key=operator.itemgetter(0))
    #generate inverted index files for uni,bi and tri
    f = open(fileName,'w')
    for key,values in sorted_x:
        term = key
        dict_index = values
        df = len(dict_index)
        k=0
        docs = ''
        for each_key in dict_index.keys():
            k+=1
            if k < df:
                docs += "(" + each_key + "," + str(dict_index[each_key]) + ")" + ","
            else:
                docs += "(" + each_key + "," + str(dict_index[each_key]) + ")"

        f.write(term+"---->"+docs+"\n")

    f.close()


def createInvertedIndex(dirName):

    files = os.listdir(dirName)

    for eachFile in files:
        print eachFile
        formatted_fName = eachFile.split(".txt")
        fileName = open(dirName + '\\' + eachFile, 'r+')
        data = fileName.read()
        data_list = data.split()

        #to create inverted index for unigram
        unigram_index(data_list,formatted_fName)
        # to create inverted index for bigram
        bigram_index(data_list,formatted_fName)
        # to create inverted index for trigram
        trigram_index(data_list,formatted_fName)

    # to create Tfs and DFs for uni,bi and tri grams
    create_tf(dict_unigram,"Unigram_Tf")
    create_tf(dict_bigram,"Bigram_Tf")
    create_tf(dict_trigram,"Trigram_Tf")
    create_df(dict_unigram,"Unigram_Df")
    create_df(dict_bigram, "Bigram_Df")
    create_df(dict_trigram,"Trigram_Df")

    #to create files containing number of tokens in each file
    create_tokens_dict(dict_unigram_tokens,"unigram_tokens")
    create_tokens_dict(dict_bigram_tokens, "bigram_tokens")
    create_tokens_dict(dict_trigram_tokens, "trigram_tokens")

    #to creates file containing invserted index for uni,bi and tri grams
    create_index_file(dict_unigram,"inverted_index_unigram")
    create_index_file(dict_bigram, "inverted_index_bigram")
    create_index_file(dict_trigram, "inverted_index_trigram")

#call to create inverted index
createInvertedIndex(S_PATH)