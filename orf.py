#!/usr/bin/env python3
"""
Author: Wing Yu Chung
Return unique candidate protein sequences from possible ORFs in any order
"""

# Import statements
from sys import argv
import test


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

def split_dataset_dict(dataset):
    """
    Turns line of strings into dictonary
    
    Input: lines of string
    Output: dictionary of string
    """
    dataset = dataset.split()
    seqs = {}
    for line in dataset:
        if not line.strip(): 
            continue
        if line.startswith('>'):
            label = line.strip()[1:]
            seqs[label] = ""
        else:
            seqs[label] += line.strip()[0:]
    return seqs

def add_rev(seqs):
    """
    Add reverse strand into dictonary
        
    Input: dictionary of string
    Output: dictionary of string and reverse sequence string
    """ 
    rev_key = []
    rev_value = []
    count = 0
    for key,value in seqs.items():
        rev_key.append(key +'_rev')
        rev_value.append(value[::-1])
    
    for key in rev_key:
        seqs[key] = rev_value[count]   
        count+=1
        
    return seqs

def complementary_rev(seqs):
    """
    turn reverse strand in dictonary into complementary
        
    Input: dictionary of string
    Output: dictionary of string and complementary reverse sequence string
    """ 
    for key,value in seqs.items():
        if key.endswith('_rev'):
            comp_seq = ""
            for nuc in seqs[key]:
                if nuc == "A":
                    nuc = "T"
                    comp_seq += nuc
                elif nuc == "T":
                    nuc = "A"
                    comp_seq += nuc
                elif nuc == "G":
                    nuc = "C"
                    comp_seq += nuc
                elif nuc == "C":
                    nuc = "G"
                    comp_seq += nuc
            seqs[key] = comp_seq
    return seqs
 
def orf_list(seqs):
    """
    Create a list with all the possible reading frames
        
    Input: dictionary with sequences
    Output: List with reading frames for each sequence
    """ 
    orflist = []
    
    for value in seqs.values():
        i = 0
        while i < 3:
            orflist.append(value[i:])
            i += 1
    return orflist

def translate_orf(seqs):
    """
    Translate the reading frames into protein sequences
        
    Input: list of dna sequences
    Output: list of translated dna sequences in protein sequences
    """ 
    prot_list = []
     
    for orf in seqs:
       amino = ''
       length = 0
       i = 0
       while length < (len(orf)/3 ):
           if orf[i:i+3] in AMINO_ACID_DICT.keys():
               amino += AMINO_ACID_DICT[orf[i:i+3]]
           i += 3
           length += 1
       prot_list.append(amino)    
    return prot_list


def extract_orf(seqs):
    """
    Extract the unqie ORFs from the reading frames starting from startcodon to stopcodon
        
    Input: list of protein sequences
    Output: list of unique ORF protein sequences
    """ 
    start_orfs = []
    orfs = []
    startcodon = "M"
    stopcodon = "_"
    
    for orf in seqs:
        count = 0
        for start_nuc in orf:
            if start_nuc == startcodon:
                start_index = count
                #start_index = orf.index(start_nuc) why does this not work?
                start_orfs.append(orf[start_index:])
            count +=1

    for orf in start_orfs:
        for stop_nuc in orf:
            if stop_nuc == stopcodon:
                stop_index = orf.index(stopcodon)
                orfs.append(orf[:stop_index])
    orfs = set(orfs)

    return orfs


if __name__ == "__main__":
    sequences = read_dataset(argv[1])
    seqdict = split_dataset_dict(sequences)
    seqdict = add_rev(seqdict)
    seqdict = complementary_rev(seqdict)
    orflist = orf_list(seqdict)
    protlist = translate_orf(orflist)
    orfs_output = extract_orf(protlist)
    for i in orfs_output:
        print(i)
