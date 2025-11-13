"""07-ascii-art
Permet d'encoder une chaîne de caractères sous forme de liste
de tuples (ASCII Art).
"""

# Mandatory for the recursive solution to work on large inputs
import sys
from typing import List, Tuple

sys.setrecursionlimit(2000)


def artcode_i(s: str) -> List[Tuple[str, int]]:
    """Encode une chaîne de caractères en liste de tuples selon
    un algorithme itératif.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        List[Tuple[str, int]]: Liste des tuples (caractère, nombre
        d'occurrences consécutives)
    """
    if not s:
        return []

    chars: List[str] = [s[0]]
    counts: List[int] = [1]

    for char in s[1:]:
        if char == chars[-1]:
            counts[-1] += 1
        else:
            chars.append(char)
            counts.append(1)

    return list(zip(chars, counts))


def artcode_r(s: str) -> List[Tuple[str, int]]:
    """Encode une chaîne de caractères en liste de tuples selon
    un algorithme récursif.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        List[Tuple[str, int]]: Liste des tuples (caractère, nombre
        d'occurrences consécutives)
    """
    if not s:
        return []

    count: int = 1
    while count < len(s) and s[count] == s[0]:
        count += 1

    return [(s[0], count)] + artcode_r(s[count:])

def main() -> None:
    """Fonction principale"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
