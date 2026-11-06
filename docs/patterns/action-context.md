---
status: new
---

# Action and context

A good name answers two questions: what does the code do, and to what? This page shows how to order the words so the answer is clear.

!!! success "General patterns"

    - Use the **A/HC/LC** order: action, high context, low context. `get_user_messages()` reads as "get (action) the user (high context) messages (low context)".
    - Start with the verb in functions and methods: `cancel_order()`, `apply_discount_code()`, `send_receipt_email()`.
    - Put the broad word before the narrow word: `shipping_address_city`, `payment_retry_count`.
    - Make names **S-I-D**: short, intuitive and descriptive. `fetch_open_orders()` passes. `f_oo()` is short but not intuitive. `fetch_all_orders_that_are_still_open_and_unpaid()` is descriptive but not short.
    - Keep the high context equal to the thing the code works on. If the function changes an order, `order` is the high context: `refund_order()`, `close_order()`.
    - Read the name aloud. If it sounds odd, the word order is probably wrong.

!!! tip "Useful tips"

    - Test a new name by swapping the context words. If the meaning changes, the order matters and you must choose with care: `get_payment_refunds()` is not `get_refund_payments()`.
    - The module or class often gives the high context. Then drop it from the name: `order.cancel()`, not `order.cancel_order()`.
    - For the verb list, use one term per operation. See the [glossary](../common/references-and-glossary.md).
    - For function rules in Python, see [Functions](../python/functions.md).

!!! danger "General anti-patterns"

    - Noun-first function names: `order_cancel()` → `cancel_order()`
    - Context in the wrong order: `message_user_get()` → `get_user_message()`
    - Long chains of context words: `get_all_active_user_unread_messages_count()` → `count_unread_messages()` on a `user` object
    - Words with no content: `handle_data()`, `process_item()`, `do_stuff()`
    - Mixed verbs for one operation: `fetch_order()`, `retrieve_invoice()`, `get_refund()` in one codebase

## A/HC/LC pattern

