---
status: new
---

# Negation and optionality

Names that say what is not true, or values that may be missing, cause many mistakes. This page shows how to write positive names, how to handle a name that you cannot change, and how to name a value that may be absent.

!!! success "General patterns"

    - Name the positive state: `is_enabled`, `has_stock`, `is_active`.
    - Make a flag mean "yes" when it is `True`: `should_send_email = True`, not `skip_email = False`.
    - Use one clear opposite word instead of a prefix: `is_hidden` instead of `is_not_visible`.
    - Name an optional value by its meaning, and show the optional type in the type system: `middle_name: str | None`.
    - Use `NULL` or `None` for "no value". Do not use `-1`, `0`, `""` or `9999-12-31` for it.
    - Use `find_` when no result is a normal answer: `find_coupon()`. On other verbs, add `_or_none` or `_or_default` when the result can be missing: `get_coupon_or_none()`, `get_setting_or_default()`.

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
    - A function that returns `None` without saying so: `get_coupon()` → `find_coupon()`

## Negation

### Double negatives and inverted flags

| Bad | Better | Why |
|---|---|---|
| `is_not_disabled` | `is_enabled` | Two negatives mean one positive. |
| `not is_invalid` | `is_valid` | The reader does not need to flip the meaning. |
| `disable_cache = False` | `is_cache_enabled = True` | A negative name with `False` is a double negative. |
| `skip_validation = False` | `should_validate = True` | The flag says what happens, not what is skipped. |
| `no_discount = False` | `has_discount = True` | The positive form states the fact. |
| `is_not_empty` (a cart or list) | `has_items` | The domain word states what the value holds. For a string, use `is_empty` with `not`. |
| `hide_banner = False` | `is_banner_visible = True` | Use the state, not the command to change it. |
| `is_unavailable = False` | `is_available = True` | Flip the name and the value together. The meaning stays the same. |
| `dont_retry = True` | `should_retry = False` | A name with `dont_` is hard to read in an `if`. The usual default is `should_retry = True`. |
| `ignore_case = False` | `is_case_sensitive = True` | Names the state of the match. |
| `exclude_deleted = False` | `should_include_deleted = True` | Use the positive of the pair. See [Symmetry](symmetry.md). |
| `non_active_users` | `inactive_users` | One word for the opposite state. |

### Negative prefixes

| Prefix | Fine | Use with care | Why |
|---|---|---|---|
| `un-` | `unsubscribed`, `unpaid` | `is_not_unpaid` | Two negatives cancel each other and slow the reader. |
| `in-` | `inactive`, `invalid` | `is_not_inactive` | One negative is enough. |
| `non-` | `non_refundable`, `non_taxable` | `is_non_inactive` | A domain term that is negative by nature is fine. |
| `no_` | the HTTP token `no-cache`, at the boundary | `no_discount_flag` | Prefer `has_` for state. |
| `dis-` | `disabled`, `disconnected` (as domain terms) | `is_not_disabled` | In a boolean name, prefer `is_enabled` and `is_connected`. |

### Names from outside

Some negative names come from a standard. Keep the exact name at the boundary and name your own variable in the positive form.

| Outside name | Where it comes from | Inside name | Why |
|---|---|---|---|
| `Cache-Control: no-cache` | HTTP header | `always_revalidate = True` | The header value is a standard token. `must-revalidate` and `no-store` are different directives. |
| `--no-verify` | Git flag | `should_run_hooks = False` | Keep the flag text in the command line only. The flag skips the commit hooks. |
| `--no-color` | CLI flag | `should_use_color = False` | The flag stays as the user types it. |
| `NOT NULL` | SQL constraint | `is_nullable = False` | The constraint is the storage rule. A required input is a separate rule: `is_required`. |
| `noindex` | HTML robots value | `is_indexing_allowed = False` | The HTML value stays as written. |

## Optionality

### Missing, empty and unknown

| Situation | Name | Value | Why |
|---|---|---|---|
| A value may be missing | `middle_name` | `None` / `NULL` | Absence is not an empty string. |
| A list is empty | `orders` | `[]` | Return an empty list, not `None`. |
| A value is unknown | `delivered_on` | `NULL` until delivery | `NULL` says "not yet". |
| A value does not apply | `company_name` | `NULL` for a person | `NULL` says "not applicable". |
| A value never expires | `expires_at` | `NULL` | Do not use `9999-12-31`. |
| A limit does not exist | `upload_max_bytes` | `None` | Do not use `0` or `-1`. |
| A value exists but is empty | `note` | `""` | Only when an empty note is a real input. |

`NULL` covers "missing", "not yet" and "not applicable". If a reader must tell them apart, add a status field or an enum.

### Names for optional results

| Bad | Better | Why |
|---|---|---|
| `get_coupon()` that may return `None` | `find_coupon()` | `find` says that no result is a normal answer. If you keep `get_`, add `_or_none`. |
| `find_user()` that raises | `get_user()` | `find` suggests that no result is a normal answer. See [Action and context](action-context.md). |
| `get_setting()` with a fallback | `get_setting_or_default()` | The fallback is part of the contract. |
| `try_parse_date()` returning a flag | `parse_date_or_none()` | The name states what comes back. Change the return value too. |
| `lookup_discount()` | `find_discount()` | One verb for a search. See [Action and context](action-context.md). |
| `get_email()` that may return `""` | `get_email_or_none()` | An empty string is a value. Return `None` instead. |
| `user.phone = ""` | `user.phone = None` | The empty string hides the missing value. |
| `discount_cents = -1` | `discount_cents = None` | A sentinel can leak into arithmetic. |
| `deleted = 0 / 1` | `deleted_at = NULL / timestamp` | The timestamp states when. `NULL` states not deleted. |
| `expires_at = '9999-12-31'` | `expires_at = NULL` | A far date is a magic value. |
| `items_max = 0` (no limit) | `items_max = None` | `0` can also mean "none allowed". |
| `limit=-1` (all rows) | `limit=None` | The type shows that there is no limit. |

### Language examples

| Language | Optional field | Why |
|---|---|---|
| Python | `middle_name: str \| None` | The type states it (Python 3.10 or later, otherwise `Optional[str]`). |
| TypeScript | `middleName?: string` | A question mark states that the field may be missing. |
| Go | `MiddleName *string` | A pointer is a common idiom for an optional value. `sql.NullString` is another. |
| SQL | `middle_name TEXT` | Columns accept `NULL` unless you add `NOT NULL`. Add it where a value must exist. |

## Sources

- [Python typing: Optional](https://docs.python.org/3/library/typing.html#typing.Optional) — the optional type.
- [MDN: Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) — the `no-cache` response directive.
- [Git: git-commit documentation](https://git-scm.com/docs/git-commit) — the `--no-verify` option.
- [kettanaito/naming-cheatsheet](https://github.com/kettanaito/naming-cheatsheet) — avoid negative names.
