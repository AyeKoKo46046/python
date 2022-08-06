#!/usr/bin/python3

while 1:
    amount=int(input("Enter amount:  "))
    if amount<1000:
        discount=amount*0.05
        print("Discount", discount)
    else:
        discount=amount*0.1
        print("Discount:",  discount)
    print("Net payable:", amount-discount)