#!/usr/bin/env python3
"""
Author: Wing Yu Chung
Return ID of ID of sequence string and content of GC from file c
containing multiple sequences.
"""	

#Import statements    	
from sys import argv
import operator

# Functions
def read_file(filetxt):
    """
    Turns dataset into list of records
    Input: fasta file with multiple short sequences
    Output: list of fasta sequences
    """
    with open(filetxt, 'r') as text:
        dataset = text.read()
        dataset = dataset.split('>')[1:]
    return dataset

def split_dataset(dataset):
    """
    Turns dataset into dictonary with id and sequence object
    Input: txt file with fasta sequences
    Output: dictonary of id and sequences.
    """
    fasta_list = []
    for record in dataset:
        record = record.split()[1:]
        record = "".join(record)
        fasta_list.append(record)

    return fasta_list

def consensus_sequence(dataset):
    """"
    Create consensus sequence from list of sequences
    input dataset: list of sequences
    output: consensus string
    """
    cons_string = ''
    for nuc in range(len(dataset[0])):
        cons = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
        for sequence in range(len(dataset)):
            cons[dataset[sequence][nuc]] += 1
        max(cons.items(), key=operator.itemgetter(1))[0]
        cons_string += max(cons.items(), key=operator.itemgetter(1))[0]
    return cons_string

def consensus_list(dataset):
    """
    Turns dataset into dictonary with id and sequence object
    Input: txt file with fasta sequences
    Output: dictonary of id and sequences.
    """
    nucleotides = ['A','C','G','T']
    cons = {'A': '', 'C': '', 'G': '', 'T': ''}

    for nuc in nucleotides:
        position = []
        for nucleo in range(len(dataset[0])):
            count = 0
            for sequence in range(len(dataset)):
                if nuc == dataset[sequence][nucleo]:
                    count += 1
            position.append(count)
            cons[nuc] = position
    return cons

def print_consensus_list(dataset):
    '''
    print the dictionary with consensus data like example below:
    ATGCAACT
    A: 5 1 0 0 5 5 0 0
    C: 0 0 1 4 2 0 6 1
    G: 1 1 6 3 0 1 0 0
    T: 1 5 0 0 0 1 1 6
    input dataset: dictionary with lists of consensus data for each nucleobase
    '''
    for key, value in dataset.items():
        print(key + ': ', end='')
        for count in value:
            print(count, ' ', end='')
        print('')
    return


if __name__ == "__main__":
    data = read_file(argv[1])
    dataset =split_dataset(data)

    consensus_position = (consensus_list(dataset))

    consensus_string = consensus_sequence(dataset)
    print(consensus_string)

    print_consensus_list(consensus_position)

