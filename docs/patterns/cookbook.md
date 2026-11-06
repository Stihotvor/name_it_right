---
status: new
---

# Bad → better cookbook

A catalogue of common weak names and better replacements, grouped by category. Each row says why the new name is better. Use the page as a checklist during code review.

!!! success "General patterns"

    - Name what the thing is or does, not its type: `orders`, not `order_list`.
    - Put the unit, the zone or the key in the name when the type does not carry it: `timeout_seconds`, `created_at`, `orders_by_id`.
    - Use one word for one idea in the whole code base.
    - Prefer a name that a new teammate can guess without reading the code.

!!! tip "Useful tips"

    - A "better" name depends on what the code really does. Where a row says "if", check that the condition is true for your code before you rename.
    - Rename in small steps. Rename first, then change behaviour in a separate commit.
    - The pattern pages give the rule behind each row. This page gives only the fast answer.

!!! danger "General anti-patterns"

    - Renaming only the variable and leaving the old word in the docs, the tests and the logs.
    - Adding a comment instead of fixing the name: `d = 30  # days` → `retention_days = 30`.

## Abbreviations

See [Abbreviations](../common/abbreviations.md).

| Bad | Better | Why |
|---|---|---|
| `cust_id` | `customer_id` | The reader should not need to guess the word. |
| `calc_ttl_amt()` | `calculate_total_amount()` | Three abbreviations in one name hide the meaning. |
| `addr_ln1` | `address_line_1` | The full words cost little and stay readable. |
| `pmt_mthd` | `payment_method` | Vowel-dropping hurts search and speech. |
| `ord_dt` | `ordered_on` | `dt` could be date or datetime. `_on` marks a date. |
| `UsrMgr` | `UserManager` | A class name is read often. Spell it out. |

## Generic names

| Bad | Better | Why |
|---|---|---|
| `data` | `order_summary` | `data` fits any variable. |
| `info` | `shipping_details` | Say what the information is about. |
| `process()` | `capture_payment()` | `process` hides the action. |
| `handle_item(item)` | `pack_item(item)` | Name the step, not the act of dealing with it. |
| `tmp` | `unpaid_orders` | A temporary value still has a meaning. |
| `result` | `refund_receipt` | `result` says nothing about content. |
| `OrderManager` (if it schedules orders) | `OrderScheduler` | `Manager` hides the job. Name the class after the job. |

## Misleading names

| Bad | Better | Why |
|---|---|---|
| `is_valid()` that also saves the order | `validate_order()` and `save_order()` | A check must not change state. |
| `get_total()` that changes the cart | `recalculate_total()` | `get` suggests a read with no side effect. |
| `orders_list` that is a dict | `orders_by_id` | The type and the name disagree. |
| `user_email` that holds a user object | `user` | The name promises a string. |
| `delete_cart()` that only archives | `archive_cart()` | The name must match what happens. |
| `discount_percent = 0.15` | `discount_rate = 0.15` | `percent` suggests the scale 0 to 100. |
| `remaining_days` that holds seconds | `remaining_seconds` | A wrong unit causes silent defects. |

## Booleans

See [Booleans, collections, units and time](booleans-collections-units-time.md) and [Negation and optionality](negation-and-optionality.md).

| Bad | Better | Why |
|---|---|---|
| `paid_flag` | `is_paid` | `flag` says the type, not the meaning. |
| `disable_logging = False` | `is_logging_enabled = True` | A negative name with `False` is a double negative. |
| `valid` | `is_valid` | A bare adjective hides the type. |
| `discount` (as a boolean) | `has_discount` | A noun can be an amount, a code or a flag. |
| `not_shipped` | `is_shipped` (with the value `False`) | State the fact in the positive form. |
| `check_stock` (as a field) | `should_check_stock` | A bare verb reads as an action. |

## Collections

| Bad | Better | Why |
|---|---|---|
| `order_list` | `orders` | The plural already says that it is a collection. |
| `order` (a group of orders) | `orders` | A singular name for many objects misleads. |
| `num_items` | `item_count` | `num` could mean "number" or "numeric". |
| `sku_to_qty_dict` | `quantity_by_sku` | The name shows value and key. |
| `id_list` | `order_ids` | The name says what the ids belong to. |
| `items_array` | `line_items` | Do not put the type in the name. |

## Units and time

See [Booleans, collections, units and time](booleans-collections-units-time.md).

| Bad | Better | Why |
|---|---|---|
| `timeout = 30` | `timeout_seconds = 30` | The reader does not need to open the docs. |
| `price = 19.99` | `price_cents = 1999` | Integer money avoids rounding errors. |
| `created` | `created_at` | `_at` marks a timestamp. |
| `ttl = 3600` | `ttl_seconds = 3600` | A unit removes the guess. |
| `size` | `file_size_bytes` | `size` has many meanings. |
| `discount = 0.2` | `discount_rate = 0.2` | A ratio needs a clear word. |

## Functions

See [Functions](../python/functions.md) and [Action and context](action-context.md).

