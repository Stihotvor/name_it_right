---
status: new
---

# Warehouse and analytics

!!! success "General patterns"

    - Name a table after its layer and its grain: the layer says how raw the data is, the grain says what one row is
    - Use `snake_case` for every object, as on the other database pages
    - Mark the role of a table with a prefix (`stg_`, `int_`, `fact_`, `dim_`, `bridge_`). Do not mark the object type
    - Use one key suffix for each key kind: `_id` for a source key, `_key` for a surrogate key. This split is for warehouse tables. Application tables follow [Columns](columns.md), where the surrogate key is `id`
    - Use `_at` for a timestamp and `_date` for a date, as in [Columns](columns.md)

!!! tip "Useful tips"

    - Decide plural or singular once. This page uses plural names (`dim_customers`). Some teams use singular (`dim_customer`) or `fct_` for facts. Any one choice works if the project uses it everywhere
    - The dbt rules come from the dbt guides. Kimball sets the table roles and the ideas (grain, bridge, SCD), not name formats. The name formats on this page, such as `_daily_snapshot`, `agg_`, `_key` and the `_loaded_at` columns, are the choice of this guide

!!! danger "General anti-patterns"

    - Names that hide the layer: `orders_final`, `orders_new`, `orders_v2`
    - Names that hide the grain: `sales` (one row per what?)
    - Mixed key suffixes: `customer_id` for a surrogate key in one table and for a source key in another

The examples use an e-commerce checkout. For the rules inside one table, see [Tables](tables.md) and [Columns](columns.md).

## Layers

A warehouse moves data through steps. The two common naming systems differ, but they describe the same idea.

| Step | dbt layer | Medallion layer | What it holds |
|---|---|---|---|
| 1 | source | bronze | Raw copies of the source data. |
| 2 | staging (`stg_`) | silver | Clean and typed data, one table for each source table. |
| 3 | intermediate (`int_`) | silver | Joins and steps that are not for end users. This mapping to silver is approximate and is the choice of this guide. |
| 4 | marts | gold | Business tables for reports and tools. |

