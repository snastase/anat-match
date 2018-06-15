"""
Package information for anatmatch
"""

__version__ = '0.1'

NAME = 'anatmatch'
MAINTAINER = 'Sam Nastase'
EMAIL = 'sam.nastase@gmail.com'
VERSION = __version__
LICENSE = 'Apache 2.0'
DESCRIPTION = 'A toolbox for matching anatomical T1w images'
URL = 'http://github.com/snastase/anat-match'

DOWNLOAD_URL = (
    'https://github.com/snastase/anat-match/archive/{ver}.tar.gz'.format(
        ver=__version__))

INSTALL_REQUIRES = [
]

TESTS_REQUIRE = [
    'pytest'
]

PACKAGE_DATA = {
}
