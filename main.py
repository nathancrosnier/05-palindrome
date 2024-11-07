"""
Palindromes
"""
import string
from unidecode import unidecode
#### Fonction secondaire


def ispalindrome(p):
    """
    Permet de savoir 
    """
    p = unidecode(p.replace(" ", "")).lower()
    p = p.translate(str.maketrans("", "", string.punctuation))
    return p == p[::-1]

#### Fonction principale


def main():
    """
    Test de la fonction
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
