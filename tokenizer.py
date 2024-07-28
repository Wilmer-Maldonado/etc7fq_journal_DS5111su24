import string
import logging

# add logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def clean_text(text: str) -> str:
    # checks input is str
    assert isinstance(text, (str)), "clean_text input must be a string"
    # make text all lowercase
    text = text.lower()
    # make translator to remove punctuation from strings
    translator = str.maketrans("", "", string.punctuation)
    # apply translator to text
    cleaned_text = text.translate(translator)
    # checks cleaned_text is still str
    assert isinstance(cleaned_text, (str))
    logging.debug("clean_text return is str type")
    # return text with no punctuation
    return cleaned_text


def tokenize(text: str) -> list[str]:
    # checks input is str
    assert isinstance(text, (str)), "tokenize input must be a string"
    # remove punctuation from text
    cleaned_text = clean_text(text)
    # makes text into split list of words
    list_words = cleaned_text.split()
    # checks list_words is now list
    assert isinstance(list_words, (list))
    logging.debug("tokenize return is list type")
    # returns list of words
    return list_words


def count_words(text: str) -> dict:
    # checks input is str
    assert isinstance(text, (str)), "count_words input must be a string"
    # split text into list of words
    all_words = tokenize(text)
    # track word counts in list all_words
    all_word_counts = {}
    for word in all_words:
        all_word_counts[word] = all_word_counts.get(word, 0) + 1
    logging.info(
        f"""Analyzed list of words:\n{all_words}
                 \ninto these counts\n\n{all_word_counts}"""
    )
    # checks all_word_counts is now dictionary
    assert isinstance(all_word_counts, (dict))
    logging.debug("count_words return is dict type")
    # return dictionary of word counts
    return all_word_counts


def main():
    text = """HeLlo WorLD! hello WorlD@, 
    'Monty PYTHON' is the best best best movie. Correct?"""
    print(f"clean_text output:\n{clean_text(text)}\n")
    print(f"tokenize output:\n{tokenize(text)}\n")
    print(f"cout_words output:\n{count_words(text)}\n")


if __name__ == "__main__":
    main()
