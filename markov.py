import sys


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    original_text = open(corpus)
    source_text = []
    concat_list = []

#    for line in file_object:
#        new_line = line.rstrip().split("|")
#        houses.add(new_line[2])

    for line in original_text:
        split_text = line.rstrip().split(" ")
        source_text.append(split_text)
    
    for item in source_text:
        i = 0
        concat_list = concat_list + source_text[i]
        i += 1
    print concat_list


    # bi-gram_dictionary = {}
    # for word_pair in source_text:

    #     loop through text two words at a time
    #     create bi-gram keys
    
    # for tri-grams in source_text:
    #     i = 0
    #     create values that are sets of single words that follow established bi-grams
    #     word by word, index by index
    #     i += 0

    # return dictionary

    # close(corpus)

make_chains("green-eggs.txt")

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "Some text"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
