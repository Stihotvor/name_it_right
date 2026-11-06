!!! success "General patterns"

    - Use `snake_case` and plural nouns: `users`, `orders`, `order_items`, `shipping_addresses`
    - Use singular nouns for lookup / enum tables: `country`, `currency`, `order_status`
    - Junction (many-to-many) tables: combine both entity names, listing the primary/owner entity first: `user_roles`, `product_categories`, `student_courses`
    - Junction table PK: for a pure link table, use a composite key `(a_id, b_id)`, not a surrogate `id`. If the same pair can repeat, such as two redemptions of one coupon, use a surrogate `id`
    - Use a single-word name when possible; two words if needed: `invoices` not `customer_invoice_data`

!!! tip "Useful tips"

    - Avoid prefixes and suffixes: `users` not `tbl_users` or `users_table`
    - Keep table names under 30 characters for cross-database portability
    - Use consistent singular/plural — plural for rows (collections), singular for dictionaries (status, type)

!!! danger "General anti-patterns"

    - Prefixes like `tbl_`, `tab_`, `tb_` — they add noise and serve no purpose
    - Names like `Table1`, `tmp`, `test` — never commit these
    - Including the database or schema name in the table name: `app_users` inside the `app` schema

## Singular or plural?

Both styles work. Choose one style and use it for all tables of the same kind.

| Style | Examples | Who uses it | Why choose it |
|---|---|---|---|
| Plural for entity tables | `users`, `orders`, `order_items` | Rails: [Active Record basics](https://guides.rubyonrails.org/active_record_basics.html) names tables in the plural | A table holds many rows. Queries read well: `FROM orders`. |
| Singular for lookup tables | `country`, `currency`, `order_status` | This guide | A lookup table is a dictionary of values. |
| Singular for all tables | `user`, `order`, `order_item` | Some teams | The table name matches the model name. `order` and `user` are reserved words in PostgreSQL, so they need quotes. |
| App prefix plus model name | `shop_order`, `shop_orderitem` | Django: see [model options](https://docs.djangoproject.com/en/5.1/ref/models/options/) for `db_table` | The default is the app label, an underscore and the lower-case model name, with no underscores inside it. Set `db_table` to get other names. |

This guide uses plural names for entity tables and singular names for lookup tables. A container noun stays singular: `audit_log`, `job_queue`, `order_history`, `order_archive`.

## Examples by kind

The tables use an e-commerce checkout. For column names inside these tables, see [Columns](columns.md).

### Entity and junction tables

| Table | Kind | Meaning | Why this name |
|---|---|---|---|
| `customers` | Entity | The people who buy. | A plural noun. |
| `orders` | Entity | The purchases. | A plural noun. |
| `order_items` | Dependent entity | The lines of an order. | The owner first, then the part. |
| `shipping_addresses` | Entity | Addresses for delivery. | A plural noun with a clear role. |
| `product_categories` | Junction | Links products to categories. | Both entity names. |
| `customer_roles` | Junction | Links customers to roles. | The owner first. |
| `coupon_redemptions` | Junction with data | A customer used a coupon. | A domain word for a link with its own attributes. |
| `enrollments` | Junction with data | A student takes a course. | Name the meaning, not both table names. |

A junction table with extra data usually has its own domain name. `order_items` carries quantity and price, so it is not named `order_products`.

### Lookup tables

| Table | Meaning | Why this name |
|---|---|---|
| `country` | ISO countries. | A dictionary, singular. |
| `currency` | ISO 4217 currencies. | A dictionary, singular. |
| `order_status` | Allowed order states. | A dictionary, singular. |
| `payment_method` | Allowed ways to pay. | A dictionary, singular. |
| `shipping_carrier` | Known carriers. | A dictionary, singular. |

For enum types and their values, see [Enums](enums.md).

!!! warning "Name clash in PostgreSQL"

    PostgreSQL makes a row type with the name of each table. A table `order_status` and an enum type `order_status` in the same schema collide. Use a table or an enum, not both.

### History, version and audit tables

| Table | Meaning | Why this name |
|---|---|---|
| `order_history` | Every past state of an order, as rows. | `_history` for time-ordered copies. |
| `order_status_history` | Only the status changes of an order. | Narrow the scope in the name. |
| `product_versions` | Every saved version of a product. | `_versions` when users read old versions. |
| `document_revisions` | Edits of a document. | `_revisions` for edit trails. |
| `price_changes` | One row per price change. | A change log with a clear subject. |
| `audit_log` | Who changed what, for all tables. | One shared log with a generic scope. |
| `order_archive` | Orders moved out of the live table. | `_archive` for rows that left the live table. Prefer a `deleted_at` column unless rows must leave. |

### Partition, event and queue tables

| Table | Meaning | Why this name |
|---|---|---|
| `orders_2026_11` | The partition of `orders` for November 2026. | The parent name plus the range. |
| `orders_2026_12` | The next monthly partition. | Same pattern, so partitions sort. |
| `orders_default` | Rows that match no other partition. | `_default` for the catch-all. |
| `events_p0`, `events_p1` | Hash partitions of `events` in PostgreSQL. | `p` and the number. In MySQL, `p0` is a partition name inside the table, not a table. |
| `outbox_events` | Events that wait to be published. | The pattern name plus the content. |
| `job_queue` | Background jobs that wait to run. | A container noun stays singular. |
| `webhook_deliveries` | Each attempt to call a webhook. | A plural noun for events with a result. |

### Bridge, fact and dimension tables

The prefixes `fact_`, `dim_` and `bridge_` name the role of the table in an analytics model. They do not repeat the object type, so they do not break the rule against prefixes. Some teams use `dim_date` (singular) and dbt projects often use `fct_` for facts. Choose one form for the project.

| Table | Kind | Meaning | Why this name |
|---|---|---|---|
| `fact_orders` | Fact | One row per order. | `fact_` marks a fact table. |
| `fact_order_items` | Fact | One row per order line. | A finer grain than `fact_orders`. |
| `dim_customers` | Dimension | Customer attributes. | `dim_` marks a dimension. |
| `dim_products` | Dimension | Product attributes. | Same prefix. |
| `dim_dates` | Dimension | One row per calendar day. | A date dimension. |
| `bridge_order_promotions` | Bridge | Links orders to many promotions. | `bridge_` links a fact to a multivalued dimension (Kimball). |

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `tbl_orders` | `orders` | A prefix repeats what the context shows. |
| `orders_table` | `orders` | A suffix repeats the object type. |
| `Order` | `orders` | PostgreSQL folds an unquoted `Order` to `order`, a reserved word, so queries fail. |
| `order_product` (with quantity and price) | `order_items` | A link with data has a domain name. |
| `user_role_map` | `user_roles` | `map` adds nothing. |
| `customer_invoice_data` | `invoices` | `data` is filler, and the owner is clear. |
| `orders_old` | `order_history` or a partition `orders_2025_12` | `old` has no date and no meaning. |
| `orders_backup_final2` | `order_archive` | Version words in names rot. |
| `temp`, `test1` | name the real purpose | Never commit these. |
| `app_users` (inside schema `app`) | `users` | The schema already gives the scope. |
| `statuses` (a dictionary) | `order_status` | Lookup tables are singular in this guide. |
| `log` | `audit_log` or `webhook_deliveries` | A bare `log` has no scope. |

!!! info "See also"

    - [Columns](columns.md), [Indexes](indexes.md), [Constraints](constraints.md) and [Enums](enums.md)
    - [Bad → better cookbook](../patterns/cookbook.md) for more rewrites
    - [Symmetry](../patterns/symmetry.md) for pairs such as `source` and `target`
