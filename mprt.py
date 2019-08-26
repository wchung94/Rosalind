#!/usr/bin/env python3
"""
Author: Wing Yu Chung
Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, 
output its given access ID followed by a list of locations in 
the protein string where the motif can be found.
"""

# Import statements
from sys import argv
import urllib.request
import re

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

def open_uniprotsite(prot_names):
    """
    create dictionary with protein ids and fasta sequence from uniprot site
    Input: list with prot names
    Output: dictionary with prot ids and fasta sequences.
    """
    fasta_dict = {}
    for prot_id in prot_names:
    
        uniprot_link = "https://www.uniprot.org/uniprot/" + prot_id + ".fasta"

        uniprot_fasta = urllib.request.urlopen(uniprot_link)
        fasta_sequence = uniprot_fasta.readlines()#.decode('utf-8')
        fasta_sequence = fasta_sequence[1:]
        fasta_sequence = list(f.decode('utf-8') for f in fasta_sequence)
        fasta_sequence = ''.join(fasta_sequence)
        fasta_sequence = fasta_sequence.replace('\n','')

        fasta_dict[prot_id] = fasta_sequence
        uniprot_fasta.close()

    return fasta_dict

def search_motif(sequences):
    """
    create dictionary with protein ids and motif positions of N{P}[ST]{P} +overlapping matches
    Input: dictionary of protein ids and sequences
    """
    motif = re.compile(r'(?=(N[^P](S|T)[^P]))')  #N{P}[ST]{P}
    motif_index = {}

    for key,value in sequences.items():
        match_motif = re.finditer(motif, value)
        motif_start_list = []

        for i in match_motif:
            motif_start_list.append(str(i.start()+1))
        motif_index[key] = ' '.join(motif_start_list)
    return motif_index

def print_motif(motifs):
    #print protein ids that have motifs present and print position of the motifs.
    #input is dictionary of protein id and motifs
    for key, value in motifs.items():
        if len(value) > 1:
            print(key)
            print(value)
    return

if __name__ == "__main__":
    protein_ids = read_dataset(argv[1])
    protein_id_list = split_dataset(protein_ids)
    protein_sites = open_uniprotsite(protein_id_list)
    motifs = search_motif(protein_sites)
    print_motif(motifs)
