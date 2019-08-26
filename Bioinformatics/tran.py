#!/usr/bin/env python3
"""
Author: Wing Yu Chung
problem 20:
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2).
"""

# Import statements
from sys import argv
import itertools

#Functions
def parse_fasta(fasta_file):
    """
    Turns fasta file into dictionary object
    Input: fasta file with multiple short sequences
    Output: dict of labels and fasta sequences
    """

    fasta_dct = {}

    with open(fasta_file,'r') as text:
        label = ''
        for line in text:
            if line.startswith('>'):
                if label in fasta_dct.keys():
                    fasta_dct[current_line] = str(''.join(fasta_dct[current_line]))
                label = line.strip()[1:]
                fasta_dct[label] = []
                current_line = label
            else:
                fasta_dct[current_line].append(line.strip())
        fasta_dct[current_line] = str(''.join(fasta_dct[current_line]))


    return fasta_dct

def find_mutation(seq1, seq2):
    ''''
    search for mutation between sequences
    input two strings of sequences
    return return tuple of transition and transversion integers
    '''
    transition = 0
    transversion = 0
    for base in range(len(seq1)):
        if seq1[base] == seq2[base]:
            continue
        elif seq1[base] in 'A' and seq2[base] in 'G':
            transversion += 1
        elif seq1[base] in 'C' and seq2[base] in 'T':
            transversion += 1
        elif seq1[base] in 'G' and seq2[base] in 'A':
            transversion += 1        
        elif seq1[base] in 'T' and seq2[base] in 'C':
            transversion += 1    
        elif seq1[base] in 'AG' and seq2[base] in 'CT':
            transition+= 1 
        elif seq1[base] in 'CT' and seq2[base] in 'AG':
            transition+= 1     

    return (transition, transversion)

def compare_sequences(fasta_dct):
    '''
    compare two sequences of equal length in dictionary values 
    for ratio point mutations transition and transversion
    input: dictionary of fasta labels and sequences
    output ratio of transitions and transversions
    '''
    sequence = list(fasta_dct.values())
    mutation = find_mutation(sequence[0],sequence[1])
    ratio = mutation[1]/ mutation[0]         
    
    return ratio

if __name__ == "__main__":
    fasta_dct = parse_fasta(argv[1])
    print(compare_sequences(fasta_dct))
