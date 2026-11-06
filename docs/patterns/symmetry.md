---
status: new
---

# Symmetry

When two names describe opposite or matching sides of one idea, make them look like a pair. A reader who knows `open_session` can then guess `close_session`. This page lists pairs, shows how to choose one pair for one idea, and shows mismatched pairs to avoid.

!!! success "General patterns"

    - Use the exact opposite word: `price_min` and `price_max`, `lock_cart` and `unlock_cart`.
    - Keep the pair at the same length and in the same form: `starts_at` and `ends_at`, not `starts_at` and `finish_time`.
    - Choose one pair for one idea and use it in the whole code base: `source`/`target`, or `source`/`destination`, but not both.
    - Put the shared part first, so that the pair sorts together: `shipping_from`, `shipping_to`. See [Action and context](action-context.md).
    - Use the same verb forms for both sides of an action pair: `add_item` and `remove_item`, not `add_item` and `delete_item_from_cart`.
    - Name a range with its bounds: `price_min` and `price_max`, or `valid_from` and `valid_to`. The glossary uses the suffix form `_min` and `_max`.

!!! tip "Useful tips"

    - When you add a function, ask "What undoes this?" Then name the second function now, even if you write it later.
    - State in the name or in the docs whether a bound is inclusive. For example, write `valid_from` and `valid_to` and document that the start is included and the end is not.
    - Standard libraries often give you the pair. Python locks use `acquire()` and `release()`. Many SQL databases use `BEGIN`, `COMMIT` and `ROLLBACK`.
    - For negative names, see [Negation and optionality](negation-and-optionality.md).

!!! danger "General anti-patterns"

    - Half pairs: `open_session()` with `shutdown_session()`. Use `close_session()`.
    - Different words for the same side: `start_date` in one table and `begin_date` in another.
    - Pairs that are close but not opposite: `price_min` with `highest_price`. Use `price_max`.
    - Two pairs for one idea: `source`/`target` in one module and `origin`/`destination` in another.

## Pairs by category

### Range and bounds

| Pair | Example identifiers | Why |
|---|---|---|
| `min` / `max` | `quantity_min`, `quantity_max` | The exact opposite of the lowest value is the highest value. Suffix form, as in the glossary. |
| `lower` / `upper` | `lower_bound`, `upper_bound` | Use for the edges of an interval. |
| `from` / `to` | `valid_from`, `valid_to` | A range between two points. |
| `starts` / `ends` | `starts_at`, `ends_at` | Moments of an event: same suffix `_at`. |
| `before` / `after` | `placed_before`, `placed_after` | Filters on a moment. |
| `since` / `until` | `since_date`, `until_date` | The start and the end of a period. Say in the docs if the end is included. |

### Position and order

| Pair | Example identifiers | Why |
|---|---|---|
| `first` / `last` | `first_item`, `last_item` | Positions in an ordered group. |
| `head` / `tail` | `queue_head`, `queue_tail` | Ends of a queue or a list. |
| `previous` / `next` | `previous_page`, `next_page` | Neighbours in a sequence. |
| `parent` / `child` | `parent_category`, `child_category` | Levels in a tree. |
| `left` / `right` | `left_node`, `right_node` | Sides of a binary tree. |
| `top` / `bottom` | `top_offset`, `bottom_offset` | Vertical sides in layout code. |

### Direction and flow

| Pair | Example identifiers | Why |
|---|---|---|
| `source` / `target` | `source_warehouse`, `target_warehouse` | Where data or goods leave and arrive. |
| `sender` / `recipient` | `sender_address`, `recipient_address` | The two parties in a message or parcel. |
| `producer` / `consumer` | `order_producer`, `order_consumer` | The two ends of a queue. |
| `inbound` / `outbound` | `inbound_shipment`, `outbound_shipment` | Direction relative to your system. |
| `request` / `response` | `payment_request`, `payment_response` | A call and its answer. |
| `upload` / `download` | `upload_invoice`, `download_invoice` | Direction relative to the client. |
| `import` / `export` | `import_catalog`, `export_catalog` | Data moves into or out of the system. |
| `send` / `receive` | `send_notice`, `receive_notice` | Sides of one transfer. |

### Lifecycle and state

| Pair | Example identifiers | Why |
|---|---|---|
| `open` / `close` | `open_session`, `close_session` | A resource that you must release. |
| `start` / `stop` | `start_worker`, `stop_worker` | A process. |
| `pause` / `resume` | `pause_subscription`, `resume_subscription` | A process that continues later. |
| `enable` / `disable` | `enable_feature`, `disable_feature` | A switch. |
| `lock` / `unlock` | `lock_cart`, `unlock_cart` | A state flag on a record. |
| `acquire` / `release` | `acquire_lock`, `release_lock` | Take and give back a shared resource, such as a lock or a connection. |
| `activate` / `deactivate` | `activate_coupon`, `deactivate_coupon` | A record that changes state. |
| `connect` / `disconnect` | `connect_gateway`, `disconnect_gateway` | A link. |

