#!/usr/bin/env python3
"""
Author: Wing Yu Chung
Return the locations of subsequence in sequence in a string separated by spaces
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

def join_list_int(list):
    """
    combine integers into 1 string separated by a space.
    """
    str_list = map(str,list)
    joined_string = ' '.join(str_list)
    return joined_string


if __name__ == "__main__":
    sequences = read_dataset(argv[1])
    sequences = split_dataset(sequences)
    long_sequence = extract_sequence(sequences)
    sub_sequence = extract_subsequence(sequences)
    position_list = detect_position(long_sequence,sub_sequence)
    print(join_list_int(position_list))
