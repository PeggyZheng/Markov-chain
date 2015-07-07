import sys
import random


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    original_text = open(corpus)
    source_text = []
    concat_list = []

    for line in original_text:
        split_text = line.rstrip().split(" ")
        source_text.append(split_text)
    i = 0
    for item in source_text:
        concat_list = concat_list + source_text[i]
        i += 1

    bi_gram_dictionary = {}
    index = 0

    for index in range(len(concat_list) - 2):
#    while index < (len(concat_list) - 2):
        word_pair = (concat_list[index], concat_list[index + 1])
        if word_pair in bi_gram_dictionary:      
            bi_gram_dictionary[word_pair].append(concat_list[index + 2])
        else:
            bi_gram_dictionary[word_pair] = [concat_list[index + 2]]


    original_text.close()
    return bi_gram_dictionary


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    random_string = ""
    starting_point = random.choice(chains.keys())
    random_string = random_string + starting_point[0].title() + " " + starting_point[1]
    pair = starting_point
    ending_punctuation = ["!", "?", "."]

    while random_string[-1] not in ending_punctuation:
    #!= "!" and random_string[-1] != "." and random_string[-1] \
    #    != "?":
        value_list = chains[pair]
        random_word = random.choice(value_list)
        random_string = random_string + " " + random_word
        pair = (pair[1], random_word)

    return random_string

#a = make_chains("green-eggs.txt")

#make_text(a)

b = make_chains("gettsburg.txt")
print make_text(b)

# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "Some text"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
