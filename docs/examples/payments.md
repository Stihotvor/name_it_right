---
status: new
---

# Payments

!!! success "General patterns"

    - Name the intent to pay, the attempt to pay and the movement of money as three separate entities: `payment_intent`, `payment_attempt`, `charge`
    - Name the actor with the word that the payment network uses: `customer`, `merchant`, `acquirer`, `issuer`
    - Keep the amount in minor units with a currency code: `amount_cents`, `currency_code`. Never use a float
    - Use a past participle for a state (`captured`) and a verb for an action (`capture`)
    - Give each money movement its own entity with its own states: `refund`, `dispute`, `payout`

!!! tip "Useful tips"

    - Use `authorized_amount_cents`, `captured_amount_cents` and `refunded_amount_cents` when the amounts differ. A single `amount` hides the difference
    - Use an idempotency key on each create call: `idempotency_key`
    - Use the id of the provider as `provider_payment_intent_id`, and keep your own `id`
    - Store the reason of a failure as a code and a message: `failure_code`, `failure_message`

!!! danger "General anti-patterns"

    - `payment` for the intent, the attempt and the money movement at once
    - `status` for the status of the payment and of the refund in the same field
    - `amount` with no unit and no currency
    - `paid` as the state of a payment or an intent. It does not say authorized or captured. `paid` is fine for a payout, as in Stripe
    - `card_number` in a database column. Store a token and the last four digits

The page uses Stripe words for the examples. Stripe is a de facto reference. The message names of bank-to-bank payments come from ISO 20022 and are in the table below.

## Entities

| Entity | Meaning | Table | Notes |
|---|---|---|---|
| Customer | The payer, as the payment system knows them. | `customers` | |
| Merchant | The business that receives the money. | `merchants` | In a platform: a connected account. |
| Payment method | A way to pay that a customer saved. | `payment_methods` | A card, a bank account, a wallet. |
| Card | A card as a payment method. | `cards` | Keep a token, `last4`, `brand`, `expiry_month`, `expiry_year`. |
| Payment intent | The plan to collect one amount from one customer. | `payment_intents` | Has the whole lifecycle. |
| Payment attempt | One try to pay for an intent. | `payment_attempts` | An intent can have many. |
| Charge | The result of an attempt on a card or a method. | `charges` | Stripe: `Charge`. |
| Authorization | A hold of funds on a card. | `authorizations` | Expires in days. |
| Capture | The taking of held funds. | `captures` | Can be partial. |
| Refund | Money returned to the payer. | `refunds` | Linked to a payment intent. |
| Dispute | A payer asks the bank to reverse a charge. | `disputes` | Often called a chargeback. Strictly, the chargeback is the reversal. |
| Payout | Money sent from the provider to the merchant bank account. | `payouts` | |
| Settlement batch | A group of charges that the acquirer settles together. | `settlement_batches` | |
| Balance transaction | A line that changes the merchant balance. | `balance_transactions` | Charges, fees, refunds, payouts. |
| Fee | A cost of the provider for a charge. | `fees` | |
| Transfer | A move of money between two accounts of the provider. | `transfers` | Not a payout. |
| Mandate | The permission to debit a bank account again. | `mandates` | SEPA, ACH. |
| Invoice payment | A payment for an invoice. | `invoice_payments` | See [SaaS](saas.md). |
| Webhook event | A message from the provider about a change. | `webhook_events` | Store the id to remove duplicates. |
| Idempotency key | A unique key for a create call. | column `idempotency_key` | Not a table in most designs. |

## States

### Payment intent

| State | Meaning | Next states |
|---|---|---|
| `requires_payment_method` | The intent has no method yet, or the last try failed. | `requires_confirmation`, `processing`, `succeeded`, `canceled` |
| `requires_confirmation` | The intent waits for the confirm call. | `requires_action`, `processing`, `requires_capture`, `succeeded`, `canceled` |
| `requires_action` | The payer must do a step (3-D Secure). | `processing`, `requires_capture`, `succeeded`, `requires_payment_method`, `canceled` |
| `processing` | The provider processes the payment. | `requires_capture`, `succeeded`, `requires_payment_method` |
| `requires_capture` | The funds are held and wait for capture. | `succeeded`, `canceled` |
| `succeeded` | The funds are taken. | none |
| `canceled` | The intent is stopped. | none |

### Other entities

