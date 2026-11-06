---
status: new
---

# SaaS

!!! success "General patterns"

    - Name the customer of the product `account` or `organization`, and the person who signs in `user`. Keep the two apart
    - Name what the customer buys (`plan`), what they have now (`subscription`) and what they may use (`entitlement`) as three entities
    - Name the bill `invoice` and each line of it `invoice_item`
    - Name the use of the product with a meter: `meter`, `usage_record`
    - Give each tenant-owned table an `account_id` so that data stays apart

!!! tip "Useful tips"

    - Use `workspace` or `project` for a group inside an account, and pick one word for the whole product
    - Use `seat` for a paid place for a user. A seat is not a user
    - Use `trial_ends_at`, `current_period_start`, `current_period_end` for time limits. They match Stripe Billing
    - Use `feature_key` for the code name of a feature, and `plan_code` for the code name of a plan

!!! danger "General anti-patterns"

    - `user` for the customer who pays and the person who signs in
    - `plan` for the product plan, the price and the subscription at once
    - `status` that mixes billing state and access state
    - `premium` or `is_pro` as a boolean on the user. Use an entitlement
    - A plan name in code: `if plan == "Gold"`. Check an entitlement

The billing words follow Stripe Billing (`Customer`, `Product`, `Price`, `Subscription`, `Invoice`). Payment words are in [Payments](payments.md).

## Entities

| Entity | Meaning | Table | Notes |
|---|---|---|---|
| Account | The customer that pays for the product. | `accounts` | Also called a tenant or an organization. |
| User | A person who signs in. | `users` | |
| Membership | The link between a user and an account. | `memberships` | Has a role. |
| Role | A set of permissions. | `roles` | `owner`, `admin`, `member`. |
| Permission | The right to do one action. | `permissions` | |
| Workspace | A group of resources inside an account. | `workspaces` | |
| Invitation | An offer to join an account. | `invitations` | |
| Product | What the vendor sells. | `products` | |
| Plan | A package of features and limits. | `plans` | Has a code. |
| Price | How much a plan costs for a period. | `prices` | A plan can have many prices. |
| Subscription | The right of an account to a plan for a period. | `subscriptions` | |
| Subscription item | One price inside a subscription. | `subscription_items` | |
| Seat | A paid place for one user. | `seats` | |
| Entitlement | A feature or a limit that an account may use now. | `entitlements` | Comes from the plan and from add-ons. |
| Feature | A capability of the product. | `features` | Has a `feature_key`. |
| Meter | A counter of use. | `meters` | API calls, storage. |
| Usage record | One reading of a meter. | `usage_records` | |
| Invoice | The bill for a period. | `invoices` | |
| Invoice item | One line of an invoice. | `invoice_items` | |
| Credit note | A document that lowers an invoice. | `credit_notes` | |
| Trial | A free period. | column `trial_ends_at` | A field of the subscription. |
| API key | A secret for the API of an account. | `api_keys` | Store a hash. |
| Audit log entry | A record of an action. | `audit_log_entries` | |
| Webhook endpoint | A URL that gets events. | `webhook_endpoints` | |

## States

| Entity | States |
|---|---|
| Subscription (Stripe) | `incomplete`, `incomplete_expired`, `trialing`, `active`, `past_due`, `canceled`, `unpaid`, `paused` |
| Invoice (Stripe) | `draft`, `open`, `paid`, `void`, `uncollectible` |
| Account | `active`, `suspended`, `closed` |
| User | `invited`, `active`, `disabled` |
| Invitation | `pending`, `accepted`, `expired`, `revoked` |
| API key | `active`, `revoked`, `expired` |

Keep the billing state (`past_due`) apart from the access state (`suspended`). A policy maps one to the other. For example, a subscription that stays `past_due` for 14 days suspends the account.

## Actions

| Action | Function name | Meaning | Trap |
|---|---|---|---|
| Sign up | `sign_up_account` | Creates an account and its first user. | |
| Invite a user | `invite_user` | Sends an invitation. | |
| Accept an invitation | `accept_invitation` | Creates a membership. | |
| Subscribe | `subscribe_account` | Starts a subscription. | |
| Change a plan | `change_plan` | Moves a subscription to another price. | Decide on proration. |
| Start a trial | `start_trial` | Sets the trial end. | |
| Cancel at period end | `cancel_subscription_at_period_end` | The subscription ends later. | Not the same as cancel now. |
| Cancel now | `cancel_subscription` | The subscription ends now. | |
| Add a seat | `add_seat` | Adds a paid place. | |
| Assign a seat | `assign_seat` | Gives a place to a user. | |
| Record usage | `record_usage` | Adds a meter reading. | Use an idempotency key. |
| Issue an invoice | `finalize_invoice` | Moves a draft to open. | |
| Void an invoice | `void_invoice` | Cancels an open invoice. | |
| Check an entitlement | `has_entitlement` | Answers whether a feature is on. | Do not test the plan name. |
| Revoke an API key | `revoke_api_key` | Disables a key. | |
| Suspend an account | `suspend_account` | Blocks access. | |

