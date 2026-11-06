# Tests

Pytest is the de-facto standard for Python tests. These conventions apply to test files, functions, fixtures, classes, and mocks.

## Test functions

!!! success "General patterns"

    - Use the `test_<unit>_<condition>_<expected>` pattern: `test_calculate_total_for_empty_cart_returns_zero()`
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
    - Name the test `test_<unit>_<condition>_<expected>` and let the param id carry the variation

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
    def test_send_welcome_email_sends_to_user_address(
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
| Normal result | `test_<unit>_returns_<value>` | `test_calculate_total_returns_sum_of_line_items`, `test_find_user_for_unknown_email_returns_none` |
| Edge case | `test_<unit>_<condition>_<expected>` | `test_calculate_total_for_empty_cart_returns_zero`, `test_apply_coupon_with_expired_code_raises_error` |
| Side effect | `test_<unit>_<effect>` | `test_cancel_order_refunds_payment`, `test_checkout_sends_receipt_email` |
| State change | `test_<unit>_sets_<state>` | `test_pay_order_sets_status_to_paid`, `test_cancel_order_sets_cancelled_at` |
| Rule | `test_<rule>_<outcome>` | `test_free_shipping_applies_above_threshold`, `test_discount_never_exceeds_order_total` |
| Failure | `test_<unit>_fails_when_<cause>` | `test_checkout_fails_when_card_is_declined`, `test_refund_fails_when_already_refunded` |
| Permission | `test_<actor>_can_<action>` or `test_<actor>_cannot_<action>` | `test_customer_can_cancel_unshipped_order`, `test_guest_cannot_view_other_orders` |

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
| Test class | `Test<Unit>` or `Test<Feature>`. No `__init__`, because pytest does not collect a class that has one. | `TestOrderCheckout`, `TestCouponRules`, `TestCartMerge` |
| Scenario class | One class per scenario when the setup is shared. | `TestCheckoutWithDeclinedCard`, `TestCheckoutAsGuest` |
| Test method | Same as a test function. The class names the feature. The method names the rule under test. | `TestCart.test_add_item_increases_item_count` |

## Fixtures and factories

| Kind | Rule | Examples |
|---|---|---|
| Plain fixture | A noun for the object it returns. | `order`, `cart`, `customer` |
| Fixture in a state | A state word and a noun. | `paid_order`, `empty_cart`, `guest_customer` |
| Factory fixture | A verb for the function it returns. Use `create_` if the factory stores the object, `build_` if it stays in memory, and `make_` if neither applies. | `make_order`, `build_cart`, `create_customer` |
| Test data factory | A class named for the model, in a `factories` module. This is the accepted use of the `Factory` suffix for test data, for example with factory_boy. See [Classes](classes.md). | `OrderFactory`, `CustomerFactory` |
| Mock fixture | `mock_` and the replaced object. Use `spy_` for a spy. | `mock_payment_gateway`, `mock_email_service`, `spy_logger` |
| Session resource | A noun for the shared resource. | `database`, `http_client`, `redis_connection` |
| Autouse fixture | A verb that states the effect. It runs for every test without being requested (`autouse=True`). | `freeze_clock`, `reset_cache`, `disable_network` |

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
| `fixture_order` | `order` | The decorator already marks the fixture. |
| `order` (a paid order) | `paid_order` | Name the state. |
| `get_order` (a factory fixture) | `make_order` | `get` suggests a read. |
| `class OrderTests` | `class TestOrderCheckout` | The `Test` prefix is needed by pytest's default discovery. |

!!! info "See also"

    - [Functions](functions.md) for production function names
    - [Classes](classes.md) for production class names
    - [Bad → better cookbook](../patterns/cookbook.md) for more rewrites
    - [pytest: conventions for Python test discovery](https://docs.pytest.org/en/stable/explanation/goodpractices.html#conventions-for-python-test-discovery) for the rules about `test_` names

## Advanced test topics

The tables below extend the sections above. The examples use an e-commerce checkout.

### Parametrized ids

An id is the label of one case in the test report. Write the id as a short phrase about the case.

| Kind | Pattern | Examples |
|---|---|---|
| Valid case | `valid_<case>` | `valid_standard_email`, `valid_plus_alias`, `valid_long_domain` |
| Invalid case | `invalid_<reason>` | `invalid_missing_domain`, `invalid_empty_string`, `invalid_double_at` |
| Edge case | `edge_<case>` | `edge_zero_quantity`, `edge_max_quantity`, `edge_single_cent` |
| Business case | `<role>_<situation>` | `guest_with_coupon`, `member_free_shipping`, `vip_double_points` |
| Generated ids | `ids=` with a function when the data is large | `ids=lambda case: case.name` |

```py
@pytest.mark.parametrize("quantity,expected_cents", [
    pytest.param(0, 0, id="edge_zero_quantity"),
    pytest.param(1, 1999, id="valid_single_item"),
    pytest.param(10, 18990, id="valid_bulk_discount"),
])
def test_calculate_line_total_applies_bulk_discount(quantity: int, expected_cents: int) -> None:
    ...
```

### Mocks, spies and fakes

| Kind | Rule | Examples |
|---|---|---|
| Mock | `mock_` and the replaced object. | `mock_payment_gateway`, `mock_email_service` |
| Spy | `spy_` and the wrapped object. The real code still runs. | `spy_logger`, `spy_cache` |
| Fake | `fake_` and the replaced object. It is a working light version. | `fake_clock`, `fake_inventory`, `fake_payment_gateway` |
| Stub | `stub_` and the replaced object. It returns fixed answers. | `stub_tax_rates`, `stub_carrier_quotes` |
| Patch target | Patch where the name is used, not where it is defined. | `patch("checkout.service.send_email")` |
| Mock call | `assert_called_once_with(...)` states the contract. | `mock_email_service.send.assert_called_once_with(user.email)` |

Use `autospec=True` or `create_autospec` so the mock keeps the real signature. Then `mock_payment_gateway.charge` fails if the real class has no `charge`.

### Exception tests

| Pattern | Examples |
|---|---|
| `test_<unit>_raises_<error>_when_<cause>` | `test_apply_coupon_raises_expired_error_when_code_is_old` |
| `test_<unit>_rejects_<input>` | `test_create_order_rejects_empty_cart` |
| `test_<unit>_fails_when_<cause>` | `test_checkout_fails_when_card_is_declined` |
| `test_<unit>_does_not_raise_<error>` | `test_refund_does_not_raise_for_zero_amount` |

```py
def test_apply_coupon_raises_expired_error_when_code_is_old(old_coupon: Coupon) -> None:
    with pytest.raises(CouponExpiredError, match="expired"):
        apply_coupon(old_coupon)
```

### Async tests

| Kind | Rule | Examples |
|---|---|---|
| Test function | The same name as a sync test. Add `async def`. | `async def test_capture_payment_returns_receipt` |
| Async fixture | The same noun or verb as a sync fixture. | `async_client`, `open_connection` |
| Marker | Use the marker or the mode of your async plugin. | `@pytest.mark.asyncio` with pytest-asyncio |
| Timing | Name the wait in the test, not in the unit. | `test_poll_order_status_stops_after_timeout` |

An async test needs a plugin, such as pytest-asyncio or anyio. Without a plugin, pytest does not run the coroutine.

### Performance and slow tests

| Kind | Rule | Examples |
|---|---|---|
| Benchmark test | `test_<unit>_benchmark` or `test_<unit>_is_fast_for_<size>` | `test_calculate_total_benchmark`, `test_search_products_is_fast_for_10k_items` |
| Marker | A marker for slow tests. | `@pytest.mark.slow`, `@pytest.mark.integration` |
| Limits in the name | Put the limit and the unit in the name. | `test_checkout_finishes_within_2_seconds` |

Register custom markers in `pytest.ini` or `pyproject.toml`, so that a typo in a marker name does not pass silently.

### Snapshot tests

| Kind | Rule | Examples |
|---|---|---|
| Test name | State what the snapshot captures. | `test_invoice_pdf_matches_snapshot`, `test_order_json_matches_snapshot` |
| Snapshot name | Use the test name, or a short name with the snapshot plugin. | `invoice_with_discount`, `order_with_two_items` |
| Update rule | Review each snapshot change as a code change. | `--snapshot-update` with syrupy |

A snapshot name should describe the scenario. The plugin may add the file name for you.

## Advanced bad → better

| Bad | Better | Why |
|---|---|---|
| `id="case1"` | `id="invalid_missing_domain"` | The report shows the reason. |
| `mock` | `mock_payment_gateway` | A bare `mock` hides the replaced object. |
| `patch("payment.gateway.charge")` in a test of checkout | `patch("checkout.service.charge")` | Patch the name where the code under test uses it. |
| `test_exception` | `test_apply_coupon_raises_expired_error_when_code_is_old` | The name shows the error and the cause. |
| `test_async` | `async def test_capture_payment_returns_receipt` | The test states the behaviour. The word `async` is in the keyword. |
| `test_speed` | `test_checkout_finishes_within_2_seconds` | The limit is in the name. |
| `test_snapshot_1` | `test_order_json_matches_snapshot` | A counter says nothing. |
| `slow_test_checkout` | `test_checkout_end_to_end` with `@pytest.mark.slow` | Use a marker, not a prefix. pytest finds tests by `test_`. |

!!! info "See also"

    - [pytest: parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html) for ids
    - [unittest.mock: where to patch](https://docs.python.org/3/library/unittest.mock.html#where-to-patch) for patch targets
    - [pytest: custom markers](https://docs.pytest.org/en/stable/how-to/mark.html) for markers
