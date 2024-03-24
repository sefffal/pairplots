<img src="https://github.com/sefffal/PairPlots.jl/raw/master/docs/src/assets/logo.png" width=100> 

# PairPlots.py


*Beautiful and flexible vizualizations of high dimensional data*

[![](https://img.shields.io/badge/docs-dev-blue.svg)](https://sefffal.github.io/PairPlots.jl/dev/)
![Build status](https://github.com/sefffal/PairPlots.jl/actions/workflows/ci.yml/badge.svg)
[![Package Downloads](https://shields.io/endpoint?url=https://pkgs.genieframework.com/api/v1/badge/PairPlots)](https://pkgs.genieframework.com?packages=PairPlots)
[![codecov](https://codecov.io/gh/sefffal/PairPlots.jl/branch/master/graph/badge.svg?token=1II9NYRIXT)](https://codecov.io/gh/sefffal/PairPlots.jl)
[![License](https://img.shields.io/github/license/sefffal/PairPlots.jl)](LICENSE)
[![PkgEval](https://juliaci.github.io/NanosoldierReports/pkgeval_badges/P/PairPlots.svg)](https://juliaci.github.io/NanosoldierReports/pkgeval_badges/report.html)



This python package produces pair plots, otherwise known as corner plots or scatter plot matrices: grids of 1D and 2D histograms that allow you to visualize high dimensional data.

Pair plots are an excellent way to vizualize the results of MCMC simulations, but are also a useful way to vizualize correlations in general data tables.

Read the documentation here: (https://sefffal.github.io/PairPlots.jl/dev/)

## Installation

```bash
pip install -U pairplots
```

The default styles of this package roughly reproduce the output of the Python library [corner.py](https://corner.readthedocs.io/en/latest/index.html) for a single series, and [chainconsumer.py](https://samreay.github.io/ChainConsumer/usage.html) for multiple series.
If these are not to your tastes, this package is highly configurable.


## Credits
This package is built on top of the great packages Makie.jl, Contour.jl, KernelDensity.jl, and Tables.jl. The overall inspiration and a few lines of code are taken  from corner.py and chainconsumer.py