See the dbt guide to [project structure](https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview) and the Databricks page on the [medallion architecture](https://docs.databricks.com/aws/en/lakehouse/medallion).

## dbt model names

| Layer | Pattern | Examples | Why this name |
|---|---|---|---|
| Staging | `stg_<source>__<entity>` | `stg_shop__orders`, `stg_shop__order_items`, `stg_stripe__payments` | A double underscore splits the source from the entity. A single underscore splits words. |
| Intermediate | `int_<entity>_<verb>` | `int_orders_joined_to_payments`, `int_payments_pivoted_to_orders` | The verb says what the step does. |
| Mart, entity | `<entity>` | `orders`, `customers` | The dbt guide names marts after the business entity. |
| Mart, with role prefix | `fact_<entity>`, `dim_<entity>` | `fact_orders`, `dim_customers` | Use this form if the project follows Kimball. |
| Source file | `_<folder>__sources.yml` | `_shop__sources.yml` | The leading underscore keeps the file at the top of the folder. In staging, the folder is named after the source. |
| Model file | `_<folder>__models.yml` | `_marts__models.yml` | Same pattern. |
| Snapshot | `<entity>_snapshot` | `customers_snapshot` | The suffix shows that the table stores history. The dbt documentation uses this form in its examples. |
| Seed | `<entity>` | `country_codes`, `tax_rates` | A plain entity name, like a mart, because a seed is reference data. It is a small file in `seeds/`. |
| Custom test | `assert_<expectation>` | `assert_order_total_matches_item_sum` | The name states what must be true. |

Staging models keep the source grain and do only light work: rename, cast and clean. See the dbt [style guide](https://docs.getdbt.com/best-practices/how-we-style/0-how-we-style-our-dbt-projects), the page on [snapshots](https://docs.getdbt.com/docs/build/snapshots) and the page on [seeds](https://docs.getdbt.com/docs/build/seeds).

## Medallion names

Databricks uses a three-level name: `catalog.schema.table`. The medallion layers fit well as schema names.

| Layer | Pattern | Examples | Why this name |
|---|---|---|---|
| Bronze | `bronze.<source>_<entity>` | `bronze.shop_orders`, `bronze.stripe_payments` | The source is in the name. The data is raw. |
| Silver | `silver.<entity>` | `silver.orders`, `silver.customers` | Clean data has the business name. |
| Gold | `gold.<report_or_entity>` | `gold.daily_revenue`, `gold.customer_lifetime_value` | A gold table answers a business question. |
| Environment | the catalog | `prod.gold.daily_revenue`, `dev.gold.daily_revenue` | The catalog names the environment. The table name stays the same. |

## Kimball tables

Kimball modeling puts measures in fact tables and descriptions in dimension tables.

| Kind | Pattern | Examples | Grain, or why this name |
|---|---|---|---|
| Fact | `fact_<process>` | `fact_orders` | One row per order. |
| Fact, finer grain | `fact_<process>_<part>` | `fact_order_items` | One row per order line. |
| Periodic snapshot fact | `fact_<process>_daily_snapshot` | `fact_inventory_daily_snapshot` | One row per product per day. |
| Accumulating snapshot fact | `fact_<process>_lifecycle` | `fact_order_fulfillment_lifecycle` | One row per order. The row updates as the order moves along. |
| Dimension | `dim_<entity>` | `dim_customers`, `dim_products`, `dim_stores` | One row per entity. |
| Date dimension | `dim_dates` | `dim_dates` | One row per calendar day. |
| Junk dimension | `dim_<process>_flags` | `dim_order_flags` | Holds low-cardinality flags in one table. |
| Bridge | `bridge_<fact>_<dimension>` | `bridge_order_promotions` | Links a fact to a multivalued dimension. |
| Aggregate | `agg_<grain>_<measure>` | `agg_daily_revenue`, `agg_monthly_orders_by_country` | A pre-computed summary. The grain is in the name. |

## Keys

| Kind | Column pattern | Examples | Why this name |
|---|---|---|---|
| Source (natural) key | `<entity>_id` | `customer_id`, `order_id` | The key from the source system. |
| Surrogate key | `<entity>_key` | `customer_key`, `product_key` | A key made by the warehouse. A different suffix shows that it is not a source key. |
| Date key, role-playing | `<role>_date_key` | `order_date_key`, `ship_date_key` | Two roles of one `dim_dates`. The role is the prefix. |
| Degenerate dimension | the source number | `order_number` | An identifier that stays in the fact table. It has no dimension of its own. |
| Unknown member | a reserved key value, often `-1` | `customer_key = -1` | Kimball advises a default row for missing dimensions. The value `-1` is a common choice. |

A surrogate key can be a counter or a hash of the source key. The `dbt_utils.generate_surrogate_key` macro makes a hash. Name the column the same in the dimension and in every fact that uses it.

## History: SCD type 2

A slowly changing dimension of type 2 keeps one row for each version of an entity.

| Column | Type idea | Meaning | Why this name |
|---|---|---|---|
| `customer_key` | surrogate key | One version of the customer. | A new version gets a new key. |
| `customer_id` | source key | The customer in the source system. | It repeats in every version. |
| `valid_from` | timestamp | When the version starts. | A pair with `valid_to`. |
| `valid_to` | timestamp, nullable | When the version ends. `NULL` means open. | Document whether the end is included. |
| `is_current` | boolean | The latest version. | `is_` marks a boolean, and the name is positive. |
| `dbt_valid_from`, `dbt_valid_to` | timestamp | The same idea in a dbt snapshot. | dbt makes these columns for you. |
| `dbt_updated_at`, `dbt_scd_id` | timestamp, text | The change time and the row key in a dbt snapshot. | dbt makes these too. |

## Load and audit columns

| Column | Meaning | Why this name |
|---|---|---|
| `_loaded_at` | When the pipeline wrote the row. | A leading underscore marks a technical column. |
| `_source_file` | The file that the row came from. | Names the origin. |
| `_source_system` | The system that the row came from. | Pairs with `_source_file`. |
| `_is_deleted` | The source deleted the row. | `is_` marks a boolean, and the underscore marks a technical column. |
| `_fivetran_synced`, `_fivetran_deleted` | The same ideas from the Fivetran connector. | Keep the connector names in bronze. Rename them in staging. |

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `orders_final` | `fact_orders` or `orders` | A layer name tells more than a state word. |
| `stg_orders` | `stg_shop__orders` | The source is in the name. A second source can have `orders` too. |
| `stg_shop_orders` | `stg_shop__orders` | A double underscore splits the source from the entity. |
| `sales` | `fact_order_items` | The grain is in the name. |
| `customer_dim` | `dim_customers` | The role is the prefix, as in the other names. |
| `dim_customers.customer_id` as a surrogate key | `customer_key` | One suffix for each key kind. |
| `is_latest_flag` | `is_current` | `is_` already marks a boolean, so `flag` adds nothing. |
| `start_date`, `end_date` for versions | `valid_from`, `valid_to` | The pair has a clear meaning. |
| `tmp_orders_2` in a mart | `int_orders_joined_to_payments` | An intermediate step has a verb. |
| `daily` | `agg_daily_revenue` | The grain and the measure are in the name. |

!!! info "See also"

    - [Tables](tables.md), [Columns](columns.md) and [Constraints](constraints.md)
    - [Booleans, collections, units and time](../patterns/booleans-collections-units-time.md) for `_at`, `_date` and units
    - [Bad → better cookbook](../patterns/cookbook.md) for more rewrites
