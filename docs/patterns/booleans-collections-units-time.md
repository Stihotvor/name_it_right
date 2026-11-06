---
status: new
---

# Booleans, collections, units and time

Four small decisions appear in almost every code base: how to name a flag, a group of things, a number with a unit, and a moment in time. This page gives a pattern for each one, with examples in Python, SQL, TypeScript and Go. A table of verb families at the end helps you to choose one verb per operation.

!!! success "General patterns"

    - Name a boolean as a statement that is true or false: `is_paid`, `has_discount`, `can_cancel`, `should_retry`, `must_verify`, `was_refunded`.
    - Use the positive form: `is_enabled`, not `is_not_disabled`.
    - Name a collection in the plural: `orders`, `line_items`. Name a map `<value>_by_<key>`: `orders_by_id`.
    - Name a count `<thing>_count`: `order_count`, `retry_count`.
    - Put the unit in the name when the type does not carry it: `timeout_seconds`, `amount_cents`, `file_size_bytes`.
    - Store money as integer minor units plus a currency code: `order_total_cents` and `currency_code`. `_cents` fits currencies with 100 minor units. For others, use `_minor_units`.
    - End a timestamp with `_at` and a date with `_on` or `_date`: `paid_at`, `delivered_on`.

!!! tip "Useful tips"

    - Read the boolean in an `if`: `if order.is_paid:` reads like speech. `if order.paid_flag:` does not.
    - Some languages and style guides choose other forms. Swift asks that a boolean reads as an assertion about the receiver, such as `x.isEmpty` or `a.intersects(b)`, and does not require a prefix for verb forms. .NET recommends an affirmative name and makes the `Is/Can/Has` prefix optional. See [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/#naming) and [Names of type members](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/names-of-type-members). This guide uses the `is_/has_/can_/should_` family as the project convention, not as a universal law.
    - If a language type carries the unit (`timedelta`, `time.Duration`), do not repeat the unit in the name.
    - For function names with the same prefixes, see [Functions](../python/functions.md). For variable rules, see [Variables](../python/variables.md). For column rules, see [Columns](../databases/columns.md).

!!! danger "General anti-patterns"

    - Flags: `paid_flag`, `discount_flag` → `is_paid`, `has_discount`
    - Negative booleans: `is_not_active`, `disable_cache = False` → `is_active`, `is_cache_enabled = True`
    - A singular name for a collection: `order = get_open_orders()` → `orders = get_open_orders()`
    - A bare number for a duration: `timeout = 30` → `timeout_seconds = 30`
    - A float for money: `price = 19.99` → `price_cents = 1999`
    - A timestamp with no zone information: `created = now()` → `created_at = now(tz=UTC)`

## Booleans

### Prefixes

| Prefix | Use it for | Python | TypeScript | SQL | Go |
|---|---|---|---|---|---|
| `is_` | A state | `is_paid` | `isPaid` | `is_paid` | `isPaid` |
| `has_` | Owning something | `has_discount` | `hasDiscount` | `has_discount` | `hasDiscount` |
| `can_` | Permission or ability | `can_cancel` | `canCancel` | `can_cancel` | `canCancel` |
| `should_` | A decision or advice | `should_retry` | `shouldRetry` | `should_retry` | `shouldRetry` |
| `must_` | A requirement | `must_verify_email` | `mustVerifyEmail` | `must_verify_email` | `mustVerifyEmail` |
| `was_` | A past fact | `was_refunded` | `wasRefunded` | `was_refunded` | `wasRefunded` |
| `will_` | A planned future fact | `will_renew` | `willRenew` | `will_renew` | `willRenew` |
| `allows_` | Permission granted by the object | `allows_guest_checkout` | `allowsGuestCheckout` | `allows_guest_checkout` | `allowsGuestCheckout` |

In Go, a name that starts a field in an exported struct begins with a capital letter: `IsPaid`. A local variable uses `isPaid`.

### Bad → better

| Bad | Better | Why |
|---|---|---|
| `paid_flag` | `is_paid` | `flag` says the type, not the meaning. |
| `status_ok` | `is_status_ok` | The prefix marks a boolean and reads as a statement in an `if`. |
| `is_not_disabled` | `is_enabled` | Double negatives make readers stop and think. |
| `disable_notifications = False` | `should_send_notifications = True` | A negative name with `False` becomes a double negative. |
| `no_discount` | `has_discount` | State the fact in the positive form. |
| `discount` (as a boolean) | `has_discount` | A noun can be an amount, a code or a flag. |
| `check_stock` (as a field) | `should_check_stock` | A verb alone reads as an action, not as a value. |
| `cart_empty()` | `is_cart_empty()` | The prefix tells the reader the result is a boolean. |
| `valid` | `is_valid` | A bare adjective hides the type. |
| `guest` | `is_guest` | `guest` could be a user object. |
| `order.refund` | `order.was_refunded` | The prefix shows a fact about the past. |
| `email_verified_boolean` | `is_email_verified` | Never put the type in the name. |

## Collections and counts

### Patterns

| Pattern | Rule | Python | TypeScript | SQL | Go |
|---|---|---|---|---|---|
| List | Plural noun | `orders` | `orders` | `orders` | `orders` |
| Map | `<value>_by_<key>` | `orders_by_id` | `ordersById` | n/a (a table keyed by id) | `ordersByID` |
| Unique values | `unique_<items>` | `unique_skus` | `uniqueSkus` | n/a (use `DISTINCT`) | `uniqueSKUs` |
| Count | `<thing>_count` | `order_count` | `orderCount` | `order_count` | `orderCount` |
| Sum of money | `<owner>_total_<value>` | `order_total_cents` | `orderTotalCents` | `order_total_cents` | `orderTotalCents` |
| Index | `<thing>_index` | `item_index` | `itemIndex` | `item_index` | `itemIndex` |
| Id list | `<thing>_ids` | `order_ids` | `orderIds` | `order_ids` | `orderIDs` |
| Batch | `<thing>_batch` | `order_batch` | `orderBatch` | `order_batch` | `orderBatch` |
| Page | `<thing>_page` | `order_page` | `orderPage` | `order_page` | `orderPage` |

!!! note "Id casing"

    Go style writes initialisms in capitals: `orderID`, `orderIDs`. Python and SQL use lower case. TypeScript commonly writes `orderId`.

### Bad → better

| Bad | Better | Why |
|---|---|---|
| `order_list` | `orders` | The plural already says that it is a collection. |
| `orders` (one order) | `order` | A plural name for one object misleads. |
| `order_dict` | `orders_by_id` | `by_id` states the key. The type is not in the name. |
| `orders_map` | `orders_by_id` | A map without a key name hides how to look up. |
| `num_orders` | `order_count` | `num` can mean "number" or "numeric". |
| `orders_len` | `order_count` | `len` is a function name, not a domain word. |
| `count` | `retry_count` | A bare `count` does not say what is counted. |
| `i` (index of an item) | `item_index` | One-letter names are fine only in tiny loops. |
| `id_list` | `order_ids` | The name says what the ids belong to. |
| `data` | `order_summary` | `data` fits any variable. Use a name that says what the data is. |
| `total` (number of rows) | `row_count` | `total` can also be a money sum. Count with `_count`. |
| `items_array` | `line_items` | Never put the type in the name. |

!!! warning "Count or total?"

    `order_count` is the number of orders. `order_total_cents` is a sum of money for an order. Do not mix the two.

## Units, money and ratios

### Units in names

| Quantity | Name | Unit | Why |
|---|---|---|---|
| Timeout | `timeout_seconds` | seconds | No guess about seconds or milliseconds. |
| Retry delay | `retry_delay_ms` | milliseconds | The short form `ms` is common and clear. |
| Cache lifetime | `cache_ttl_seconds` | seconds | TTL needs a unit. |
| File size | `file_size_bytes` | bytes | `size` alone could be KB or MB. |
| Upload limit | `max_upload_megabytes` | megabytes | `mb` could mean megabytes or megabits. |
| Distance | `distance_km` | kilometres | Avoids a mix of miles and km. |
| Weight | `package_weight_grams` | grams | Shipping systems often use grams or ounces. |
| Temperature | `temperature_celsius` | °C | Kelvin and Fahrenheit also exist. |
| Rate limit | `requests_per_minute` | per minute | The period is part of the meaning. |
| Bandwidth | `bandwidth_mbps` | megabits per second | Avoids confusion with megabytes. |

!!! note "Unit symbols"

    Standard unit symbols such as `ms`, `km` and `mbps`, and standard acronyms such as `ttl`, are exceptions to the full-words rule. Write them in lower case. Spell out a unit when two readings are possible.

### Money

Store money as an integer amount in minor units, with an ISO 4217 currency code. Floating-point numbers cannot store `0.1` exactly. The [ISO 20022 message definitions](https://www.iso20022.org/iso-20022-message-definitions) pair every amount with a currency code. ISO 20022 uses decimal amounts in major units, so convert at the system boundary. [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) defines the codes and the number of minor-unit digits.

| Concept | Name | Example value | Why |
|---|---|---|---|
| Total in minor units | `order_total_cents` | `1999` | Integers avoid rounding errors. |
| Currency | `currency_code` | `"EUR"` | Use the three-letter ISO 4217 code. |
| Tax | `tax_amount_cents` | `320` | Same unit as the total. |
| Discount | `discount_amount_cents` | `500` | `discount` alone could be a percent. |
| Refund | `refunded_amount_cents` | `1999` | Past participle shows a fact. |
| Exchange rate | `eur_to_usd_rate` | `1.0842` | A rate between two currencies. Name the pair. |
| Fee rate | `fee_rate` | `0.029` | A ratio from 0 to 1. |
| Rounding | `rounding_mode` | `"half_even"` | Name the rule, not the code. |

Use `_cents` only for currencies with 100 minor units. For currencies with another number of minor units, use `_minor_units`: `order_total_minor_units`.

### Ratios and percentages

In this guide, `rate` means a ratio. For events per period, put the period in the name: `requests_per_minute`.

| Name | Meaning | Example value | Why |
|---|---|---|---|
| `discount_rate` | Ratio from 0 to 1 | `0.15` | `rate` says "ratio", not "percent". |
| `discount_percent` | Number from 0 to 100 | `15` | `percent` states the scale. |
| `conversion_ratio` | Ratio of two counts | `0.032` | A ratio has no unit. |
| `error_rate` | Errors per request | `0.001` | Same scale as `discount_rate`. |
| `tax_basis_points` | Parts per 10,000 | `250` | `basis_points` avoids decimals. |

## Time

### Timestamps, dates and durations

| Concept | Python | SQL | TypeScript | Go | Why |
|---|---|---|---|---|---|
| Moment an event happened | `paid_at` | `paid_at` | `paidAt` | `paidAt` | `_at` marks a timestamp. |
| Moment in UTC | `created_at_utc` | `created_at_utc` | `createdAtUtc` | `createdAtUTC` | State the zone when it is not obvious. |
| Calendar date | `delivered_on` | `delivered_on` | `deliveredOn` | `deliveredOn` | `_on` marks a date without a time. |
| Birth date | `birth_date` | `birth_date` | `birthDate` | `birthDate` | `_date` also works for a date. |
| Duration | `session_duration_seconds` | `session_duration_seconds` | `sessionDurationSeconds` | `sessionDuration` (type `time.Duration`) | The unit is in the name, unless the type carries it. |
| Expiry moment | `expires_at` | `expires_at` | `expiresAt` | `expiresAt` | Points to a moment. |
| Time to live | `ttl_seconds` | `ttl_seconds` | `ttlSeconds` | `ttl` (type `time.Duration`) | Duration, not a moment. |
| Start and end | `starts_at`, `ends_at` | `starts_at`, `ends_at` | `startsAt`, `endsAt` | `startsAt`, `endsAt` | A matching pair. |

### Bad → better

| Bad | Better | Why |
|---|---|---|
| `timeout = 30` | `timeout_seconds = 30` | The reader does not need to open the docs. |
| `created` | `created_at` | `created` could be a boolean or an object. |
| `date` (timestamp) | `occurred_at` | A timestamp is not a date. Use a verb in the past tense that fits the event. |
| `delivery_time` (a date) | `delivered_on` | `time` could be a duration. |
| `ttl = 3600` | `ttl_seconds = 3600` | A unit removes the guess. |
| `price = 19.99` | `price_cents = 1999` | Integer money avoids rounding errors. |
| `amount` | `amount_cents` | A bare `amount` hides the unit. |
| `tax = 0.2` | `tax_rate = 0.2` | `tax` could be an amount. |
| `expiry` | `expires_at` | A noun does not say if it is a date or a duration. |
| `created_at` (naive local time) | `created_at` stored as UTC, or `created_at_local` | A name may claim UTC only if the value is UTC. Convert first, or say `local`. |
| `retry_interval = 5` | `retry_interval_seconds = 5` | A bare number hides the unit. |
| `size` | `file_size_bytes` | `size` has many meanings. |

!!! info "Metrics use base units"

    Prometheus recommends base units without prefixes: seconds, bytes and meters. A metric name ends with the unit, for example `http_request_duration_seconds`. See [Prometheus naming practices](https://prometheus.io/docs/practices/naming/).

## Verb families

Use this table to choose one verb per operation. Keep the same verb in the whole code base. See the [glossary](../common/references-and-glossary.md).

| Verb | Meaning | Example 1 | Example 2 | Example 3 |
|---|---|---|---|---|
| `get` | Read known data cheaply | `get_order` | `get_user_email` | `get_order_total` |
| `find` | Search, may return nothing | `find_user_by_email` | `find_product_by_sku` | `find_open_cart` |
| `list` | Return a collection | `list_open_orders` | `list_active_coupons` | `list_user_addresses` |
| `calculate` | Compute a value | `calculate_cart_subtotal` | `calculate_cart_tax` | `calculate_shipping_cost` |
| `create` | Make a new record | `create_order` | `create_refund` | `create_shipment` |
| `update` | Change a record | `update_shipping_address` | `update_cart_item` | `update_payment_method` |
| `delete` | Remove a record | `delete_expired_carts` | `delete_draft_order` | `delete_saved_card` |
| `validate` | Check without changing | `validate_coupon` | `validate_address` | `validate_order` |
| `send` | Cause a message to go out | `send_receipt_email` | `send_shipping_notice` | `send_payment_reminder` |
| `cancel` | Stop a process | `cancel_order` | `cancel_subscription` | `cancel_shipment` |

## Sources

- [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/#naming) — boolean names read as assertions.
- [Names of type members, .NET design guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/names-of-type-members) — affirmative boolean names.
- [Google AIP-141, Quantities](https://google.aip.dev/141) — units in field names.
- [ISO 20022 message definitions](https://www.iso20022.org/iso-20022-message-definitions) — amount with currency code.
- [ISO 4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html) — three-letter currency codes.
- [Prometheus naming practices](https://prometheus.io/docs/practices/naming/) — base units and unit suffixes.
- [kettanaito/naming-cheatsheet](https://github.com/kettanaito/naming-cheatsheet) — boolean prefixes and plural names.
