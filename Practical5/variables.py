a=19245301
b=4218520
c=271
d=b-c
e=a-b
print('d=',d)
print('e=',e) #Obviously e>a, so e is greater
print('the rate of new cases in 2021=',d/c)
print('the rate of new cases in 2022=',e/b)
 #Obviously the rate of new cases in 2021 is greater

x="deng"
y="jiaqi"
w=x and y
print(w)

x="1"
y="2"
w=x and y
print(w)

x="dog"
y="cat"
w=x and y
print(w)

x="0"
y="jiaqi"
w=x and y
print(w) #I find that almost everything except 0, '', etc. are True.
