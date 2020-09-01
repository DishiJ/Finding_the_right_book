#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Name- Dishi Jain
Student ID-30759307
Start Date-9th October 2019
Last Modified Date-11th October 2019
High Level Description-In this task, we are required to define a class that will perform the basic preprocessing on
each input text. This class has one instance variable which is a string that holds the text of the book. Reading and
cleaning of the book content is carried out where cleaned text should contain only letters(of Enlish alphabet)
or a numbers or white-spaces.
"""

class Preprocessor:    
    #constrictor used to define an instance variable of the class
    def __init__(self):
        self.book_content = ""
        
    #function to present content of book    
    def __str__(self):
        return str(self.book_content)
    
    def clean(self):
        cleaned_text = ""
        #if book_content is an empty string return 1
        if self.book_content == "":
            return 1
        
        else :
            #converting entire string to lowercase
            self.book_content = self.book_content.lower()
            for char in self.book_content:
                if char.isalpha():
                    #to include only english alphabets in the cleaned_text
                    if char in "abcdefghijklmnopqrstuvwxyz":
                        cleaned_text = cleaned_text + char
                elif char.isdigit():
                    #including digits as it is in cleaned_text
                    cleaned_text = cleaned_text + char
                elif char == "-" or char == "_":
                    #replacing hypen and underscore with space
                    cleaned_text = cleaned_text + " "
                elif char == " " or char == "\n" or char == "\t":
                    #including spaces, newlines and tabs as it is in cleaned_text
                    cleaned_text = cleaned_text + char
            #storing back the cleaned_text into book_content
            self.book_content = cleaned_text
            return None

    def read_text(self,text_name):
        #opening file in readable format which is utf8 encoded
        with open(text_name,encoding = "utf-8-sig") as object:
            self.book_content = object.read()

