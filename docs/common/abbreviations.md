# Abbreviations

!!! success "General patterns"

    - Write names as full words: `customer_name` not `c_nm`, `user_buffer_size` not `usr_buf_sz`
    - Use standard industry abbreviations only when universally understood: `html`, `url`, `api`, `http`

!!! tip "Useful tips"

    - An abbreviation that saves 3 characters but costs 3 minutes of reader time is a bad trade
    - When in doubt, spell it out — readability beats line length

!!! warning "Abbreviations save typing, but cost readers"

    ```py
    bnfd = 12            # What is bnfd? Buffer? Bandwidth? Binary?
    dstr = 100.12        # dstr = distance? destination? data stream?
    ```

    - Abbreviations that are obvious to you today will be opaque to everyone else tomorrow
- A name should be understood without consulting a glossary or the author

!!! warning "One-letter names"

    ```py
    v = 'comis'          # A string, but what does it represent?
    x = calculate()      # What was calculated? Where does x go next?
    ```

    - The only acceptable exception is `i`, `j`, `k` as loop counters (and only inside tight loops)
    - Even `i` should be `user_index` or `page_num` when the loop body is longer than 5 lines
