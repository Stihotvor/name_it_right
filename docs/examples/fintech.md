---
status: new
---

# Fintech and banking

!!! success "General patterns"

    - Name the ledger parts with the words of accounting: `account`, `ledger_entry`, `journal`, `balance`
    - Record each money change as a new entry. Never change an old entry
    - Use `debit` and `credit` as the two sides of an entry. Do not use `plus` and `minus`
    - Keep the amount in minor units with a currency code: `amount_cents`, `currency_code`
    - Give the booking date and the value date their own names: `booked_at`, `value_date`

!!! tip "Useful tips"

    - Name a balance for the moment it describes: `available_balance_cents`, `ledger_balance_cents`, `pending_balance_cents`
    - Use `posted_at` for the time a journal becomes final, and `created_at` for the time you wrote the row. `booked_at` is a timestamp here and `value_date` is a date. ISO 20022 uses dates for both, so use `booking_date` if you need only the date
    - Use a reference that a person can read: `end_to_end_id`, `statement_reference`
    - Name the unit of a rate: `interest_rate_percent` (4.5 means 4.5%) or `interest_rate_bps`. A plain `_rate` is a 0-to-1 ratio or an exchange rate, such as `fx_rate`

!!! danger "General anti-patterns"

    - `balance` with no kind. Available or ledger?
    - `transaction` for a ledger entry, a database transaction and a payment at the same time
    - `amount` that can be negative with no rule for the sign
    - `date` for the booking date, the value date and the creation date
    - A float for money: `balance = 10.1`

The words come from double-entry bookkeeping, from ISO 20022 and from the vocabulary of retail banks. Names for the bank to customer messages are in [Payments](payments.md).

## Entities

| Entity | Meaning | Table | Notes |
|---|---|---|---|
| Customer | The person or company that owns accounts. | `customers` | |
| Party | Any person or company in a deal. | `parties` | A customer, a counterparty, a beneficiary. |
| Account | A record that holds a balance for one owner. | `accounts` | On this page `account` means the customer account. The books use `ledger_account`. |
| Account holder | The link between a party and an account. | `account_holders` | Joint accounts have more than one. |
| Ledger account | An account of the books of the bank. | `ledger_accounts` | Assets, liabilities, equity, income, expenses. |
| Journal | A group of entries that must balance. | `journals` | The sum of debits equals the sum of credits. |
| Ledger entry | One debit or one credit on one ledger account. | `ledger_entries` | Never changed. |
| Balance | The amount of an account at a moment. | `balances` | A view or a table. |
| Transaction | A business event that makes a journal. | `bank_transactions` | Do not call it `transactions` next to database transactions. |
| Transfer | A move of money between two accounts. | `transfers` | Two entries. |
| Beneficiary | The party that receives a transfer. | `beneficiaries` | |
| Counterparty | The other side of a deal. | `counterparties` | |
| Mandate | The permission to debit an account. | `mandates` | Direct debit. |
| Standing order | A fixed transfer that repeats. | `standing_orders` | |
| Settlement | The final exchange of money between banks. | `settlements` | |
| Reconciliation | The match of two sets of records. | `reconciliations` | Bank file against ledger. |
| Statement | A list of entries for a period. | `statements` | |
| Card | A payment card linked to an account. | `cards` | |
| Loan | Money lent to a customer. | `loans` | |
| Repayment schedule | The plan of loan payments. | `repayment_schedules` | |
| Interest accrual | The interest that builds up per day. | `interest_accruals` | |
| Fee | A charge of the bank. | `fees` | |
| FX rate | The price of one currency in another. | `fx_rates` | |
| KYC check | A check of who the customer is. | `kyc_checks` | Know your customer. |
| AML alert | A flag for a suspicious pattern. | `aml_alerts` | Anti money laundering. |

## States

