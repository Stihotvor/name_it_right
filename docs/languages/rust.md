---
status: new
---

# Rust

!!! success "General patterns"

    - Use `snake_case` for functions, methods, variables and modules: `calculate_total`, `order_total`. Crate names may use `snake_case` or `kebab-case`
    - Use `UpperCamelCase` for types, traits and enum variants: `OrderService`, `PaymentGateway`, `OrderStatus::Pending`
    - Use `SCREAMING_SNAKE_CASE` for constants and statics: `MAX_RETRY_COUNT`
    - Treat an acronym as a word in `UpperCamelCase`: `Uuid`, `HttpClient`, `Json`. In `snake_case`, write it in lower case: `parse_json`
    - Use lower case for a lifetime, and keep it short: `'a`, `'de`
    - Use a verb first for functions, as in the [action and context pattern](../patterns/action-context.md)

!!! tip "Useful tips"

    - Run `cargo clippy`. The compiler (`rustc`) warns about names that break the case rules (`non_snake_case`, `non_camel_case_types`, `non_upper_case_globals`)
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
| Function | `snake_case`; verb first is common practice | `calculate_total`, `find_orders` | RFC 430 sets the case. The verb first comes from the [action and context pattern](../patterns/action-context.md). |
| Method | `snake_case` | `total`, `add_item` | Same as a function. |
| Local variable | `snake_case` noun | `order_total`, `customer_email` | RFC 430. |
| Boolean (community practice) | `is_` or `has_` plus a word | `is_active`, `has_gift_wrap` | A boolean reads as a statement. The standard library uses `is_empty` and `has_root`. |
| Type (struct, enum, union) | `UpperCamelCase` noun | `Order`, `OrderStatus` | RFC 430. |
| Trait | `UpperCamelCase`; an adjective or a role | `Display`, `Iterator`, `OrderRepository` | The standard library uses roles and adjectives. |
| Enum variant | `UpperCamelCase` | `Pending`, `Shipped` | RFC 430. |
| Constant | `SCREAMING_SNAKE_CASE` | `MAX_RETRY_COUNT` | RFC 430. |
| Static | `SCREAMING_SNAKE_CASE` | `GLOBAL_COUNTER` | Same as a constant. |
| Type parameter | short `UpperCamelCase`, often one letter | `T`, `K`, `V`, `Key` | A short scope. |
| Lifetime | short lower case | `'a`, `'de`, `'src` | Lifetimes are short by convention. |
| Macro | `snake_case` plus `!` | `vec!`, `println!`, `assert_eq!` | RFC 430. |
| Feature name | no `use-` or `with-` (C-FEATURE); `kebab-case` or `snake_case` (community practice) | `serde`, `json`, `tls` | The API guidelines say a feature name has no placeholder word. |
| Getter | the field name, no `get_` | `fn total(&self) -> u64` | The API guidelines. |
| Mutable getter | the field name plus `_mut` | `fn items_mut(&mut self)` | The API guidelines. |
| Setter | `set_` plus the field | `fn set_owner(&mut self, owner: String)` | The usual form. |
| Constructor | `new`, or `with_` plus a detail | `Order::new`, `Vec::with_capacity` | The standard library form. |
| Builder | the type plus `Builder` | `OrderBuilder` | Says what it builds. |
| Test function (community practice) | a sentence in `snake_case` | `adds_tax_to_total` | The test report reads as a sentence. |
| Test module | `tests` | `mod tests { ... }` | The usual name under `#[cfg(test)]`. |
| Error type | description plus `Error` | `ParseIntError`, `ParseOrderError` | Verb-object-error order (C-WORD-ORDER), as in the standard library. |
| Error variant | description of the cause | `NotFound`, `InvalidInput` | A variant describes the cause. The type already says `Error`. |
| Unused binding | a leading underscore on the name | `_unused` | The `unused_variables` lint does not fire. The value still lives until the end of the scope. |
| Ignored value | `_` alone | `let _ = send();` | A wildcard pattern. It does not bind, so the value drops at once. |
| Iterator method | `iter`, `iter_mut`, `into_iter` | `orders.iter()` | The API guidelines. |

