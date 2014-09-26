"""
Settings used by funkyroad project.

This consists of the general produciton settings, with an optional import of any local
settings.
"""

# Import production settings.
from funkyroad.settings.production import *

# Import optional local settings.
try:
    from funkyroad.settings.local import *
except ImportError:
    pass