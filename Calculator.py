#!/usr/bin/python3
#Calculator Program
#programmer: Aye Ko Ko

while 1:
    first_no = float(input('Please Enter First No.:  '))
    operator = input ('Please Enter operator:  ')
    second_no = float (input('Please Enter Second No.:  '))
    if operator == '+':
        result = first_no + second_no
    elif operator == '-':
        result = first_no - second_no
    elif operator == '*':
        result = first_no * second_no
    elif operator == '/':
        result = first_no / second_no
    elif operator == '%':
        result = first_no % second_no
    else:
        print ('Wrong Number Sir!')
    print('The answer is:  ', result)

