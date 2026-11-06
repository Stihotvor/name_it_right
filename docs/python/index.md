# General rules

Python is a dynamically typed language — you can assign different types to the same variable. Avoid it by any means. Type annotations are your primary defence.

!!! success "PEP 8 naming at a glance"

    | Entity | Convention | Example |
    |---|---|---|
    | Variables | `snake_case` | `user_name`, `order_total` |
    | Functions | `snake_case` | `fetch_orders()`, `validate_email()` |
    | Classes | `CamelCase` | `OrderProcessor`, `Customer` |
    | Exceptions | `CamelCase` + `Error`/`Warning` suffix | `PaymentError`, `DeprecationWarning` |
    | Constants | `UPPER_SNAKE_CASE` | `MAX_RETRIES`, `DEFAULT_TIMEOUT_MS` |
    | Modules | `snake_case` | `email_sender.py` |
    | Packages | lowercase, no underscores | `payment`, `order_processing` |
    | Type variables | short `CamelCase` | `T`, `T_co`, `K`, `V` |

!!! tip "Useful tips"

    - Use type annotations for every function signature — they serve as documentation and enable static analysis
    - Use `TypeVar` with descriptive names for generic types: `T = TypeVar("T")`, `T_co = TypeVar("T_co", covariant=True)`, `K = TypeVar("K")` for keys, `V = TypeVar("V")` for values
    - Use conventional aliases for popular libraries: `import pandas as pd`, `import numpy as np`, `import matplotlib.pyplot as plt`
    - Use `TYPE_CHECKING` guard for type-only imports to avoid circular dependencies: `from __future__ import annotations` is often simpler
    - Prefer `from __future__ import annotations` at the top of every file — it makes all annotations strings (faster, no forward-reference issues)
    - Prefix non-public names with a single underscore: `_internal_helper()`, `_cache_size`. Double underscore `__name_mangling` is rarely needed — reserve it for mixins and base classes to avoid name clashes
    - Use `_` as a throwaway name for unpacking: `key, _, value = partition("a=b")`

!!! danger "General anti-patterns"

    - Using `from module import *` — pollutes the namespace and makes the source of names invisible
    - Overusing `__double_underscore` on every private attribute — prefer `_single_underscore` unless you specifically need name mangling
    - Ignoring type annotations in public APIs — callers have no way to know what types to pass

## Naming at a glance

| Entity | Convention | Details |
|---|---|---|
| Variables | `snake_case` | [Patterns and anti-patterns](variables.md) |
| Functions | `snake_case` | [Patterns, tips, and verb glossary](functions.md) |
| Class methods | `snake_case` | [Verb glossary by letter](class_methods.md) |
| Classes | `CamelCase` | [Patterns, tips, and naming examples](classes.md) |
| Modules & packages | `snake_case` / lowercase | [File and directory naming](modules.md) |
| Constants | `UPPER_SNAKE_CASE` | [Constants vs variables](constants.md) |
| Exceptions | `CamelCase` + suffix | [Exception hierarchy naming](exceptions.md) |
| Enums | class `CamelCase`, members `UPPER_SNAKE_CASE` | [Enum naming conventions](enums.md) |
| Generators, async, decorators | `snake_case` | [Special function naming](special_functions.md) |
| Tests | `test_` prefix | [Test functions, fixtures, mocks](tests.md) |

!!! info "See also"

    - [Languages overview](../languages/index.md) to compare Python with five other languages
    - [Naming patterns](../patterns/index.md) and [Common rules](../common/index.md) for rules that do not depend on a language
    - [Databases](../databases/index.md) and [Systems](../systems/index.md) for the names that code shares with a schema or an API
    - [Examples](../examples/index.md) for Python snippets in seven domains
