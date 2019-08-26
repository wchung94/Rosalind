#!/usr/bin/env python3
"""
Author: Wing Yu Chung
Given: A positive integer n≤7.
Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""	

#Import statements    	
from sys import argv
from itertools import permutations

def read_file(filetxt):
    """
    read file.txt and turns it into an integer
    Input: fasta file with permutation number
    Output: permutation integer
    """
    with open(filetxt, 'r') as text:
        dataset = text.read()
        dataset = dataset.strip()

    return int(dataset)

def permutation_list(integer):
    """
    Create permutation list from integer
    input is integer
    output is print of number of permutations and combinations
    """
    perm_list = list(permutations(range(1,integer+1)))
    print(len(perm_list))
    for tuple in perm_list:
        for perm in tuple:
            print(perm, end=' ')
        print('')
    return perm_list

if __name__ == "__main__":
    dataset = read_file(argv[1])
    perm_list = permutation_list(dataset)

