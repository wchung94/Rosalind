#!/usr/bin/env python3
"""
Author: WYC
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
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

def read_file_list(filetxt):
    """
    Turns dataset into list object
    Input: fasta file with multiple short sequences
    Output: list of fixed positions of fasta ids
    """

    fasta_list = []
    with open(filetxt,'r') as text:
        dataset = text.readlines()

        for line in dataset:
            line = line.strip()
            if line.startswith('>'):
                fasta_list.append(line[1:])

    return fasta_list


def detect_overlap(fasta_dict, overlap_size):
    """
    analyze each value(sequence)with other values
    fasta_dict: dictionary of id and sequences
    overlap_size: integer of overlap size
    Output: output of list with ids wherein there is overlap at
    N-terminal with C-terminal
    """
    overlap_list = []
    for key1, key2 in itertools.combinations(fasta_dict,2):
        if fasta_dict[key1][-overlap_size:] == fasta_dict[key2][:overlap_size]:
            overlap_list.append(key1 + ' ' + key2)
        if fasta_dict[key1][:overlap_size] == fasta_dict[key2][-overlap_size:]:
            overlap_list.append(key2 + ' ' + key1)
    return overlap_list

if __name__ == "__main__":
    data_structure = read_file(argv[1])
    overlap_list = detect_overlap(data_structure, 3)
    data_list = read_file_list(argv[1])

    for key in data_list:
        for match in overlap_list:
            if key in match[:len(key)]:
                print(match)
