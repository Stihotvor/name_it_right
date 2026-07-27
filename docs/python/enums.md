# Enums

!!! success "General patterns"

    - Use `CamelCase` for the enum class name
    - Use `UPPER_SNAKE_CASE` for enum members (PEP 8 convention): `class Color(Enum): RED = 1; GREEN = 2`
    - If you need to mix enums with string values, inherit from `StrEnum`
    - Use `auto()` when the exact value is irrelevant: `class Priority(IntEnum): LOW = auto(); MEDIUM = auto(); HIGH = auto()`

!!! tip "Useful tips"

    - Use `IntEnum` when enum values participate in numeric operations or comparisons with integers
    - Use `StrEnum` when your enums represent string constants and need to compare cleanly with strings
    - Add a `__str__` or `@property` for human-readable labels: `class Status(Enum): ACTIVE = 1; @property def label(self): ...`
    - If a boolean flag is better expressed as an enum, prefer the enum for extensibility: `ConnectionMode.SSL` vs `is_secure=True`

!!! danger "General anti-patterns"

    - Mixing member naming styles within the same enum class
    - Assigning arbitrary or meaningless values when `auto()` would suffice
    - Using a plain class with module-level constants instead of `Enum` (loses iteration, type-safety, and repr)
    - Naming the class in `snake_case`: `class connection_mode(Enum):` (should be `ConnectionMode`)

```py
from enum import Enum, auto, IntEnum, StrEnum

class OrderStatus(Enum):
    PENDING = auto()
    CONFIRMED = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()

    @property
    def label(self) -> str:
        return self.name.title()

class Priority(IntEnum):
    LOW = 10
    MEDIUM = 50
    HIGH = 100
    CRITICAL = 200

class ShippingMethod(StrEnum):
    STANDARD = "standard"
    EXPRESS = "express"
    SAME_DAY = "same_day"
```
