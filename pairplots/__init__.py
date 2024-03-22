# This must be imported as early as possible to prevent
# library linking issues caused by numpy/pytorch/etc. importing
# old libraries:
from .julia_import import jl, PairPlots  # isort:skip

from .julia_helpers import jl_array
from .python_interface import *

# This file is created by setuptools_scm during the build process:
from .version import __version__

__all__ = [
    "jl",
    "PairPlots",
    "pairplot",
    "pairplot_interactive",
    "Series",
    "rich",
    "superscript",
    "subscript",
    "latex",
    "save",
    "__version__",
]
