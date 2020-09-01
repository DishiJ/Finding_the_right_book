#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Name- Dishi Jain
Student ID-30759307
Start Date-13th October 2019
Last Modified Date-14th October 2019
High Level Description-This task is defined to use Term Frequency-Inverse Document Frequency (TF-IDF) to determine
the most suitable document for a given term. The tf-idf value is calculated for a given term for all the documents.
The document with the highest tf-idf value is selected as the most suitable document for that term.
"""

def choice(term,documents):
    max_tdf_value = 0
    #iterating inside the column represented by the term in the data frame
    for value in documents.data[term]:
        tf_idf_value = value * documents.get_IDF(term)
        #comparing calculated tf_idf_value with the max_tdf_value
        if max_tdf_value < tf_idf_value:
            max_tdf_value = tf_idf_value
            final_value = value
    #getting the index value that matches the maximum value inside the dataframe column represented by term
    index_value = documents.data.index[documents.data[term] == final_value]
    #using the index value as a string
    index_value = ','.join(index_value)
    return index_value

