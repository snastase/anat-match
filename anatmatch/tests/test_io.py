"""
Tests for anatmatch.io
"""

from functools import reduce
import os.path as op
from anatmatch import io
from anatmatch.tests import get_test_data_path

DATASETS = [
    op.join(get_test_data_path(), 'attention'),
    op.join(get_test_data_path(), 'life')
]

EXPECTED_T1S = [
    12, 19
]


def test_get_T1w():
    for dset, num_t1s in zip(DATASETS, EXPECTED_T1S):
        t1s = io.get_T1w(op.join(get_test_data_path(), dset))
        assert len(t1s) == num_t1s


def test_pairwise_combo():
    pairs = io.pairwise_combo(*DATASETS)
    assert len(pairs) == reduce(lambda x, y: x * y, EXPECTED_T1S)
