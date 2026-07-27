# Tests

Pytest is the de-facto standard for Python tests. These conventions apply to test files, functions, fixtures, classes, and mocks.

## Test functions

!!! success "General patterns"

    - Use `test_<unit>_<condition>` pattern: `test_calculate_total_returns_zero_for_empty_cart()`
    - Every test name should describe one specific behavior or outcome
    - Name tests so a failing name tells you what broke without reading the body

    ```py
    def test_apply_discount_reduces_total() -> None:
        ...

    def test_apply_discount_negative_amount_raises_error() -> None:
        ...
    ```

!!! tip "Useful tips"

    - One assertion per test when possible. Two assertions about the same result are fine; two about different behaviors suggest a split
    - Avoid `and` in test names — the same rule as production functions: `test_order_cancels_and_refunds()` → two tests

!!! danger "General anti-patterns"

    - Test names like `test_functionality()` or `test_1()` — they explain nothing
    - Tests named after the implementation instead of the behavior: `test_calls_apply_method()` breaks on refactor

## Parametrized tests

!!! success "General patterns"

    - Use descriptive `id` values with `pytest.param` so failures pin-point the exact case
    - Name the test `test_<unit>_<condition>` and let the param id carry the variation

    ```py
    @pytest.mark.parametrize("email,expected", [
        pytest.param("user@example.com", True, id="valid_standard"),
        pytest.param("user@", False, id="invalid_missing_domain"),
        pytest.param("", False, id="invalid_empty_string"),
    ])
    def test_is_valid_email(email: str, expected: bool) -> None:
        ...
    ```

!!! tip "Useful tips"

    - Group param ids by scenario: `valid_*`, `invalid_*`, `edge_*` — they sort well in test output
    - Keep the test function body short — if logic is needed, extract a helper

## Test classes

!!! success "General patterns"

    - Group tests into a class when they share a common fixture or setup: `class TestOrderCheckout:`
    - Use `CamelCase` prefixed with `Test`: `TestPaymentGateway`, `TestDiscountEngine`
    - Name the class after the feature or unit under test, not the test runner

!!! tip "Useful tips"

    - Use `Test` prefix so pytest discovers the class automatically
    - Avoid `__init__` in test classes — use `setup_method` or fixtures instead

!!! danger "General anti-patterns"

    - Adding `Test` prefix to non-test classes — they will be collected and attempted as tests
    - Putting every test in one class — group by feature, not by file

## Mocks and patches

!!! success "General patterns"

    - Name mocks after the object they replace: `mock_payment_gateway`, `mock_email_service`
    - Use `mock_` prefix consistently for all `unittest.mock` objects
    - Keep the mock name in the test function signature aligned with the patched target

    ```py
    def test_send_email_calls_external_service(
        mock_email_service: MagicMock,
        sample_user: User,
    ) -> None:
        result = send_welcome_email(sample_user)
        mock_email_service.send.assert_called_once_with(sample_user.email)
    ```

!!! tip "Useful tips"

    - Use `spy_` prefix for spies (mocks that wrap the real object): `spy_logger`, `spy_cache`
    - Use `patch()` as a decorator when the mock is used by every test in the class; use `with patch()` when only one path needs it
    - Align mock method names with the real API — if the real method is `send()`, use `mock.send` not `mock.deliver`

!!! danger "General anti-patterns"

    - Generic mock names: `mock_obj`, `m` — they obscure what is being replaced
    - Mixing `mock_` and other prefixes within the same test file
    - Mocking what you don't own (stdlib, third-party libs in integration tests) — prefer integration patching

## Pytest Fixtures

!!! success "General patterns"

    - Use nouns for fixtures returning final objects: `user`, `order`, `cart`
    - Use verbs for fixtures returning callables: `make_user()`, `build_order()`, `generate_token()`
    - Name fixture files after their domain: `conftest.py` for session-scoped, `order_fixtures.py` for domain-specific

    ```py
    @pytest.fixture
    def sample_user() -> User:
        return User(email="test@example.com", name="Test User")

    @pytest.fixture
    def make_user() -> Callable[..., User]:
        def _make_user(**overrides: Any) -> User:
            defaults = {"email": "test@example.com", "name": "Test User"}
            return User(**{**defaults, **overrides})
        return _make_user
    ```

!!! tip "Useful tips"

    - Name factory fixtures (fixtures that return a function) with a verb so the caller knows to call them: `make_`, `build_`, `create_`
    - Use `conftest.py` for fixtures shared across multiple test files
    - Add type hints to fixture return values — IDEs and type checkers can then infer types in test functions

!!! danger "General anti-patterns"

    - Fixture names that don't reflect the returned object: `fixture_user`, `user_fixture` — just `user` is enough
    - Over-scoping fixtures to `session` when `function` is sufficient — it hides test pollution