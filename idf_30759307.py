#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Name- Dishi Jain
Student ID-30759307
Start Date-10th October 2019
Last Modified Date-11th October 2019
High Level Description-In this task, we have to define a class which will calculate the IDF value of each word using
a given formula. The higher the IDF value the more important the word is. The class will contain one instance 
variable called data that is a Pandas Dataframe. data will contain loaded term frequencies as rows. Each row 
represents the frequencies of a single cleaned text and each column corresponds to a word.
"""

import pandas as pd
import numpy as np
class IDFAnalyser:
    #constructor of class to create data frame
    def __init__(self):
        self.data = pd.DataFrame()
        
    def load_frequency(self,book_frequency,book_title):
        #append the dataframe with new frequency_dictionary as row everytime the function is called
        self.data = self.data.append(pd.DataFrame(book_frequency,index=book_title))
        #Fill the Nan values in the dataframe equal to 0
        self.data.fillna(0,inplace= True)

    def get_IDF(self,term):
        #counting the total number of documents or indexes in dataframe
        D = len(self.data.index)
        N = 0
        for value in self.data[term]:
            #if term's frequency is a number other than 0, it means the term exist in document
            if value != 0:
                N +=1
        idf_value = 1 + (np.log(D/(1+N)))
        return idf_value

