---
status: new
---

# Negation and optionality

Names that say what is not true, or values that may be missing, cause many mistakes. This page shows how to write positive names, how to handle a name that you cannot change, and how to name a value that may be absent.

!!! success "General patterns"

    - Name the positive state: `is_enabled`, `has_stock`, `is_active`.
    - Make a flag mean "yes" when it is `True`: `send_email = True`, not `skip_email = False`.
    - Use one clear opposite word instead of a prefix: `is_hidden` instead of `is_not_visible`.
    - Name an optional value by its meaning, and show the optional type in the type system: `middle_name: str | None`.
    - Use `NULL` or `None` for "no value". Do not use `-1`, `0`, `""` or `9999-12-31` for it.
    - Add `_or_none` or `_or_default` to a function name when the result can be missing: `get_coupon_or_none()`, `get_setting_or_default()`.

!!! tip "Useful tips"

    - Put the name in an `if` and read it aloud. `if not order.is_not_paid` takes two steps to read. `if order.is_paid` takes one.
    - A name that you cannot change comes from an outside standard. Keep it at the boundary and wrap it with a positive name inside your code. See the section "Names from outside".
    - A negative name is fine when the negative is the normal word in the domain: `non_refundable`, `unsubscribed`, `offline`.
    - For the prefixes that start a good boolean, see [Booleans, collections, units and time](booleans-collections-units-time.md).

!!! danger "General anti-patterns"

    - Double negatives: `if not is_not_ready:` → `if is_ready:`
    - Inverted flags: `disable_cache = False` → `is_cache_enabled = True`
    - Negative prefixes that stack: `is_non_inactive` → `is_active`
    - Magic values for "missing": `discount_cents = -1` → `discount_cents = None`
    - A function that returns `None` without saying so: `get_coupon()` → `get_coupon_or_none()`

## Negation

### Double negatives and inverted flags

| Bad | Better | Why |
|---|---|---|
| `is_not_disabled` | `is_enabled` | Two negatives mean one positive. |
| `not is_invalid` | `is_valid` | The reader does not need to flip the meaning. |
| `disable_cache = False` | `is_cache_enabled = True` | A negative name with `False` is a double negative. |
| `skip_validation = False` | `should_validate = True` | The flag says what happens, not what is skipped. |
| `no_discount = False` | `has_discount = True` | The positive form states the fact. |
| `is_not_empty` | `has_items` | The domain word states what the value holds. |
| `hide_banner = False` | `is_banner_visible = True` | Use the state, not the command to change it. |
| `is_unavailable = False` | `is_available = True` | Flip the name, not the value. |
| `dont_retry` | `should_retry` (with the value `False`) | A name with `dont_` is hard to read in an `if`. |
| `ignore_case = False` | `is_case_sensitive = True` | Names the state of the match. |
| `exclude_deleted = False` | `include_deleted = True` | Use the positive of the pair. See [Symmetry](symmetry.md). |
| `non_active_users` | `inactive_users` | One word for the opposite state. |

### Negative prefixes

| Prefix | Fine | Use with care | Why |
|---|---|---|---|
| `un-` | `unsubscribed`, `unpaid` | `unlocked_unavailable` | Stacking two prefixes makes a puzzle. |
| `in-` | `inactive`, `invalid` | `is_not_inactive` | One negative is enough. |
| `non-` | `non_refundable`, `non_taxable` | `is_non_non_member` | A domain term that stays negative is fine. |
| `no_` | `no_cache` (HTTP value) | `no_discount_flag` | Prefer `has_` for state. |
| `dis-` | `disabled`, `disconnected` | `is_not_disabled` | Use the base word: `enabled`, `connected`. |

### Names from outside

Some negative names come from a standard. Keep the exact name at the boundary and name your own variable in the positive form.

| Outside name | Where it comes from | Inside name | Why |
|---|---|---|---|
| `Cache-Control: no-cache` | HTTP header | `must_revalidate = True` | The header value is a standard token. |
| `--no-verify` | Git flag | `should_verify_hooks = False` | Keep the flag text in the command line only. |
| `--no-color` | CLI flag | `use_color = False` | The flag stays as the user types it. |
| `NOT NULL` | SQL constraint | `is_required` (in a model) | The constraint is the storage rule. The model field states the meaning. |
| `noindex` | HTML robots value | `allow_indexing = False` | The HTML value stays as written. |

## Optionality

### Missing, empty and unknown

| Situation | Name | Value | Why |
|---|---|---|---|
| A value may be missing | `middle_name` | `None` / `NULL` | Absence is not an empty string. |
| A list is empty | `orders` | `[]` | A list can be empty. It is never missing. |
| A value is unknown | `delivered_on` | `NULL` until delivery | `NULL` says "not yet". |
| A value does not apply | `company_name` | `NULL` for a person | `NULL` says "not applicable". |
| A value never expires | `expires_at` | `NULL` | Do not use `9999-12-31`. |
| A limit does not exist | `max_upload_bytes` | `None` | Do not use `0` or `-1`. |
| A value exists but is empty | `note` | `""` | Only when an empty note is a real input. |

### Names for optional results

| Bad | Better | Why |
|---|---|---|
| `get_coupon()` that may return `None` | `get_coupon_or_none()` | The name warns the reader. |
| `find_user()` that raises | `get_user()` | `find` suggests that no result is a normal answer. See [Action and context](action-context.md). |
| `get_setting()` with a fallback | `get_setting_or_default()` | The fallback is part of the contract. |
| `try_parse_date()` returning a flag | `parse_date_or_none()` | The name states what comes back. |
| `lookup_discount()` | `find_discount_or_none()` | Verb and result in the name. |
| `get_email()` that may return `""` | `get_email_or_none()` | An empty string is a value. |
| `user.phone = ""` | `user.phone = None` | The empty string hides the missing value. |
| `discount_cents = -1` | `discount_cents = None` | A sentinel can leak into arithmetic. |
| `deleted = 0 / 1` | `deleted_at = NULL / timestamp` | The timestamp states when. `NULL` states not deleted. |
| `expires_at = '9999-12-31'` | `expires_at = NULL` | A far date is a magic value. |
| `max_items = 0` (no limit) | `max_items = None` | `0` can also mean "none allowed". |
| `limit=-1` (all rows) | `limit=None` | The type shows that there is no limit. |

### Language examples

| Language | Optional field | Why |
|---|---|---|
| Python | `middle_name: str \| None` | The type states it. The name stays short. |
| TypeScript | `middleName?: string` | A question mark states that the field may be missing. |
| Go | `MiddleName *string` | A pointer states that the value may be absent. |
| SQL | `middle_name TEXT NULL` | Allow `NULL` only where a missing value is valid. |

## Sources

- [Python typing: Optional](https://docs.python.org/3/library/typing.html#typing.Optional) — the optional type.
- [MDN: Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) — the `no-cache` response directive.
- [Git: git-commit documentation](https://git-scm.com/docs/git-commit) — the `--no-verify` option.
- [kettanaito/naming-cheatsheet](https://github.com/kettanaito/naming-cheatsheet) — avoid negative names.
