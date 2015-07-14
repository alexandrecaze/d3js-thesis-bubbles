# read_thesis.py reads the text file 'thesis_pdf.txt' and
# generates an array containing the words of the thesis

# Get data
# ====================
file=open('./thesis_pdf.txt'); # Opening the file thesis_pdf.txt
thesis=file.read() # Reading the file into a single string
words=thesis.split() # Splitting the string into words, using space as a separation
Nwords=len(words) # Length of words
sentences=thesis.split('.') # Splitting the string into sentences, using dot as a separation
Nsentences=len(sentences) # Length of sentences

# display(tab,istart,n) displays n elements from tab
# starting from index istart
# ====================================================
def display(tab,istart,n):
    for i in range(istart,istart+n):
        print i,tab[i]

print 'First 10 words of the thesis:'
display(words,0,10)
print ''
print '10 sentences in the middle of the thesis:'
display(sentences,Nsentences/2,10)
print ''

# display_words(istart,n) displays n words from words
# starting from index istart
# ====================================================
def display_words(istart,n):
    for i in range(istart,istart+n):
        print i,words[i]

#print 'First 100 words of the thesis:'
#display_words(0,100)
#print ''
#print '1000 words in the middle of the thesis:'
#display_words(Nwords/2,1000)
#print ''
# print '100 words at 3/4 of the thesis:'
# display_words(Nwords*3/4,100)
# print ''

# number_occurences(str) returns the number of occurences
# of the string str in words
# ========================================================
def number_occurences(str):
    number=0
    for word in words:
        if (str==word):
            number=number+1
    return number

print 'Number of occurences of the word \'CDOS\':', number_occurences('CDOS')
print 'Number of occurences of the word \'LDOS\':', number_occurences('LDOS')

# is_in(str,dic) returns true is str is already a key of
# the dictionnary dic and false otherwise
# =======================================================
def is_in(str,dic):
    str_is_in_dic=False
    for word,number in dic.iteritems():
        if (str==word):
            str_is_in_dic=True
            break # gets out of the for loop
    return str_is_in_dic

dic={'CDOS':41, 'LDOS':273}
print is_in('CDOS',dic)
print is_in('LDOS',dic)
print is_in('Bonjour',dic)


# hist_occurences(istart,n) returns a dictionnary dic where
# dic['str'] is the number of occurences of str
# in the n words following word number istart in the array
# of strings words
# ========================================================
def hist_occurences(istart,n):
    dic={}
    for word in words[istart:istart+n]:
        if (is_in(word,dic)):
            dic[word]=dic[word]+1
        else:
            dic[word]=1
    return dic

dic=hist_occurences(0,Nwords)

# hist_clean(dic,thr) returns a dictionnary dic_new where
# all words with a number of occurences below thr are
# deleted
# ========================================================
def dic_clean(dic,thr):
    dic_new={}
    for word,number in dic.iteritems():
        if (number>thr):
            dic_new[word]=number
    return dic_new

# rewrite_dic(dic) rewrites the dictionnary dic as
# an array
#  ========================================================
def rewrite_dic(dic):
    array=[]
    i=0
    array= {"children":[{"word":word,"value":number} for word, number in dic.iteritems()]}
    return array

dic_new=dic_clean(dic,10)
array=rewrite_dic(dic_new)

import json

with open('thesis.json','w') as outfile:
    json.dump(array,outfile)


