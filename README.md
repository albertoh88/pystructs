# pystructs

`pystructs` is a lightweight Python library providing **functional utilities for working with nested data structures and validations**.  
Ideal for developers handling JSON, deeply nested dictionaries, or complex data from APIs and databases.

---

## Installation

Clone the repository and install in editable mode:

```bash
git clone https://github.com/albertoh88/pystructs.git
cd pystructs
pip install -e .
```

## Modules
### 1️⃣ Data Structures (pystructs.data_structures)
Functions to manipulate nested lists and dictionaries.
**Examples:**
```bash
from pystructs.data_structures import deep_map, merge_deep, pluck_path, filter_deep

data = {"a": 1, "b": {"c": 2, "d": 3}}

# Apply a function to every value
print(deep_map(lambda x: x*10, data))
# Output: {'a': 10, 'b': {'c': 20, 'd': 30}}

# Merge two nested dictionaries
dict1 = {"a": 1, "b": {"c": 2}}
dict2 = {"b": {"d": 3}, "e": 4}
print(merge_deep(dict1, dict2))
# Output: {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}

# Extract nested value safely
print(pluck_path(data, ["b", "c"]))  # 2

# Filter nested structure
nested = {"a": 1, "b": [2, 3, 4]}
print(filter_deep(lambda x: x % 2 == 0, nested))
# Output: {'b': [2, 4]}
```

### 2️⃣ Validators (pystructs.validators)

Composable validators to check values and nested structures.
Examples:
```bash
from pystructs.validators import all_of, any_of, not_fn, is_string, is_number

print(is_string("hello"))  # True
print(is_number(42))       # True

# Combine multiple validators
validate = all_of(is_string, lambda x: len(x) > 3)
print(validate("Test"))    # True

# Negate a validator
negate = not_fn(is_number)
print(negate("abc"))       # True
```

You can also combine validators with deep_map to validate nested structures.

### Benefits
 - Simplifies manipulation of nested data structures in Python.
 - Provides composable functional validators.
 - Ideal for working with JSON, API responses, or complex configs.
 - Lightweight, easy to install and integrate.

### Contribution
Contributions are welcome! You can help by:
 - Adding new data structure utilities.
 - Adding more advanced validators.
 - Improving documentation and examples.
 - Writing additional tests.
Pull requests are welcome!