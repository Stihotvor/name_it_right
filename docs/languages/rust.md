---
status: new
---

# Rust

!!! success "General patterns"

    - Use `snake_case` for functions, methods, variables, modules and crates: `calculate_total`, `order_total`
    - Use `UpperCamelCase` for types, traits and enum variants: `OrderService`, `PaymentGateway`, `OrderStatus::Pending`
    - Use `SCREAMING_SNAKE_CASE` for constants and statics: `MAX_RETRY_COUNT`
    - Treat an acronym as a word in `UpperCamelCase`: `Uuid`, `HttpClient`, `Json`. In `snake_case`, write it in lower case: `parse_json`
    - Use lower case for a lifetime, and keep it short: `'a`, `'de`
    - Use a verb first for functions, as in the [action and context pattern](../patterns/action-context.md)

!!! tip "Useful tips"

    - Run `cargo fmt` and `cargo clippy`. The compiler warns about names that break the case rules (`non_snake_case`, `non_camel_case_types`, `non_upper_case_globals`)
    - Do not put `get_` in front of a getter: `total()`, not `get_total()`. The Rust API guidelines give this rule
    - Name a conversion for its cost: `as_` is free, `to_` has a cost, `into_` takes ownership
    - Name an error type in verb-object-error order: `ParseIntError`, not `IntParseError`. The API guidelines give this rule

!!! danger "General anti-patterns"

    - `camelCase` for functions: `calculateTotal`
    - `get_` on a plain getter: `get_total()`
    - A `-rs` or `-rust` suffix on a crate name: `orders-rs`
    - An `I` prefix on a trait: `IOrderRepository`

## Names by kind

| Kind | Rule | Examples | Why this name |
|---|---|---|---|
| Crate | `snake_case` or `kebab-case`; no `-rs` or `-rust` suffix | `order_utils` or `order-utils` | The compiler turns `-` into `_` in code. RFC 430 says the crate style is unclear, so choose one. |
| Module | `snake_case` | `payment`, `order_items` | RFC 430. |
| File | `snake_case.rs` | `order_service.rs` | The file name equals the module name. |
| Function | `snake_case`, verb first | `calculate_total`, `find_orders` | RFC 430. |
| Method | `snake_case` | `total`, `add_item` | Same as a function. |
| Local variable | `snake_case` noun | `order_total`, `customer_email` | RFC 430. |
| Boolean | `is_`, `has_`, `can_` plus a word | `is_active`, `has_gift_wrap` | A boolean reads as a statement. The standard library uses `is_empty`. |
| Type (struct, enum, union) | `UpperCamelCase` noun | `Order`, `OrderStatus` | RFC 430. |
| Trait | `UpperCamelCase`; an adjective or a role | `Display`, `Iterator`, `OrderRepository` | The standard library uses roles and adjectives. |
| Enum variant | `UpperCamelCase` | `Pending`, `Shipped` | RFC 430. |
| Constant | `SCREAMING_SNAKE_CASE` | `MAX_RETRY_COUNT` | RFC 430. |
| Static | `SCREAMING_SNAKE_CASE` | `GLOBAL_COUNTER` | Same as a constant. |
| Type parameter | short `UpperCamelCase`, often one letter | `T`, `K`, `V`, `Item` | A short scope. |
| Lifetime | short lower case | `'a`, `'de`, `'src` | Lifetimes are short by convention. |
| Macro | `snake_case` plus `!` | `vec!`, `println!`, `assert_eq!` | RFC 430. |
| Feature name | `kebab-case` or `snake_case`; no `use-` or `with-` | `serde`, `json`, `tls` | The API guidelines say features name what they add. |
| Getter | the field name, no `get_` | `fn total(&self) -> u64` | The API guidelines. |
| Mutable getter | the field name plus `_mut` | `fn items_mut(&mut self)` | The API guidelines. |
| Setter | `set_` plus the field | `fn set_owner(&mut self, owner: String)` | The usual form. |
| Constructor | `new`, or `with_` plus a detail | `Order::new`, `Vec::with_capacity` | The standard library form. |
| Builder | the type plus `Builder` | `OrderBuilder` | Says what it builds. |
| Test function (community practice) | a sentence in `snake_case` | `adds_tax_to_total` | The test report reads as a sentence. |
| Test module | `tests` | `mod tests { ... }` | The usual name under `#[cfg(test)]`. |
| Error type | description plus `Error` | `ParseIntError`, `OrderError` | Verb-object-error order, as in the standard library. |
| Error variant | description of the cause | `NotFound`, `InvalidInput` | A variant describes the cause. The type already says `Error`. |
| Unused binding | a leading underscore | `_unused`, `_` | The compiler does not warn. |
| Iterator method | `iter`, `iter_mut`, `into_iter` | `orders.iter()` | The API guidelines. |

