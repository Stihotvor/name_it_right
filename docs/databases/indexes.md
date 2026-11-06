!!! success "General patterns"

    - Use `idx_<table>_<columns>` for regular indexes: `idx_customers_email`, `idx_orders_customer_id_created_at`
    - Use `uq_<table>_<columns>` for unique indexes: `uq_customers_email`, `uq_country_code`
    - Write the columns in the name in the same order as in the index. Choose that order for the queries (see "Column order in an index name")

!!! tip "Useful tips"

    - Name composite indexes after the columns in the order they appear in the index: `idx_orders_customer_id_created_at`
    - Drop unused indexes — every index adds write overhead

!!! danger "General anti-patterns"

    - Index names without the table name: `idx_1`, `ix_email` (which table?)
    - Generic suffixes like `_idx` without the table context

```sql
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE UNIQUE INDEX uq_customers_email ON customers(email);
CREATE INDEX idx_order_items_order_id_product_id ON order_items(order_id, product_id);
CREATE INDEX idx_orders_created_at ON orders(created_at DESC);
```

## Index kinds

The examples use an e-commerce checkout. Add a suffix for the index method only when the method is not B-tree. B-tree is the default, so most names have no suffix.

| Kind | Pattern | Example | Why this name |
|---|---|---|---|
| Single column | `idx_<table>_<column>` | `idx_orders_customer_id` | The table and the column, in this order. |
| Foreign key support | `idx_<table>_<fk_column>` | `idx_order_items_order_id` | Same pattern. A foreign key needs an index on the child side for fast joins and deletes. |
| Composite | `idx_<table>_<col1>_<col2>` | `idx_orders_customer_id_created_at` | Column order in the name equals column order in the index. |
| Descending | `idx_<table>_<column>_desc` | `idx_orders_created_at_desc` | Add `_desc` only when the direction matters for a sort. |
| Unique | `uq_<table>_<columns>` | `uq_customers_email` | `uq_` marks a rule, not only speed. |
| Unique composite | `uq_<table>_<col1>_<col2>` | `uq_order_items_order_id_product_id` | One product only once per order. |
| Partial | `idx_<table>_<columns>_<condition>` | `idx_orders_created_at_open` | The condition word says which rows are in the index. |
| Partial unique | `uq_<table>_<columns>_<condition>` | `uq_customers_email_active` | Unique only for rows where `deleted_at IS NULL`. |
| Covering | `idx_<table>_<columns>_incl_<columns>` | `idx_orders_customer_id_incl_total_cents` | `incl` is short for `INCLUDE`. This is a convention of this guide. |
| Expression | `idx_<table>_<function>_<column>` | `idx_customers_lower_email` | The function is part of what you search for. |
| Unique expression | `uq_<table>_<function>_<column>` | `uq_customers_lower_email` | A case-insensitive unique email. |
| GIN | `idx_<table>_<column>_gin` | `idx_products_attributes_gin` | For `jsonb`, arrays and full-text search. |
| GIN for text search | `idx_<table>_<column>_gin` | `idx_products_search_vector_gin` | The column holds a `tsvector`. |
| GIN for trigrams | `idx_<table>_<column>_trgm` | `idx_customers_last_name_trgm` | `pg_trgm` serves `LIKE '%text%'`. |
| GiST | `idx_<table>_<column>_gist` | `idx_shipping_zones_area_gist` | For geometry and ranges. |
| BRIN | `idx_<table>_<column>_brin` | `idx_events_created_at_brin` | A small index for a big table that is stored in order. |
| Hash | `idx_<table>_<column>_hash` | `idx_sessions_token_hash` | Equality lookups only. Do not confuse it with a column named `token_hash`. |

The method names (`gin`, `gist`, `brin`, `hash`) are PostgreSQL. Other databases use other kinds. For example, MySQL has `FULLTEXT` and `SPATIAL` indexes.

### More examples

| Index | Kind |
|---|---|
| `idx_payments_order_id`, `idx_shipments_order_id`, `idx_products_category_id` | Foreign key support |
| `idx_coupon_redemptions_customer_id`, `idx_orders_status_created_at` | Single and composite |
| `idx_webhook_deliveries_event_id_created_at` | Composite |
| `uq_products_sku`, `uq_coupons_code` | Unique |

## Column order in an index name

Write the columns in the same order as in the index. Choose that order for the queries, not for the name:

1. Put columns that you compare with `=` first.
2. Put the column with a range (`>`, `BETWEEN`) or a sort after them.
3. Put a column in the index only if a query uses it.

For example, the query `WHERE customer_id = ? AND created_at > ?` needs `idx_orders_customer_id_created_at`. The reverse order would scan more entries. A B-tree index helps a query most when the query uses its leftmost columns. See the PostgreSQL pages on [multicolumn indexes](https://www.postgresql.org/docs/current/indexes-multicolumn.html), [partial indexes](https://www.postgresql.org/docs/current/indexes-partial.html) and [index types](https://www.postgresql.org/docs/current/indexes-types.html).

## Name length and scope

| Database | Index name scope | Limit |
|---|---|---|
| PostgreSQL | Unique in the schema. | 63 bytes. A longer name is cut. |
| MySQL | Unique per table. | 64 characters. |
| SQL Server | Unique per table. | 128 characters. |

The table name in the index name keeps names unique in PostgreSQL and clear in every database. If a name is too long, shorten the column words in the same way everywhere, for example `cust_id`. Never cut the name at random. PostgreSQL then cuts it, and two long names can end up equal.

PostgreSQL makes a name when you give none: `<table>_<column>_idx`. This is a valid but weak choice, because it lacks a prefix that tells unique from non-unique.

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `idx_1` | `idx_orders_customer_id` | A number says nothing. |
| `ix_email` | `idx_customers_email` | The name lacks the table. |
| `email_idx` | `idx_customers_email` | The suffix form hides the table in some tools. Use one prefix form. |
| `idx_orders_created_at_customer_id` for `WHERE customer_id = ? ORDER BY created_at` | `idx_orders_customer_id_created_at` | The equality column goes first. |
| `idx_customers_email` (case-insensitive search by `lower(email)`) | `idx_customers_lower_email` | The name must match what the index stores. |
| `idx_orders_status` on a column with 3 values | a partial index such as `idx_orders_created_at_open` | A low-selectivity index on its own rarely helps. |
| `idx_orders_all` | `idx_orders_customer_id_created_at` | `all` is not a column. |
| `index_new`, `idx_test` | name the real columns | Never commit these. |
| `idx_order_items_order_id_product_id_quantity_unit_price_cents_created_at` | `idx_order_items_order_id_product_id` | Too long. Keep the columns that the queries need. |
| `idx_customers_email` for a unique rule | `uq_customers_email` | A rule that blocks duplicates needs the `uq_` prefix. |

!!! info "See also"

    - [Constraints](constraints.md) for the rules that create unique indexes
    - [Tables](tables.md) and [Columns](columns.md) for the names that go into index names
    - [Bad → better cookbook](../patterns/cookbook.md) for more rewrites
