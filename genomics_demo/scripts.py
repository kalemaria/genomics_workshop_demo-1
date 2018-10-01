import sys
from dna import DNA


def get_reverse_complement(seq):
    return DNA(seq).compliment()


if __name__ == '__main__':
    seq = sys.argv[1]
    print(get_reverse_complement(seq))