| Bad | Better | Why |
|---|---|---|
| `order_cancel()` | `cancel_order()` | Verb first reads as a command. |
| `check_stock(sku)` returning a boolean | `is_in_stock(sku)` | A boolean function uses `is_` or `has_`. |
| `do_checkout()` | `complete_checkout()` | `do` adds no meaning. |
| `get_and_save_user()` | `get_user()` and `save_user()` | `and` often hides two jobs. |
| `email(order)` | `send_order_email(order)` | `email` could be a noun or a verb. |
| `user_by_email()` | `find_user_by_email()` | A bare noun does not say if the code searches, creates or loads. |

## Classes

See [Classes](../python/classes.md) and [Class methods](../python/class_methods.md).

| Bad | Better | Why |
|---|---|---|
| `UserData` | `UserProfile` | `Data` is filler. |
| `PaymentHelper` | `PaymentGateway` | `Helper` hides the role. |
| `OrderUtil` | module `orders` with functions | Utility classes group functions that need no state. |
| `AbstractBaseOrderFactoryImpl` | `OrderFactory` | Remove layers of filler words. |
| `Order2` | `OrderSnapshot` | A number does not say how the class differs. |
| `Exception1` | `PaymentDeclinedError` | The class name states the failure. |

## Databases

See [Tables](../databases/tables.md), [Columns](../databases/columns.md), [Indexes](../databases/indexes.md) and [Enums](../databases/enums.md).

| Bad | Better | Why |
|---|---|---|
| `tbl_order` | `orders` | A table prefix repeats what the context shows. |
| `OrderID` | `order_id` | PostgreSQL folds unquoted names to lower case, so mixed case needs quotes. |
| `fk_user` | `customer_id` | Name a foreign key column after the key it holds. |
| `is_deleted TINYINT` | `deleted_at TIMESTAMP` | A timestamp says when. `NULL` says not deleted. |
| `idx1` | `idx_orders_customer_id` | The index name shows table and column. |
| `price FLOAT` | `price_cents BIGINT` | Integer minor units avoid rounding errors. |

## Tests

See [Tests](../python/tests.md).

| Bad | Better | Why |
|---|---|---|
| `test1()` | `test_cancel_order_refunds_payment()` | The test name states the rule. |
| `test_order()` | `test_create_order_rejects_empty_cart()` | One behaviour per test name. |
| `test_happy_path()` | `test_checkout_succeeds_with_valid_card()` | Name the case, not the mood. |
| `test_error()` | `test_checkout_fails_when_card_is_declined()` | The reader sees the cause and the result. |
| `test_it_works()` | `test_apply_coupon_reduces_total()` | `works` is not a check. |

## APIs

| Bad | Better | Why |
|---|---|---|
| `GET /getOrders` | `GET /orders` | The HTTP method is the verb. |
| `POST /orders/create` | `POST /orders` | Same reason. |
| `GET /order/{id}` | `GET /orders/{id}` | Resources are plural nouns. |
| `GET /orders?customerID=7` | `GET /orders?customer_id=7` | Keep one casing in query parameters. |
| `POST /orders/{id}/cancelOrder` | `POST /orders/{id}:cancel` | A custom method uses a colon and a verb. See [Google AIP-136](https://google.aip.dev/136). |
| `{"error": 5}` | `{"code": "PAYMENT_DECLINED"}` | A stable, readable code helps clients. |

## Events

| Bad | Better | Why |
|---|---|---|
| `CreateOrder` (as an event) | `order.created` | An event is a fact in the past. |
| `order_create_event` | `order.created` | The word `event` repeats the context. |
| `OrderUpdate` | `order.address_changed` | Say what changed. |
| `payment` (as a topic) | `payment.captured` | A topic names a kind of fact. |
| `process_refund` (as an event) | `refund.processed` | A command is `process_refund`. The event is `refund.processed`. |

## Metrics

| Bad | Better | Why |
|---|---|---|
| `requests` | `http_requests_total` | A counter ends with `_total`. See [Prometheus naming practices](https://prometheus.io/docs/practices/naming/). |
| `latency_ms` | `http_request_duration_seconds` | Prometheus recommends base units. |
| `errors` | `checkout_errors_total` | Say what fails. |
| `memoryUsage` | `process_memory_bytes` | One casing and an explicit unit. |
| label `user_id` on a metric | no `user_id` label | A label with many values makes too many series. |

## Configuration

| Bad | Better | Why |
|---|---|---|
| env `Timeout` | `PAYMENT_TIMEOUT_SECONDS` | Environment variables are upper case, with a scope and a unit. |
| `DISABLE_EMAIL=false` | `EMAIL_ENABLED=true` | Avoid a double negative. |
| env `db-url` | `DATABASE_URL` | A shell variable name cannot contain a hyphen. |
| Kubernetes name `OrderService` | `order-service` | Most Kubernetes object names are lower case with hyphens. See [Kubernetes object names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/). |
| flag `new_checkout_flag_2` | `checkout_new_payment_form` | The name states the feature and no longer needs a number. |

## Sources

- [Google AIP-136, Custom methods](https://google.aip.dev/136) — colon and verb for custom methods.
- [Prometheus naming practices](https://prometheus.io/docs/practices/naming/) — metric names, units and `_total`.
- [Kubernetes object names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/) — name constraints.
- [PostgreSQL lexical structure](https://www.postgresql.org/docs/current/sql-syntax-lexical.html) — folding of unquoted identifiers.
- [kettanaito/naming-cheatsheet](https://github.com/kettanaito/naming-cheatsheet) — naming heuristics.
