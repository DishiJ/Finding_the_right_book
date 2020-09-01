#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Name- Dishi Jain
Student ID-30759307
Start Date-10th October 2019
Last Modified Date-11th October 2019
High Level Description-In this task, we are required to define a class for analysing the number of occurrences for
each word from a given cleaned text. Hence we create two dictionaries, one for counting word occurences and another
for the frequency count of each word. This class has one instance variable called word_counts. The instance variable
is returned in a readable format.
"""

class WordAnalyser:
    #Constructor to create an instance variable
    def __init__(self):
        self.word_counts = {}
        
    
    def __str__(self):
        output = ""
        for key in self.word_counts:
            #presenting the word_counts dictionary in a readable format
            output = output + str(key) + ":" + str(self.word_counts[key]) + "\n"
        return output    
        
    def analyse_words(self,book_text):
        #splitting the cleaned text with delimiter space and storing it in a list using .split()
        book_text = book_text.split()
        #emptying the dictionary for every time the function is called 
        self.word_counts = {}
        for word in book_text:
            if word not in self.word_counts:
                #storing keys only with values as 0 into word_counts dictionary
                self.word_counts[word] = 0
        for key in self.word_counts:
            #counting value of every key in word_counts from the list book_text
            self.word_counts[key] = book_text.count(key)
            
            
    def get_word_frequency(self):
        all_words_sum = 0
        frequency_count = {}
        for key in self.word_counts:
            #counting the sum of all values in the dictionary word_counts
            all_words_sum = all_words_sum + self.word_counts[key]
        for key in self.word_counts:
            #calculating frequency value as each word_counts value divided by sum of all values
            frequency_count[key] = self.word_counts[key]/all_words_sum
        return frequency_count

