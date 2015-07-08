import sys
import random


def make_chains(corpus, number):
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

    for index in range(len(concat_list) - number):
        word_set = []
        for element in range(number):
            word_set.append(concat_list[element + index])
        word_set = tuple(word_set)    

        if word_set in bi_gram_dictionary:      
            bi_gram_dictionary[word_set].append(concat_list[index + number])
        else:
            bi_gram_dictionary[word_set] = [concat_list[index + number]]


    original_text.close()
    return bi_gram_dictionary

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    random_string = ""
    starting_point = random.choice(chains.keys())
    step = len(starting_point)

    for word in starting_point[1:]:
        random_string = random_string + " " + word

    random_string = starting_point[0].title() + random_string
    tuple_key = starting_point
    ending_punctuation = ["!", "?", "."]

    while random_string[-1] not in ending_punctuation:

        value_list = chains[tuple_key]
        random_word = random.choice(value_list)
        
        random_string = random_string + " " + random_word

        tuple_key = tuple_key[-(step - 1):] + (random_word,)

    return random_string

b = make_chains("gettsburg.txt", 2)
#print b
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