| Entity | States |
|---|---|
| Account | `pending`, `active`, `frozen`, `dormant`, `closed` |
| Transfer | `created`, `pending`, `booked`, `settled`, `rejected`, `returned`, `canceled` |
| Journal | `open`, `posted`, `reversed`. A posted journal is final, and so are its entries |
| Mandate | `pending`, `active`, `suspended`, `revoked`, `expired` |
| Loan | `applied`, `approved`, `declined`, `canceled`, `disbursed`, `current`, `delinquent`, `defaulted`, `repaid`, `written_off` |
| KYC check | `not_started`, `pending`, `verified`, `rejected`, `expired` |
| AML alert | `open`, `under_review`, `escalated`, `closed_false_positive`, `reported` |

The states are community practice. They follow the vocabulary of retail banking. No standard fixes them. In this guide a transfer is `booked` when its journal is created. The journal is `posted` before the transfer is `settled`.

## Actions

| Action | Function name | Meaning | Trap |
|---|---|---|---|
| Open an account | `open_account` | Creates an account. | `create_account` may skip KYC. |
| Close an account | `close_account` | Ends an account. | The balance must be zero. |
| Freeze an account | `freeze_account` | Blocks debits. | Credits may still come in, by policy. |
| Post a journal | `post_journal` | Checks that the journal balances and makes it final. | Post a whole journal, never one entry. |
| Reverse a journal | `reverse_journal` | Adds a new journal that cancels an old one. | Never delete. The new journal has `reverses_journal_id`. |
| Initiate a transfer | `initiate_transfer` | Starts a transfer. | |
| Book a transfer | `book_transfer` | Creates the journal with its entries. | |
| Settle a transfer | `settle_transfer` | Records the final exchange. | |
| Return a payment | `return_payment` | The receiver bank sends the money back. | Not a refund. |
| Accrue interest | `accrue_interest` | Adds the daily interest. | |
| Capitalize interest | `capitalize_interest` | Adds accrued interest to the principal. | |
| Convert currency | `convert_currency` | Changes an amount with an FX rate. | |
| Reconcile | `reconcile_statement` | Matches the bank file to the ledger. | |
| Verify a customer | `verify_customer` | Runs the KYC check. | |

## Traps

| Trap | Why it is a problem | Better |
|---|---|---|
| `balance` | Available, ledger or pending? | `available_balance_cents`, `ledger_balance_cents`. |
| `transaction` | A ledger entry, a database transaction and a bank event share the word. | `ledger_entry`, `bank_transaction`, `db_transaction`. |
| `debit` and `credit` as signs | Debit means an increase on an asset account and a decrease on a liability account. | A `side` column with `debit` or `credit`, and a positive amount. |
| `amount` with a sign | Plus and minus differ by bank. | `amount_cents` positive, and the side in `side`. |
| `date` | Booking date, value date or creation date? | `booked_at`, `value_date`, `created_at`. |
| `booked` and `posted` and `settled` | Three stages that look alike. In ISO 20022 camt messages, `BOOK` (booked) already means final and `PDNG` means pending. | This guide's convention: `booked` when the transfer is recorded, `posted` when its journal is final in the ledger, `settled` when the money moved between banks. Say which meaning you use. |
| `reverse` and `refund` and `return` | A reverse is an accounting move. A refund is a business act. A return is an interbank message. | `reverse_journal`, `refund_charge`, `return_payment`. |
| `account` | A customer account or a ledger account? | On this page `account` is the customer account. Use `ledger_account` for the books. When both exist in one system, write `customer_account` in full. |
| `iban` as a key | It can change. | A surrogate `id` and a unique `iban`. |
| `interest` | Rate, accrual or paid amount? | `interest_rate_percent`, `interest_accrued_cents`, `interest_paid_cents`. |
| `fee` and `charge` | Charge also means a card payment. | `fee` for a bank cost, `charge` for a card payment. |
| `currency` | A code or a symbol? | `currency_code` with ISO 4217. |
| `rate` | Interest rate or FX rate? | `interest_rate_percent`, `fx_rate`. |

## Worked example

