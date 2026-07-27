# Consistency

!!! success "General patterns"

    - Pick one verb for each operation and use it everywhere — `fetch` or `get` or `retrieve`, not all three
    - Keep singular/plural distinct: `user` (one) vs `users` (many) vs `User` (class)

!!! tip "Useful tips"

    - Inconsistency is worse than a slightly imperfect convention that everyone follows
    - Document your team's vocabulary in a shared glossary

!!! warning "Inconsistent naming across the same codebase"

    ```py
    # Three files, three styles for the same operation
    get_user()       # file A
    fetch_user()     # file B
    retrieve_user()  # file C
    ```

    - Pick one verb for each operation and use it everywhere: `fetch` or `get` or `retrieve` — not all three
    - Inconsistency is worse than a slightly imperfect convention that everyone follows

!!! warning "Sound-alike names"

    ```py
    user    # singular — one user
    users   # plural — a collection
    User    # class — the blueprint
    ```

    - `user` vs `User` vs `users` should never be interchangeable — each has a distinct role
    - Mixing them up in code is a bug waiting to happen