### Collections and records

| Pair | Example identifiers | Why |
|---|---|---|
| `add` / `remove` | `add_item`, `remove_item` | Change a collection. |
| `create` / `delete` | `create_order`, `delete_order` | Change a stored record. |
| `include` / `exclude` | `include_tax`, `exclude_tax` | A filter or a choice. |
| `attach` / `detach` | `attach_label`, `detach_label` | Link and unlink two records. |
| `register` / `unregister` | `register_webhook`, `unregister_webhook` | Add and remove a listener. |
| `subscribe` / `unsubscribe` | `subscribe_to_newsletter`, `unsubscribe_from_newsletter` | A feed. |
| `load` / `save` | `load_cart`, `save_cart` | Move a record from and to storage. |

### Transform and security

| Pair | Example identifiers | Why |
|---|---|---|
| `encode` / `decode` | `encode_cursor`, `decode_cursor` | A reversible change of format. |
| `serialize` / `deserialize` | `serialize_order`, `deserialize_order` | Object to text and back. |
| `compress` / `decompress` | `compress_export`, `decompress_export` | A reversible size change. |
| `encrypt` / `decrypt` | `encrypt_card_token`, `decrypt_card_token` | A reversible secret. |
| `grant` / `revoke` | `grant_role`, `revoke_role` | A permission. |
| `allow` / `deny` | `allow_list`, `deny_list` | A rule list. |

### Money and transactions

| Pair | Example identifiers | Why |
|---|---|---|
| `debit` / `credit` | `debit_account`, `credit_account` | The two sides of an accounting entry. |
| `authorize` / `void` | `authorize_payment`, `void_authorization` | Hold money, then release the hold. Gateways differ. Stripe Payment Intents use `capture` to take the money and `cancel` on the intent. See [Stripe Payment Intents](https://docs.stripe.com/api/payment_intents/object). |
| `begin` / `commit` / `rollback` | `begin_transaction`, `commit_transaction`, `rollback_transaction` | Common SQL commands. PostgreSQL uses `BEGIN`. Standard SQL spells it `START TRANSACTION`. See [PostgreSQL BEGIN](https://www.postgresql.org/docs/current/sql-begin.html). |
| `buy` / `sell` | `buy_order`, `sell_order` | The two sides of a trade. |
| `charge` / `refund` | `charge_order`, `refund_order` | Take money and give it back. |

## Mismatched pairs

| Bad | Better | Why |
|---|---|---|
| `start_date` / `finish_time` | `starts_at` / `ends_at` | Different words and different types. If you need a date, use `starts_on` and `ends_on`. |
| `begin_session()` / `shutdown_session()` | `open_session()` / `close_session()` | The second word is not the opposite of the first. |
| `add_item()` / `delete_item()` | `add_item()` / `remove_item()` | `add` and `remove` change a collection. `create` and `delete` change a stored record. |
| `price_min` / `highest_price` | `price_min` / `price_max` | `highest` is not the exact opposite of `min`. |
| `enable_feature()` / `turn_off_feature()` | `enable_feature()` / `disable_feature()` | One word family for both sides. |
| `source_warehouse` in one module, `origin_warehouse` in another | `source_warehouse` everywhere | Either pair works. Do not use both. |
| `first_page` / `end_page` | `first_page` / `last_page` | `first` pairs with `last`. |
| `lock_cart()` / `open_cart()` | `lock_cart()` / `unlock_cart()` | `open` does not undo `lock`. |
| `from_date` / `end_date` | `from_date` / `to_date` | Two words of the same type. |
| `sender_address` in one module, `from_address` in another | `sender_address` / `recipient_address` | One word for each side in the whole code base. |
| `parent_id` / `kid_id` | `parent_id` / `child_id` | Use the standard word. |
| `encrypt_token()` / `unlock_token()` | `encrypt_token()` / `decrypt_token()` | `unlock` belongs to `lock`. |

## Sources

- [Python threading: Lock objects](https://docs.python.org/3/library/threading.html#lock-objects) — `acquire()` and `release()`.
- [PostgreSQL: BEGIN](https://www.postgresql.org/docs/current/sql-begin.html) — `BEGIN`, `COMMIT` and `ROLLBACK` in PostgreSQL.
- [Stripe: Payment Intents](https://docs.stripe.com/api/payment_intents/object) — capture and cancel vocabulary.
- [kettanaito/naming-cheatsheet](https://github.com/kettanaito/naming-cheatsheet) — naming heuristics.
