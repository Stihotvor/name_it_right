---
status: new
---

# Action and context

A good name answers two questions: what does the code do, and to what? This page shows how to order the words so the answer is clear.

!!! success "General patterns"

    - Use the **A/HC/LC** order: action, high context, low context. `get_user_messages()` reads as "get (action) the user (high context) messages (low context)".
    - Start with the verb in functions and methods: `cancel_order()`, `apply_discount_code()`, `send_receipt_email()`.
    - Put the broad word before the narrow word: `shipping_address_city`, `payment_retry_count`.
    - Make names **S-I-D**: short, intuitive and descriptive. `get_open_orders()` passes. `g_oo()` is short but not intuitive. `get_all_orders_that_are_still_open_and_unpaid()` is descriptive but not short.
    - Keep the high context equal to the thing the code works on. If the function changes an order, `order` is the high context: `refund_order()`, `close_order()`.
    - In a boolean, put the subject before the state: `is_order_valid()`, `is_cart_empty()`.
    - Read the name aloud. If it sounds odd, the word order is probably wrong.

!!! tip "Useful tips"

    - Test a new name by swapping the context words. If the meaning changes, the order matters and you must choose with care: `get_post_tags()` is not `get_tag_posts()`.
    - The module or class often gives the high context. Then drop it from the name: `order.cancel()`, not `order.cancel_order()`.
    - Use one verb for one operation. This guide uses `get_` for a cheap read of known data, `find_` for a search that may return nothing, `list_` for a collection, and `calculate_` for a computed value. You can choose other verbs. Keep them the same in the whole code base. See the [glossary](../common/references-and-glossary.md).
    - For function rules in Python, see [Functions](../python/functions.md).

!!! danger "General anti-patterns"

    - Noun-first function names: `order_cancel()` → `cancel_order()`
    - Context in the wrong order: `message_user_get()` → `get_user_message()`
    - Long chains of context words: `get_all_active_user_unread_messages_count()` → `user.count_unread_messages()`
    - Words with no content: `handle_data()`, `process_item()`, `do_stuff()`
    - Mixed verbs for one operation: `fetch_order()`, `retrieve_invoice()`, `get_refund()` in one code base

## A/HC/LC pattern

