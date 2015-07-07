import sys


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
    while index < (len(concat_list) - 2):

        word_pair = (concat_list[index], concat_list[index + 1])
        #print word_pair
        if word_pair in bi_gram_dictionary:      
            bi_gram_dictionary[word_pair].append(concat_list[i + 2])
            #print bi_gram_dictionary[word_pair]
        else:
            bi_gram_dictionary[word_pair] = [concat_list[i + 2]]
            #print word_pair
        index += 1

    print bi_gram_dictionary
    # for tri-grams in source_text:
    #     i = 0
    #     create values that are sets of single words that follow established bi-grams
    #     word by word, index by index
    #     i += 0


    original_text.close()

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
