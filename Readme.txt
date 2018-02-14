^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

STEPS TO RUN TASK 1:
1. Navigate to the direcotry in which the file HW4.java is present
2. Run the follwing command
   javac HW4.java
   java HW4
3. Provide the path when it asks where to create an index
4. The program asks for the path containing the corpus for index creation. Provide the path
5. The program then asks for the path of the file containig the queries.
   Provide a file containing the queries in which the queries are written in the file in the below format
   query_id:query
   Ex: 1:hurricane isabel
5. Follow the the instructions which is displayed in the console
6. Please provide the paths in terms of absolute path
   Ex: D:\IR-6200\hw4\
7. A file containing the related tables are created in the same direcory where java file is present.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

STEPS TO RUN TASK 2:

1. Import the following:
   
   import math
   import operator
  
2. provide the source paths for the documents and assign it to the variables as indicated below:
   variable_name         Name of the file whose path is to be specified
   
   unigram_tokens_path   unigram_tokens
   unigram_tf_path 		 Unigram_Tf
   unigram_df_path   	 Unigram_Df
   inverted_index_path   inverted_index_unigram
   query_text_path 		 query.txt

3. queries in the query.txt should be in the below format
   query_id:query
   Ex: 1:hurricane isabel
   
3. Navigate to the directory in which the file HW4BM25.py is present and run the following command
   python HW4BM25.py
   
4. A file containing the table will be present in the same direcory where the file HW4BM25.py is present
5. Dictionary data structure is considered mainly to read data from the files

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FILES PRESENT IN HERE:

1. HW4.java               - Task 1 
2. HW4BM25.py             - Task 2
3. inverted_index_unigram - inverted index for unigrams-task2
4. Unigram_Tf             - term frequency table for unigram-task3.1
5. Unigram_Df             - document frequeny table for unigrams-task3.2
6. unigram_tokens         - table comprising filenames and number of tokens in that for unigram - task2
7. query.txt              - File containing the queries
8. Readme.txt             - Readme file providing various information on how to run the programs
9. Ranking_Lucene.txt     - File conatining 9 tables from Task1
10.Ranking_bm25.txt       - File conatining 9 tables from Task2
11.Ranking_Comparison.txt - A bried discussion comparing the top 5 results between the two search engines for 
                            each query						
12.Implementation.txt     - A brief report on the implementaion of BM_25.
13.Task2.py               - File from Task2 of HW3 assignement

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^