"""
Tests for anatmatch.run
"""

import argparse
import pytest
from anatmatch import run


def test_get_parser():
    parser = run.get_parser()
    assert isinstance(parser, argparse.ArgumentParser)
    datasets = []
    for dset in ['dset1', 'dset2', 'dset3']:
        datasets += dset
        options = parser.parse_args(datasets)
        assert options.datasets == datasets


def test_main():
    with pytest.raises(NotImplementedError):
        run.main()
