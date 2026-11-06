---
status: new
---

# Feature flags

!!! success "General patterns"

    - Name a flag for the feature it controls, not for the team or the ticket: `checkout_one_click`, not `team_b_flag_2`
    - Write a flag as a positive statement: `new_checkout_enabled`, not `disable_old_checkout`
    - Use one case style for all flags, and keep the style of the flag tool
    - Put the kind of flag in the name or in the tool: release, experiment, operations, permission
    - Give each flag an owner and a removal date

!!! tip "Useful tips"

    - Use a prefix for the area when the project has many flags: `checkout_`, `search_`
    - Name the flag for the new behavior, so the code reads well: `if flags.checkout_one_click:`
    - Remove a release flag when the feature is fully on. A flag that stays for months is a hidden branch in the code
    - Use `kill_switch` in the name of an operations flag that turns off a risky part in an incident

!!! danger "General anti-patterns"

    - A negative name: `disable_cache`, `no_new_ui`
    - A name with a ticket or a person: `jira_1234`, `anna_test`
    - A vague name: `new_feature`, `flag1`, `test`
    - A name with a version or a state in it: `new_search_v2_on`
    - A flag that is never removed

The examples use an e-commerce shop. No standard sets flag names. The OpenFeature specification only says that a flag key is a string. The patterns below are community practice. The four kinds of flag (release, experiment, operations, permission) come from Martin Fowler's article on feature toggles. For the same rules on environment variables, see [Configuration](configuration.md).

## Names by kind

| Kind | Pattern | Examples | Why this name |
|---|---|---|---|
| Release flag | `<feature>_enabled` or `<feature>` | `checkout_one_click_enabled`, `new_search_ranking` | Turns on a finished feature step by step. |
| Experiment | `exp_<name>`; choose this one form | `exp_cart_recommendations`, `exp_pricing_page` | The prefix marks a test that ends. |
| Operations flag | `<area>_<behavior>_enabled` | `payment_retry_enabled`, `search_cache_enabled` | Controls the load or the behavior of the system. |
| Kill switch (practice) | `<area>_kill_switch` | `recommendations_kill_switch`, `email_sending_kill_switch` | Turns a part off in an incident. |
| Permission flag | `<capability>_allowed` or `<plan>_<feature>` | `bulk_export_allowed`, `pro_reports` | Gives a feature to a group of users. |
| Variant | the name of the arm | `control`, `treatment`, `variant_a` | The values of an experiment. |
| Percentage rollout (practice) | the flag stays the same; the percent is data | `new_checkout_enabled` at 10% | Do not put the number in the name. |
| Dark launch (practice) | `<feature>_dark` or `<feature>_shadow` | `new_pricing_shadow` | Runs the code with no effect for the user. |
| Migration flag (practice) | `migrate_<what>` | `migrate_orders_to_new_db` | The flag ends with the migration. |

## Flag lifecycle

| Stage | Meaning | Action | Example |
|---|---|---|---|
| Created | The flag exists and is off. | Name it, set an owner and a removal date. | `new_checkout_enabled` |
| Rolling out | The flag is on for a part of the users. | Watch the metrics. | 5%, 25%, 100% |
| Fully on | The flag is on for all users. | Remove the old code path. | |
| Removed | The flag and the old code are gone. | Delete the flag in the tool. | |
| Permanent | An operations flag or a permission flag stays. | Review it each quarter. | `payment_retry_enabled` |

## Flag metadata

| Field | Meaning | Example |
|---|---|---|
| `key` | The name that code uses. | `new_checkout_enabled` |
| `description` | One sentence on what the flag does. | `Shows the one-click checkout button.` |
| `owner` | The team or person who removes it. | `checkout-team` |
| `kind` | The type of flag. | `release` |
| `created_at` | When the flag was made. | `2026-11-07` |
| `remove_by` | The date to remove it. | `2026-12-31` |

## In the code

| Case | Rule | Examples |
|---|---|---|
| Constant for a key | Use the case of the language | `FLAG_NEW_CHECKOUT`, `flags.newCheckoutEnabled` |
| Call that reads a flag | A boolean question; OpenFeature names it `getBooleanValue` | `is_enabled("new_checkout_enabled")`, `client.getBooleanValue("new_checkout_enabled", false)` |
| A branch | Name the new path for what it does | `if new_checkout_enabled: render_one_click()` |
| A test | Name the flag state | `test_checkout_with_one_click_enabled` |

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `disable_old_checkout` | `new_checkout_enabled` | A positive name. |
| `flag1` | `checkout_one_click_enabled` | A name states the feature. |
| `jira_1234` | `checkout_one_click_enabled` | A ticket id says nothing about the feature. |
| `new_search_v2_on` | `new_search_ranking` | A version number and `on` become wrong when the flag changes. The suffix `_enabled` is different: it names the question, and the flag value answers it. |
| `anna_test` | `exp_cart_recommendations` | Name the test, not the person. |
| `use_new_db` | `migrate_orders_to_new_db` | The flag is for a migration with an end. |
| `experiment` | `exp_cart_recommendations` | A prefix and a subject. |
| `killswitch` | `recommendations_kill_switch` | Say what it turns off. |

!!! info "See also"

    - [Systems overview](index.md), [Observability](observability.md) and [Configuration](configuration.md)
    - [OpenFeature specification](https://openfeature.dev/specification/), [Martin Fowler: feature toggles](https://martinfowler.com/articles/feature-toggles.html)
