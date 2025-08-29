import pytest
from pystructs.validators import is_string, is_number, all_of, not_fn

def test_basic_validators():
    assert is_string("hello")
    assert not is_string(42)
    assert is_number(3.14)
    assert not is_number("abc")

def test_combinators():
    validate = all_of(is_string, lambda x: len(x) > 3)
    assert validate("Test")
    assert not validate("Hi")

    negate = not_fn(is_number)
    assert negate("abc")
    assert not negate(10)
