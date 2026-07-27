!!! success "General patterns"

    - Use `snake_case`: `first_name`, `created_at`, `order_total`
    - Primary key: `id` (surrogate) or a descriptive natural key: `email`, `slug`
    - Foreign key: `<referenced_table_singular>_id`: `user_id`, `order_id`, `country_code`
    - Boolean columns: `is_` or `has_` prefix: `is_active`, `has_shipped`, `is_available`
    - Timestamps: `_at` suffix: `created_at`, `updated_at`, `deleted_at`, `expires_at`
    - Dates: `_date` suffix: `start_date`, `end_date`, `birth_date`
    - Counters: `_count` suffix: `login_count`, `retry_count`, `item_count`
    - Monetary values: include currency or unit: `amount_cents`, `price_usd`, `balance_btc`

!!! tip "Useful tips"

    - Don't repeat the table name in a column name: `users.name` not `users.user_name`
    - Use the same column name across tables for the same concept: `created_at` everywhere, not `created` in one table and `created_at` in another
    - Name soft-delete columns consistently: `deleted_at` (nullable timestamp) is clearer than a boolean `is_deleted` for point-in-time recovery
    - For polymorphic foreign keys, use `<target>_type` and `<target>_id`: `document_type`, `document_id`

!!! danger "General anti-patterns"

    - Hungarian prefixes: `vc_name`, `i_id`, `dt_created` — type info belongs in the schema, not the name
    - Abbreviations that save only 1-2 characters: `cust_addr` → `customer_address`, `qty` → `quantity`
    - Generic names like `value`, `code`, `type`, `desc` in tables where they could mean anything
    - Using reserved words: `order`, `group`, `select`, `from`, `table` — wrap in quotes everywhere or just rename
