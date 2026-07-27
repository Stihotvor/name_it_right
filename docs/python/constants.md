# Constants

!!! success "General patterns"

    - Use `UPPER_SNAKE_CASE` for all module-level constants: `MAX_RETRIES = 3`, `DEFAULT_TIMEOUT_SECONDS = 30`
    - Prefix internal (non-exported) constants with a single underscore: `_INTERNAL_CACHE_SIZE = 1024`
    - Group related constants into classes or frozen dataclasses when they form a logical set
    - Type-annotate constants for better IDE support: `API_BASE_URL: str = "https://example.com"`

!!! tip "Useful tips"

    - Place constants at the top of the module, right after imports
    - Use `Final` from `typing` to signal a constant is not meant to be reassigned: `from typing import Final; MAX_CONNECTIONS: Final[int] = 10`
    - For domain-specific numeric values, include the unit in the name: `TIMEOUT_MS`, `BUFFER_SIZE_KB`
    - Prefer `enum.Enum` or `enum.StrEnum` over a module full of string constants when values belong together

!!! danger "General anti-patterns"

    - Lowercase or mixed-case constant names: `max_retries = 3` (looks like a regular variable)
    - Magic literals scattered through code — they should be named constants
    - Spreading related constants across unrelated modules
    - Using a dict instead of a class or enum for a fixed set of related constants (loses type safety)

```py
from typing import Final

API_BASE_URL: Final[str] = "https://api.example.com/v2"
DEFAULT_PAGE_SIZE: Final[int] = 50
MAX_UPLOAD_SIZE_MB: Final[int] = 100
REQUEST_TIMEOUT_MS: Final[int] = 5000

# Related constants grouped in a frozen dataclass
from dataclasses import dataclass

@dataclass(frozen=True)
class PaginationDefaults:
    size: int = 20
    max_size: int = 100
    starting_page: int = 1
```
