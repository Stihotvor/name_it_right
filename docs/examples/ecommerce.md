---
status: new
---

# E-commerce

!!! success "General patterns"

    - Use `customer` for a person who buys. Use `user` only for a person who signs in to the system
    - Use `order` for a purchase that the customer has placed. Use `cart` before that
    - Give each entity one state field and one list of states. Do not mix the state of an order with the state of its payment
    - Use a past participle for a state (`shipped`) and a verb for an action (`ship`)
    - Store money in minor units with a currency code: `total_amount_cents`, `currency_code`

!!! tip "Useful tips"

    - Name the money fields for what they hold: `subtotal_amount_cents`, `tax_amount_cents`, `total_amount_cents`
    - Keep `payment`, `shipment` and `return` as separate entities. Each has its own states
    - Use one spelling for words that differ between countries: this guide uses `canceled`, as Stripe does

!!! danger "General anti-patterns"

    - `item` alone. It can mean a product, a variant, a cart line or an order line
    - `status` with no owner. Use `order_status`, `payment_status`, `shipment_status`
    - `total` alone. Name which total: before or after tax, discount and shipping
    - `type` for a payment method or a product kind

## Entities

| Entity | Meaning | Table | Notes |
|---|---|---|---|
| Customer | A person or company that buys. | `customers` | One row per buyer. |
| Address | A place for delivery or billing. | `addresses` | Has a role: billing or shipping. |
| Product | What the shop sells, as a concept. | `products` | A shirt. |
| Variant | A product in a size or color. | `product_variants` | A blue shirt in size M. |
| SKU | The code that identifies a variant for stock. | column `sku` | A text code. Not a table. |
| Category | A group of products. | `categories` | Can nest. |
| Price | The price of a variant in a currency. | `prices` | Can change over time. |
| Cart | Items that a customer may buy. | `carts` | Before the order. |
| Cart line | One variant in a cart. | `cart_items` | Has a quantity. |
| Order | A purchase that the customer placed. | `orders` | Has a number and a state. |
| Order line | One variant in an order, with the price at that time. | `order_items` | Prices are copied here. |
| Payment | A charge for an order. | `payments` | An order can have many. |
| Refund | Money returned for a payment. | `refunds` | Linked to a payment. |
| Shipment | A group of packages sent together. | `shipments` | An order can have many. |
| Package | One physical box. | `packages` | Has a tracking number. |
| Return | Goods that come back. | `returns` | Has lines and a reason. |
| Coupon | A code that gives a discount. | `coupons` | Has limits. |
| Promotion | A rule that gives a discount with no code. | `promotions` | Applies by a condition. |
| Stock level | How many units are in a place. | `stock_levels` | One row per variant and warehouse. |
| Warehouse | A place where stock is kept. | `warehouses` | |
| Review | A customer's rating of a product. | `reviews` | |
| Tax rate | A rule for tax by place and product. | `tax_rates` | |

## States

### Order

| State | Meaning | Next states |
|---|---|---|
| `pending` | The order is placed and not yet paid. | `paid`, `canceled`, `failed` |
| `paid` | The payment is captured. | `processing`, `refunded` |
| `processing` | The shop prepares the goods. | `shipped`, `on_hold`, `canceled` |
| `on_hold` | The shop stopped the order for a check. | `processing`, `canceled` |
| `shipped` | All goods are with the carrier. | `delivered` |
| `partially_shipped` | Some goods are with the carrier. | `shipped` |
| `delivered` | The customer has the goods. | `completed`, `returned` |
| `completed` | The order is closed and no return is open. | none |
| `canceled` | The order was stopped before shipping. | none |
| `failed` | The payment failed. | `pending`, `canceled` |
| `returned` | The goods came back. | `refunded` |
| `refunded` | All the money was returned. | none |
| `partially_refunded` | Some of the money was returned. | `refunded` |

### Payment and shipment

| Entity | States |
|---|---|
| Payment | `pending`, `authorized`, `captured`, `failed`, `voided`, `refunded`, `partially_refunded` |
| Shipment | `label_created`, `in_transit`, `out_for_delivery`, `delivered`, `delivery_failed`, `returned_to_sender` |
| Return | `requested`, `approved`, `received`, `rejected`, `refunded` |

## Actions

| Action | Function name | Meaning | Trap |
|---|---|---|---|
| Add a variant to a cart | `add_item_to_cart` | Creates or changes a cart line. | `add_to_cart` is also fine. Choose one. |
| Remove a variant from a cart | `remove_item_from_cart` | Deletes a cart line. | Not `delete_cart_item` in the API. |
| Apply a coupon | `apply_coupon` | Checks and adds a discount. | `redeem_coupon` marks it as used. |
| Place an order | `place_order` | Turns a cart into an order. | Not `create_order` in the domain. |
| Authorize a payment | `authorize_payment` | Holds the money. | Not the same as capture. |
| Capture a payment | `capture_payment` | Takes the held money. | |
| Void a payment | `void_payment` | Releases a hold before capture. | Not a refund. |
| Cancel an order | `cancel_order` | Stops an order before shipping. | After shipping, use a return. |
| Reserve stock | `reserve_stock` | Holds units for an order. | |
| Release stock | `release_stock` | Frees held units. | |
| Ship an order | `ship_order` | Hands the goods to a carrier. | |
| Mark as delivered | `mark_order_delivered` | Records the delivery. | The carrier does the delivery. |
| Request a return | `request_return` | Starts a return. | |
| Receive a return | `receive_return` | Records that the goods came back. | |
| Refund a payment | `refund_payment` | Returns money. | After capture only. |
| Restock | `restock_items` | Adds returned units to stock. | |

