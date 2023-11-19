from lib.vowel_remover import *

def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."

# Test to remove all vowels from a string

def test_remove_vowel_from_string_of_vowels_return_empty_string():
    remover = VowelRemover("aeiou")
    assert remover.remove_vowels() == ""