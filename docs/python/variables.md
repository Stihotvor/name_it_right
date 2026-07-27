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
