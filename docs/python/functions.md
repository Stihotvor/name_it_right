??? success "General patterns"
    
    - Use snake_case in function names ONLY! Don't look at some bad examples, even if they have 1k+ stars on GitHub  
    - Functions which validate or check something and return boolean value, should start with `is_`, `has_`: `has_tax_applied()`, `is_valid()`  
    - Functions, which are not covered by the above rule, should have executable names: `compile()`, `collect()`, `process()`, `fetch()`  
    - If the function has `and` in the name, there is a high chance, the function does multiple things. Probably You should split it.  
    
??? tip "Useful tips"  

    - Good function arguments can help to shorten the function name: `add_car_to_catalog(name: str)` => `add_car_to(catalog: "str")`  
    - Use the same naming everywhere. Create a vocabulary standard for the company and never break it. If You use `fetch_`, use it everywhere.  
    - In order to shorten the function name, You can use the module name:  
    ```py
    # Before
    from food import create_french_fries
    
    create_french_fries()
    ...
    
    # After
    from food import france
    
    france.create_fries()
    ...
    
    # Or even shorter
    from food.france import create_fries()
    
    create_fries()
    ...
    ```

??? danger "General anti-patterns"
    
    - Abreviations: `compile_frst()`  
    - One-letter functions: `v()`

## Glossary
### A  
__aggregate_something(**building blocks)__ - function collects all the building blocks' values and generated/aggregate the necessary objects with all the data inside it.  
_Category: [Domain Driven Development](link-here)_