```sql
CREATE TABLE ledger_accounts (
    id              bigint GENERATED ALWAYS AS IDENTITY,
    code            text NOT NULL,
    name            text NOT NULL,
    kind            text NOT NULL,
    currency_code   char(3) NOT NULL,
    CONSTRAINT pk_ledger_accounts PRIMARY KEY (id),
    CONSTRAINT uq_ledger_accounts_code UNIQUE (code),
    CONSTRAINT chk_ledger_accounts_kind_allowed CHECK (kind IN ('asset', 'liability', 'equity', 'income', 'expense'))
);

CREATE TABLE journals (
    id              bigint GENERATED ALWAYS AS IDENTITY,
    description     text NOT NULL,
    booked_at       timestamptz NOT NULL,
    value_date      date NOT NULL,
    status          text NOT NULL DEFAULT 'open',
    posted_at       timestamptz,
    reverses_journal_id bigint,
    created_at      timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT pk_journals PRIMARY KEY (id),
    CONSTRAINT fk_journals_reversed_journal FOREIGN KEY (reverses_journal_id) REFERENCES journals (id),
    CONSTRAINT chk_journals_status_allowed CHECK (status IN ('open', 'posted', 'reversed'))
);

CREATE TABLE ledger_entries (
    id                  bigint GENERATED ALWAYS AS IDENTITY,
    journal_id          bigint NOT NULL,
    ledger_account_id   bigint NOT NULL,
    side                text NOT NULL,
    amount_cents        bigint NOT NULL,
    currency_code       char(3) NOT NULL,
    created_at          timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT pk_ledger_entries PRIMARY KEY (id),
    CONSTRAINT fk_ledger_entries_journals FOREIGN KEY (journal_id) REFERENCES journals (id),
    CONSTRAINT fk_ledger_entries_ledger_accounts FOREIGN KEY (ledger_account_id) REFERENCES ledger_accounts (id),
    CONSTRAINT chk_ledger_entries_side_allowed CHECK (side IN ('debit', 'credit')),
    CONSTRAINT chk_ledger_entries_amount_cents_positive CHECK (amount_cents > 0)
);

CREATE INDEX idx_journals_reverses_journal_id ON journals (reverses_journal_id);
CREATE INDEX idx_ledger_entries_ledger_account_id ON ledger_entries (ledger_account_id);
CREATE INDEX idx_ledger_entries_journal_id ON ledger_entries (journal_id);
```

```
POST /v1/transfers                               initiate a transfer
GET  /v1/accounts/{account_id}/balances          list the balances of an account
GET  /v1/accounts/{account_id}/ledger-entries    list the entries of an account
POST /v1/journals/{journal_id}:reverse           reverse a journal
```

```
TransferInitiated   TransferBooked   TransferSettled   JournalReversed   AccountFrozen
```

The service also checks that the currency of each entry equals the currency of its ledger account.

```py
from collections import defaultdict


def post_journal(journal: Journal) -> None:
    if len(journal.entries) < 2:
        raise UnbalancedJournalError(journal.id, {})
    balance_cents_by_currency: dict[str, int] = defaultdict(int)
    for entry in journal.entries:
        sign = 1 if entry.side == "debit" else -1
        balance_cents_by_currency[entry.currency_code] += sign * entry.amount_cents
    if any(balance_cents != 0 for balance_cents in balance_cents_by_currency.values()):
        raise UnbalancedJournalError(journal.id, dict(balance_cents_by_currency))
    journal.mark_posted(posted_at=utc_now())
```

## Related patterns

- [Symmetry](../patterns/symmetry.md) for `debit` and `credit`, `open` and `close`
- [Booleans, collections, units and time](../patterns/booleans-collections-units-time.md) for `booked_at`, `value_date` and rate units
- [Constraints](../databases/constraints.md) for the checks that keep a journal valid

!!! info "See also"

    - [Examples overview](index.md), [Payments](payments.md), [Columns](../databases/columns.md) and [Constraints](../databases/constraints.md)
    - [ISO 20022 message definitions](https://www.iso20022.org/iso-20022-message-definitions), [ISO 4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html)
