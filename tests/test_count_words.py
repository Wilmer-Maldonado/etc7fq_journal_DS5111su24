import sys
import os
import subprocess

repo_path = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(1, repo_path)

from tokenizer import count_words
import pytest


def test_count_words_type():
    # Given: sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: count_words method is called on sample text
    output = count_words(sample_text)
    # Then: Verify Output is a dict
    assert isinstance(output, dict), f"Output is not a dictionary, but {type(output)}"


@pytest.mark.xfail
def test_count_words_type_error():
    # Given: sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: count_words method is called on sample text
    output = count_words(sample_text)
    # Then: Verify Output is a list - expect error
    assert isinstance(output, list)


def test_count_words_key_type():
    # Given: sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: count_words method is called on sample text
    output = count_words(sample_text)
    # Then: Verify Output dict's keys are only type strings
    assert all(
        isinstance(word, str) for word in output.keys()
    ), "All keys in output dict should be strings"


@pytest.mark.xfail
def test_count_words_key_type_error():
    # Given: sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: count_words method is called on sample text
    output = count_words(sample_text)
    # Then: Verify Output dict's keys are only type int - expect error
    assert all(isinstance(word, int) for word in output.keys())


def test_count_words_value_type():
    # Given: sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: count_words method is called on sample text
    output = count_words(sample_text)
    # Then: Verify Output dict's values are only type int
    assert all(
        isinstance(count, int) for count in output.values()
    ), "All values in output dict should be integers"


@pytest.mark.xfail
def test_count_words_value_type_error():
    # Given: sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: count_words method is called on sample text
    output = count_words(sample_text)
    # Then: Verify Output dicts's values are only type str- expect error
    assert all(isinstance(count, str) for count in output.values())


def test_count_words_full_match():
    # Given: sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: count_words method is called on sample text
    output = count_words(sample_text)
    # Then: Verify Output and Expected Match: dictionary with word counts
    expected_output = {
        "but": 1,
        "the": 2,
        "raven": 1,
        "sitting": 1,
        "lonely": 1,
        "on": 1,
        "placid": 1,
        "bust": 1,
        "spoke": 1,
        "only": 1,
        "that": 2,
        "one": 2,
        "word": 2,
        "as": 1,
        "if": 1,
        "his": 1,
        "soul": 1,
        "in": 1,
        "he": 1,
        "did": 1,
        "outpour": 1,
    }
    # Assertion Flags
    assert (
        output == expected_output
    ), "The test output and expected dictionary did not have matching word counts"


@pytest.mark.xfail
def test_count_words_full_match_error():
    # Given: sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: count_words method is called on sample text
    output = count_words(sample_text)
    # Then: Verify Output and Expected Match: dictionary with word counts - expect error for word 'but'
    expected_output = {
        "but": 3,
        "the": 2,
        "raven": 1,
        "sitting": 1,
        "lonely": 1,
        "on": 1,
        "placid": 1,
        "bust": 1,
        "spoke": 1,
        "only": 1,
        "that": 2,
        "one": 2,
        "word": 2,
        "as": 1,
        "if": 1,
        "his": 1,
        "soul": 1,
        "in": 1,
        "he": 1,
        "did": 1,
        "outpour": 1,
    }
    # Assertion Flags
    assert output == expected_output


# List of text files to test
text_files = ["pg17192.txt", "pg932.txt", "pg1063.txt", "pg10031.txt", "pg14082.txt"]


@pytest.mark.parametrize("file_name", text_files)
def test_count_words_all_files(file_name):
    # Given: The full text of a file
    file_path = os.path.join(repo_path, file_name)
    with open(file_path, "r") as file:
        full_text = file.read()
    # When: clean_text method is called on the full text
    output = count_words(full_text)
    # Then: Verify Output is a dict
    assert isinstance(output, dict), f"Output is not a dictionary, but {type(output)}"
    # Then: Verify Output dict's keys are only type strings
    assert all(
        isinstance(word, str) for word in output.keys()
    ), "All keys in output dict should be strings"
    # Then: Verify Output dict's values are only type int
    assert all(
        isinstance(count, int) for count in output.values()
    ), "All values in output dict should be integers"


def test_running_linux_os():
    # Given OS from sys.platform
    # When linux is not OS
    # Then fail, and send error message
    assert sys.platform == "linux", "Requires running linux"


def test_python_version_at_least_3_8():
    # Given python version from sys.version_info
    # When python not in between version 3.9 and 3.12, tested on each version.
    # Then fail, and send error message
    assert sys.version_info >= (3, 8) and sys.version_info <= (
        3,
        12.4,
    ), "Use python version between 3.8 and 3.12"


def test_count_words_bash_vs_python():
    # Given test string
    test_string = "hello world hello world python world"
    # When using sub process to execute bash command on test_string
    bash_test_hello = f"echo {test_string} | grep -o 'hello' | wc -l"
    bash_output_hello = subprocess.check_output(
        bash_test_hello, shell=True, text=True
    ).strip()
    # When using sub process to execute bash command on test_string
    bash_test_world = f"echo {test_string} | grep -o 'world' | wc -l"
    bash_output_world = subprocess.check_output(
        bash_test_world, shell=True, text=True
    ).strip()
    # When using sub process to execute bash command on test_string
    bash_test_python = f"echo {test_string} | grep -o 'python' | wc -l"
    bash_output_python = subprocess.check_output(
        bash_test_python, shell=True, text=True
    ).strip()
    # Getting the result from the Python function
    python_output = count_words(test_string)
    # Then: Verify both word counts are the same
    assert python_output["hello"] == int(bash_output_hello)
    assert python_output["world"] == int(bash_output_world)
    assert python_output["python"] == int(bash_output_python)


def test_count_words_french():
    # Given: French text string
    sample_text = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""
    # When: count words method is called on sample text
    output = count_words(sample_text)
    # Then: Verify Output's dict keys are lowercase, values are integers
    # and output is dict
    assert all([word.islower() for word in output.keys()])  # lowercase
    assert isinstance(output, dict)  # output is dict
    assert all(type(count) == int for count in output.values())  # each value is int
    assert output["ce"] == 4
