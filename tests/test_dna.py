from genomics_demo.dna import DNA
import pytest


def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        DNA('ATB')


def test_complementary_sequence_works():
    assert DNA('GTC').complement == DNA('CAG')
    assert DNA('ATC').complement == DNA('TAG')


def test_gc_content():
    assert DNA('ATTTATGGCC').gc_content == 0.4
    assert DNA('AGGTATGGCC').gc_content == 0.6
    assert DNA('ATAT').gc_content == 0


def test_triplets():
    assert DNA('AAA').split_DNA_triplets == ['AAA']
    assert DNA('AAATTTGGG').split_DNA_triplets == ['AAA','TTT','GGG']
    assert DNA('AAAT').split_DNA_triplets == ['AAA','T']


def test_find_start():
    assert DNA('ATGGG').find_first_start_site == 0
    assert DNA('CCCCATG').find_first_start_site == 4
    with pytest.raises(TypeError):
        DNA('GGG').find_first_start_site()


def test_find_start_codons():
    """New test to test the function to find start codons"""
    assert DNA('ATGGTACATGCGA').find_start_codons() == [0, 7]


def test_transcribe():
    assert DNA('GTC').transcribe() == 'GAC'
    assert DNA('ATC').transcribe() == 'GAU'
