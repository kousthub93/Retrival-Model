import math
import operator

unigram_tokens_path ='unigram_tokens' # provide path for unigram tokens
unigram_tf_path = 'Unigram_Tf' # provide path for unigram tf
unigram_df_path = 'Unigram_Df' # provide path for unigram df
inverted_index_path = 'inverted_index_unigram' # provide path for inverted index
query_text_path = 'query.txt'  # provide path for query text
N = 1000 # corpus size
b=0.75
k1 = 1.2
k2 = 100

term_doc_dict={} # dictionary containing uniagram Dfs
dict_unigram_tokens={} # dictionary containing unigram tokens
dict_inverted_index={} # dictionary containing inverted index

# compute average document length
def average_doc_length():
    sum = 0
    string_entry=[]
    f = open(unigram_tokens_path,'r+')
    lines = f.readlines()
    for line in lines:
        string_entry.append(line.strip())
    for line in string_entry:
        temp = line.split("----->")
        dict_unigram_tokens.update({temp[0]:int(temp[1])})
        sum+=int(temp[1])
    return sum

avdl = (float(average_doc_length())/float(N))

# compute fi for and put it in the dictionary
def compute_fi():
    f = open(inverted_index_path,'r+')
    lines = f.readlines()
    for line in lines:
        temp = line.split("---->")
        indexes = temp[1].strip()
        dict_inverted_index.update({temp[0]:indexes})

compute_fi()

# compute ni for each term in the query
def compute_ni():
    f = open(unigram_df_path,'r+')
    string_entry = []
    lines = f.readlines()
    for line in lines:
        string_entry.append(line.strip())
    for line in string_entry:
        temp = line.split('-------->')
        term = temp[0].strip()
        rest_temp = temp[1]
        term_doc_dict[term]=rest_temp

compute_ni()

# get term occurences in the document for the given word
def get_fi(term,doc_id):
    postings = dict_inverted_index[term]
    doc_ids = postings.split(",")
    for index, val in enumerate(doc_ids):
        if doc_id == val[1:]:
            fi = doc_ids[index + 1]
            return fi

# compute bm_25 score for each doc for the given query
def compute_score(query,doc_id):
    each_query_term = query.split()
    score_bm=0
    for each_term in each_query_term:
        try:
            dl = dict_unigram_tokens[doc_id]
            K = k1 * ((1-b) + (b * (dl/avdl)))
            ri =0 # since no relevance information is given
            R=0

            num = term_doc_dict[each_term].split(",")
            ni = int(num[-1])
            temp_fi = get_fi(each_term,doc_id)

            if(isinstance(temp_fi, str)):
                fi = float(temp_fi.strip(")"))
            else:
                fi=0

            qfi = each_query_term.count(each_term)

            exp1 = (((float(ri) + 0.5) / (float(R) - float(ri) + 0.5)) / ((float(ni) - float(ri) + 0.5) / (float(N) - float(ni) - float(R) + float(ri) + 0.5)))
            exp2 = math.log(exp1)
            exp3 = (((float(k1) + 1) * float(fi)) / (float(K) + float(fi)))
            exp4 = (((float(k2) + 1) * float(qfi)) / (float(k2) + float(qfi)))
            score_temp = exp2*exp3*exp4
            score_bm+=score_temp

        except:
            pass
    return score_bm

# get the score for each doc and print it into a file
def compute_bm25(query,query_id):
    rank =0;
    dict_bm25={}
    each_query = query.split()
    doc_list=[]
    for each_term in each_query:
        if each_term in term_doc_dict.keys():
            str1 = term_doc_dict[each_term]
            str2 = str1.split(",")
            for x in str2[:-1]:
                if x.strip() not in doc_list:
                    doc_list.append(x.strip())

    for x in doc_list:
        score_bm25 = compute_score(query,x)
        dict_bm25.update({x:score_bm25})

    sorted_dict = sorted(dict_bm25.items(), key=operator.itemgetter(1))

    ranked_tuples = sorted_dict[::-1][0:100]

    file = open("Ranking_bm25.txt",'a')

    for key,value in ranked_tuples:
        rank+=1;
        temp_str = str(query_id) + " " + "Q0" + " " + " " + str(key) + " " + str(rank) + " " + str(value) + " " + "BM_25" + "\n"
        file.write(temp_str)

    file.close()

# read queries from the file
def main_program():
    query_id = 0
    f = open(query_text_path,'r+')
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    for each_query in lines:
        query = each_query.split(":")
        query_id+=1
        compute_bm25(query[1],query_id)

# call main function
main_program()