| Entity | States |
|---|---|
| Charge | `pending`, `succeeded`, `failed` |
| Refund | `pending`, `requires_action`, `succeeded`, `failed`, `canceled` |
| Dispute | `warning_needs_response`, `warning_under_review`, `warning_closed`, `needs_response`, `under_review`, `won`, `lost` |
| Payout | `pending`, `in_transit`, `paid`, `failed`, `canceled` |
| Settlement batch | `open`, `closed`, `settled` |

The first table follows Stripe `PaymentIntent`. The other lists follow Stripe where Stripe has the object. Stripe adds states in new API versions, so check the version you use. The settlement batch states are community practice.

## Actions

| Action | Function name | Meaning | Trap |
|---|---|---|---|
| Create an intent | `create_payment_intent` | Records the plan to collect money. | No money moves yet. |
| Attach a method | `attach_payment_method` | Links a method to a customer. | |
| Confirm an intent | `confirm_payment_intent` | Starts the attempt. | |
| Authorize | `authorize_payment_intent` | Holds funds. | A hold is not a payment. |
| Capture | `capture_payment_intent` | Takes held funds. | Partial capture is allowed. |
| Void | `void_authorization` | Releases a hold. | Not a refund. In the Stripe model, a void is `cancel_payment_intent` from `requires_capture`. Use `void_authorization` for your own authorization entity. |
| Refund | `refund_payment_intent` | Returns money after capture. | Full or partial. |
| Cancel an intent | `cancel_payment_intent` | Stops an intent before success. | |
| Respond to a dispute | `submit_dispute_evidence` | Sends proof to the bank. | |
| Create a payout | `create_payout` | Sends the balance to the bank. | |
| Reconcile | `reconcile_settlement` | Matches the bank file to your records. | |
| Handle a webhook | `handle_webhook_event` | Applies a provider event once. | Use the event id. |
| Retry | `retry_payment_attempt` | Tries again with the same intent. | New attempt, same intent. |

## Message names (ISO 20022)

Bank-to-bank messages use a fixed family of names. The short form is a message identifier. Use the full name in code and the short form in comments.

| Message | Short form | Meaning |
|---|---|---|
| Customer credit transfer initiation | `pain.001` | The customer asks the bank to send money. |
| Customer payment status report | `pain.002` | The bank reports the status of a request. |
| Customer direct debit initiation | `pain.008` | The creditor asks to debit an account. |
| Financial institution credit transfer | `pacs.008` | One bank asks another bank to send money. |
| Payment return | `pacs.004` | One bank returns a payment. |
| Bank to customer statement | `camt.053` | The statement of an account. |
| Bank to customer debit credit notification | `camt.054` | A notice of one or more entries. |

## Traps

| Trap | Why it is a problem | Better |
|---|---|---|
| `payment` for everything | The intent, the try and the money are different things. | `payment_intent`, `payment_attempt`, `charge`. |
| `authorize` and `capture` as one word | A hold and a capture have different states and amounts. | `authorized_at` and `captured_at`. |
| `cancel`, `void`, `refund`, `reverse` | Four words for stopping a payment. | `cancel` the intent (in Stripe this also releases a hold), `void` for your own authorization entity, `refund` a capture, `reverse` in the ledger. |
| `refund` and `chargeback` | The merchant starts a refund. The payer starts a dispute. | `refund` and `dispute`. |
| `chargeback` and `dispute` | A chargeback is the reversal. A dispute is the case. | `dispute` for the case and `chargeback` only for the reversal. |
| `transfer` and `payout` | A transfer moves money between accounts of the provider. A payout leaves to a bank. | `transfer` and `payout`. |
| `settlement` and `payout` | The acquirer settles. The provider pays out. | Keep both words with their own entity. |
| `fee` and `commission` and `markup` | Three words for the cost. | `fee` for the provider cost, `application_fee` for a platform cut. |
| `amount` | Authorized, captured or refunded? | `authorized_amount_cents`, `captured_amount_cents`, `refunded_amount_cents`. |
| `status = paid` | It hides authorized and captured. | `succeeded` for a Stripe intent. `captured` as a flag or a state of your own charge. `paid` stays correct for a payout. |
| `card` for a token | A card number must never be in your data. | `card_token`, `last4`, `brand`. |
| `reference` | Whose reference? | `merchant_reference`, `provider_payment_intent_id`, `bank_reference`. |
| `currency` | A code or a symbol? | `currency_code` with ISO 4217 (`USD`). |

## Worked example

Inside a table, the status column is just `status`. Code and DTOs keep the full name, for example `payment_intent_status`. The column `requested_amount_cents` is the amount that the merchant asked for. The key `idempotency_key` is unique in the whole table here. Stripe scopes keys per account, so a system with many merchants adds `merchant_id` to the constraint. The table `customers` is not shown.

