"""
    CS5001-5003 Fall 2022
    Lab 04 -- Coding Practice 5-- Problem 2, add spaces
    (Bruce) Chuanzhao Huang / 
"""


def add_spaces(word):
    index = 0
    result = ""
    if len(word) > 0:
        while index < len(word) - 1:
            letter = word[index]
            output = letter + "   "
            result += output
            index += 1
        final_result = result + word[-1]
    else:
        final_result = ""
    return final_result 


if __name__ == "__main__":
    print(add_spaces(""))
