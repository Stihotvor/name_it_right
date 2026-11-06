---
status: new
---

# E-commerce

!!! success "General patterns"

    - Use `customer` for a person who buys. Use `user` only for a person who signs in to the system
    - Use `order` for a purchase that the customer has placed. Use `cart` before that
    - Give each entity its own state field and its own list of states. Do not mix the state of an order with the state of its payment
    - Use a past participle for a state (`shipped`) and a verb for an action (`ship`)
    - Store money in minor units with a currency code: `total_amount_cents`, `currency_code`

!!! tip "Useful tips"

    - Name the money fields for what they hold: `subtotal_amount_cents`, `tax_amount_cents`, `total_amount_cents`
    - Keep `payment`, `shipment` and `return` as separate entities. Each has its own states
    - Pick one spelling for `canceled` and keep it. This guide uses `canceled`, as Stripe does. Shopify, Schema.org (`OrderCancelled`) and the glossary of this guide also show `cancelled`. If you map to one of those, keep their spelling in the mapped field
    - `_cents` assumes a currency with two decimals. For other currencies use `_minor_units` (see [Columns](../databases/columns.md))

!!! danger "General anti-patterns"

    - `item` alone. It can mean a product, a variant, a cart item or an order item
    - `status` with no owner in code. Use `order_status`, `payment_status`, `shipment_status` for variables and fields in a DTO. Inside the `orders` table the column is just `status`
    - `total` alone. Name which total: before or after tax, discount and shipping
    - `type` for a payment method or a product kind

The states below are the choice of this guide. They map loosely to Stripe, Shopify and Schema.org, and they are not a copy of any of them.

## Entities

| Entity | Meaning | Table | Notes |
|---|---|---|---|
| Customer | A person or company that buys. | `customers` | One row per buyer. |
| Address | A place. | `addresses` | The order points to a billing and a shipping address. |
| Product | What the shop sells, as a concept. | `products` | A shirt. |
| Variant | A product in a size or color. | `product_variants` | A blue shirt in size M. |
| SKU | The code that identifies a variant for stock. | column `sku` | A text code. Not a table. |
| Category | A group of products. | `categories` | Can nest. |
| Price | The price of a variant in a currency. | `prices` | Can change over time. |
| Cart | What a customer may buy. | `carts` | Before the order. |
| Cart item | One variant in a cart. | `cart_items` | Has a quantity. |
| Order | A purchase that the customer placed. | `orders` | Has a number and a state. |
| Order item | One variant in an order, with the price at that time. | `order_items` | The line of an order. Prices are copied here. |
| Payment | A charge for an order. | `payments` | An order can have many. |
| Refund | Money returned for a payment. | `refunds` | Linked to a payment. |
| Shipment | A group of packages sent together. | `shipments` | An order can have many. |
| Package | One physical box. | `packages` | Has a tracking number. |
| Return | Goods that come back. | `returns` | Has items and a reason. |
| Coupon | A discount that a customer enters as a code. | `coupons` | Has limits. Stripe splits it: `Coupon` is the rule and `PromotionCode` is the code. |
| Promotion | A rule that gives a discount with no code. | `promotions` | Applies by a condition. Shopify: an automatic discount. |
| Stock level | How many units are in a place. | `stock_levels` | One row per variant and warehouse. |
| Warehouse | A place where stock is kept. | `warehouses` | |
| Review | A customer's rating of a product. | `reviews` | |
| Tax rate | A rule for tax by place and product. | `tax_rates` | |

## States

### Order

The order states cover the work on the order. The money is in the payment states below.

| State | Meaning | Next states |
|---|---|---|
| `pending` | The order is placed. Payment may be open. | `processing`, `on_hold`, `canceled` |
| `processing` | The shop prepares the goods. | `partially_shipped`, `shipped`, `on_hold`, `canceled` |
| `on_hold` | The shop stopped the order for a check. | `processing`, `canceled` |
| `partially_shipped` | Some goods are with the carrier. | `shipped` |
| `shipped` | All goods are with the carrier. | `delivered` |
| `delivered` | The customer has the goods. | `completed` |
| `completed` | The order is closed and no return is open. | none |
| `canceled` | The order was stopped before shipping. | none |

A return does not change the order state. It has its own states. A refund changes the payment state.

### Payment, shipment and return