## Conversions

| Prefix | Cost | Takes | Examples |
|---|---|---|---|
| `as_` | free; a view | `&self` to a reference | `as_str`, `as_bytes`, `as_ref`, `as_slice` |
| `to_` | costs; may allocate | `&self` | `to_string`, `to_owned`, `to_vec`, `to_lowercase` |
| `into_` | free or costs; consumes the value | `self` | `into_bytes`, `into_boxed_str`, `into_iter` |
| `from_` | builds a value from another | none | `String::from_utf8`, `Duration::from_secs` |
| `try_` | may fail; returns `Result` | any | `try_from`, `try_into`, `try_lock` |
| `_mut` suffix | gives a mutable view | `&mut self` | `as_mut_slice`, `iter_mut`, `get_mut` |
| `_unchecked` suffix | skips a check; `unsafe` | any | `get_unchecked`, `from_utf8_unchecked` |
| `_lossy` suffix | allows a lossy result | any | `from_utf8_lossy`, `to_string_lossy` |

The conversion names are from the [API guidelines](https://rust-lang.github.io/api-guidelines/naming.html#ad-hoc-conversions-follow-as_-to_-into_-conventions-c-conv). The table has 20 examples with their cost.

## Acronyms

| Case | Rule | Examples |
|---|---|---|
| In `UpperCamelCase` | An acronym is a word | `Uuid`, `HttpClient`, `Json`, `Utf8Error` |
| In `snake_case` | All lower case | `parse_json`, `uuid`, `http_client` |
| In a constant | All capitals | `DEFAULT_HTTP_PORT` |

Conflict: Go writes `HTTPClient` and `userID`. Rust writes `HttpClient` and `user_id`. The standard library has `Ipv4Addr` and `Utf8Error`, not `IPv4Addr`.

## Iterators

| Method | Meaning | Examples |
|---|---|---|
| `iter` | Items by reference. | `orders.iter()` |
| `iter_mut` | Items by mutable reference. | `orders.iter_mut()` |
| `into_iter` | Items by value. The collection is consumed. | `orders.into_iter()` |
| Iterator type | The method name in `UpperCamelCase` | `Iter`, `IterMut`, `IntoIter` |
| Adapter | A verb that describes the step | `map`, `filter`, `take_while` |

## Crates and features

| Case | Rule | Examples |
|---|---|---|
| Crate name | Short, no `-rs` or `-rust` suffix | `serde`, `tokio`, `order_utils` |
| Crate with a name clash | Add a word for the field | `order_utils` and `payment_utils` |
| Feature that adds a dependency | The name of the dependency | `serde`, `tokio` |
| Feature that adds a capability | A noun | `json`, `tls`, `std` |
| Feature to avoid | `use-`, `with-`, `enable-` prefix | `use-serde` |

!!! info "See also"

    - [Languages overview](index.md) for the matrix of all languages
    - [Naming patterns](../patterns/index.md) and the [cookbook](../patterns/cookbook.md)
    - [Rust API guidelines: naming](https://rust-lang.github.io/api-guidelines/naming.html), [RFC 430](https://rust-lang.github.io/rfcs/0430-finalizing-naming-conventions.html), [The Rust style guide](https://doc.rust-lang.org/style-guide/)
