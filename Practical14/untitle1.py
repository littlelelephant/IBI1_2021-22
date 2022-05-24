import xml.sax
import matplotlib.pyplot as plt
import time





plt.subplot()
plt.boxplot()
plt.title('Distribution of child node number of all GO terms')
plt.xlabel("GO terms")
plt.ylabel("Number")
plt.subplot()
plt.boxplot()
plt.title('Distribution of child node number of terms associated with ‘translation’')
plt.xlabel("associated with ‘translation’")
plt.ylabel("Number")
plt.show()