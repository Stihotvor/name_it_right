!!! success "General patterns"

    - Use `idx_<table>_<columns>` for regular indexes: `idx_users_email`, `idx_orders_user_id_created_at`
    - Use `uq_<table>_<columns>` for unique indexes: `uq_users_email`, `uq_countries_code`
    - Order columns by selectivity (most selective first) in the index name

!!! tip "Useful tips"

    - Name composite indexes after the columns in the order they appear in the index: `idx_orders_user_id_created_at`
    - Drop unused indexes — every index adds write overhead

!!! danger "General anti-patterns"

    - Index names without the table name: `idx_1`, `ix_email` (which table?)
    - Generic suffixes like `_idx` without the table context

```sql
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE UNIQUE INDEX uq_users_email ON users(email);
CREATE INDEX idx_order_items_order_id_product_id ON order_items(order_id, product_id);
CREATE INDEX idx_orders_created_at ON orders(created_at DESC);
```
