# Constraints

!!! success "General patterns"

    - Primary key: `pk_<table>` — `pk_customers`, `pk_order_items`
    - Foreign key: `fk_<table>_<referenced_table>` — `fk_orders_customers`, `fk_order_items_orders`
    - Check constraint: `chk_<table>_<description>` — `chk_orders_total_amount_cents_non_negative`, `chk_customers_age_range`
    - Unique constraint: `uq_<table>_<columns>`, the same as for unique indexes — `uq_customers_email`

!!! tip "Useful tips"

    - Explicitly name constraints rather than relying on auto-generated names — error messages become readable: `"violates fk_orders_customers"` tells you exactly which key failed
    - For composite foreign keys, use the same pattern. The definition lists the columns: `fk_order_items_product_variants`

!!! danger "General anti-patterns"

    - Auto-generated constraint names like `FK__orders__customer_id__5A3B6F` — unreadable in error logs
    - Skipping foreign key constraints entirely — data integrity should be enforced at the database level, not just in the application

```sql
ALTER TABLE orders ADD CONSTRAINT pk_orders PRIMARY KEY (id);
ALTER TABLE orders ADD CONSTRAINT fk_orders_customers FOREIGN KEY (customer_id) REFERENCES customers(id);
ALTER TABLE orders ADD CONSTRAINT chk_orders_total_amount_cents_non_negative CHECK (total_amount_cents >= 0);
```

## Constraint kinds

The examples use an e-commerce checkout. All names have the form `<prefix>_<table>_<description>`, except `pk_<table>`.

| Kind | Pattern | Example | Why this name |
|---|---|---|---|
| Primary key | `pk_<table>` | `pk_orders` | A table has one primary key. The table name is enough. |
| Composite primary key | `pk_<table>` | `pk_user_roles` | Same pattern. List the columns in the definition, not in the name. |
| Foreign key | `fk_<table>_<referenced_table>` | `fk_orders_customers` | Child table first, then the parent. |
| Foreign key, second link to a table | `fk_<table>_<role>` | `fk_orders_billing_address`, `fk_orders_shipping_address` | When a table has two keys to one parent, name the role. |
| Foreign key on a junction | `fk_<table>_<referenced_table>` | `fk_user_roles_roles` | Same pattern. |
| Foreign key, composite | `fk_<table>_<referenced_table>` | `fk_order_items_product_variants` | The name stays short. The definition lists the columns. |
| Unique | `uq_<table>_<columns>` | `uq_products_sku` | The same prefix as a unique index. |
| Unique composite | `uq_<table>_<col1>_<col2>` | `uq_coupon_redemptions_coupon_id_customer_id` | A customer uses a coupon once. |
| Check, range | `chk_<table>_<description>` | `chk_orders_discount_rate_range` | The description states the rule. |
| Check, sign | `chk_<table>_<column>_<rule>` | `chk_orders_total_amount_cents_non_negative` | The column and the rule. |
| Check, positive | `chk_<table>_<column>_positive` | `chk_order_items_quantity_positive` | A common rule has a fixed word. |
| Check, order of dates | `chk_<table>_<later>_after_<earlier>` | `chk_shipments_delivered_after_shipped` | The words state the order. |
| Check, pair | `chk_<table>_<a>_after_<b>` | `chk_coupons_ends_after_starts` | Matches the `starts_at` and `ends_at` pair. |
| Check, allowed values | `chk_<table>_<column>_allowed` | `chk_payments_method_allowed` | Use a lookup table when the list changes often. A PostgreSQL enum cannot drop a value. |
| Check, format | `chk_<table>_<column>_format` | `chk_currency_code_format` | For example `code ~ '^[A-Z]{3}$'`. |
| Exclusion | `ex_<table>_<description>` | `ex_price_rules_no_overlap` | PostgreSQL only. The period of two rows must not overlap. |
| Default (SQL Server) | `df_<table>_<column>` | `df_orders_status` | Only SQL Server names a default as an object. |

### More examples

