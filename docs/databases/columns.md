!!! success "General patterns"

    - Use `snake_case`: `first_name`, `created_at`, `order_total`
    - Primary key: `id` (surrogate) or a descriptive natural key: `email`, `slug`
    - Foreign key: `<referenced_table_singular>_id`: `user_id`, `order_id`, `country_code`
    - Boolean columns: `is_` or `has_` prefix: `is_active`, `has_shipped`, `is_available`
    - Timestamps: `_at` suffix: `created_at`, `updated_at`, `deleted_at`, `expires_at`
    - Dates: `_date` suffix: `start_date`, `end_date`, `birth_date`
    - Counters: `_count` suffix: `login_count`, `retry_count`, `item_count`
    - Monetary values: include currency or unit: `amount_cents`, `price_cents` with `currency_code`, `balance_btc`

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

## Examples by kind

The tables use an e-commerce checkout. The patterns follow [Booleans, collections, units and time](../patterns/booleans-collections-units-time.md). In SQL, all names use `snake_case`.

### Audit columns

| Column | Type idea | Meaning | Why this name |
|---|---|---|---|
| `created_at` | timestamp with time zone | When the row was inserted. | `_at` marks a moment. |
| `updated_at` | timestamp with time zone | When the row last changed. | Same suffix as `created_at`. |
| `deleted_at` | timestamp with time zone, nullable | When the row was soft-deleted. `NULL` means live. | A timestamp says when. A boolean does not. |
| `created_by_user_id` | foreign key to `users` | Who created the row. | A role plus the table: `<role>_<table_singular>_id`. |
| `updated_by_user_id` | foreign key to `users` | Who changed the row last. | Same pattern. |
| `row_version` | integer | A counter for optimistic locking. | `version` alone could mean a product version. |
| `source_system` | text | Where the row came from. | Names the origin, not the type. |

### Money and currency

Store money as an integer in minor units plus a currency code. For other approaches, see [Booleans, collections, units and time](../patterns/booleans-collections-units-time.md).

| Column | Type idea | Meaning | Why this name |
|---|---|---|---|
| `total_amount_cents` | bigint | The order total in cents. | The unit is in the name. Inside `orders`, drop the `order_` prefix. |
| `tax_amount_cents` | bigint | The tax part of the total. | Same unit as the total. |
| `discount_amount_cents` | bigint | The discount in cents. | `discount` alone could be a rate. |
| `currency_code` | char(3) | The ISO 4217 code, such as `EUR`. | `code` states the format. |
| `unit_price_minor_units` | bigint | The price in minor units for currencies that do not use cents. | `_minor_units` replaces `_cents` for other currencies. |
| `eur_to_usd_rate` | numeric | The rate from euro to US dollar. | Name the direction of the rate. |
| `discount_rate` | numeric | The discount as a ratio from 0 to 1. | `rate` marks a ratio. |

### Temporal columns

| Column | Type idea | Meaning | Why this name |
|---|---|---|---|
| `starts_at` | timestamp with time zone | When an offer begins. | A matching pair with `ends_at`. |
| `ends_at` | timestamp with time zone | When an offer ends. | Same suffix. |
| `valid_from` | timestamp with time zone | Start of a validity period. | A pair with `valid_to`. A common exception to the `_at` rule. |
| `valid_to` | timestamp with time zone, nullable | End of a validity period. `NULL` means open. | Document whether the end is included. |
| `birth_date` | date | A calendar date. | `_date` marks a date with no time. |
| `delivery_date` | date | The planned delivery day. | Same suffix. |
| `expires_at` | timestamp with time zone, nullable | When a token stops working. | `NULL` can mean it never expires. |
| `last_login_at` | timestamp with time zone, nullable | The last login moment. | `last_` plus a timestamp name. |

### JSON and array columns

The type ideas use PostgreSQL names. The column names apply to any JSON type. MySQL has `JSON` and no array type. SQL Server stores JSON as text, or in a native `json` type on newer versions, and has no array type.

| Column | Type idea | Meaning | Why this name |
|---|---|---|---|
| `raw_payload` | jsonb | The original webhook body. | Names the content, not the type. |
| `shipping_options` | jsonb | A bag of options for shipping. | A plural noun for a group. |
| `attributes` | jsonb | Flexible product attributes. | The content word, not `data`. |
| `settings` | jsonb | Per-account settings. | A common noun for configuration. |
| `tags` | text array | The labels of a product. | A plural noun for an array. |
| `allowed_country_codes` | text array | The countries where an offer runs. Array elements cannot have a foreign key. | Plural and states the format. |

