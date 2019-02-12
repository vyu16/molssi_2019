"""
molssi_2019
A funny repo for the 2019 MolSSI bootcamp
"""

# Make Python 2 and 3 imports work the same
# Safe to remove with Python 3-only code
from __future__ import absolute_import

# Add imports here
from .molssi_math import mean
from .string_util import title_case
from .chop import chop1, chop2

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
