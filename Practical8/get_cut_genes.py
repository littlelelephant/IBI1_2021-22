import re
sequence=open(r"C:\Users\OMEN\IBI1_2021-22\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r')#open the file and read only
all_sequence=sequence.read()
cut1=re.sub(r'\n','',all_sequence)
cut2=re.sub(r'\r','',cut1)#cut off LF and CR
split_sequence=re.split('(>)',cut2)#devided the data by '>'
a=[]#creat a new list
counts=len(split_sequence)
for i in range (0,counts):
    if 'GAATTC' in split_sequence[i]:
        a.append(split_sequence[i])
file_output=open('cut_genes.fa','w+')#open a new file
for b in range(0,len(a)):
    add_1=re.findall(r'gene:.+?\s',a[b])
    cut3=re.sub(r'.+]', '', a[b])
    length_gene = str(len(cut3))#calculate the length
    str_add_1= ''.join(add_1)
    file_output.write(str_add_1)
    file_output.write(length_gene)
    file_output.write('\n')
file_output.close()
