#!/usr/bin/env python3
"""
Author: Wing Yu Chung
problem 19:
Given: At most 50 DNA strings of approximately equal length, 
not exceeding 1 kbp, in FASTA format (which represent reads deriving 
from the same strand of a single linear chromosome).
The dataset is guaranteed to satisfy the following condition: 
there exists a unique way to reconstruct the entire chromosome 
from these reads by gluing together pairs of reads that overlap by more 
than half their length.
Return: A shortest superstring containing all the given strings 
(thus corresponding to a reconstructed chromosome). 
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

def find_overlap(seq1, seq2):
    ''''
    search for overlap between sequences
    input dictionary of 2 fasta seqs.
    return consensus string
    '''
    overlap_len1 = round(len(seq1)/2)
    overlap_len2 = round(len(seq2)/2)

    minlength = max(overlap_len1,overlap_len2)

    length = 0
    consensus = ''

    while length < overlap_len1 -1  :
        if seq1[length:] == seq2[:len(seq1[length:])]:

            consensus = seq1 + seq2[len(seq1[length:]):]
            return consensus
        elif seq2[length:] == seq1[:len(seq2[length:])]:

            consensus = seq2 + seq1[len(seq2[length:]):]
            return consensus
        else:
            length += 1

    return consensus

def compare_sequences(fasta_dct):
    """
    compares sequences to create a list with one consensus string
    input dictionary labels and fasta seqs,
    output list with 1 consensus string
    """

    sequences = list(fasta_dct.values())


    while len(sequences) > 1 :
        for seq1 in sequences:
            for seq2 in sequences:
                if seq1 == seq2:
                    continue
                cons = find_overlap(seq1, seq2)
                if len(cons) > 1 :
                    sequences.append(cons)
                    sequences.remove(seq1)
                    sequences.remove(seq2)

                break

            print(len(sequences))
            print(sequences)

    for values in fasta_dct.values():
        if values in sequences[0]:
            return sequences[0]

    return sequences[0]



if __name__ == "__main__":
    fasta_dct = parse_fasta(argv[1])
    consensus = compare_sequences(fasta_dct)
    print(consensus)


