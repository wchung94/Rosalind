#!/usr/bin/env python3
"""
Author: Wing Yu Chung

Complementing a Strand of DNA.
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


def str_lst_to_int_lst(lst):
    """
    Turns list string to int string
    """
    int_lst = list(map(int, lst))
    return(int_lst)


def write_to_txt(string):
    text_file = open("answer.txt", "w")
    text_file.write(string)
    text_file.close()
    return

def dominant_probability(popu_lst):
    k = popu_lst[0]
    m = popu_lst[1]
    n = popu_lst[2]
    total_pop = sum(popu_lst)

    k_p = 1
    m_p_D = 1/2
    m_p_R = 1 - m_p_D
    n_p = 0



    k_prob = k_p * (k/total_pop)
    D_m_prob = m_p_D*(m/total_pop)

    R_m_prob = m_p_R*(m/total_pop) * ( (k/(total_pop-1)) + (((m-1)/(total_pop-1))*m_p_D) )

    n_prob = (n/total_pop) *  ( (k/(total_pop-1)) + ((m/(total_pop-1))*m_p_D ))

    dom_prob = [k_prob,D_m_prob,R_m_prob,n_prob]

    return sum(dom_prob)



if __name__ == "__main__":
    sequences = read_dataset(argv[1])
    print(sequences)
    sequences_lst = split_dataset(sequences)
    sequences_lst = str_lst_to_int_lst(sequences_lst)
    print(sequences_lst)
    dominant_gene_prob= dominant_probability(sequences_lst)
    print(dominant_gene_prob)