```sql
CREATE TABLE payment_intents (
    id                      bigint GENERATED ALWAYS AS IDENTITY,
    customer_id             bigint NOT NULL,
    requested_amount_cents  bigint NOT NULL,
    captured_amount_cents   bigint NOT NULL DEFAULT 0,
    refunded_amount_cents   bigint NOT NULL DEFAULT 0,
    currency_code           char(3) NOT NULL,
    status                  text NOT NULL DEFAULT 'requires_payment_method',
    idempotency_key         text NOT NULL,
    provider_payment_intent_id text,
    created_at              timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT pk_payment_intents PRIMARY KEY (id),
    CONSTRAINT fk_payment_intents_customers FOREIGN KEY (customer_id) REFERENCES customers (id),
    CONSTRAINT uq_payment_intents_idempotency_key UNIQUE (idempotency_key),
    CONSTRAINT chk_payment_intents_status_allowed CHECK (status IN (
        'requires_payment_method', 'requires_confirmation', 'requires_action',
        'processing', 'requires_capture', 'succeeded', 'canceled'
    )),
    CONSTRAINT chk_payment_intents_currency_code_format CHECK (currency_code ~ '^[A-Z]{3}$'),
    CONSTRAINT chk_payment_intents_requested_amount_cents_positive CHECK (requested_amount_cents > 0),
    CONSTRAINT chk_payment_intents_captured_within_requested CHECK (captured_amount_cents <= requested_amount_cents),
    CONSTRAINT chk_payment_intents_refunded_within_captured CHECK (refunded_amount_cents <= captured_amount_cents)
);

CREATE INDEX idx_payment_intents_customer_id ON payment_intents (customer_id);

CREATE TABLE refunds (
    id                  bigint GENERATED ALWAYS AS IDENTITY,
    payment_intent_id   bigint NOT NULL,
    amount_cents        bigint NOT NULL,
    currency_code       char(3) NOT NULL,
    status              text NOT NULL DEFAULT 'pending',
    reason_code         text,
    created_at          timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT pk_refunds PRIMARY KEY (id),
    CONSTRAINT fk_refunds_payment_intents FOREIGN KEY (payment_intent_id) REFERENCES payment_intents (id),
    CONSTRAINT chk_refunds_status_allowed CHECK (status IN ('pending', 'requires_action', 'succeeded', 'failed', 'canceled')),
    CONSTRAINT chk_refunds_currency_code_format CHECK (currency_code ~ '^[A-Z]{3}$'),
    CONSTRAINT chk_refunds_amount_cents_positive CHECK (amount_cents > 0)
);

CREATE INDEX idx_refunds_payment_intent_id ON refunds (payment_intent_id);
```

```
POST /v1/payment-intents                              create an intent
POST /v1/payment-intents/{payment_intent_id}:confirm  confirm an intent
POST /v1/payment-intents/{payment_intent_id}:capture  capture the held funds
POST /v1/payment-intents/{payment_intent_id}:cancel   cancel an intent
POST /v1/refunds                                      refund a charge
```

```
PaymentIntentCreated   PaymentIntentSucceeded   ChargeRefunded   DisputeCreated   PayoutPaid
```

```py
def capture_payment_intent(intent: PaymentIntent, capture_amount_cents: int | None = None) -> PaymentIntent:
    if intent.payment_intent_status != "requires_capture":
        raise PaymentIntentStateError(intent.id, intent.payment_intent_status)
    captured_amount_cents = intent.requested_amount_cents if capture_amount_cents is None else capture_amount_cents
    if captured_amount_cents > intent.requested_amount_cents:
        raise AmountTooLargeError(intent.id, captured_amount_cents)
    return intent.with_capture(captured_amount_cents)
```

## Related patterns

- [Booleans, collections, units and time](../patterns/booleans-collections-units-time.md) for amounts, currency codes and timestamps
- [Symmetry](../patterns/symmetry.md) for `authorize` and `void`, `charge` and `refund`
- [Errors](../systems/errors.md) for `failure_code` and error names

!!! info "See also"

    - [Examples overview](index.md), [E-commerce](ecommerce.md), [Fintech](fintech.md) and [REST](../systems/rest.md)
    - [Stripe API reference](https://docs.stripe.com/api), [ISO 20022 message definitions](https://www.iso20022.org/iso-20022-message-definitions), [ISO 4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html)
