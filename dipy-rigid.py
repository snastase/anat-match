#!/usr/bin/env python

from os.path import join
from glob import glob
import nibabel as nib
from dipy.viz import regtools
from dipy.align.imaffine import (AffineMap,
                                 MutualInformationMetric,
                                 AffineRegistration)
from dipy.align.transforms import RigidTransform3D
from nilearn.image import new_img_like
from scipy.stats import pearsonr

def resample_moving(fixed, moving):
    identity = np.eye(4)
    affine_map = AffineMap(identity,
                           fixed.shape, fixed.affine,
                           moving.shape, moving.affine)
    resampled = affine_map.transform(moving.get_data())
    return resampled

def rigid_registration(fixed, moving, metric=MutualInformationMetric(), **kwargs):
    affreg = AffineRegistration(metric=metric, **kwargs)
    rigid = affreg.optimize(fixed.get_data(), moving.get_data(),
                            RigidTransform3D(), None,
                            fixed.affine, moving.affine)
    transformed = rigid.transform(moving.get_data())
    # convert transformed to full nibabel image, just data now
    # TODO: get affine for transformed from rigid.affine?
    transformed = new_img_like(moving, transformed)
    return transformed
    
def correlation_metric(fixed, moving):
    correlation = pearsonr(fixed.get_data().ravel(),
                           moving.get_data().ravel())[0]
    return correlation

# Try out on a sample subject across two datasets
fixed = nib.load(glob(join('haxby', 'life', 'sub-rid000041', 'anat', '*T1w.nii.gz'))[0])
moving = nib.load(glob(join('haxby', 'attention', 'sub-rid000041', 'anat', '*T1w.nii.gz'))[0])

# Resample moving image if different geometry
if moving.shape != fixed.shape:
    moving = resample(fixed, moving)

# Transform moving into to the target fixed image
transformed = rigid_registration(fixed, moving,
                                 level_iters=[100, 10, 5],
                                 sigmas=[3.0, 1.0, 0.0],
                                 factors=[4, 2, 1])

# Evaluate before and after correlation of images
pre = correlation_metric(fixed, moving)
post = correlation_metric(fixed, transformed)
print(("Pre-alignment correlation: {0} \n" +
       "Post-alignment correlation: {1}").format(
        pre, post))

# Visualize the before/after images
regtools.overlay_slices(fixed.get_data(), moving.get_data(), None, 2,
                        "Fixed", "Moving")
regtools.overlay_slices(fixed.get_data(), transformed.get_data(), None, 2,
                        "Fixed", "Transformed")