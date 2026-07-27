!!! success "General patterns"

    - Use database-native `ENUM` or `CREATE TYPE` when the set of values is stable and small
    - Use a lookup table when the set may grow or needs metadata (display names, sort order)
    - Use `CHECK` constraints when enum type is not available in the database

!!! warning "Prefer lookup tables over hard-coded enums when the values are business concepts: `order_status`, `shipping_method`, `payment_provider`"

    - Business enums change more often than code enums — a lookup table lets you add values without a migration
