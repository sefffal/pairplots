"""Functions for initializing the Julia environment and installing deps."""

import numpy as np
from juliacall import convert as jl_convert  # type: ignore

from .julia_import import jl

jl.seval("using PythonCall: PythonCall")

PythonCall = jl.PythonCall


# def _escape_filename(filename):
#     """Turn a path into a string with correctly escaped backslashes."""
#     str_repr = str(filename)
#     str_repr = str_repr.replace("\\", "\\\\")
#     return str_repr



def jl_array(x):
    if x is None:
        return None
    return jl_convert(jl.Array, x)

def jl_named_tuple(keys, values):
    jl.keys_sym = jl.map(jl.Symbol, keys)
    nt_constructor = jl.seval("NamedTuple{(keys_sym...,)}")
    return nt_constructor(values)

# def jl_serialize(obj):
#     buf = jl.IOBuffer()
#     Serialization.serialize(buf, obj)
#     return np.array(jl.take_b(buf))


# def jl_deserialize(s):
#     if s is None:
#         return s
#     buf = jl.IOBuffer()
#     jl.write(buf, jl_array(s))
#     jl.seekstart(buf)
#     return Serialization.deserialize(buf)
