import juliacall
import collections
from pairplots import PairPlots
from pairplots import jl
from .julia_helpers import *
import sys
# import pandas as pd

# Inside Planet and System blocks, which are resolved in the Main module,
# we need various names available to the user
jl.seval("using PairPlots, Makie")

Makie = jl.Makie

# We accept the following kinds of inputs:
# * plain matrix, series as columns
# * plain matrix, labels=["list", "of", "strings"]
# * pandas Dataframe
# * pandas Dataframe, labels={} dict mapping labels to rich types

# Rich text formatting:
rich = jl.Makie.rich
superscript = jl.Makie.superscript
subscript = jl.Makie.subscript
# Latex formatting:
def latex(string):
    return jl.Makie.latexstring(string)

# Save figures
save = jl.Makie.save

_dict_sym = jl.seval("(list) -> Dict{Symbol,Any}((Pair(l[1], l[2]) for l in list)...)")

def _handle_args(
    *args,
    labels=[],
    axis={},
    diagaxis={},
    bodyaxis={},
    legend={},
    **kwargs
    ):
    # TODO: multiple tables, pandas
    if len(args) == 1 and len(labels) > 0 and not isinstance(labels, collections.abc.Mapping):
        if len(labels) == np.shape(args[0])[1]:
            series = jl_named_tuple(labels, [col for col in args[0].T])
        else:
            raise ValueError(f"number of labels {len(labels)} does not match shape of array {np.shape(args[0])}")

    series = [
        _handle_series(arg)
        for arg in args
    ]
    
    if isinstance(labels, collections.abc.Mapping):
        prepared = jl_array([
            (jl.Symbol(k), v)
            for k,v in labels.items()
        ])
        labels_prepared = _dict_sym(prepared)
        kwargs["labels"] = labels_prepared

    if isinstance(axis, collections.abc.Mapping):
        prepared = jl_array([
            (jl.Symbol(k), v)
            for k,v in axis.items()
        ])
        axis_prepared = _dict_sym(prepared)
        kwargs["axis"] = axis_prepared

    if isinstance(diagaxis, collections.abc.Mapping):
        prepared = jl_array([
            (jl.Symbol(k), v)
            for k,v in diagaxis.items()
        ])
        diagaxis_prepared = _dict_sym(prepared)
        kwargs["diagaxis"] = diagaxis_prepared

    if isinstance(bodyaxis, collections.abc.Mapping):
        prepared = jl_array([
            (jl.Symbol(k), v)
            for k,v in bodyaxis.items()
        ])
        bodyaxis_prepared = _dict_sym(prepared)
        kwargs["bodyaxis"] = bodyaxis_prepared


    fig = PairPlots.pairplot(*series,**kwargs)

    # TODO! can't figure out how to handle passing Series => viz pairs

    return fig

series = PairPlots.Series
def _handle_series(data):
    if isinstance(data, tuple):
        if len(data) == 2:
            return jl.Pair._jl_raw()(data[0], data[1])._jl_any()
        else:
            raise ValueError("Pass series as a tuple of (data, viz_layers) where viz_layers is itself a tuple.")
    return data
    # if isinstance(labels, collections.abc.Mapping):
    # if isinstance(data, pd.DataFrame):
        # return PairPlots.Series(data)
    # elif jl.isa(data, PairPlots.series):
        # return data
    # else:
    #     arr = np.array(data)
    #     return PairPlots.Series(data)

# These functions require us to load a plotting backend, which is a little
# slow. Only load it when we need it.
def pairplot(*args, **kwargs):
    jl.seval("using CairoMakie")
    jl.seval("CairoMakie.activate!()")
    fig = _handle_args(*args, **kwargs)
    return fig

def pairplot_interactive(*args, **kwargs):
    if isipynb():
        print(
            "WARNING: you ran pairplot_interactive(...) from a Jupyter notebook. "
            "An interactive window will open outside the notebook. If you are connected "
            "to a remote Jupyter kernel/server, you might want to stop this cell and try "
            "pairplot() instead."
        )
    jl.seval("using GLMakie")
    jl.GLMakie.activate_b(focus_on_show=True, title="pairplot")
    fig = _handle_args(*args, **kwargs)
    jl.wait(jl.display(fig))
    return fig


def isipynb():
    try:
        get_ipython = sys.modules["IPython"].get_ipython
        if "IPKernelApp" not in get_ipython().config:
            raise ImportError("console")
        return True
    except Exception:
        return False