def choco(total_money,price):
    change=total_money%price
    bars=(total_money-change)/price
    print('bars=',bars,'change=',change)
    return ''
print(choco(100,7))
#For example, if a bar of chocolate costs 7$, use 100$ to buy chocolate.
#It turns out you end up with 14 bars of chocolate and $2 change.

