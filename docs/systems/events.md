---
status: new
---

# Events

!!! success "General patterns"

    - Name an event for a fact that already happened, in the past tense: `OrderPlaced`, `PaymentCaptured`
    - Name a command for a request in the imperative: `PlaceOrder`, `CapturePayment`
    - Name a topic for the stream of one kind of event, in lower case with a clear scope: `shop.orders.v1`
    - Use the same field names in an event as in the REST API and the database: `order_id`, `customer_id`
    - Put the metadata in an envelope and the data of the fact in the payload

!!! tip "Useful tips"

    - Name an event for what the business sees, not for a row change: `OrderShipped`, not `OrderRowUpdated`
    - Add a version to the event type or the topic, so consumers can handle two versions at once
    - Use a timestamp in RFC 3339 form, in UTC. In the CloudEvents envelope the attribute is `time`. In a payload, a field such as `occurred_at` is fine
    - Use CloudEvents attribute names when the platform supports them

!!! danger "General anti-patterns"

    - A name that says how the data changed instead of what happened: `OrderUpdated`, `OrderChanged`
    - One name for a command and an event: `OrderPlaced` for both a request and a fact
    - A topic that names the consumer: `billing-service-input`
    - A payload that has the whole database row

The examples use an e-commerce shop.

## Events and commands

| Kind | Tense | Examples | Why this name |
|---|---|---|---|
| Event | past | `OrderPlaced`, `OrderShipped`, `PaymentCaptured` | A fact cannot be refused. |
| Command | imperative | `PlaceOrder`, `ShipOrder`, `CapturePayment` | A request can be refused. |
| Query | a question | `WhatIsOrderStatus` | Asks for data. Most systems use a request-response API for this, not a message. |
| Failure event | past, with the failure | `PaymentFailed`, `OrderRejected` | The fact is that it failed. |
| Compensation event | past | `PaymentRefunded`, `OrderCanceled` | The undo step is also a fact. |
| Deadline event | past | `OrderExpired`, `PaymentTimedOut` | Time passed. |

## Event type names

| Pattern | Examples | Notes |
|---|---|---|
| `<Aggregate><PastVerb>` | `OrderPlaced`, `CustomerRegistered`, `InvoiceIssued` | A common form in domain-driven design (community practice). |
| Reverse domain | `com.shop.order.placed` | CloudEvents recommends a reverse-DNS prefix for `type`. |
| With a version | `com.shop.order.placed.v1`, `OrderPlacedV1` | A version in the name or in the schema. |
| Dotted lower case | `order.placed`, `payment.captured` | Used by webhooks, for example `invoice.paid`. |
| Domain scope | `shipping.parcel.dispatched` | Adds the bounded context. |

Conflict: some platforms use `PascalCase` names (`OrderPlaced`). Others use dotted lower case (`order.placed`). Choose one and use it in the whole company.

## Topic and queue names

Kafka and other brokers set no naming rules beyond the allowed characters. The patterns below are community practice. In Kafka, a topic name can mix `.` and `_`, but the two collide in metric names, so use one of them.

| Kind | Pattern | Examples | Why this name |
|---|---|---|---|
| Topic | `<domain>.<entity>.<version>` | `shop.orders.v1`, `shop.payments.v1` | The scope and the version are in the name. |
| Topic, by event | `<domain>.<entity>.<event>` | `shop.orders.placed` | One topic for one event type. |
| Dead-letter topic (community practice) | the topic plus `.dlq` | `shop.orders.v1.dlq` | Where failed messages go. |
| Retry topic (community practice) | the topic plus `.retry` | `shop.orders.v1.retry` | Where messages wait for a new try. |
| Queue | `<consumer>.<source>` | `billing.orders-placed` | A queue belongs to its consumer. |
| Consumer group | the service name | `billing-service` | Names the reader. |
| Environment | prefix or the cluster, not both | `prod.shop.orders.v1` | Do not repeat it in both places. |

## Envelope fields

CloudEvents defines the names of the envelope. The table shows the required and common attributes.

| Field | Meaning | Examples | Why this name |
|---|---|---|---|
| `id` | An id that is unique within the `source`. | `evt_01HZ...` | Needed for de-duplication. |
| `source` | Where the event came from. | `/shop/orders` | A context for `id`. |
| `specversion` | The CloudEvents version. | `1.0` | Required by the standard. |
| `type` | The kind of event. | `com.shop.order.placed` | Consumers route by type. |
| `time` | When the event occurred (RFC 3339). | `2026-11-07T10:15:00Z` | A timestamp. Use UTC by habit. RFC 3339 also allows an offset. |
| `subject` | The thing that the event is about. | `orders/12345` | Narrows the source. |
| `datacontenttype` | The format of the data. | `application/json` | Tells how to read `data`. |
| `dataschema` | A link to the schema of the data. | `https://schemas.shop/order-placed/v1` | Helps validation. |
| `data` | The payload. | `{ "order_id": "12345" }` | The data of the fact. |
| `correlationid` | Links events of one flow. | `req_7d9a...` | A common extension (community practice). For tracing, the `traceparent` extension is the standard way. |
| `causationid` | The id of the cause. | `evt_01HY...` | A common extension (community practice). |

The names of all CloudEvents attributes, including extensions, use only lower-case letters and digits, with no underscore. They should be at most 20 characters. The required attributes are `id`, `source`, `specversion` and `type`. The others are optional.

## Payload fields

| Kind | Rule | Examples |
|---|---|---|
| Identifier | `<entity>_id` | `order_id`, `customer_id` |
| Timestamp | `<event>_at` | `placed_at`, `shipped_at` |
| Money | an integer in minor units plus a currency code | `total_amount_cents`, `currency_code` |
| Status | the new state, not the old | `status: "shipped"` |
| Previous value | `previous_<field>` | `previous_status` |
| Items | plural noun | `items` |

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `OrderUpdated` | `OrderShipped` | The name tells what happened. |
| `PlaceOrderEvent` | `OrderPlaced` | An event is a past fact; drop the type word. |
| `order_place` | `PlaceOrder` | A command is a verb phrase in the imperative. |
| `topic1` | `shop.orders.v1` | The scope and the version are in the name. |
| `billing-input` | `shop.orders.v1` | A topic is named for the data, not for the reader. |
| `ts` | `time` in the envelope; `occurred_at` in a payload | A full word, as in CloudEvents. |
| `OrderCreatedV2` and `OrderCreated` in one topic | `OrderCreated` with a versioned `dataschema`, or a new topic `shop.orders.v2` | Version the schema or the topic, not the event name. |
| `OrderPaid` for a failed payment | `PaymentFailed` | Say what really happened. |

!!! info "See also"

    - [Systems overview](index.md), [REST](rest.md) and [GraphQL](graphql.md)
    - [CloudEvents specification](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md), [AsyncAPI](https://www.asyncapi.com/docs)
