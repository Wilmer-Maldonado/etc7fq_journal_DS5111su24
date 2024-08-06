import sys
import os
import subprocess

repo_path = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(1, repo_path)

from pkg_etc7fq import clean_text
import pytest
import string


def test_clean_text_type():
    # Given sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: clean_text method is called on sample text
    output = clean_text(sample_text)
    # Then: Verify Output is str
    assert isinstance(
        output, str
    ), f"Output should be a string, but received {type(output)}"


@pytest.mark.xfail(strict=False)
def test_clean_text_type_error():
    # Given sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: clean_text method is called on sample text
    output = clean_text(sample_text)
    # Then: Verify Output is list - expect error
    assert isinstance(output, list)


def test_clean_text_case():
    # Given sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: clean_text method is called on sample text
    output = clean_text(sample_text)
    # Then: Verify Output is all lowercase
    assert output.islower(), "Output should be all lowercase"


@pytest.mark.xfail(strict=False)
def test_clean_text_case_error():
    # Given sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: clean_text method is called on sample text
    output = clean_text(sample_text)
    # Then: Verify Output is all uppercase - expect error
    assert output.isupper()


def test_clean_text_full_match():
    # Given sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: clean_text method is called on sample text
    output = clean_text(sample_text)
    # Then: Verify Output with Expected Match: lowercase/punctuation
    expected_cleaned_text = """but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour"""
    assert (
        output == expected_cleaned_text
    ), f"""The test and expected output did not match exactly, check lowercase/punctuation"""


@pytest.mark.xfail(strict=False)
def test_clean_text_full_match_error():
    # Given sample text
    sample_text = """But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."""
    # When: clean_text method is called on sample text
    output = clean_text(sample_text)
    # Then: Verify Output with Expected Match: lowercase/punctuation - expect error
    expected_cleaned_text = """the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour"""
    assert output == expected_cleaned_text


# List of text files to test
text_files = ["pg17192.txt", "pg932.txt", "pg1063.txt", "pg10031.txt", "pg14082.txt"]


@pytest.mark.parametrize("file_name", text_files)
def test_clean_text_all_files(file_name):
    # Given: The full text of a file
    file_path = os.path.join(repo_path, file_name)
    with open(file_path, "r") as file:
        full_text = file.read()
    # When: clean_text method is called on the full text
    output = clean_text(full_text)
    # Then: Verify output is str
    assert isinstance(
        output, str
    ), f"Output should be a string, but received {type(output)}"
    # Then: Verify output is all lowercase
    assert output.islower(), "Output should be all lowercase"


@pytest.mark.skip(reason="Japanese version not ready yet")
def test_japanese_clean_text_type():
    # Given Japanese Text string
    japanese_test_string = "モンティ・パイソンは良い映画です"
    # When: clean_text method is called  on japanese text
    output = clean_text(japanese_test_string)
    # Then: Verify Output is str
    assert isinstance(
        output, str
    ), f"Output should be a string, but received {type(output)}"


def test_running_linux_os():
    # Given OS from sys.platform
    # When linux is not OS
    # Then fail, and send error message
    assert sys.platform == "linux", "Requires running linux"


def test_python_version_at_least_3_8():
    # Given python version from sys.version_info
    # When python version in between 3.8 and 3.12, tested on each version.
    # Then fail, and send error message
    assert sys.version_info >= (3, 8) and sys.version_info <= (
        3,
        12.4,
    ), "Use python version between 3.8 and 3.12"


def test_clean_text_bash_vs_python():
    # Given test string
    test_string = "Hello worlD!"
    # When using sub process to execute bash command on test_string
    bash_test = f"echo {test_string} | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]'"
    bash_output = subprocess.check_output(bash_test, shell=True, text=True).strip()
    # Getting the result from the Python function
    python_output = clean_text(test_string)
    # Then: Verify both outputs are the same
    assert (
        python_output == bash_output
    ), "bash and python outputs on test string do not match"


def test_clean_text_french():
    # Given: French text string
    sample_text = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""
    # When: clean_text method is called on sample text
    output = clean_text(sample_text)
    # Then: Verify Output is lowercase, a string
    # and removed all punctuation
    assert output.islower()  # lowercase
    assert isinstance(output, str)  # string
    assert not any(i in string.punctuation for i in output)  # no punctuation
