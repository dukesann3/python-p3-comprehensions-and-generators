#!/usr/bin/env python3

def return_evens(num_list):
    evens_list = [i for i in num_list if i % 2 == 0]
    return evens_list


def make_exclamation(sentence_list):
    new_sentence_list = [sentence+"!" for sentence in sentence_list if sentence != ""]
    return new_sentence_list