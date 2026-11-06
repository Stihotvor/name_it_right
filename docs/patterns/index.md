---
status: new
---

# Naming patterns

Patterns work across languages. Learn the pattern once, then use it for variables, functions, columns, endpoints and events.

!!! success "General patterns"

    - Order the words as action, high context, low context: `get_user_messages`. See [Action and context](action-context.md).
    - Use one verb for one operation across the code base: `fetch_order`, `fetch_invoice`, `fetch_refund`.
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

## Pages planned

These pages are not published yet. The same running example, an e-commerce checkout, appears on each page.

| Planned page | Topic | Example names |
|---|---|---|
| Booleans | Prefixes and affirmative names | `is_paid`, `has_discount` |
| Collections and counts | Plurals, `_by_`, counts | `orders_by_id`, `order_count` |
| Units and time | Units, money, time zones | `timeout_seconds`, `created_at_utc` |
| Symmetry | Pairs that match | `min_price`, `max_price` |
| Negation and optionality | Avoid double negatives | `is_enabled` instead of `is_not_disabled` |
| Bad → better cookbook | 60+ rewrites | `data` → `order_summary` |

## Pattern at a glance

| Pattern | Rule | Good example | Bad example |
|---|---|---|---|
| A/HC/LC | Action, high context, low context | `get_user_messages` | `messages_user_get` |
| Verb first | Functions start with a verb | `cancel_order` | `order_cancel` |
| One verb per operation | Same operation, same verb | `fetch_invoice` | `retrieve_invoice` next to `get_order` |
| Short and clear | Two to four words | `order_total_price` | `o_tp` |
| Full words | No guessable abbreviations | `customer_id` | `cust_id` |
| Boolean statement | `is_`, `has_`, `can_`, `should_` | `has_discount` | `discount_flag` |
| Units | Unit in the name | `timeout_seconds` | `timeout` |
| Event as fact | Past tense | `order_created` | `create_order_event` |
| Command as order | Imperative | `create_order` | `order_creation` |

## Sources

- [kettanaito/naming-cheatsheet](https://github.com/kettanaito/naming-cheatsheet) — A/HC/LC and S-I-D.
- [Naming Guidelines for Professional Programmers, Hilton and Hermans](https://ppig.org/files/2017-PPIG-28th-hilton.pdf) — length of names and defects.
- [How Developers Choose Names, Feitelson et al.](https://arxiv.org/abs/2103.07487) — only about 7% of developers choose the same name.
