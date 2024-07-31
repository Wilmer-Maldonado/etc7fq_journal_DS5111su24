import sys
import os
import subprocess

repo_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(1,repo_path)

from tokenizer import tokenize
import pytest

def test_tokenize_type():
    # Given: sample text 
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: tokenize method is called on sample text
    output = tokenize(sample_text)
    # Then: Verify Output is type list
    assert isinstance(output, list), f"Output was not a list, but {type(output)}"

@pytest.mark.xfail
def test_tokenize_type_error():
    # Given: sample text 
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: tokenize method is called on sample text
    output = tokenize(sample_text)
    # Then: Verify Output is type str - expect error
    assert isinstance(output, str)

def test_tokenize_type_elements():
    # Given: sample text 
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: tokenize method is called on sample text
    output = tokenize(sample_text)
    # Then: Verify Output list's elements contained only strings
    assert all(isinstance(word, str) for word in output), "All elements in output should be strings"

@pytest.mark.xfail
def test_tokenize_type_elements_error():
    # Given: sample text 
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: tokenize method is called on sample text
    output = tokenize(sample_text)
    # Then: Verify Output list's elements contained int - expect error
    assert all(isinstance(word, int) for word in output)

def test_tokenize_elements_letters_only():
    # Given: sample text 
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: tokenize method is called on sample text
    output = tokenize(sample_text)
    # Then: Verify Output list's elements contained only letters
    assert all(word.isalpha() for word in output), "All elements in output should be strings"

@pytest.mark.xfail
def test_tokenize_elements_letters_only_error():
    # Given: sample text 
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: tokenize method is called on sample text
    output = tokenize(sample_text)
    # Then: Verify Output list's elements contained only numbers - expect error
    assert all(word.isnumeric() for word in output)

def test_tokenize_full_match():
    # Given: sample text 
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: tokenize method is called on sample text
    output = tokenize(sample_text)
    # Then: Verify Output with Expected Match: lowercase words in list
    expected_tokenize_list = ['but', 'the', 'raven', 'sitting', 'lonely', 'on', 'the', 'placid', 'bust', 'spoke', 'only', 'that', 'one', 'word', 'as', 'if', 'his', 'soul', 'in', 'that', 'one', 'word', 'he', 'did', 'outpour']
    assert output == expected_tokenize_list, "The test and expected output did not match exactly"

@pytest.mark.xfail
def test_tokenize_full_match_error():
    # Given: sample text 
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: tokenize method is called on sample text
    output = tokenize(sample_text)
    # Then: Verify Output with Expected Match: lowercase words in list
    expected_tokenize_list = ['But', 'the', 'raven', 'sitting', 'Lonely', 'on', 'the', 'placid', 'bust', 'spoke', 'only', 'that', 'one', 'word', 'as', 'if', 'his', 'soul', 'in', 'that', 'one', 'word', 'he', 'did', 'outpour']
    assert output == expected_tokenize_list

# List of text files to test
text_files = ['pg17192.txt', 
              'pg932.txt', 
              'pg1063.txt', 
              'pg10031.txt', 
              'pg14082.txt']

@pytest.mark.parametrize("file_name", text_files)
def test_tokenize_all_files(file_name):
    # Given: The full text of a file
    file_path = os.path.join(repo_path, file_name)
    with open(file_path, 'r') as file:
        full_text = file.read()
    # When: clean_text method is called on the full text
    output = tokenize(full_text)
    # Then: Verify Output is type list
    assert isinstance(output, list), f"Output was not a list, but {type(output)}"
    # Then: Verify Output list's elements contained only strings
    assert all(isinstance(word, str) for word in output), f"All elements in output should be strings, but received{output}"

def test_running_linux_os():
    # Given OS from sys.platform
    # When linux is not OS
    # Then fail, and send error message
    assert sys.platform == "linux", "Requires running linux"

def test_python_version_at_least_3_9():
    # Given python version from sys.version_info
    # When python not >=3.9
    # Then fail, and send error message
    assert sys.version_info >= (3,9), "Use python version 3.9 or higher"

def test_tokenize_bash_vs_python():
    # Given test string
    test_string ="hello world"
    # When using sub process to execute bash command on test_string
    bash_test = f"echo {test_string} | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]'"
    bash_output = subprocess.check_output(bash_test, shell=True, text=True).strip()
    # Getting the result from the Python function
    python_output = tokenize(test_string)
    # Then: Verify both outputs are the same
    assert python_output  == bash_output.split()



