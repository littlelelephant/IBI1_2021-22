marks=[45,36,86,57,53,92,65,45] #list the list
marks.sort() #sort the marks
print(marks) #show the marks


import pandas as pd #use the module
import matplotlib.pyplot as plt #use the module
df = pd.DataFrame(marks) #use the data in the list
df.plot.box(title="Distribution of Marks") #give the boxplot a title
plt.grid(linestyle="--", alpha=0.3) #write some parameters about the boxplot
plt.show() #show the boxplot

m=len(marks) #let m equals to the elements number in the list
i=0
j=0
while i<m:
    j+=marks[i] #get the sum of all marks
    i+=1 #to calculate the next element in the list
print('the average mark is',j/m) #show the average mark.Obviously is smaller than 60%



