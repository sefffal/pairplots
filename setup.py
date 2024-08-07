import os
import re

from setuptools import setup

if os.path.exists(".git"):
    kwargs = {
        "use_scm_version": {
            "write_to": "pairplots/version.py",
        },
        "setup_requires": ["setuptools", "setuptools_scm"],
    }
else:
    # Read from pyproject.toml directly

    with open(os.path.join(os.path.dirname(__file__), "pyproject.toml")) as f:
        data = f.read()
        # Find the version
        version = re.search(r'version = "(.*)"', data).group(1)

    with open(os.path.join(os.path.dirname(__file__), "pairplots", "juliapkg.json")) as f:
        data = f.read()
        # Find the version
        backend_version = re.search(r'"version":\s+"\W*(.*)"', data).group(1)

    # Write the version to version.py
    with open(os.path.join(os.path.dirname(__file__), "pairplots", "version.py"), "w") as f:
        f.write(f'__version__ = "{version}"\n')
        f.write(f'__pairplots_jl_version__ = "{backend_version}"\n')

    kwargs = {
        "use_scm_version": False,
        "version": version,
    }


# Build options are managed in pyproject.toml
setup(**kwargs)

if os.path.exists(".git"):
    # Write the version to version.py
    with open(os.path.join(os.path.dirname(__file__), "pairplots", "juliapkg.json")) as f:
        data = f.read()
        # Find the version
        backend_version = re.search(r'"version":\s+"\W*(.*)"', data).group(1)
    with open(os.path.join(os.path.dirname(__file__), "pairplots", "version.py"), "a") as f:
        f.write(f'__pairplots_jl_version__ = "{backend_version}"\n')
