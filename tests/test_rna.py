from genomics_demo.rna import RNA
import pytest

def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        RNA('ATB')

def test_complimentary_sequence_works():
    assert RNA('GUC').complimentary_sequence == RNA('CAG')
    assert RNA('AUC').complimentary_sequence == RNA('UAG')

def test_motifs_works():
    assert RNA('GAUGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA').type_rna() == 'polyA tail mRNA'
    assert RNA('AUCAUCAUCAUCGAGAGUA').type_rna() == 'clover leaf loop tRNA'
    assert RNA('UCAUCAAGUGC').type_rna() == 'microRNA'
    assert RNA('AUCAUCAUCAUCGAGAGUAUCAUCAAGUGC').type_rna() == 'clover leaf loop tRNA'

def test_get_aa_sequence():
    assert RNA('UUUUUCUUAU').get_aa_sequence() == 'Phe-Phe-Leu'
    assert RNA('GCCACCUAG').get_aa_sequence() == 'Ala-Thr-Stop'
