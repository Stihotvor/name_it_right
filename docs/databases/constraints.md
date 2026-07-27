!!! success "General patterns"

    - Primary key: `pk_<table>` — `pk_users`, `pk_order_items`
    - Foreign key: `fk_<table>_<referenced_table>` — `fk_orders_users`, `fk_order_items_orders`
    - Check constraint: `chk_<table>_<description>` — `chk_orders_total_positive`, `chk_users_age_range`
    - Default constraint name for unique columns handled by the `uq_` index naming

!!! tip "Useful tips"

    - Explicitly name constraints rather than relying on auto-generated names — error messages become readable: `"violates fk_orders_users"` tells you exactly which key failed
    - For composite foreign keys, list both columns: `fk_order_items_order_product`

!!! danger "General anti-patterns"

    - Auto-generated constraint names like `FK__orders__user_id__5A3B6F` — unreadable in error logs
    - Skipping foreign key constraints entirely — data integrity should be enforced at the database level, not just in the application

```sql
ALTER TABLE orders ADD CONSTRAINT pk_orders PRIMARY KEY (id);
ALTER TABLE orders ADD CONSTRAINT fk_orders_users FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE orders ADD CONSTRAINT chk_orders_total_positive CHECK (total_cents >= 0);
```
