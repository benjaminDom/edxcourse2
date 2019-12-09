# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 07:17:41 2019

@author: BenTemp
"""

import collections
 
mydict={}


file1=open('98-0.txt',encoding="utf8")
x=file1.read().lower()




x=x.replace('\n',' ')
x=x.replace(".","")
x=x.replace(",","")
x=x.replace("\"","")
x=x.replace("“","")



x=x.split(' ')

for i in x:
    i.strip()


for i in x:
    if i=='':
        x.remove(i)
    

file2=open('stopwords')
sw=file2.read().lower()
sw=sw.split("\n")


"""
use stop words
"""
"""
for i in x:    
    if i in sw:
        x.remove(i)
"""    

words=[]
for i in x:
    if i not in sw:
       words.append(i) 

for i in words:
    if i in mydict:
        mydict[i]+=1
    else:
        mydict[i]=1
        
      
        
d =collections.Counter(mydict)

#print(d.most_common(10))
for word, count in d.most_common(20):
	print(word, ": ", count)        
        
        
"""
for i in x:
    print(i)


if i in mydict:
        print('key found')

file2=open('stopwordstest.txt')
sw=file2.read()
sw=sw.split("\n")

if x[10] in sw:
    x.remove(x[10])
    
    
    
     import collections

d = collections.Counter(mydict)
#print(d.most_common(10))
for word, count in d.most_common(10):
	print(word, ": ", count)
 
 :  4377
the :  4338
a :  1663
I :  1446
his :  1080
Mr. :  602
The :  586
he :  579
to :  579
said :  570
    
    
   


k=1
for i in x:    
    if i in sw:
        x.remove(i)
        if i=='the':
            print('removed the word="the" :',i,',',k,'times')
            k+=1





 
    
"""    