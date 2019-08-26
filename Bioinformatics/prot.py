#!/usr/bin/env python3
"""
Author: Wing Yu Chung
Return the protein sequence of nucleotide sequence
"""

# Import statements
from sys import argv

#GLOBAL VIARABLES
AMINO_ACID_DICT = {
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'', 'UAG':'',
    'UGC':'C', 'UGU':'C', 'UGA':'', 'UGG':'W'}

#Functions
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


def split_codon(dna_sequence):
    """
    split sequence into codon in list
    Input: List with two strings
    Output: number of differences between the two strings
    Return the counted differences of two strings in a list.
    """
    codon_list = []
    codon = 0
    while codon < len(dna_sequence):
        if len(dna_sequence[codon:codon+3]) == 3:
            codon_list.append(dna_sequence[codon:codon+3])
        codon +=3
    return codon_list

def codon_amino_acid(codon_list):
    """
    Translate codons into amino acids
    Input: List with codons
    Output: string of amino acids
    Return the translated protein sequence of codons in list.
    """
    amino_acids = ''
    for codon in codon_list:
        if codon in AMINO_ACID_DICT.keys():
            amino_acids += AMINO_ACID_DICT[codon]
    return amino_acids


if __name__ == "__main__":
    sequences = read_dataset(argv[1])
    #print(sequences)
    codons = split_codon(sequences)
    #print(codons)
    amino_acids = codon_amino_acid(codons)
    print(amino_acids)