## Conversions

The API guidelines (C-CONV) define three prefixes by cost and ownership. The other names are standard library practice.

| Prefix | Cost | Input to output | Source |
|---|---|---|---|
| `as_` | free | borrowed to borrowed | C-CONV |
| `to_` | costs: may allocate, copy or check | borrowed to borrowed or owned | C-CONV |
| `into_` | variable; consumes the value | owned to owned | C-CONV |
| `from_` | builds a value from another | any to owned | standard library practice |
| `try_` | may fail; returns `Result` | any | standard library practice |
| `_mut` suffix | gives a mutable view | `&mut` to `&mut` | standard library practice |
| `_unchecked` suffix | skips a check; `unsafe` | any | standard library practice |
| `_lossy` suffix | accepts a lossy result | any | standard library practice |

| Method | Pattern | Cost | Input to output |
|---|---|---|---|
| `str::as_bytes` | `as_` | free | `&str` to `&[u8]` |
| `String::as_str` | `as_` | free | `&String` to `&str` |
| `Vec::as_slice` | `as_` | free | `&Vec<T>` to `&[T]` |
| `Option::as_ref` | `as_` | free | `&Option<T>` to `Option<&T>` |
| `Vec::as_mut_slice` | `as_`, `_mut` | free | `&mut Vec<T>` to `&mut [T]` |
| `str::to_owned` | `to_` | allocates | `&str` to `String` |
| `str::to_lowercase` | `to_` | allocates a new string | `&str` to `String` |
| `slice::to_vec` | `to_` | allocates and clones each item | `&[T]` to `Vec<T>` |
| `Path::to_str` | `to_` | checks UTF-8, no allocation | `&Path` to `Option<&str>` |
| `String::into_bytes` | `into_` | free | `String` to `Vec<u8>` |
| `String::into_boxed_str` | `into_` | may reallocate | `String` to `Box<str>` |
| `Vec::into_iter` | `into_` | free | `Vec<T>` to an iterator of `T` |
| `BufReader::into_inner` | `into_` | free | `BufReader<R>` to `R` |
| `Duration::from_secs` | `from_` | free | `u64` to `Duration` |
| `String::from_utf8` | `from_` | checks UTF-8 | `Vec<u8>` to `Result<String, _>` |
| `String::from_utf8_lossy` | `from_`, `_lossy` | allocates only for invalid bytes | `&[u8]` to `Cow<str>` |
| `i32::try_from` | `try_` | checks the range | `i64` to `Result<i32, _>` |
| `slice::get_unchecked` | `_unchecked` | free; `unsafe` | `&[T]` and an index to `&T` |

Not every `get_` name is a field getter. `get_mut` and `get_unchecked` look up an item by index or key. The API guidelines allow `get` for that case.

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
| Iterator type | The method name in `UpperCamelCase` (C-ITER-TY) | `Iter`, `IterMut`, `IntoIter` |
| Adapter | A verb that describes the step | `map`, `filter`, `take_while` |

## Crates and features

| Case | Rule | Examples |
|---|---|---|
| Crate name | Short, no `-rs` or `-rust` suffix | `serde`, `tokio`, `order_utils` |
| Feature that adds a dependency | The name of the dependency | `serde`, `tokio` |
| Feature that adds a capability | A noun | `json`, `tls`, `std` |
| Feature to avoid | `use-`, `with-` prefix (C-FEATURE); `enable-` is the same kind of word | `use-serde` |

!!! info "See also"

    - [Languages overview](index.md) for the matrix of all languages
    - [Naming patterns](../patterns/index.md) and the [cookbook](../patterns/cookbook.md)
    - [Rust API guidelines: naming](https://rust-lang.github.io/api-guidelines/naming.html), [RFC 430](https://rust-lang.github.io/rfcs/0430-finalizing-naming-conventions.html)
