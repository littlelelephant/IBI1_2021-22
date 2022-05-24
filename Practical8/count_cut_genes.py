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
file_name=input("Enter the file name")
file_output=open("%s.fa" % file_name, 'w')#open the file
for b in range(0,len(a)):#create a loop
    add_1=re.findall(r'gene:.+?\s',a[b])
    fragments=len(re.findall(r'GAATTC',a[b]))+1
    cut3=re.sub(r'.+]', '',a[b])
    file_output.write(str(add_1))
    file_output.write('        ')
    file_output.write(str(fragments))
    file_output.write('\n')
    file_output.write(cut3)
    file_output.write('\n')
file_output.close