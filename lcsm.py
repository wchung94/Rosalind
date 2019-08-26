#!/usr/bin/env python3
"""
Author: Wing Yu Chung
problem 14:
Given:A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return:A longest common substring of the collection. (If multiple solutions exist, 
you may return any single solution.)
"""

# Import statements
from sys import argv

#Functions
def read_file_list(filetxt):
    """
    Turns dataset into list object
    Input: fasta file with multiple short sequences
    Output: list of fasta sequences
    """

    fasta_list = []
    with open(filetxt,'r') as text:
        dataset = text.read()
        dataset = dataset.split('>')[1:]

    #I should split this part in separate function. Too lazy to do now
    for record in dataset:
        record = record.split()[1:]
        record = "".join(record)
        fasta_list.append(record)
  
    return fasta_list

def generates_kmers(sequence_list):
    '''
    generates kmers from longest sequence from a list of sequences
    sequence_list: list of sequence strings
    output: generator of kmers from long to short
    '''

    sequence = max(sequence_list, key=len)
    kmer_length = len(sequence)

    while kmer_length >= 1:
        for i in range(len(sequence) - kmer_length + 1):
            kmer = sequence[i:i+kmer_length]

            yield kmer
        kmer_length -= 1

def detect_overlap(seq_overlap, seq_list):
    """
    analyze if the kmer is present in all sequences by checking presence of all kmers in the sequences.
    seq_overlap = kmer generator (generates_kmers())
    seq_list = list of sequences
    """

    for overlap in seq_overlap:
        motif_signal = True
        for seq in seq_list:
            if overlap not in seq:
                motif_signal = False
                continue
        if motif_signal == True:
            return overlap
    return 'No overlap found'

if __name__ == "__main__":
    data_structure = read_file_list(argv[1])

    #iterates all possible kmers over the present sequences to check for longest similar motif
    overlap = detect_overlap(generates_kmers(data_structure),data_structure)
    print(overlap)