| Constraint | Kind |
|---|---|
| `pk_customers`, `pk_order_items`, `pk_products` | Primary key |
| `fk_order_items_orders`, `fk_order_items_products`, `fk_payments_orders` | Foreign key |
| `uq_customers_email`, `uq_shipping_carrier_code` | Unique |
| `chk_products_weight_grams_positive`, `chk_customers_age_range` | Check |

## Not null

Most databases do not let you name a `NOT NULL` rule. Do not try. Put the rule in the column definition and read it in the schema. Oracle and PostgreSQL 18 and newer can store a name for it. This is rarely worth the work.

## Auto-generated names

Always name constraints yourself. The default names differ by database and are hard to read in an error.

| Database | Default names | Example |
|---|---|---|
| PostgreSQL | `<table>_pkey`, `<table>_<column>_fkey`, `<table>_<column>_key`, `<table>_<column>_check` | `orders_customer_id_fkey` |
| MySQL | `PRIMARY`, `<table>_ibfk_<n>`, `<table>_chk_<n>` | `orders_ibfk_1` |
| SQL Server | `PK__<table>__<hash>`, `FK__<table>__<column>__<hash>` | `FK__orders__user_id__5A3B6F` |

Names with a counter or a hash change when you create the schema again. A migration that drops a constraint by its default name can fail on another server. See the PostgreSQL pages on [constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) and the MySQL page on [FOREIGN KEY constraints](https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html).

## Scope of constraint names

| Database | Where the name must be unique |
|---|---|
| PostgreSQL | In the table. A key that has an index also needs a free name in the schema, because the index takes the same name. |
| MySQL | Foreign key and check names: in the database. Unique names are index names: in the table. A primary key is always `PRIMARY`, whatever name you give. |
| SQL Server | In the schema. |

Put the table name in every constraint name. Then the same name works in all three databases.

## Examples in SQL

```sql
ALTER TABLE order_items ADD CONSTRAINT pk_order_items PRIMARY KEY (order_id, line_number);
ALTER TABLE orders ADD CONSTRAINT fk_orders_billing_address FOREIGN KEY (billing_address_id) REFERENCES addresses (id);
ALTER TABLE orders ADD CONSTRAINT fk_orders_shipping_address FOREIGN KEY (shipping_address_id) REFERENCES addresses (id);
ALTER TABLE coupons ADD CONSTRAINT chk_coupons_ends_after_starts CHECK (ends_at > starts_at);
ALTER TABLE coupon_redemptions ADD CONSTRAINT uq_coupon_redemptions_coupon_id_customer_id UNIQUE (coupon_id, customer_id);
ALTER TABLE price_rules ADD CONSTRAINT ex_price_rules_no_overlap
    EXCLUDE USING gist (product_id WITH =, validity WITH &&);
```

The exclusion example needs the `btree_gist` extension and a range column named `validity`.

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `FK__orders__user_id__5A3B6F` | `fk_orders_customers` | The default name has a hash. |
| `fk1` | `fk_orders_customers` | A number says nothing. |
| `orders_ibfk_1` | `fk_orders_customers` | A counter changes when you create the schema again. |
| `check_1` | `chk_orders_total_amount_cents_non_negative` | The name states the rule. |
| `chk_orders_valid` | `chk_orders_discount_rate_range` | `valid` says nothing. |
| `fk_orders_addresses` twice, when `orders` has two links to `addresses` | `fk_orders_billing_address` and `fk_orders_shipping_address` | Two keys to one parent need a role. |
| `uq_email` | `uq_customers_email` | The name lacks the table. |
| `pk` | `pk_orders` | The name lacks the table. |
| `chk_age` | `chk_customers_age_range` | Name the table and the rule. |
| `ck_status_in_list` for a list that changes each month | a lookup table plus `fk_orders_order_status` | A check cannot change without a migration. |

!!! info "See also"

    - [Indexes](indexes.md) for `uq_` indexes and the same naming rules
    - [Tables](tables.md) and [Columns](columns.md) for the names that go into constraint names
    - [Enums](enums.md) for a list of allowed values
