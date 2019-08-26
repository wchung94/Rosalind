#!/usr/bin/env python3
"""
Author: Wing Yu Chung
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns.
All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons of s.
(Note: Only one solution will exist for the dataset provided.)
"""

# Import statements
from sys import argv
import re

#FUNCTIONS
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
    split dataset into dictionary
    dataset: string separates by enters
    """
    fasta_dict = {}
    dataset = dataset.split()
    for line in dataset:
        if line.startswith('>'):
            fasta_dict[line[1:]] = ''
            current_line = line[1:]
        else:
            fasta_dict[current_line] += line


    return fasta_dict


def transcribe(sequence):
    """
    Change DNA string into RNA string by replacing T with U
    Input sequence: DNA sequence string
    Ouput: RNA sequence string

    """
    transcription = sequence.replace('T','U')
    return transcription


def find_index_match(substring, main_string):
    """"
    return indice of substring in mainstring
    yield integer of index substring in main string
    """
    motif = re.compile(substring)
    match_motif = re.finditer(motif, main_string)
    for intron in match_motif:
        yield intron.start()



def extract_sequences(fasta_dict):
    """
    extract  sequence into main sequence and introns
    Input: dictionary with sequences
    Output: exon
    """
    fasta_list = []
    for fasta_id, sequence in fasta_dict.items():
        fasta_list.append(sequence)

    exon = fasta_list[0]
    introns = fasta_list[1:]

    intron_dict = {}

    for intron in introns:
        if intron in exon: #dont forget to check for duplicates and overlap
            for match in find_index_match(intron, exon):

                intron_dict[match] = len(intron)


    for key,value in sorted(intron_dict.items(), reverse=True):
        exon = exon[:key] + exon[key+value:]


    exon = transcribe(exon)
    return exon




def translate(exon):
    """
    Translate codons into amino acids
    Input: List with codons
    Output: string of amino acids
    Return the translated protein sequence of codons in list.
    """
    amino_acids = ''
    codon = 0
    while codon < len(exon):
        if exon[codon:codon+3] in AMINO_ACID_DICT.keys():
            amino_acids += AMINO_ACID_DICT[exon[codon:codon+3]]
        codon += 3
    print(amino_acids)
    return amino_acids




if __name__ == "__main__":
    sequences = read_dataset(argv[1])

    sequences = split_dataset(sequences)
    exon = extract_sequences(sequences)
    translate(exon)


