risk_dict={'30':1.03,'35':1.07,'40':1.11,'45':1.17,'50':1.23,'55':1.32,'60':1.42,'65':1.55,'70':1.72,'75':1.94}
#make a dictionary of the relative risk of CHD
import matplotlib.pyplot as plt #use the module
x=list(risk_dict.keys()) #use keys as x-value
y=list(risk_dict.values()) #use keys as y-value
plt.scatter(x,y) #make the scatter plots graph
plt.xlabel('paternal_age')
plt.ylabel('CHD')
plt.show() #show the graph

riskrate=risk_dict['60'] #we use '60' for example, we can change the key to get different value
print(riskrate)
