"""
Main code
"""
from collections import Counter
import random

#import nltk

# nltk.download("gutenberg")
# nltk.download("punkt")


# choose the last n-1 words in the test sentence as n_gram
def n_test(sentence, n):
    # max_capacity = len(sentence) + 1
    # if max_capacity < n:
    # raise ValueError("Invalid n")
    n_text = sentence[len(sentence) - (n - 1) :]
    return n_text


# get the n_gram token model from the training test
def n_grams(n, corpus):
    n_grams_model = [tuple(corpus[i : i + n]) for i in range(len(corpus) - n + 1)]
    return n_grams_model


# get the count n_gram token model from the training test
def n_grams_count(n_grams):
    count_model = Counter(n_grams)
    return count_model


# Create n_gram dictionary
def n_grams_dic(n_grams_count, n_test):
    dic = {}
    # print(n_grams_count)
    # print(n_test)
    for a, b in n_grams_count.items():  # for each tuple element in n_gram_count
        # print("true", a[-1], a[: len(a) - 1])
        if (
            tuple(n_test) == a[: len(a) - 1]
        ):  # if the last n-1 words in the test sentence is the same as all the element except the last one of the first element in the tuple element
            # print(a[-1], b)
            dic[
                a[-1]
            ] = b  # append a key (last element of the n_gram token) and a value (number of key) to the dictionary
    return dic


# generate the highest frequency word as the next word to append to the sentence
def select_next(n_grams_dic):
    # print(n_grams_dic)
    max_key = max(
        n_grams_dic, key=n_grams_dic.get
    )  # get the key with the maximum value in the n_grams dictionary
    # max_key = max(n_grams_dic, key=lambda key: n_grams_dic[key])
    next_word = max_key  # the next word would be the key
    # print("next word", next_word)
    return next_word


# generate the highest frequency word as the next word to append to the sentence when randomnize==True
def random_select_next(n_grams_dic):
    # Select a random key with the calculated weights
    random_next_word = random.choices(
        list(n_grams_dic.keys()), weights=list(n_grams_dic.values()), k=1
    )[
        0
    ]  # Access the first (and only) element of the list

    return random_next_word


# Combine steps to produce n-gram dictionary into one function
def produce_dictionary(sentence, n, corpus):
    n_test_result = n_test(sentence, n)
    n_grams_result = n_grams(n, corpus)
    n_grams_count_result = n_grams_count(n_grams_result)
    n_grams_dic_result = n_grams_dic(n_grams_count_result, n_test_result)
    return n_grams_dic_result


def back_off(dic, n, sentence, corpus):
    # Base case: If n is less than 1, return an error value (e.g., None)
    if n < 1:
        return None

    # Base case: If n is 1, return the result of produce_dictionary
    elif n == 1:
        return produce_dictionary(sentence, n, corpus)

    # Recursive case: If produce_dictionary is empty, recursively call with n-1
    elif dic == {}:
        return back_off(
            produce_dictionary(sentence, n - 1, corpus), n - 1, sentence, corpus
        )

    else:
        return produce_dictionary(sentence, n, corpus)


def finish_sentence(sentence, n, corpus, randomize=False):
    while sentence[-1] not in [".", "?", "!"] and len(sentence) < 10:
        produce_dictionary_result = produce_dictionary(sentence, n, corpus)
        back_off_result = back_off(produce_dictionary_result, n, sentence, corpus)
        if randomize == True:
            # Perform weighted random selection using random.choices
            select_result = random_select_next(back_off_result)
        else:
            select_result = select_next(back_off_result)

        sentence.append(select_result)

    return sentence
