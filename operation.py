# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pywebio.input import *
from pywebio.output import *
import math

def mathematicalOperation():
    a = input("enter a number",type=FLOAT)
    b = input("enter another number",type=FLOAT)
    c = 0

    operation = radio("choose one option",options=['+','-','*','/','%','log','fact','sqrt'])
    operation_name = ""
    
    if operation=='+':
        operation_name = "addition"
        c= a+b
    elif operation=='-':
        operation_name = "subtraction"
        if a >= b:
            c = a-b
        else:
            c = b-a
    elif operation == '*':
        operation_name = "multiplication"
        c = a*b
        
    elif operation=='/':
        operation_name = "division"
        c = a/b
        
    elif operation=='log':
        operation_name = "logarithm"
        c =  math.log2(a)
        
    elif operation == 'fact':
        operation_name = "factorial"
        c = math.factorial(a)
    
    elif operation=='%':
        operation_name = "modulo"
        c = a%b
    
    else:
        operation_name = "square root"
        c = math.sqrt(a)
        
        
        
    put_text('The operation selected is: %s. and the output is: %.1f' % (operation_name, c))

if __name__ == "__main__":
    mathematicalOperation()
    


    