The pattern is: `prefix? + action + high context + low context?`. The prefix and the low context are optional. The [naming cheatsheet by kettanaito](https://github.com/kettanaito/naming-cheatsheet) describes the pattern.

| Name | Prefix | Action | High context | Low context |
|---|---|---|---|---|
| `get_user_messages` | | get | user | messages |
| `get_order_total` | | get | order | total |
| `calculate_cart_subtotal` | | calculate | cart | subtotal |
| `apply_promo_code` | | apply | promo | code |
| `refund_payment_fee` | | refund | payment | fee |
| `should_retry_payment` | should | retry | payment | |
| `is_cart_empty` | is | | cart | empty |
| `has_order_shipped` | has | | order | shipped |
| `cancel_pending_orders` | | cancel | orders | pending |
| `send_order_confirmation_email` | | send | order | confirmation email |

!!! note "Pending is a state, not a context"

    In `cancel_pending_orders`, the state `pending` filters the high context `orders`. Keep filters close to the noun they filter.

## Short, intuitive, descriptive (S-I-D)

| Property | Question | Failing example | Passing example |
|---|---|---|---|
| Short | Can you type and read it without effort? | `fetch_all_orders_that_are_still_open()` | `fetch_open_orders()` |
| Intuitive | Does it read naturally, like speech? | `order_total_get()` | `get_order_total()` |
| Descriptive | Does it show what the code does and what it does it to? | `handle_order()` | `ship_order()` |

## Verb first

Start function and method names with a verb. The verb tells the reader what happens. The noun tells the reader what it happens to.

| Bad | Better | Why |
|---|---|---|
| `order_cancel()` | `cancel_order()` | Verb first reads as a command. |
| `cart_total()` | `calculate_cart_total()` | A bare noun does not say if the code reads, computes or fetches. |
| `email_receipt()` | `send_receipt_email()` | `email` could be a noun or a verb. |
| `discount_apply(code)` | `apply_discount(code)` | Verb first matches `cancel_order()` and `refund_payment()`. |
| `user_by_email()` | `find_user_by_email()` | The verb says what the search returns when nothing is found. |
| `stock_check(sku)` | `is_in_stock(sku)` | A boolean check uses `is_` or `has_`. |
| `invoice_pdf()` | `render_invoice_pdf()` | The verb shows that the code does work. |

Exception: some APIs use nouns on purpose. A class name is a noun (`OrderCancellation`), and a property is a noun (`order.total`).

## Context order

Put the broad context first and the narrow context last. The order lets editors sort and group related names.

| Bad | Better | Why |
|---|---|---|
| `city_shipping_address` | `shipping_address_city` | `shipping_address_*` names group in the editor. |
| `retry_count_payment` | `payment_retry_count` | The owner (`payment`) comes before the detail. |
| `total_order_price` | `order_total_price` | `order_*` names group together. |
| `date_created_order` | `order_created_date` | Same owner prefix as `order_updated_date`. |
| `name_customer_first` | `customer_first_name` | The reader finds all `customer_*` fields at once. |

## Reordering changes the meaning

The same words in a different order can describe a different thing. Check the order against what the code does.

| Name | What it means | Reordered name | What the reordered name means |
|---|---|---|---|
| `get_payment_refunds()` | Return the refunds of one payment. | `get_refund_payments()` | Return the payments that belong to one refund. |
| `get_user_orders()` | Return the orders of one user. | `get_order_users()` | Return the users linked to one order. |
| `count_failed_logins()` | Count the logins that failed. | `count_login_failures()` | Count failure events about login. The meaning is close, but a failed login and a failure event are not always the same row. |
| `is_valid_order()` | A check on any order, `True` if the order is valid. | `is_order_valid()` | A check on one known order. The word order matches the `is_` + subject + state form. |
| `load_cart_items()` | Load the items of a cart. | `load_item_carts()` | Load the carts that hold an item. |
| `send_email_user()` | Unclear. Does it send an email, or send a user? | `send_user_email()` | Send an email to the user. |

### `shouldUpdateComponent` vs `shouldComponentUpdate`

React names the lifecycle method [`shouldComponentUpdate`](https://react.dev/reference/react/Component#shouldcomponentupdate). The same words in another order give a different reading.

| Name | Reads as | Who decides |
|---|---|---|
| `shouldComponentUpdate` | "Should this component update?" The component is the subject and `update` is the question about it. | The component answers about itself. |
| `shouldUpdateComponent` | "Should (I) update this component?" The component is the object of an action. | A caller decides about another component. |

The first name fits a method on the component. The second name fits a function outside the component, for example in a renderer or a scheduler. Both are valid. The two names are not interchangeable.

The same rule applies in other domains:

| Subject decides | Caller decides |
|---|---|
| `shouldOrderShip` | `shouldShipOrder` |
| `canPaymentRetry` | `canRetryPayment` |
| `willCartExpire` | `willExpireCart` |

## Examples by context

| Context | Pattern | Examples |
|---|---|---|
| CRUD on a resource | `<verb>_<resource>` | `create_order`, `update_shipping_address`, `delete_expired_carts` |
| Query by key | `find_<resource>_by_<key>` | `find_user_by_email`, `find_product_by_sku` |
| Query many | `list_<filter>_<resources>` | `list_open_orders`, `list_active_discounts` |
| Compute | `calculate_<owner>_<value>` | `calculate_order_total`, `calculate_cart_tax` |
| Side effect | `<verb>_<owner>` | `refund_payment`, `dispatch_order`, `cancel_subscription` |
| Boolean | `is_/has_/can_/should_<owner>_<state>` | `is_cart_empty`, `has_order_shipped`, `can_order_be_cancelled` |
| Event handler | `on_<owner>_<event>` | `on_order_created`, `on_payment_failed` |
| Converter | `<source>_to_<target>` | `order_to_invoice`, `cents_to_decimal` |

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `data_get()` | `get_customer_profile()` | Verb first, and `data` says nothing. |
| `process_order_and_send_email()` | `complete_order()` | `and` in a name often hides two jobs. Split them: `charge_order()`, `send_order_email()`. |
| `get_all_the_active_orders_for_user()` | `list_user_active_orders()` | Remove filler words. Keep the context order. |
| `handle_cart()` | `merge_guest_cart()` | `handle` hides the action. |
| `payment_user_id` | `payer_id` | One precise word replaces a chain. |
| `get_user_data_list()` | `list_users()` | `data` and `list` repeat what the plural already says. |

## Sources

- [kettanaito/naming-cheatsheet](https://github.com/kettanaito/naming-cheatsheet) — the A/HC/LC pattern and the S-I-D rule.
- [React: Component, shouldComponentUpdate](https://react.dev/reference/react/Component#shouldcomponentupdate) — the lifecycle method name.
- [Naming Guidelines for Professional Programmers, Hilton and Hermans](https://ppig.org/files/2017-PPIG-28th-hilton.pdf) — evidence on name length and structure.
