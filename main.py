"""Main functions"""

import string as stri

def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    string = string.replace(' ', '')
    string = string.lower()
    for simbolo in stri.punctuation:
        string = string.replace(simbolo, '')
    for indice, _caractere in enumerate(string):
        if string[indice] != string[-indice-1]:
            return False

    return True
