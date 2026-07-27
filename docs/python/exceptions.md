# Exceptions

!!! success "General patterns"

    - Use `CamelCase` and suffix with `Error` or `Warning`: `ValidationError`, `ConnectionTimeoutError`, `DeprecationWarning`
    - Custom exceptions should inherit from a built-in exception class or from your project's base exception: `class APIError(Exception):`
    - Create a project-wide base exception so callers can catch all your exceptions with one statement: `class PaymentError(Exception):`

!!! tip "Useful tips"

    - For large packages, build an exception hierarchy: `DatabaseError` → `DatabaseConnectionError`, `DatabaseQueryError`, `DatabaseMigrationError`
    - Name exceptions after the condition they represent, not the action that failed: `PaymentDeclinedError` (not `PayFailedError`)
    - Document in the docstring which exceptions a function can raise
    - Use `Exception` subclasses for recoverable errors; use `Warning` subclasses for non-fatal issues

!!! danger "General anti-patterns"

    - Generic names without suffix: `class MyError:` (unclear if it's an exception or a data class)
    - Inheriting directly from `BaseException` (reserved for system-exiting exceptions like `KeyboardInterrupt`)
    - Exception names that describe the operation instead of the failure: `ProcessPayment` (sounds like a function)
    - Overly broad names that clash with stdlib: `class TimeoutError:` (shadows built-in `TimeoutError`)

```py
# Payment module exception hierarchy
class PaymentError(Exception):
    """Base exception for all payment-related errors."""

class TransactionDeclinedError(PaymentError):
    """Payment was declined by the gateway."""

class InsufficientFundsError(PaymentError):
    """Customer account has insufficient funds."""

class GatewayTimeoutError(PaymentError):
    """Payment gateway did not respond in time."""

class ExpiredCardError(PaymentError):
    """Card is past its expiration date."""
```
