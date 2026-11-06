!!! success "General patterns"
    
    - Booleans should start with `is_`, `has_`, `should_`: `has_completed`, `is_ready`, `should_retry`
    - Use plural nouns for collections: `users = []`, `pending_orders = {}`, `active_sessions = set()`
    - Include metric units in the name: `delay_seconds`, `velocity_meters`, `timeout_ms`, `buffer_size_kb`
    - Use `_count`, `_index`, `_total` suffixes for numeric counters: `retry_count`, `page_index`, `order_total`
    - Use `previous_` / `next_` for paired state variables: `previous_cursor`, `next_offset`
    - Use `new_` / `old_` for before-and-after comparison: `new_email`, `old_email`
    - Type-annotate all variables, especially when the type is not obvious from the value
    - Name negative booleans as the positive condition to avoid double negatives: `is_empty` not `is_not_empty`

    ```py
    # Well-named variables in an e-commerce checkout
    customer: Customer = fetch_customer(session_id)
    is_cart_empty: bool = cart.item_count == 0
    available_discounts: list[Discount] = discount_service.list_active()
    selected_shipping_method: ShippingMethod | None = None
    total_weight_grams: int = sum(item.weight_g for item in cart.items)
    retry_attempts_remaining: int = 3
    ```

!!! tip "Useful tips"
    
    - Use `i`, `j`, `k` as loop counters — this is the only acceptable exception to the one-letter rule and only inside tight loop scopes
    - For short-lived scope variables, add a `_tmp` or `_buf` suffix: `parsed_tmp`, `serialized_buf`
    - In list/dict comprehensions, prefer descriptive names for the iteration variable: `(user for user in users if user.is_active)` not `(x for x in xs if x.is_active)`
    - Use `_` as a throwaway variable name when the value is intentionally unused: `_, status = result`
    - Align variable names with the domain language from the spec or product requirements

!!! danger "General anti-patterns"
    
    - Abbreviations: `dstr = 100.12`
    - One-letter variables outside tight loops: `v = 'comis'`
    - Generic names like `data`, `info`, `tmp`, `thing`, `obj` — they convey zero intent
    - Negative boolean names: `is_not_empty`, `has_no_error` (forces mental double-negation)
    - Hungarian notation: `strName`, `intCount`, `dictUsers` (type info in a typed language is noise)
    - Redundant prefixes: `my_variable`, `the_value`, `local_var` (adds length, adds nothing)
    - Shadowing built-in names: `list`, `str`, `id` — they look valid but silently break the corresponding function

## Examples by kind

The tables below show one naming pattern for each kind of variable. The examples use an e-commerce checkout. For the rules behind them, see [Booleans, collections, units and time](../patterns/booleans-collections-units-time.md) and [Negation and optionality](../patterns/negation-and-optionality.md).

### Booleans

| Kind | Pattern | Examples |
|---|---|---|
| State | `is_<state>` | `is_paid`, `is_cart_empty`, `is_guest` |
| Ownership | `has_<thing>` | `has_discount`, `has_gift_wrap`, `has_saved_card` |
| Ability | `can_<action>` | `can_cancel`, `can_refund`, `can_ship_express` |
| Decision | `should_<action>` | `should_retry`, `should_send_receipt`, `should_notify_customer` |
| Requirement | `must_<action>` | `must_verify_email`, `must_accept_terms` |
| Past fact | `was_<participle>` | `was_refunded`, `was_restocked` |
| Switch | `is_<feature>_enabled` | `is_express_shipping_enabled`, `is_logging_enabled` |

### Collections, mappings and counts

| Kind | Pattern | Examples |
|---|---|---|
| List | plural noun | `orders`, `line_items`, `pending_refunds` |
| Set | plural noun, or `unique_<items>` | `unique_skus`, `active_sessions` |
| Mapping | `<value>_by_<key>` | `orders_by_id`, `quantity_by_sku`, `prices_by_currency` |
| Count | `<thing>_count` | `order_count`, `retry_count`, `failed_payment_count` |
| Ids | `<thing>_ids` | `order_ids`, `coupon_ids` |
| Batch | `<thing>_batch` | `order_batch`, `refund_batch` |
| Index | `<thing>_index` | `item_index`, `page_index`, `row_index` |

### Units, time and money

| Kind | Pattern | Examples |
|---|---|---|
| Duration | `<thing>_<unit>` | `timeout_seconds`, `retry_delay_ms`, `session_ttl_seconds` |
| Size | `<thing>_<unit>` | `file_size_bytes`, `package_weight_grams`, `buffer_size_kb` |
| Timestamp | `<event>_at` | `paid_at`, `shipped_at`, `expires_at` |
| Date | `<event>_on` | `delivered_on`, `birth_date` |
| Money | `<thing>_cents` plus `currency_code` | `total_cents`, `tax_cents`, `currency_code` |
| Ratio | `<thing>_rate` | `discount_rate`, `tax_rate`, `error_rate` |

### Optional, comparison and state

| Kind | Pattern | Examples |
|---|---|---|
| Optional | the plain name, with `X \| None` | `selected_shipping_method: ShippingMethod \| None`, `coupon_code: str \| None` |
| Before and after | `old_` and `new_` | `old_email`, `new_email`, `old_quantity`, `new_quantity` |
| Neighbours | `previous_` and `next_` | `previous_page`, `next_page` |
| Accumulator | `<running>_<thing>` or `total_<thing>` | `running_total_cents`, `total_items_packed` |
| Cursor | `<thing>_cursor` | `order_cursor`, `next_page_cursor` |
| Flag state | `is_<state>` with the positive form | `is_active`, not `is_not_inactive` |
| Loop item | singular of the collection | `for order in orders`, `for line_item in line_items` |

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `paid_flag` | `is_paid` | `flag` says the type, not the meaning. |
| `orders_list` | `orders` | The plural already says that it is a collection. |
| `order_dict` | `orders_by_id` | `by_id` states the key. The type is not in the name. |
| `num_items` | `item_count` | `num` could mean "number" or "numeric". |
| `i` (an item index) | `item_index` | A one-letter name is fine only in a tight loop. |
| `timeout = 30` | `timeout_seconds = 30` | The unit is in the name. |
| `price = 19.99` | `price_cents = 1999` | Integer money avoids rounding errors. |
| `created` | `created_at` | `_at` marks a timestamp. |
| `ttl = 3600` | `ttl_seconds = 3600` | A unit removes the guess. |
| `discount = 0.2` (a ratio) | `discount_rate = 0.2` | A ratio needs a clear word. |
| `coupon = ""` | `coupon_code = None` | Absence is not an empty string. |
| `prev` | `previous_cursor` | Spell out the word and name the thing. |
| `emails` (one address) | `email` | A plural name for one value misleads. |
| `data` | `order_summary` | `data` fits any variable. |
| `disable_cache = False` | `is_cache_enabled = True` | A negative name with `False` is a double negative. |
| `list = get_orders()` | `orders = get_orders()` | `list` shadows the built-in. |

!!! info "See also"

    - [Functions](functions.md) for functions that return these values
    - [Bad → better cookbook](../patterns/cookbook.md) for more rewrites
    - [Glossary](../common/references-and-glossary.md) for verbs, nouns and suffixes
