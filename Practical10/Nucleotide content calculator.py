import re
strand=input('The sequence:')
C=len(re.findall('C|c',strand))/len(strand)
A=len(re.findall('A|a',strand))/len(strand)
T=len(re.findall('T|t',strand))/len(strand)
G=len(re.findall('G|g',strand))/len(strand)
print('The percentage of C is:',C)
print('The percentage of A is:',A)
print('The percentage of T is:',T)
print('The percentage of G is:',G)
#I used the sequence:CAAAAGGT as an example
#output:
#The percentage of C is: 0.125
#The percentage of A is: 0.5
#The percentage of T is: 0.125
#The percentage of G is: 0.25