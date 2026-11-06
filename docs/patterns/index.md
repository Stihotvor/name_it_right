---
status: new
---

# Naming patterns

Patterns work across languages. Learn the pattern once, then use it for variables, functions, columns, endpoints and events.

!!! success "General patterns"

    - Order the words as action, high context, low context: `get_user_messages`. See [Action and context](action-context.md).
    - Use one verb for one operation across the code base: `get_order`, `get_invoice`, `get_refund`.
    - Use two to four words per name: `order_total_price`, not `total`, and not `the_total_price_of_the_order_after_tax`.
    - Prefer full words over abbreviations: `customer_id`, not `cust_id`. See [Abbreviations](../common/abbreviations.md).
    - Name a boolean as a statement that is true or false: `is_paid`, `has_discount`, `can_cancel`, `should_retry`.
    - Put the unit in the name when the type does not carry it: `timeout_seconds`, `amount_cents`.

!!! tip "Useful tips"

    - Use the [glossary](../common/references-and-glossary.md) to choose a verb, a noun or a suffix.
    - Check a name with three questions: Does it say what the code does? Does it say to what? Can a new reader guess it?
    - Review names in code review. A bad name costs more than a bad line.

!!! danger "General anti-patterns"

    - Generic names: `data`, `info`, `item`, `handle_stuff()`
    - Names with `and`: `validate_and_save_order()` → `validate_order()` and `save_order()`
    - Names that differ by one letter: `order_item` and `orders_item`
    - Mixed words for one idea: `customer`, `client` and `user` for the same actor

## Pages in this section

| Page | Use it when | Example names |
|---|---|---|
| [Action and context](action-context.md) | You choose the word order of a function or field. | `get_user_messages`, `cancel_order`, `shipping_address_city` |
| [Booleans, collections, units and time](booleans-collections-units-time.md) | You name a flag, a group, a number with a unit or a moment. | `is_paid`, `orders_by_id`, `timeout_seconds`, `created_at_utc` |
| [Symmetry](symmetry.md) | You name two sides of one idea. | `price_min`, `price_max`, `open_session`, `close_session` |
| [Negation and optionality](negation-and-optionality.md) | You name an opposite state or a value that may be missing. | `is_enabled`, `find_coupon`, `expires_at` |

## Pages planned

These pages are not published yet. Most pages use an e-commerce checkout as the running example. Events and commands get their own pages in the systems section.

| Planned page | Topic | Example names |
|---|---|---|
| Bad → better cookbook | 60+ rewrites | `data` → `order_summary` |

## Pattern at a glance

| Pattern | Rule | Good example | Bad example |
|---|---|---|---|
| A/HC/LC | Action, high context, low context | `get_user_messages` | `messages_user_get` |
| Verb first | Functions start with a verb | `cancel_order` | `order_cancel` |
| One verb per operation | Same operation, same verb | `get_invoice` and `get_order` | `retrieve_invoice` next to `get_order` |
| Short and clear | Two to four words | `order_total_price` | `o_tp` |
| Full words | No guessable abbreviations | `customer_id` | `cust_id` |
| Boolean statement | `is_`, `has_`, `can_`, `should_` | `has_discount` | `discount_flag` |
| Units | Unit in the name | `timeout_seconds` | `timeout` |
| Symmetry | Exact opposite words, one pair per idea | `price_min` and `price_max` | `price_min` and `highest_price` |
| Positive names | Name the state that is true | `is_enabled` | `is_not_disabled` |
| Optional results | Say that a result may be missing | `find_coupon` | `get_coupon` that returns `None` |
| Event as fact | Past tense | `order_created` | `create_order_event` |
| Command as instruction | Imperative, as a function name | `create_order` | `order_creation` |

## Sources

- [kettanaito/naming-cheatsheet](https://github.com/kettanaito/naming-cheatsheet) — A/HC/LC and S-I-D (short, intuitive, descriptive).
- [Naming Guidelines for Professional Programmers, Hilton and Hermans](https://ppig.org/files/2017-PPIG-28th-hilton.pdf) — length of names and defects.
- [How Developers Choose Names, Feitelson et al.](https://arxiv.org/abs/2103.07487) — only about 7% of developers choose the same name.
