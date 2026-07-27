# Modules and packages

!!! success "General patterns"

    - Use `snake_case` for module (file) names
    - Packages (directories) should be short, lowercase, and avoid underscores when possible
    - Module names should be short, all lowercase, and use underscores only if it improves readability: `message_parser.py`, `http_client.py`
    - `__init__.py` should be empty or only contain package metadata / public API re-exports

!!! tip "Useful tips"

    - Name modules after their primary content: a module containing validators → `validators.py`
    - If a module would shadow a stdlib package, use a compound name: `custom_json.py` instead of `json.py`
    - Keep module names under 30 characters to avoid filesystem portability issues
    - Use `_` prefix for internal sub-modules: `_helpers.py`, `_types.py`

!!! danger "General anti-patterns"

    - Dashes in module names (`my-module.py` — can't be imported with `import`)
    - Names starting with digits (`1_parser.py`)
    - Naming a module after a single class inside it — name the module for the category instead: `senders.py` not `EmailSender.py`
    - Overly generic names: `utils.py`, `helpers.py` (become dumping grounds)

```py
# Well-structured package with consistent naming
payment/
    __init__.py          # re-exports public API
    gateway.py           # payment gateway integrations
    validators.py        # card number, expiry, CVV validators
    _types.py            # internal type aliases, not part of public API
    exceptions.py        # PaymentError, GatewayTimeoutError, etc.
```