## Traps

| Trap | Why it is a problem | Better |
|---|---|---|
| `user` | A person who signs in and a customer who pays are different. | `user` signs in. `account` pays. |
| `customer` | Stripe calls the payer a customer. Your product may call it an account. | `account`, with `provider_customer_id` for the Stripe id. |
| `plan` | A plan, a price and a subscription differ. | `plan` for the package, `price` for the cost, `subscription` for the account link. |
| `organization`, `account`, `tenant`, `workspace` | Four words for a group. | `account` for the payer, `workspace` for a sub-group. Say that `tenant` is a technical word. |
| `member` and `user` | A member is a user in one account. | `membership` for the link. |
| `seat` and `license` | Two words for a paid place. | `seat`. |
| `limit` and `quota` | Two words for a cap. | `limit` for the cap on the plan, `usage` for the count. |
| `subscription_status` | Billing or access? | `billing_status` and `access_status` in code. |
| `is_pro` | A flag on the user hides the source of the right. | `has_entitlement("advanced_reports")`. |
| `cancel` | Now or at period end? | `cancel_subscription` and `cancel_subscription_at_period_end`. |
| `expired` and `canceled` | A trial can expire. A subscription is canceled. | `trial_ended_at`, `canceled_at`. |
| `usage` | A reading or a total? | `usage_record` for a reading, `usage_total` for a sum. |
| `amount_due` and `amount_paid` | An invoice has many amounts. | `amount_due_cents`, `amount_paid_cents`, `amount_remaining_cents`. |

## Worked example

```sql
CREATE TABLE accounts (
    id          bigint GENERATED ALWAYS AS IDENTITY,
    name        text NOT NULL,
    status      text NOT NULL DEFAULT 'active',
    created_at  timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT pk_accounts PRIMARY KEY (id),
    CONSTRAINT chk_accounts_status_allowed CHECK (status IN ('active', 'suspended', 'closed'))
);

CREATE TABLE subscriptions (
    id                      bigint GENERATED ALWAYS AS IDENTITY,
    account_id              bigint NOT NULL,
    plan_id                 bigint NOT NULL,
    status                  text NOT NULL,
    trial_ends_at           timestamptz,
    current_period_start    timestamptz NOT NULL,
    current_period_end      timestamptz NOT NULL,
    cancel_at_period_end    boolean NOT NULL DEFAULT false,
    canceled_at             timestamptz,
    CONSTRAINT pk_subscriptions PRIMARY KEY (id),
    CONSTRAINT fk_subscriptions_accounts FOREIGN KEY (account_id) REFERENCES accounts (id),
    CONSTRAINT fk_subscriptions_plans FOREIGN KEY (plan_id) REFERENCES plans (id),
    CONSTRAINT chk_subscriptions_status_allowed CHECK (status IN (
        'incomplete', 'incomplete_expired', 'trialing', 'active',
        'past_due', 'canceled', 'unpaid', 'paused'
    ))
);

CREATE INDEX idx_subscriptions_account_id ON subscriptions (account_id);
CREATE INDEX idx_subscriptions_plan_id ON subscriptions (plan_id);

CREATE TABLE entitlements (
    account_id      bigint NOT NULL,
    feature_key     text NOT NULL,
    limit_value     bigint,
    CONSTRAINT pk_entitlements PRIMARY KEY (account_id, feature_key),
    CONSTRAINT fk_entitlements_accounts FOREIGN KEY (account_id) REFERENCES accounts (id)
);
```

The table `plans` is not shown.

```
POST /v1/subscriptions                                      subscribe an account
POST /v1/subscriptions/{subscription_id}:cancel             cancel now
GET  /v1/accounts/{account_id}/entitlements                 list the entitlements
POST /v1/invoices/{invoice_id}:finalize                     issue an invoice
POST /v1/usage-records                                      record usage
```

```
SubscriptionCreated   SubscriptionPastDue   SubscriptionCanceled   InvoicePaid   AccountSuspended
```

```py
def has_entitlement(account: Account, feature_key: str) -> bool:
    entitlement = account.entitlements.get(feature_key)
    return entitlement is not None and (entitlement.limit_value is None or entitlement.limit_value > 0)
```

!!! info "See also"

    - [Examples overview](index.md), [Payments](payments.md), [Tables](../databases/tables.md) and [Feature flags](../systems/feature-flags.md)
    - [Stripe Billing](https://docs.stripe.com/billing)