The pattern is: `prefix? + action + high context + low context?`. The prefix and the low context are optional. The [naming cheatsheet by kettanaito](https://github.com/kettanaito/naming-cheatsheet) describes the pattern.

| Name | Prefix | Action | High context | Low context |
|---|---|---|---|---|
| `get_user_messages` | | get | user | messages |
| `get_order_total` | | get | order | total |
| `calculate_cart_subtotal` | | calculate | cart | subtotal |
| `apply_coupon` | | apply | coupon | |
| `refund_payment_fee` | | refund | payment | fee |
| `should_retry_payment` | should | retry | payment | |
| `send_order_confirmation_email` | | send | order | confirmation email |

!!! note "Where the pattern does not fit"

    - A name with a prefix such as `is_cart_empty` or `has_order_shipped` has no action. The prefix takes its place: prefix, subject, state.
    - A filter sits next to the noun it filters. In `cancel_pending_orders`, the state `pending` filters `orders`. The form is `action + filter + noun`.
    - A compound noun such as `promo_code` stays together. Do not split it into two contexts.

## Short, intuitive, descriptive (S-I-D)

| Property | Question | Failing example | Passing example |
|---|---|---|---|
| Short | Can you type and read it without effort? | `get_all_orders_that_are_still_open()` | `get_open_orders()` |
| Intuitive | Does it read naturally, like speech? | `order_total_get()` | `get_order_total()` |
| Descriptive | Does it show what the code does and what it does it to? | `handle_order()` | `ship_order()` |

## Verb first

Start function and method names with a verb. The verb tells the reader what happens. The noun tells the reader what it happens to.

| Bad | Better | Why |
|---|---|---|
| `order_cancel()` | `cancel_order()` | Verb first reads as a command. |
| `cart_total()` | `calculate_cart_total()` | A bare noun does not say if the code reads, computes or loads. |
| `email_receipt()` | `send_receipt_email()` | `email` could be a noun or a verb. |
| `discount_apply(code)` | `apply_discount(code)` | Verb first matches `cancel_order()` and `refund_payment()`. |
| `user_by_email()` | `find_user_by_email()` | A bare noun does not say if the code searches, creates or loads. `find` tells the reader that the search can return nothing. |
| `stock_check(sku)` | `is_in_stock(sku)` | A boolean check uses `is_` or `has_`. |
| `invoice_pdf()` | `render_invoice_pdf()` | The verb shows that the code does work. |

Exception: some names are nouns on purpose. A class name is a noun (`OrderCancellation`), and a property is a noun (`order.total`).

## Context order

Put the broad context first and the narrow context last. In alphabetical lists and in editor autocomplete, related names then stay together.

| Bad | Better | Why |
|---|---|---|
| `city_shipping_address` | `shipping_address_city` | `shipping_address_*` names group in the editor. |
| `retry_count_payment` | `payment_retry_count` | The owner (`payment`) comes before the detail. |
| `total_order_price` | `order_total_price` | `order_*` names group together. |
| `date_created_order` | `order_created_date` | Same owner prefix as `order_updated_date`. |
| `name_customer_first` | `customer_first_name` | The reader finds all `customer_*` fields at once. |

## Reordering changes the meaning

The same words in a different order can describe a different thing. The pairs below suit many-to-many data, where each side can have many of the other.

| Name | What it means | Reordered name | What the reordered name means |
|---|---|---|---|
| `get_post_tags()` | Return the tags of one post. | `get_tag_posts()` | Return the posts that carry one tag. |
| `get_user_roles()` | Return the roles of one user. | `get_role_users()` | Return the users that hold one role. |
| `list_order_items()` | List the items in one order. | `list_item_orders()` | List the orders that contain one item. |
| `get_product_categories()` | Return the categories of one product. | `get_category_products()` | Return the products in one category. |
| `count_cart_items()` | Count the items in one cart. | `count_item_carts()` | Count the carts that hold one item. |

### `shouldComponentUpdate` and `shouldUpdateComponent`

React names a lifecycle method [`shouldComponentUpdate`](https://react.dev/reference/react/Component#shouldcomponentupdate). The method sits on the component. It answers the question "should I update?" The component is the subject, so the name does not need to say which component.

This guide suggests a convention for the two word orders. English grammar and React do not require it.

| Name | Reads as | Use it for |
|---|---|---|
| `shouldComponentUpdate` | "Should this component update?" The subject comes first, then the verb. | A method on the thing that decides, with no argument. |
| `shouldUpdateComponent` | "Should (we) update this component?" The verb comes first, then the object. | A function outside the component. The component is the argument. |

In Python, with `snake_case`, the same two forms are:

| Method on the owner | Function outside the owner |
|---|---|
| `order.should_ship()` | `should_ship_order(order)` |
| `cart.is_expired()` | `is_cart_expired(cart)` |
| `payment.can_retry()` | `can_retry_payment(payment)` |
| `subscription.should_renew()` | `should_renew_subscription(subscription)` |

Both orders are valid. Choose by where the code lives, and keep one choice in the whole code base. The React name is an older exception to the verb-first rule. Other languages use `camelCase` for these names (`shouldComponentUpdate`). Python uses `snake_case` (`should_update_component`).

## Examples by context

| Context | Pattern | Examples |
|---|---|---|
| CRUD on a resource | `<verb>_<resource>` | `create_order`, `update_shipping_address`, `delete_expired_carts` |
| Query by key | `find_<resource>_by_<key>` | `find_user_by_email`, `find_product_by_sku` |
| Query many | `list_<filter>_<resources>` | `list_open_orders`, `list_active_discounts` |
| Compute | `calculate_<owner>_<value>` | `calculate_order_total`, `calculate_cart_tax` |
| Side effect | `<verb>_<owner>` | `refund_payment`, `dispatch_order`, `cancel_subscription` |
| Boolean | `is_/has_/should_<owner>_<state>`, `can_<action>_<owner>` | `is_cart_empty`, `has_order_shipped`, `can_cancel_order` |
| Event handler | `on_<owner>_<event>` | `on_order_created`, `on_payment_failed` |
| Converter | `<source>_to_<target>` | `order_to_invoice`, `cents_to_decimal` |

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `data_get()` | `get_customer_profile()` | Verb first, and `data` says nothing. Use this when the function returns a customer profile. |
| `process_order_and_send_email()` | `charge_order()` and `send_order_email()` | `and` in a name often hides two jobs. Split them. |
| `get_all_the_active_orders_for_user()` | `list_user_active_orders()` | Remove filler words. Keep the context order. |
| `handle_cart()` | `merge_guest_cart()` | `handle` hides the action. Use this when the function merges a guest cart into a user cart. |
| `payment_user_id` | `payer_id` | One precise word replaces a chain. Use this when the user is the payer. |
| `get_user_data_list()` | `list_users()` | `list` already says that the result is a collection, and `data` is filler. Use this when the function returns users. |
| `send_email_user()` | `send_email_to_user()` | Without `to`, the reader cannot tell what is sent and what receives it. |

## Sources

- [kettanaito/naming-cheatsheet](https://github.com/kettanaito/naming-cheatsheet) — the A/HC/LC pattern and the S-I-D rule.
- [React: Component, shouldComponentUpdate](https://react.dev/reference/react/Component#shouldcomponentupdate) — the lifecycle method name.
- [Naming Guidelines for Professional Programmers, Hilton and Hermans](https://ppig.org/files/2017-PPIG-28th-hilton.pdf) — evidence on name length and structure.
