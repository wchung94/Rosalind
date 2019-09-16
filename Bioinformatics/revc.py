#!/usr/bin/env python3
"""
Author: Wing Yu Chung

Complementing a Strand of DNA.
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
    extract longest sequence from list of sequences
    Input: list with sequences
    Output: string of longest sequence
    """
    long_sequence = max(list,key=len)
    return long_sequence

def extract_subsequence(list):
    """
    extract sub/shortest sequence from list of sequences
    Input: list with sequences
    Output: string of subsequence
    """
    short_sequence = min(list,key=len)
    return short_sequence



def detect_position(long,sub):
    """
    detect position of sub sequence in sequence.
    Input: two sequence strings 1: long sequence 2: subsequence
    Output: list of the positions that subsequence is present in sequence
    Return position of subsequence in sequence
    """
    position_list =[]

    for nucl in range(len(long)):
        if long[nucl:nucl+len(sub_sequence)] == sub:
            position_list.append(nucl+1)
    return position_list



def dna_to_rna(string):
    dna = string
    rna = dna.replace('T','U')
    return rna

def write_to_txt(string):
    text_file = open("answer.txt", "w")
    text_file.write(string)
    text_file.close()

def reverse_string(string):
    rev_string = string[::-1]
    return rev_string

def comp_seq(sequence):
    """
    turn sequence into complementary sequence
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
    #comp_seq = comp_seq[::-1]
    return comp_seq

if __name__ == "__main__":
    sequences = read_dataset(argv[1])
    print(sequences)
    rev_sequence = reverse_string(sequences)
    print(rev_sequence)
    rev_comp_sequence = comp_seq(rev_sequence)
    print(rev_comp_sequence)
    write_to_txt(rev_comp_sequence)
    # sequences = split_dataset(sequences)
    # long_sequence = extract_sequence(sequences)
    # sub_sequence = extract_subsequence(sequences)
    # position_list = detect_position(long_sequence,sub_sequence)
    # print(join_list_int(position_list))
