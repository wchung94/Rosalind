#!/usr/bin/env python3
"""
Author: WYC
Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has
genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism
always mates with an organism having genotype Aa Bb.
"""

# Import statements
from sys import argv
import itertools

#Functions
def read_file(filetxt):
    """
    Turns dataset into dictionary object
    Input: fasta file with multiple short sequences
    Output: dictionary of fasta id and sequence
    """

    fasta_dict = {}
    with open(filetxt,'r') as text:
        dataset = text.readlines()

        for line in dataset:
            line = line.strip()
            if line.startswith('>'):
                fasta_dict[line[1:]] = ''
                current_line = line[1:]
            else:
                fasta_dict[current_line] += line

    return fasta_dict

def read_dataset(filetxt):
    """
    Turns dataset into string object
    Input: txt file with string
    Output: string of data from txt file.
    """
    text = open(filetxt, 'r')
    dataset = text.read()
    dataset = dataset.strip()
    text.close()
    return dataset

def split_dataset(dataset):
    """
    Turns dataset string separated by \n into a list
    """
    sequence = dataset.split()
    return sequence

def next_generation(K,N):

    gen_count = 0
    K = 1
    N = 1
    hetero_zyg = ['AaBb']

    mate = ['A','a','B','b']
    parent = ['A','a','B','b']


    generation_a = list(itertools.product(mate[0:2], parent[0:2]))
    print(generation_a)
    generation_b = list(itertools.product(mate[2:4], parent[2:4]))
    print(generation_b)

    generation = list(itertools.product(generation_a, generation_b))
    print(generation)

    for allele in generation:
        print(list(itertools.chain.from_iterable(allele)))


    return




if __name__ == "__main__":
    data_structure = read_dataset(argv[1])
    data_structure = split_dataset(data_structure)
    numbers = list(map(int, data_structure))
    print(numbers)
    AaBb_prob = next_generation(numbers[0],numbers[1])
    #print(AaBb_prob)