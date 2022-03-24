marks=[45,36,86,57,53,92,65,45] #list the list
marks.sort() #sort the marks
print(marks) #show the marks


import pandas as pd #use the module
import matplotlib.pyplot as plt #use the module
df = pd.DataFrame(marks) #use the data in the list
df.plot.box(title="Distribution of Marks") #give the boxplot a title
plt.grid(linestyle="--", alpha=0.3) #write some parameters about the boxplot
plt.show() #show the boxplot