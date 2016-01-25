#!/usr/bin/python

import sys #module that can pass arguments from command line

#filename = 'rosalind_ini6.txt' #ok, hardcoded

filename = sys.argv[1] #allows filename input from command line
infile = open(filename,'r')

words = infile.readline().rstrip().split(' ') #split words in string into a list
infile.close()

d = {} #define empty dictionary

for w in words: ##one loop
    val = words.count(w) #count each instance of w in words
    d[w] = val #add count to dict

#write dict content in requested format
outfile = open("dict_out.txt","w")

for key, value in d.items():
    outfile.write(key + ' ' + str(value) + '\n')

outfile.close() #good habit to close files
