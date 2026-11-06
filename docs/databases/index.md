# Databases

General naming conventions for database schemas — tables, columns, indexes, constraints, and relationships.

!!! success "General patterns"

    - Use `snake_case` for all database identifiers
    - Be consistent: the same concept should have the same name across every table
    - Use descriptive names that reflect the business domain
    - Explicitly name every constraint — auto-generated names are unreadable in error logs

!!! tip "Useful tips"

    - Design the schema before writing migrations — naming decisions affect every query
    - Keep a data dictionary for your team to align on column meanings
    - Prefer singular names for lookup tables and plural for data tables

---

<div class="grid cards" markdown>

-   __Tables__

    ---

    Plural nouns, junction tables, lookup tables — schema-level naming.

    [:octicons-arrow-right-24: Tables](tables.md)

-   __Columns__

    ---

    Foreign keys, booleans, timestamps, counters, monetary values — column-level conventions.

    [:octicons-arrow-right-24: Columns](columns.md)

-   __Indexes__

    ---

    `idx_` and `uq_` prefixes, index kinds, column order in composite indexes.

    [:octicons-arrow-right-24: Indexes](indexes.md)

-   __Constraints__

    ---

    Primary keys, foreign keys, check constraints — `pk_`, `fk_`, `chk_` naming.

    [:octicons-arrow-right-24: Constraints](constraints.md)

-   __Enumerated columns__

    ---

    Database enums, lookup tables, CHECK constraints — when to use what.

    [:octicons-arrow-right-24: Enums](enums.md)

-   __Warehouse and analytics__

    ---

    dbt layers, medallion layers, fact and dimension tables, keys, SCD type 2.

    [:octicons-arrow-right-24: Warehouse](warehouse.md)

</div>

## Naming examples by context

### E-commerce schema

| Table | Columns | Notes |
|---|---|---|
| `users` | `id`, `email`, `first_name`, `last_name`, `is_active`, `created_at` | Plural, natural PK on `email` |
| `orders` | `id`, `user_id`, `status`, `total_cents`, `currency`, `shipped_at`, `created_at` | `total_cents` = int, avoids float rounding |
| `order_items` | `id`, `order_id`, `product_id`, `quantity`, `unit_price_cents` | Junction table |
| `products` | `id`, `sku`, `name`, `price_cents`, `is_available`, `stock_count` | `sku` = natural secondary key |
| `shipping_addresses` | `id`, `user_id`, `street`, `city`, `country_code`, `is_default` | One user can have many addresses |

!!! info "See also"

    - [Naming patterns](../patterns/index.md) for rules about booleans, units and time
    - [Languages](../languages/index.md) for the case style in the code that reads these tables
    - [REST](../systems/rest.md) and [Events](../systems/events.md) for the same names in an API and in messages
    - [Examples](../examples/index.md) for complete schemas in seven domains
