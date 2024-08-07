"Tokenizer Module: Collection of Functions that Process Strings"
import string
import logging
from typing import List

# add logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def clean_text(text: str) -> str:
    """
    Cleans the input text by lowercasing and removing punctuation.

    args:
    text (str): The input text, uncleaned.

    returns:
    str: The cleaned text with no punctuation and in lowercase.
    """
    # checks input is str
    assert isinstance(text, str), "clean_text input must be a string"
    # make text all lowercase
    text = text.lower()
    # make translator to remove punctuation from strings
    translator = str.maketrans("", "", string.punctuation)
    # apply translator to text
    cleaned_text = text.translate(translator)
    # checks cleaned_text is still str
    assert isinstance(cleaned_text, str)
    logging.debug("clean_text return is str type")
    # return text with no punctuation
    return cleaned_text


def tokenize(text: str) -> List[str]:
    """
    Tokenizes the input text by splitting it into a list of words.

    args:
    text (str): The text that will be tokenized.

    returns:
    List[str]: A list of words from the cleaned text.
    """
    # checks input is str
    assert isinstance(text, str), "tokenize input must be a string"
    # remove punctuation from text
    cleaned_text = clean_text(text)
    # makes text into split list of words
    list_words = cleaned_text.split()
    # checks list_words is now list
    assert isinstance(list_words, list)
    logging.debug("tokenize return is list type")
    # returns list of words
    return list_words


def count_words(text: str) -> dict:
    """
    Counts the frequency of each word in the input text.

    args:
    text (str): The text whose word counts will be calculated.

    returns:
    dict: A dictionary where keys are words and values are their respective counts.
    """
    # checks input is str
    assert isinstance(text, str), "count_words input must be a string"
    # split text into list of words
    all_words = tokenize(text)
    # track word counts in list all_words
    all_word_counts = {}
    for word in all_words:
        all_word_counts[word] = all_word_counts.get(word, 0) + 1
    logging.info(
        "Analyzed list of words:\n%s\ninto these counts\n\n%s",
        all_words,
        all_word_counts,
    )
    # checks all_word_counts is now dictionary
    assert isinstance(all_word_counts, dict)
    logging.debug("count_words return is dict type")
    # return dictionary of word counts
    return all_word_counts


def main():
    """
    example usage and outputs of the functions in this module
    """
    text = """But the Ravens sitting lonely on the placid bust,
    spoke only That one word, as if his soul in that one word he did outpour."""
    print(f"clean_text output:\n{clean_text(text)}\n")
    print(f"tokenize output:\n{tokenize(text)}\n")
    print(f"cout_words output:\n{count_words(text)}\n")


if __name__ == "__main__":
    main()
