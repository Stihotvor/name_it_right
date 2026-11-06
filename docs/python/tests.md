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

## Test name patterns

A test name is a short sentence about one behaviour. The pattern is `test_<unit>_<condition>_<expected>`. The condition or the expected part may be left out when it is obvious. The examples use an e-commerce checkout.

| Part | Question | Example |
|---|---|---|
| Unit | What is under test? | `apply_coupon`, `cancel_order`, `Cart` |
| Condition | In which situation? | `with_expired_code`, `for_empty_cart`, `when_card_is_declined` |
| Expected | What happens? | `raises_error`, `returns_zero`, `refunds_payment` |

### Examples by situation

| Situation | Pattern | Examples |
|---|---|---|
| Normal result | `test_<unit>_returns_<value>` | `test_calculate_total_returns_sum_of_line_items`, `test_find_user_returns_none_for_unknown_email` |
| Edge case | `test_<unit>_<condition>_<expected>` | `test_calculate_total_for_empty_cart_returns_zero`, `test_apply_coupon_with_expired_code_raises_error` |
| Side effect | `test_<unit>_<effect>` | `test_cancel_order_refunds_payment`, `test_checkout_sends_receipt_email` |
| State change | `test_<unit>_sets_<state>` | `test_pay_order_sets_status_to_paid`, `test_cancel_order_sets_cancelled_at` |
| Rule | `test_<rule>_<outcome>` | `test_free_shipping_applies_above_threshold`, `test_discount_never_exceeds_order_total` |
| Failure | `test_<unit>_fails_when_<cause>` | `test_checkout_fails_when_card_is_declined`, `test_refund_fails_when_already_refunded` |
| Permission | `test_<actor>_can_<action>` | `test_customer_can_cancel_unshipped_order`, `test_guest_cannot_view_other_orders` |

### Behaviour, not implementation

| Tests the implementation | Tests the behaviour | Why |
|---|---|---|
| `test_calls_apply_method` | `test_apply_coupon_reduces_total` | The first name breaks on a refactor. The second does not. |
| `test_uses_dict_for_cart` | `test_cart_keeps_items_in_insertion_order` | The reader cares about the result, not the data structure. |
| `test_save_called_once` | `test_cancel_order_persists_new_status` | A call count is a means. The stored state is the goal. |
| `test_loop_over_items` | `test_calculate_total_adds_all_line_items` | A loop is a detail. |
| `test_private_helper_returns_true` | `test_checkout_accepts_valid_card` | Test through the public interface. |

## Test classes and files

| Kind | Rule | Examples |
|---|---|---|
| Test file | `test_<module>.py`, mirrors the module under test. | `test_order_checkout.py`, `test_coupon_rules.py` |
| Test class | `Test<Unit>` or `Test<Feature>`. No `__init__`. | `TestOrderCheckout`, `TestCouponRules`, `TestCartMerge` |
| Nested scenario | One class per scenario when the setup is shared. | `TestCheckoutWithDeclinedCard`, `TestCheckoutAsGuest` |
| Test method | Same as a test function. The class carries the unit. | `TestCart.test_add_item_increases_item_count` |

## Fixtures and factories

| Kind | Rule | Examples |
|---|---|---|
| Plain fixture | A noun for the object it returns. | `order`, `cart`, `customer` |
| Fixture in a state | An adjective and a noun. | `paid_order`, `empty_cart`, `guest_customer` |
| Factory fixture | A verb for the function it returns. | `make_order`, `build_cart`, `create_customer` |
| Library factory | A class named for the model, in a `factories` module. | `OrderFactory`, `CustomerFactory` |
| Mock fixture | `mock_` and the replaced object. | `mock_payment_gateway`, `mock_email_service` |
| Session resource | A noun for the shared resource. | `database`, `http_client`, `redis_connection` |
| Autouse fixture | A verb that states the setup. | `freeze_time`, `reset_cache`, `disable_network` |

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `test_1` | `test_cancel_order_refunds_payment` | A number explains nothing. |
| `test_order` | `test_create_order_rejects_empty_cart` | One behaviour per name. |
| `test_happy_path` | `test_checkout_succeeds_with_valid_card` | Name the case, not the mood. |
| `test_error` | `test_checkout_fails_when_card_is_declined` | The reader sees the cause and the result. |
| `test_it_works` | `test_apply_coupon_reduces_total` | `works` is not a check. |
| `test_calculate_total_and_tax` | `test_calculate_total_adds_line_items` and `test_calculate_tax_uses_region_rate` | `and` hides two behaviours. |
| `test_cart_1`, `test_cart_2` | `test_cart_merge_keeps_both_items` | Use the rule instead of a counter. |
| `user_fixture` | `user` | The decorator already marks the fixture. |
| `fixture_order` | `paid_order` | Name the state, not the mechanism. |
| `get_order` (a factory fixture) | `make_order` | `get` suggests a read. |
| `class OrderTests` | `class TestOrderCheckout` | `Test` prefix is needed for discovery. |

!!! info "See also"

    - [Functions](functions.md) for production function names
    - [Classes](classes.md) for production class names
    - [Bad → better cookbook](../patterns/cookbook.md) for more rewrites
    - [pytest: conventions for Python test discovery](https://docs.pytest.org/en/stable/explanation/goodpractices.html#conventions-for-python-test-discovery) for the rules about `test_` names
