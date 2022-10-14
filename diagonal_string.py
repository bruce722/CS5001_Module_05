"""
    CS5001-5003 Fall 2022
    Lab 04 -- Coding Practice 5-- Problem 3, diagonal string
    (Bruce) Chuanzhao Huang / 
"""


def diagonal_string(word):
    index = 0
    letter = ""
    if len(word) > 0:
        while index < len(word):
            if index == len(word) - 1:
                letter = letter + " " * index + word[index]
            else:
                letter = letter + " " * index + word[index] + "\n"
            index += 1
    return letter


if __name__ == "__main__":
    diagonal_string("")
