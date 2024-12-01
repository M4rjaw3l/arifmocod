from math import gcd
from collections import defaultdict

class Simbol:
    def __init__(self, letter):
        self.letter = letter
        self.repetition = 1
        self.segment_start = 0
        self.segment_end = 1


def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def build_border(simbols_lines, denominator, rep_sum):
    nod_val = nod(nod(simbols_lines[0].segment_start, simbols_lines[-1].segment_end), denominator)
    simbols_lines[0].segment_start //= nod_val
    simbols_lines[-1].segment_end //= nod_val
    denominator //= nod_val

    denominator *= rep_sum
    simbols_lines[0].segment_start *= rep_sum
    simbols_lines[-1].segment_end *= rep_sum

    unit_segment = (simbols_lines[-1].segment_end - simbols_lines[0].segment_start) // rep_sum

    simbols_lines[0].segment_end = simbols_lines[0].segment_start + unit_segment * simbols_lines[0].repetition
    for i in range(1, len(simbols_lines)):
        simbols_lines[i].segment_start = simbols_lines[i - 1].segment_end
        simbols_lines[i].segment_end = simbols_lines[i].segment_start + unit_segment * simbols_lines[i].repetition

    return denominator


def main():
    text = input("Enter text: ")
    simbols_line = []

    for letter in text:
        found = False
        for simbol in simbols_line:
            if simbol.letter == letter:
                simbol.repetition += 1
                found = True
                break
        if not found:
            simbols_line.append(Simbol(letter))

    # Bubble sort by repetition
    n = len(simbols_line)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if simbols_line[j].repetition > simbols_line[j + 1].repetition:
                simbols_line[j], simbols_line[j + 1] = simbols_line[j + 1], simbols_line[j]
                swapped = True
        if not swapped:
            break

    denominator = 1
    rep_sum = len(text)

    for simbol in simbols_line:
        #print(f"{simbol.letter} {simbol.repetition}")
        print(f"Pi: {simbol.letter}, {simbol.repetition}/{len(text)}")

    print()
    for letter in text:
        denominator = build_border(simbols_line, denominator, rep_sum)
        #print(f"{simbols_line[0].segment_start}/{denominator} {simbols_line[-1].segment_end}/{denominator}")

        for simbol in simbols_line:
            if simbol.letter == letter:
                simbols_line[0].segment_start = simbol.segment_start
                simbols_line[-1].segment_end = simbol.segment_end
        print(f"Letter: {letter}, {simbols_line[0].segment_start}/{denominator} {simbols_line[-1].segment_end}/{denominator}")

    #print(f"{simbols_line[0].segment_start}/{denominator} {simbols_line[-1].segment_end}/{denominator}")


if __name__ == "__main__":
    main()
