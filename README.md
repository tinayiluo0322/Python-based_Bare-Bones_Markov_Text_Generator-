[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)
## Python-based Bare-Bones Markov Text Generator 

The python code in this project is for building a Markov language model. Below is a summary of how the model is constructed and how it works:

1. **Tokenizing and Preprocessing:**
   - The code first imports necessary libraries, including `Counter` for counting occurrences and `random` for random selections.
   - It also imports the Natural Language Toolkit (`nltk`) but comments out the download commands for the "gutenberg" and "punkt" datasets, which are used for natural language processing. You may need to uncomment and run these lines if you haven't already downloaded them.

2. **N-grams Creation:**
   - The `n_test` function takes a sentence and an integer `n` as input and returns the last `n-1` words in the sentence as an n-gram.
   - The `n_grams` function creates n-grams (tuples of words) from a given corpus, where `n` specifies the n-gram size.
   - The `n_grams_count` function counts the occurrences of each n-gram in the provided n-gram model and returns a dictionary with n-grams as keys and their counts as values.

3. **N-grams Dictionary Creation:**
   - The `n_grams_dic` function constructs a dictionary where the keys are the last words of n-grams, and the values are the counts of those n-grams. This dictionary is constructed based on a test n-gram provided as input.

4. **Selecting Next Word:**
   - The `select_next` function chooses the next word to append to a sentence based on the highest frequency word in the n-grams dictionary.
   - The `random_select_next` function performs a weighted random selection of the next word from the n-grams dictionary. This function is used when the `randomize` parameter is set to `True`.

5. **Producing N-grams Dictionary:**
   - The `produce_dictionary` function combines the previous steps to produce an n-grams dictionary for a given sentence, n-gram size (`n`), and corpus.

6. **Back-off and Recursive Dictionary Generation:**
   - The `back_off` function implements a back-off strategy. It starts with an n-grams dictionary of size `n`, and if it's empty, it recursively calls itself with a smaller n-gram size until it finds a non-empty dictionary.

7. **Generating Sentences:**
   - The `finish_sentence` function generates sentences using the constructed language model.
   - It starts with an initial sentence, specified n-gram size (`n`), and corpus.
   - While the last word in the sentence is not a sentence-ending punctuation (".", "?", "!") and the sentence length is less than 10 words, it keeps selecting and appending words to the sentence.
   - The selection of the next word can be deterministic (`select_next`) or random (`random_select_next`) based on the `randomize` parameter.

In summary, this code builds a simple Markov language model that can generate sentences based on the statistical patterns of n-grams in a given corpus. It allows for both deterministic and randomized word selection and implements a back-off strategy to handle cases where certain n-grams are not found in the model. The resulting model can be used for text generation tasks, including on diverse news and literature datasets to generate AI-authored content.