## Traps

| Trap | Why it is a problem | Better |
|---|---|---|
| `order` as a column or a word | `order` is a reserved SQL word. It also means "sort". | `orders` for the table. `purchase_order` for a buyer's order to a supplier. |
| `canceled` and `cancelled` | Two spellings in one code base. | `canceled` everywhere. |
| `cancel`, `void`, `refund` | Three ways to stop a payment. | `void` before capture, `refund` after capture, `cancel` for the order. |
| `status` and `state` | Two words for one idea. | `status` in names, `state` in text about state machines. |
| `total` | Before or after tax, discount and shipping? | `subtotal_amount_cents`, `total_amount_cents`. |
| `price`, `amount`, `cost` | Three words for money. | `unit_price_cents` for the shop's price, `cost_cents` for the shop's cost. |
| `product`, `variant`, `sku`, `item` | Four words for what is sold. | `product` for the concept, `variant` for the sellable unit, `sku` for its code, `order_item` for a line. |
| `customer`, `user`, `account` | Three words for a person. | `customer` buys. `user` signs in. `account` is a login or a ledger. |
| `address` | Billing or shipping? | `billing_address_id`, `shipping_address_id`. |
| `shipment`, `delivery`, `fulfillment` | Three words for sending goods. | `shipment` for the group of packages. `delivered_at` for the event. |
| `stock`, `inventory`, `quantity` | Three words for units. | `stock_level` for the entity, `quantity` for a count in a line. |
| `discount`, `coupon`, `promotion` | Three words for a lower price. | `coupon` has a code. `promotion` has a rule. `discount_amount_cents` is the result. |
| `paid_at` | Authorized or captured? | `authorized_at`, `captured_at`. |
| `return` | A keyword in many languages. | `returns` (plural, a table) and `product_return` (a class). |

## Worked example

The data model in SQL:

```sql
CREATE TABLE customers (
    id              bigint PRIMARY KEY,
    email           text NOT NULL,
    created_at      timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT uq_customers_email UNIQUE (email)
);

CREATE TABLE orders (
    id                      bigint PRIMARY KEY,
    order_number            text NOT NULL,
    customer_id             bigint NOT NULL,
    order_status            text NOT NULL DEFAULT 'pending',
    subtotal_amount_cents   bigint NOT NULL,
    tax_amount_cents        bigint NOT NULL,
    total_amount_cents      bigint NOT NULL,
    currency_code           char(3) NOT NULL,
    placed_at               timestamptz NOT NULL DEFAULT now(),
    shipped_at              timestamptz,
    canceled_at             timestamptz,
    CONSTRAINT uq_orders_order_number UNIQUE (order_number),
    CONSTRAINT fk_orders_customers FOREIGN KEY (customer_id) REFERENCES customers (id),
    CONSTRAINT chk_orders_total_amount_cents_non_negative CHECK (total_amount_cents >= 0)
);

CREATE INDEX idx_orders_customer_id_placed_at ON orders (customer_id, placed_at);

CREATE TABLE order_items (
    order_id            bigint NOT NULL,
    line_number         integer NOT NULL,
    variant_id          bigint NOT NULL,
    quantity            integer NOT NULL,
    unit_price_cents    bigint NOT NULL,
    CONSTRAINT pk_order_items PRIMARY KEY (order_id, line_number),
    CONSTRAINT fk_order_items_orders FOREIGN KEY (order_id) REFERENCES orders (id),
    CONSTRAINT chk_order_items_quantity_positive CHECK (quantity > 0)
);
```

The API paths. For the rules, see [REST](../systems/rest.md):

```
POST   /v1/orders                         place an order
GET    /v1/orders/{order_id}              get one order
GET    /v1/customers/{customer_id}/orders list the orders of a customer
POST   /v1/orders/{order_id}:cancel       cancel an order
POST   /v1/orders/{order_id}:ship         ship an order
POST   /v1/payments/{payment_id}:capture  capture a payment
POST   /v1/payments/{payment_id}:refund   refund a payment
```

The events, in the past tense. For the rules, see [Events](../systems/events.md):

```
OrderPlaced   PaymentCaptured   OrderShipped   OrderCanceled   PaymentRefunded
```

The code:

```py
def place_order(cart: Cart, customer: Customer) -> Order:
    order_items = [build_order_item(line) for line in cart.lines]
    subtotal_amount_cents = sum(item.unit_price_cents * item.quantity for item in order_items)
    tax_amount_cents = calculate_tax_amount_cents(order_items, customer.shipping_address)
    return Order(
        customer_id=customer.id,
        order_items=order_items,
        subtotal_amount_cents=subtotal_amount_cents,
        tax_amount_cents=tax_amount_cents,
        total_amount_cents=subtotal_amount_cents + tax_amount_cents,
        currency_code=cart.currency_code,
    )


def can_cancel_order(order: Order) -> bool:
    return order.order_status in {"pending", "paid", "processing", "on_hold"}
```

!!! info "See also"

    - [Examples overview](index.md), [Tables](../databases/tables.md), [Columns](../databases/columns.md) and [REST](../systems/rest.md)
    - [Stripe API reference](https://docs.stripe.com/api) for payment and refund words
    - [Schema.org: Order](https://schema.org/Order) for a shared vocabulary
