#!/usr/bin/env python3
"""
Author: Wing Yu Chung
problem 18:
Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
Return: One collection of indices of s in which the symbols of t appear as a subsequence of s.
If multiple solutions exist, you may return any one.
"""

# Import statements
from sys import argv

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
    print(fasta_dct)

    return fasta_dct

def match_sequence(fasta_dct):
    ''''
    search for matches in main seq from subsequence
    input dictionary of 2 fasta seqs.
    output list with match indexes
    '''
    assert len(fasta_dct.values()) == 2, "Not 2 sequences"

    main_seq = max(fasta_dct.values(), key=len)
    sub_seq = min(fasta_dct.values(), key=len)

    match_lst = []

    main_idx = 0
    sub_idx = 0
    while main_idx < len(main_seq):
        while sub_idx <  len(sub_seq):
            if sub_seq[sub_idx] == main_seq[main_idx]:
                match_lst.append(main_idx + 1)
                main_idx += 1
                sub_idx += 1
            else:
                main_idx += 1
        break
    return match_lst


if __name__ == "__main__":
    fasta_dct = parse_fasta(argv[1])
    matches_lst = match_sequence(fasta_dct)
    for match in matches_lst:
        print(str(match) + ' ', end='')