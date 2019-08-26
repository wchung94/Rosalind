#!/usr/bin/env python3
"""
Author: Wing Yu Chung
Given: A protein string of length at most 1000 aa.
Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000.
"""

# Import statements
from sys import argv

#GLOBAL VIARABLES
AMINO_ACID_DICT = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def read_dataset(filetxt):
    """
    Turns dataset into string object
    Input: txt file with sequence
    Output: string of data from txt file.
    """
    text = open(filetxt, 'r')
    dataset = text.read()
    dataset = dataset.strip()
    text.close()
    return dataset


def extract_sequence(codons):
    """
    extract  sequence from list with fasta header and sequence
    Input: list with sequences
    Output: string of  sequence
    """
    stopcodons = 3
    total = 1
    codon = list(AMINO_ACID_DICT.values())

    for nuc in codons:
        total *= codon.count(nuc)
    total *= stopcodons

    return total

def modulo_mil(sequence):
    #return modulo of number of RNA strings after modudlo 1000000
    modulo = sequence%1000000
    return modulo

if __name__ == "__main__":
    sequences = read_dataset(argv[1])
    number_seq = extract_sequence(sequences)
    number_rna = modulo_mil(number_seq)
    print(number_rna)