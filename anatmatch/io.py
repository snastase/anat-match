"""
Functions for data io
"""

from itertools import product
import os.path as op
from bids.grabbids import BIDSLayout

EXCLUDE = [
    'sourcedata',
    'derivatives',
    'stimuli',
    'code'
]

TAGS = [
    'session',
    'run',
    'reconstruction',
    'ce'
]


def get_T1w(fpath):
    """
    Returns list of anatomical (T1w) files from ``fpath``

    Parameters
    ----------
    fpath : str
        Filepath to BIDS dataset (or loaded BIDSLayout object)

    Returns
    -------
    imgs : list-of-str
        Filepaths of T1w images
    """

    # exclude everything that isn't the subject data itself
    data = BIDSLayout(op.abspath(fpath), exclude=EXCLUDE)

    # TODO: it'd be great to do this without needing pandas...
    t1s = data.as_data_frame(modality='anat', type='T1w', extensions='.nii.gz')

    # try to get most "minimal" (i.e., fewest tags) T1w image for each subject
    cols = [f for f in TAGS if f in t1s.columns]
    if len(cols) > 0:
        t1s = t1s.sort_values(cols, na_position='first').reset_index(drop=True)
    imgs = t1s.groupby('subject').nth(0).get('path').tolist()

    if len(imgs) == 0:
        raise ValueError(f'There are no viable T1w images in {fpath}. '
                         'Check inputs and try again.')

    return imgs


def pairwise_combo(dset1, dset2):
    """
    Returns all pairwise combination of anatomical images between inputs

    Parameters
    ----------
    dset1, dset2 : str
        Filepath to input dataset

    Returns
    -------
    pairs : list-of-tuple
        Pairs of imgs from different datasets
    """

    return list(product(get_T1w(dset1), get_T1w(dset2)))
