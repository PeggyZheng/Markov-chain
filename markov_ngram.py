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
#    while index < (len(concat_list) - 2):
        word_set = []
        for element in range(number):
            word_set.append(concat_list[element + index])
        word_set = tuple(word_set)    

        #word_set = (concat_list[index], concat_list[index + 1])
        if word_set in bi_gram_dictionary:      
            bi_gram_dictionary[word_set].append(concat_list[index + number])
        else:
            bi_gram_dictionary[word_set] = [concat_list[index + number]]


    original_text.close()
    return bi_gram_dictionary

#print make_chains("gettsburg.txt", 3)
#print make_chains("green-eggs.txt", 4)
#print make_chains("gettsburg.txt", 4)

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    random_string = ""
    starting_point = random.choice(chains.keys())
    step = len(starting_point)
    print step

    for word in starting_point:
        random_string = random_string + " " + word
    print random_string

    #random_string = random_string + starting_point[0].title() + " "
    #print starting_point
    #print random_string
    tuple_value = starting_point
    ending_punctuation = ["!", "?", "."]

    while random_string[-1] not in ending_punctuation:
    #!= "!" and random_string[-1] != "." and random_string[-1] \
    #    != "?":
        value_list = chains[tuple_value]
        random_word = random.choice(value_list)
        random_string = random_string + " " + random_word
        
        for word in tuple_value[-step: 0]:

        tuple_value = (tuple_value[-step: 0], random_word)

    return random_string

#a = make_chains("green-eggs.txt")

#make_text(a)

b = make_chains("green-eggs.txt", 4)
print b
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
