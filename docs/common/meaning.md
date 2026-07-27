# Meaning and clarity

!!! success "General patterns"

    - Every name should answer: what is this, and why does it exist here?
    - Use domain vocabulary that matches the problem space

!!! tip "Useful tips"

    - If you struggle to name something, simplify the design first
    - A name that needs a comment to explain it is the wrong name

!!! warning "Misleading names"

    ```py
    # Name says one thing, code does another
    def validate_email(email: str) -> bool:
        return len(email) > 0       # This is not validation
    ```

    - A name must reflect what the code actually does, not what you wish it did
    - When the implementation changes, rename the function — don't let the name become a lie

!!! warning "Generic names that convey zero intent"

    ```py
    data = fetch()       # What data? From where?
    process(data)        # Process how?
    tmp = transform(x)   # Temp for what?
    ```

    - `data`, `info`, `tmp`, `thing`, `obj`, `item`, `stuff` — these names say nothing
    - Every name should answer: what is this, and why does it exist here?

!!! warning "Names that fight the domain"

    ```py
    # In a finance or e-commerce system
    temp = get_balance(account_id)   # temp suggests it's throwaway — it isn't
    x = apply_discount(code, total)  # x is a discounted total, not a coordinate
    ```

    - Use domain vocabulary: a payment has a `status`, not a `flag`. A customer has an `email`, not a `contact_string`
    - Names that ignore the domain force the next reader to translate back and forth
