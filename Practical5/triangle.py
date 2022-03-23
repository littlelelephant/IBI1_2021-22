for n in range(1,11):
    print('the',n,'th','triangle number:',(0.5*(2+n)*(n-1))+1) #use the formula to compute each value of the triangle sequence


p=0 #give p a definition
for n in range(0,10):
    n=n+1
    p=p+n #The value of the triangle sequence adding up as the ordinal number increases
    print('the',n,'th','triangle number:',p) #display 10 values of the triangle sequence