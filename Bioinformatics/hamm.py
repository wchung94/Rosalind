#!/usr/bin/env python3
"""
Author: Wing Yu Chung
Return the locations of subsequence in sequence
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
    lines = dataset.split()
    sequence = {}
    sequence_long = ''
    sequence_short = ''
    for line in lines:
        sequence_long = line
        if len(sequence_long) < len(sequence_short):
            sequence_short = line

    sequence[sequence_long] = sequence_short
    return sequence



def detect_position(dataset):
    """
    compare two strings in list.
    Input: List with two strings
    Output: number of differences between the two strings
    Return the counted differences of two strings in a list.
    """
    dataset = dataset.split("\n")
    sequence = dataset[0]
    sequence_cor = dataset[1]

    hamming_nr = 0
    for nuc in range(len(sequence)):
        if sequence[nuc] != sequence_cor[nuc]:
            hamming_nr +=1

    return hamming_nr



if __name__ == "__main__":
    sequences = read_dataset(argv[1])
    print(sequences)
