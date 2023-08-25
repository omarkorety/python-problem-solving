from unittest import result


test_cases=int(input())
for case in range(test_cases):
    N,sum=int(input()),0
    for num in range(N):
        value=int(input())
        result=value**(num+1)
        sum +=result

    print("sum is",sum)