| Entity | State | Meaning | Next states |
|---|---|---|---|
| Payment | `pending` | The payment waits for the customer or the bank. | `authorized`, `failed` |
| | `authorized` | The funds are held. | `captured`, `voided` |
| | `captured` | The funds are taken. | `partially_refunded`, `refunded` |
| | `failed` | The bank refused. | none |
| | `voided` | The hold was released. | none |
| | `partially_refunded` | Some money was returned. | `refunded` |
| | `refunded` | All money was returned. | none |
| Shipment | `label_created` | The carrier label exists. | `in_transit` |
| | `in_transit` | The carrier has the package. | `out_for_delivery`, `delivered`, `delivery_failed` |
| | `out_for_delivery` | The package is on the last leg. | `delivered`, `delivery_failed` |
| | `delivery_failed` | The carrier could not deliver. | `in_transit`, `returned_to_sender` |
| | `delivered` | The package arrived. | none |
| | `returned_to_sender` | The package went back to the shop. | none |
| Return | `requested` | The customer asked for a return. | `approved`, `rejected` |
| | `approved` | The shop accepts the return. | `received` |
| | `rejected` | The shop refuses the return. | `closed` |
| | `received` | The goods came back. | `closed` |
| | `closed` | The return is finished. A refund may follow. | none |

Words differ by platform. Stripe has no `captured` state for a payment intent (`captured` is a flag on a charge). Stripe cancels an uncaptured payment, and `voided` is the word of Shopify and Braintree. Shopify names the return states `REQUESTED`, `OPEN`, `CLOSED`, `CANCELED` and `DECLINED`.

## Actions

| Action | Function name | Meaning | Trap |
|---|---|---|---|
| Add a variant to a cart | `add_item_to_cart` | Creates or changes a cart item. | Do not use `add_to_cart`. |
| Remove a variant from a cart | `remove_item_from_cart` | Deletes a cart item. | In the API it is `DELETE /v1/carts/{cart_id}/items/{item_id}`. |
| Apply a coupon | `apply_coupon` | Checks and adds a discount. | `redeem_coupon` marks it as used. |
| Place an order | `place_order` | Turns a cart into an order. | The API route is `POST /v1/carts/{cart_id}:checkout`. |
| Authorize a payment | `authorize_payment` | Holds the money. | Not the same as capture. |
| Capture a payment | `capture_payment` | Takes the held money. | |
| Void a payment | `void_payment` | Releases a hold before capture. | Not a refund. |
| Cancel an order | `cancel_order` | Stops an order before shipping. | If the order is paid, also void or refund the payment. After shipping, use a return. |
| Reserve stock | `reserve_stock` | Holds units for an order. | |
| Release stock | `release_stock` | Frees held units. | |
| Ship an order | `ship_order` | Creates a shipment and hands the goods to a carrier. | The shipment has its own states. |
| Record a delivery | `record_shipment_delivered` | Sets the shipment to `delivered`. | The carrier webhook calls it. |
| Request a return | `request_return` | Starts a return. | |
| Approve a return | `approve_return` | The shop accepts the return. | |
| Reject a return | `reject_return` | The shop refuses the return. | |
| Receive a return | `receive_return` | Records that the goods came back. | |
| Refund a payment | `refund_payment` | Returns money. | After capture only. |
| Restock a return | `restock_return` | Adds returned units to stock. | Only for goods that can be sold again. |

## Traps

| Trap | Why it is a problem | Better |
|---|---|---|
| `order` as a column or a word | `order` is a reserved SQL word. It also means "sort". | `orders` for the table. `purchase_order` for a buyer's order to a supplier. |
| `canceled` and `cancelled` | Two spellings in one code base. | One spelling. This guide uses `canceled`. |
| `cancel`, `void`, `refund` | Three ways to stop a payment. | `void` before capture, `refund` after capture, `cancel` for the order. |
| `status` and `state` | Two words for one idea. | `status` in names, `state` in text about state machines. |
| `total` | Before or after tax, discount and shipping? | `subtotal_amount_cents`, `total_amount_cents`. |
| `price`, `amount`, `cost` | Three words for money. | `price` is what the buyer pays per unit. `amount` is a computed total on a record. `cost` is what the shop pays. |
| `product`, `variant`, `sku`, `item` | Four words for what is sold. | `product` for the concept, `variant` for the sellable unit, `sku` for its code, `order_item` for a line. |
| `customer`, `user`, `account` | Three words for a person. | `customer` buys. `user` signs in. Avoid `account` for a buyer. In Stripe, `account` is the seller. |
| `address` | Billing or shipping? | `billing_address_id`, `shipping_address_id`. |
| `shipment`, `delivery`, `fulfillment` | Three words for sending goods. | `shipment` for the group of packages, `delivered_at` for the event. `fulfillment` is the whole pick, pack and ship process. Shopify also uses it for a shipment. |
| `stock`, `inventory`, `quantity` | Three words for units. | `stock_level` for the entity, `quantity` for a count in an item. |
| `discount`, `coupon`, `promotion` | Three words for a lower price. | `coupon` has a code. `promotion` has a rule. `discount_amount_cents` is the result. |
| `paid_at` | Authorized or captured? | `authorized_at`, `captured_at`. |
| `return` as a variable | `return` is a keyword in many languages. | `return_request` or `product_return` for a variable. `Return` or `ProductReturn` for a class. `returns` for the table. |

## Worked example

