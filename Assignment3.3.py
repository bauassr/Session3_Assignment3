# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 17:13:34 2018

@author: singh.shivam
"""

def Longest_Word(list_of_words):
        s=""
        for w in list_of_words:
            if len(s)<=len(w):
                s=w
               
        return s

Words=["Acadgild","Data","DataScience","DataMart","programming",
       "Coding","Math","Csharp","Python","R"] 

st=Longest_Word(Words)
print("Longest word in a list :-", st," with length of:= ",len(st))
    