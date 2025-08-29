import pytest
from pystructs.data_structures import deep_map, merge_deep, pluck_path, filter_deep

def test_deep_map():
    data = {"a": 1, "b": {"c": 2}}
    result = deep_map(lambda x: x*10, data)
    assert result == {"a": 10, "b": {"c": 20}}

def test_merge_deep():
    a = {"a": 1, "b": {"c": 2}}
    b = {"b": {"d": 3}, "e": 4}
    result = merge_deep(a, b)
    assert result == {"a": 1, "b": {"c": 2, "d": 3}, "e": 4}

def test_pluck_path():
    data = {"a": {"b": {"c": 5}}}
    assert pluck_path(data, ["a", "b", "c"]) == 5
    assert pluck_path(data, ["a", "x"]) is None

def test_filter_deep():
    data = {"a": 1, "b": [2, 3, 4]}
    result = filter_deep(lambda x: x % 2 == 0, data)
    assert result == {"b": [2, 4]}