The data model in SQL. The table `product_variants` is not shown.

```sql
CREATE TABLE customers (
    id          bigint GENERATED ALWAYS AS IDENTITY,
    email       text NOT NULL,
    created_at  timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT pk_customers PRIMARY KEY (id)
);

CREATE UNIQUE INDEX uq_customers_lower_email ON customers (lower(email));

CREATE TABLE orders (
    id                      bigint GENERATED ALWAYS AS IDENTITY,
    number                  text NOT NULL,
    customer_id             bigint NOT NULL,
    billing_address_id      bigint NOT NULL,
    shipping_address_id     bigint NOT NULL,
    status                  text NOT NULL DEFAULT 'pending',
    subtotal_amount_cents   bigint NOT NULL,
    tax_amount_cents        bigint NOT NULL,
    total_amount_cents      bigint NOT NULL,
    currency_code           char(3) NOT NULL,
    placed_at               timestamptz NOT NULL DEFAULT now(),
    shipped_at              timestamptz,
    canceled_at             timestamptz,
    CONSTRAINT pk_orders PRIMARY KEY (id),
    CONSTRAINT uq_orders_number UNIQUE (number),
    CONSTRAINT fk_orders_customers FOREIGN KEY (customer_id) REFERENCES customers (id),
    CONSTRAINT fk_orders_billing_address FOREIGN KEY (billing_address_id) REFERENCES addresses (id),
    CONSTRAINT fk_orders_shipping_address FOREIGN KEY (shipping_address_id) REFERENCES addresses (id),
    CONSTRAINT chk_orders_status_allowed CHECK (status IN (
        'pending', 'processing', 'on_hold', 'partially_shipped',
        'shipped', 'delivered', 'completed', 'canceled'
    )),
    CONSTRAINT chk_orders_currency_code_format CHECK (currency_code ~ '^[A-Z]{3}$'),
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
    CONSTRAINT fk_order_items_product_variants FOREIGN KEY (variant_id) REFERENCES product_variants (id),
    CONSTRAINT chk_order_items_quantity_positive CHECK (quantity > 0)
);

CREATE INDEX idx_order_items_variant_id ON order_items (variant_id);
```

Inside the `orders` table the columns are `number` and `status`, without the table name. In code, a variable or a DTO field keeps the full name: `order_number`, `order_status`.

The API paths. For the rules, see [REST](../systems/rest.md):

```
POST   /v1/carts/{cart_id}:checkout                place an order from a cart
GET    /v1/orders/{order_id}                       get one order
GET    /v1/customers/{customer_id}/orders          list the orders of a customer
POST   /v1/orders/{order_id}:cancel                cancel an order
POST   /v1/orders/{order_id}/shipments             ship an order (creates a shipment)
POST   /v1/payments/{payment_id}:capture           capture a payment
POST   /v1/payments/{payment_id}/refunds           refund a payment
```

The events, in the past tense. For the rules, see [Events](../systems/events.md):

```
OrderPlaced   PaymentAuthorized   PaymentCaptured   PaymentFailed   OrderShipped
OrderDelivered   OrderCanceled   PaymentRefunded   ReturnReceived
```

A cancel of a paid order sends `OrderCanceled`. The payment service listens to it and then sends `PaymentRefunded`, or voids the hold.

The code:

```py
from enum import Enum


class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    ON_HOLD = "on_hold"
    PARTIALLY_SHIPPED = "partially_shipped"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    COMPLETED = "completed"
    CANCELED = "canceled"


CANCELABLE_ORDER_STATUSES = {OrderStatus.PENDING, OrderStatus.PROCESSING, OrderStatus.ON_HOLD}


def place_order(cart: Cart) -> Order:
    order_items = [build_order_item(cart_item) for cart_item in cart.cart_items]
    subtotal_amount_cents = sum(order_item.unit_price_cents * order_item.quantity for order_item in order_items)
    tax_amount_cents = calculate_tax_amount_cents(order_items, cart.shipping_address)
    return Order(
        customer_id=cart.customer_id,
        order_items=order_items,
        order_status=OrderStatus.PENDING,
        subtotal_amount_cents=subtotal_amount_cents,
        tax_amount_cents=tax_amount_cents,
        total_amount_cents=subtotal_amount_cents + tax_amount_cents,
        currency_code=cart.currency_code,
        placed_at=utc_now(),
    )


def can_cancel_order(order: Order) -> bool:
    return order.order_status in CANCELABLE_ORDER_STATUSES
```

!!! info "See also"

    - [Examples overview](index.md), [Tables](../databases/tables.md), [Columns](../databases/columns.md) and [REST](../systems/rest.md)
    - [Stripe API reference](https://docs.stripe.com/api) for payment and refund words
    - [Shopify Admin API: Order](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order) for order and fulfillment words
    - [Schema.org: Order](https://schema.org/Order) for a shared vocabulary