Do not put the type in the name: `tags_array` and `settings_json` repeat what the schema says. Use an array only for a small list that you never join. For anything else, use a junction table (see [Tables](tables.md)).

### Tenant, polymorphic and enum columns

| Column | Type idea | Meaning | Why this name |
|---|---|---|---|
| `tenant_id` | foreign key | The customer account that owns the row. | The same name in every table. |
| `organization_id` | foreign key | The company that owns the row. | `<table_singular>_id` pattern. |
| `owner_type` | text | The kind of record that owns this row, such as `order`. | `<target>_type` pairs with `<target>_id`. |
| `owner_id` | bigint | The id of the owning record. | Pairs with `owner_type`. |
| `commentable_type` | text | The kind of record that has the comment. | A role word ending in `able` is common in Rails. |
| `commentable_id` | bigint | The id of that record. | Pairs with `commentable_type`. |
| `status` | enum or text | The state of the order. | Do not repeat the table name: `orders.status`. |
| `payment_method` | enum or text | How the customer pays. | A noun for the choice. |
| `shipping_carrier` | enum or text | The carrier that delivers. | A noun for the choice. |

A polymorphic `_id` cannot have a foreign key constraint. Prefer one nullable foreign key per target when the set of targets is small. For enum types and their values, see [Enums](enums.md).

### Booleans, counters and units

| Column | Type idea | Meaning | Why this name |
|---|---|---|---|
| `is_active` | boolean | The row is in use. | The positive form. |
| `has_gift_wrap` | boolean | The order has gift wrap. | `has_` marks ownership. |
| `item_count` | integer | The number of items in the cart. | `_count` marks a counter. |
| `retry_count` | integer | The number of retries. | Same suffix. |
| `package_weight_grams` | integer | The weight in grams. | The unit is in the name. |
| `file_size_bytes` | bigint | The size of a file. | The unit is in the name. |
| `timeout_seconds` | integer | A timeout in seconds. | No guess about seconds or milliseconds. |
| `distance_km` | numeric | A distance in kilometres. | A standard unit symbol. |

## Identifier limits and case

| Database | Maximum length of a name | Case rule | Note |
|---|---|---|---|
| PostgreSQL | 63 bytes | Folds unquoted names to lower case. | A longer name is cut to 63 bytes, with a notice. A quoted mixed-case name needs quotes in every query. |
| MySQL | 64 characters for most names | Column names are not case-sensitive. Table names can be, depending on the system. | Check `lower_case_table_names`. |
| SQL Server | 128 characters | Depends on the collation. | The same name can differ by case in one database and not in another. |

Use short, lower-case names without quotes. Then the same name works in every database. See [PostgreSQL lexical structure](https://www.postgresql.org/docs/current/sql-syntax-lexical.html), [MySQL identifiers](https://dev.mysql.com/doc/refman/8.4/en/identifiers.html) and [SQL Server database identifiers](https://learn.microsoft.com/en-us/sql/relational-databases/databases/database-identifiers).

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `OrderID` | `order_id` | PostgreSQL folds an unquoted `OrderID` to `orderid`. A quoted `"OrderID"` needs quotes in every query. |
| `is_deleted` | `deleted_at` | A timestamp says when. `NULL` means not deleted. |
| `price FLOAT` | `price_cents BIGINT` plus `currency_code` | Integer minor units avoid rounding errors. |
| `amount` | `total_amount_cents` | A bare `amount` hides the unit. |
| `created` | `created_at` | `_at` marks a timestamp. |
| `date` | `delivery_date` | `date` is a type name and a vague word. |
| `status_ok` | `is_status_ok` | A boolean reads as a statement. |
| `weight` | `package_weight_grams` | The unit is in the name. |
| `data_json` | `raw_payload` | Name the content, not the type. |
| `tags_array` | `tags` | The schema already shows the array type. |
| `fk_user` | `user_id` | A foreign key column is `<referenced_table_singular>_id`. |
| `type` | `payment_method` | `type` alone could mean anything. |
| `qty` | `quantity` | Saves two letters and costs clarity. |
| `order` (as a column) | `order_number` | `order` is a reserved word. |
| `tenant` | `tenant_id` | A foreign key ends with `_id`, or with the referenced natural key, such as `country_code`. |

!!! info "See also"

    - [Tables](tables.md), [Indexes](indexes.md), [Constraints](constraints.md) and [Enums](enums.md)
    - [Negation and optionality](../patterns/negation-and-optionality.md) for `NULL` and missing values
    - [Bad → better cookbook](../patterns/cookbook.md) for more rewrites
