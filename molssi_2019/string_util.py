"""
string_util.py
A funny repo for the 2019 MolSSI bootcamp

Misc. string processing functions
"""


def title_case(sentence):
    """
    Convert string to title case.

    Title case means thtat the first character of every word is capitalized.
    otherwise lowercase

    Parameters
    ---------
    sentence: string
        String to be converted to title case
    """
    if not isinstance(sentence, str):
        raise TypeError('sentence {} not a string'.format(sentence))

    if len(sentence) == 0:
        raise ValueError('len(sentence) is zero')

    return ' '.join([word[0].upper() + word[1:].lower() for word in sentence.split()])
