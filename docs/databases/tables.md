!!! success "General patterns"

    - Use `snake_case` and plural nouns: `users`, `orders`, `order_items`, `shipping_addresses`
    - Use singular nouns for lookup / enum tables: `country`, `currency`, `order_status`
    - Junction (many-to-many) tables: combine both entity names, listing the primary/owner entity first: `user_roles`, `order_products`, `student_courses`
    - Junction table PK: use a composite key `(a_id, b_id)`, not a surrogate `id`
    - Use a single-word name when possible; two words if needed: `invoice` not `customer_invoice_data`

!!! tip "Useful tips"

    - Avoid prefixes and suffixes: `users` not `tbl_users` or `users_table`
    - Keep table names under 30 characters for cross-database portability
    - Use consistent singular/plural — plural for rows (collections), singular for dictionaries (status, type)

!!! danger "General anti-patterns"

    - Prefixes like `tbl_`, `tab_`, `tb_` — they add noise and serve no purpose
    - Names like `Table1`, `tmp`, `test` — never commit these
    - Including the database or schema name in the table name: `app_users` inside the `app` schema
