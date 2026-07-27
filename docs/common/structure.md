# Structure

!!! success "General patterns"

    - Use the type system and annotations to convey type information — not the name
    - Names should describe purpose, not implementation

!!! tip "Useful tips"

    - Language-ambiguous contexts (older JavaScript, PHP, Bash) may still benefit from type prefixes — evaluate per-language

!!! warning "Names that include type information (Hungarian)"

    ```py
    strName = "Alice"         # The annotation tells us it's a string
    intCount = 5              # Python 3+ has type hints
    dictUsers = {}            # The {} literal already signals a dict
    ```

    - Type information in the name is noise — type annotations and IDEs handle this
    - Exception: type-ambiguous languages without type hints (JavaScript, etc.)

!!! warning "Redundant prefixes"

    ```py
    my_variable = ...         # Whose else would it be?
    the_value = ...           # Which other value?
    local_counter = ...       # It's already local by scope
    ```

    - `my_`, `the_`, `local_` — strip these prefixes. They add length and add nothing
