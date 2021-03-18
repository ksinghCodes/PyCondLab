#!/usr/bin/env/python 3.7

# FizzBuzz

num = int(input("Enter and Integer value between 1-100 inclusive: "))

if ( num%5==0 ) & (num%3==0):
    print("FizzBuzz")
elif(num%5==0):
    print("Buzz")
elif(num%3==0):
    print("Fizz")
else:
    print("num)


