# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/13/2022
# Description: A function that takes as a parameter a list and reverses the order
# of the elements in that list.

def reverse_list(vals):
    for i in range(len(vals) // 2):
        vals[i], vals[len(vals) - i - 1] = vals[len(vals) - i - 1], vals[i]
