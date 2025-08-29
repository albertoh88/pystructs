def all_of(*funcs):
    """Return a function that is True if all funcs return True."""
    return lambda x: all(f(x) for f in funcs)

def any_of(*funcs):
    """Return a function that is True if any funcs return True."""
    return lambda x: any(f(x) for f in funcs)

def not_fn(func):
    """Return a function that negates the result of func."""
    return lambda x: not func(x)

# Example validators for common use
def is_string(x):
    return isinstance(x, str)

def is_number(x):
    return isinstance(x, (int, float))

def is_non_empty(x):
    return bool(x)
