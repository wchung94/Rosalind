#!/usr/bin/env python3
"""
Author: Wing Yu Chung
Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12.
You may return these pairs in any order.
"""

# Import statements
from sys import argv

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

def extract_sequence(list):
    """
    extract  sequence from list with fasta header and sequence
    Input: list with sequences
    Output: string of  sequence
    """
    sequence =''
    for line in list:
        if line.startswith('>'):
            continue
        else:
            sequence += line
    return sequence

def comp_seq(sequence):
    """
    turn sequence into complementary reverse sequence
    Input: string
    Output: complementary reverse sequence string
    """
    comp_seq = ""
    for nuc in sequence:
            if nuc == "A":
                comp_seq += "T"
            elif nuc == "T":
                comp_seq += "A"
            elif nuc == "G":
                comp_seq += "C"
            elif nuc == "C":
                comp_seq += "G"
    comp_seq = comp_seq[::-1]
    return comp_seq

def detect_position(sequence):
    """
    detect position and length of palindromic sequences.
    Input: sequence string
    Output: list of position and length of palindromic sequences
    iterates first right to left and then removes most left part of sequence for the iteration.
    after every iteration, compares sequence with complement reverse sequence.
    """
    sequence_comp = sequence
    position_list = []
    while len(sequence_comp) > 0:
        for nuc in range(len(sequence_comp)):
            if sequence_comp[nuc:] == comp_seq(sequence_comp[nuc:]):
                if len(sequence_comp[nuc:]) > 3 and len(sequence_comp[nuc:]) < 13:
                    position_list.append(str(nuc+1) + ' ' +  str(len(sequence_comp[nuc:])))
        sequence_comp = sequence_comp[:-1]

    return position_list



if __name__ == "__main__":
    sequences = read_dataset(argv[1])
    sequences = split_dataset(sequences)
    sequence = extract_sequence(sequences)
    #print(sequence)
    position_list = detect_position(sequence)
    #print(position_list)

    for i in position_list:
        print(i)