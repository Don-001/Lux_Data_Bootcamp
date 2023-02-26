#!/bin/bash

def sum_array(arr):
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum

n = int(input("Enter the number of integers: "))
arr = []

for i in range(n):
    num = int(input("Enter an integer: "))
    arr.append(num)

print("The sum of the array is:", sum_array(arr))
