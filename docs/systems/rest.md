---
status: new
---

# REST

!!! success "General patterns"

    - Name a resource with a plural noun: `/v1/orders`, `/v1/customers`
    - Put the id of one resource after the collection: `/v1/orders/{order_id}`
    - Use the HTTP method as the verb. Do not put a verb in the path for a standard action
    - Name a custom action with a verb after a colon: `POST /v1/orders/{order_id}:cancel`
    - Use one case style for all JSON fields and query parameters
    - Put the version first in the path: `/v1/`

!!! tip "Useful tips"

    - Keep the path nesting to two levels: `/v1/customers/{customer_id}/orders`. For a deeper link, use a query filter
    - Use the same word in the path, in the field and in the database: `customer_id`
    - Name a request and a response type from the method and the resource: `ListOrdersRequest`, `ListOrdersResponse`
    - Follow the Google API Improvement Proposals (AIP) when you have no style guide of your own

!!! danger "General anti-patterns"

    - A verb in the path for a standard action: `/getOrders`, `/createOrder`
    - A singular collection: `/v1/order`
    - A file extension in the path: `/v1/orders.json`
    - `snake_case` in one response and `camelCase` in another
    - A name from the database that leaks in the API: `tbl_orders`, `order_fk`

The examples use an e-commerce shop. Where this guide differs from the AIPs, the text says so. For names inside a database, see [Databases](../databases/index.md).

## Resource paths

| Rule | Examples | Why this name |
|---|---|---|
| Collection: plural noun | `/v1/orders`, `/v1/products` | The path names a set. |
| Item: collection plus id | `/v1/orders/{order_id}` | The id picks one member. |
| Nested collection | `/v1/customers/{customer_id}/orders` | Orders that belong to one customer. |
| Nested item | `/v1/customers/{customer_id}/orders/{order_id}` | A third level makes the path long, so use a filter instead. |
| Singleton | `/v1/customers/{customer_id}/profile` | One profile for each customer. |
| Multi-word segment | `/v1/shipping-addresses` or `/v1/shippingAddresses` | See the conflict below. |
| Path variable | `{order_id}` (house style) | The resource name and `id` say what the value is. AIP-122 writes `{order}`. |
| Collection name, not a verb | `/v1/payments` | Not `/v1/makePayment`. |

Conflict: AIP-122 asks for `lowerCamelCase` collection ids (`shippingAddresses`). The Microsoft REST guidelines allow `kebab-case` (`shipping-addresses`) or `camelCase`. Choose one and do not mix them.

## Standard methods

AIP-131 to AIP-135 define five standard methods. The table shows how they map to HTTP.

| Method | HTTP | Path | Request type | Response type |
|---|---|---|---|---|
| Get | `GET` | `/v1/orders/{order_id}` | `GetOrderRequest` | `Order` |
| List | `GET` | `/v1/orders` | `ListOrdersRequest` | `ListOrdersResponse` |
| Create | `POST` | `/v1/orders` | `CreateOrderRequest` | `Order` |
| Update | `PATCH` | `/v1/orders/{order_id}` | `UpdateOrderRequest` | `Order` |
| Delete | `DELETE` | `/v1/orders/{order_id}` | `DeleteOrderRequest` | empty |

The response of a list method holds the items in a plural field and a token for the next page: `orders`, `next_page_token`.

## Custom methods

AIP-136 names a custom method with a colon and a verb after the resource.

| Endpoint | Meaning | Why this name |
|---|---|---|
| `POST /v1/orders/{order_id}:cancel` | Cancel one order. | A verb for an action that is not a standard method. |
| `POST /v1/orders/{order_id}:ship` | Mark an order as shipped. | A verb after a colon, as in `:cancel`. |
| `POST /v1/orders/{order_id}:refund` | Refund an order. | A verb after a colon, as in `:cancel`. |
| `GET /v1/orders:batchGet` | Get many orders in one call (AIP-231). | A verb on the collection. |
| `POST /v1/products:search` | Search with a body that is too big for a query. | `search` is a verb on the collection. |
| `POST /v1/customers/{customer_id}:merge` | Merge two customers. | A verb after a colon, as in `:cancel`. |
| `POST /v1/orders/{order_id}/cancellation` | The same as `:cancel`, written as a sub-resource (community practice). | An alternative style when the action has its own state. |

Conflict: some APIs avoid the colon form and use a sub-resource such as `/cancellation`. Choose one form for the API.

## More endpoint examples

| Endpoint | Meaning |
|---|---|
| `GET /v1/products` | List products. |
| `GET /v1/products/{product_id}` | Get one product. |
| `GET /v1/products/{product_id}/reviews` | List the reviews of a product. |
| `POST /v1/products/{product_id}/reviews` | Create a review. |
| `GET /v1/customers` | List customers. |
| `GET /v1/customers/{customer_id}/addresses` | List the addresses of a customer. |
| `PATCH /v1/customers/{customer_id}` | Change some fields of a customer. |
| `DELETE /v1/customers/{customer_id}/addresses/{address_id}` | Delete one address. |
| `GET /v1/orders/{order_id}/items` | List the items of an order. |
| `POST /v1/orders/{order_id}/items` | Add an item. |
| `GET /v1/orders/{order_id}/payments` | List the payments of an order. |
| `GET /v1/carts/{cart_id}` | Get a cart. |
| `POST /v1/carts/{cart_id}:checkout` | Start the checkout of a cart. |
| `GET /v1/coupons/{coupon_id}` | Get a coupon. |
| `POST /v1/coupons/{coupon_id}:redeem` | Redeem a coupon. |
| `GET /v1/shipments/{shipment_id}/tracking-events` | List the tracking events. |
| `GET /v1/me` | Get the current user. A common alias. |
| `GET /v1/health` | A health check for a load balancer. |
| `GET /v1/orders/{order_id}/invoice` | The invoice of an order (a singleton). |
| `PATCH /v1/customers/{customer_id}/preferences` | Update a singleton (AIP-156 allows Get and Update). |

## Query parameters

| Purpose | Parameter | Examples | Why this name |
|---|---|---|---|
| Filter by value | the field name | `?status=pending`, `?customer_id=42` | The same name as the field, so no new word to learn. |
| Filter by range (community practice) | `<field>_after`, `<field>_before` | `?created_after=2026-11-01`, `?created_before=2026-12-01` | The field name says which date the bound is for. |
| Filter expression | `filter` | `?filter=status = "pending" AND total_amount_cents > 10000` | AIP-160 defines a filter language. Microsoft guidelines use `$filter`. |
| Sort | `order_by` | `?order_by=created_at desc` | AIP-132 uses `order_by` with a direction. |
| Sort, short form | `sort` | `?sort=-created_at` | JSON:API uses a leading minus. |
| Fields to return | `read_mask` (AIP-157); `fields` is community practice | `?read_mask=id,status,total_amount_cents` | The caller asks only for the fields it needs. JSON:API writes `fields[type]`. |
| Include a related resource | `include` or `expand` | `?include=items`, `?expand[]=customer` | JSON:API uses `include`. Stripe uses `expand[]`. Microsoft guidelines use `$expand`. |
| Search text (community practice) | `q` or `query` | `?q=blue+shirt` | A short name that many search APIs use. |
| Show deleted items | `show_deleted` | `?show_deleted=true` | AIP-135 uses this name. |
| Validate only | `validate_only` | `?validate_only=true` | AIP-163: a request that checks a change and does not apply it. |

## Pagination

AIP-158 defines token pagination. Other APIs use limit and offset or a page number. Choose one style for the whole API.

| Style | Request | Response | Examples |
|---|---|---|---|
| Token (AIP-158) | `page_size`, `page_token` | `next_page_token` | `?page_size=50&page_token=ey...` |
| Cursor (community practice; Stripe: `starting_after`, `has_more`) | `limit`, `cursor` or `after` | `next_cursor` | `?limit=50&after=ord_123` |
| Offset | `limit`, `offset` | `total_count` | `?limit=50&offset=100` |
| Page number | `page`, `per_page` | `page`, `total_pages` | `?page=3&per_page=50` |

| Case | Rule | Example |
|---|---|---|
| Last page | An empty `next_page_token` | `"next_page_token": ""` |
| `page_size` of 0 or missing | Use a default | `page_size` omitted returns the default (for example 50) |
| `page_size` above the maximum | Reduce it to the maximum | With a maximum of 100, `page_size=10000` returns 100 items |
| `page_size` below zero | Return `400` | `page_size=-1` returns `INVALID_ARGUMENT` |
| `offset` past the end (common practice) | Return `200` with an empty list | `offset=9999` returns `"orders": []` |
| Bad `page_token` | Return `400` | `page_token=abc` returns `INVALID_ARGUMENT` |
| Token from another query | Should return `400` (AIP-158) | A token is valid for the same filter and sort only |

## Request and response types

| Kind | Pattern | Examples |
|---|---|---|
| Get | `Get<Resource>Request` | `GetOrderRequest` |
| List | `List<Resources>Request`, `List<Resources>Response` | `ListOrdersRequest`, `ListOrdersResponse` |
| Create | `Create<Resource>Request` | `CreateOrderRequest` |
| Update | `Update<Resource>Request` | `UpdateOrderRequest` |
| Delete | `Delete<Resource>Request` | `DeleteOrderRequest` |
| Custom | `<Verb><Resource>Request` | `CancelOrderRequest`, `RefundOrderRequest` |
| Batch | `BatchGet<Resources>Request` | `BatchGetOrdersRequest` |
| Field of a list response | the plural resource name | `orders`, `products` |

## Fields and headers

| Kind | Rule | Examples |
|---|---|---|
| JSON field | one style: `snake_case` or `camelCase` | `next_page_token` or `nextPageToken` |
| Identifier | `<resource>_id` | `customer_id`, `order_id` |
| Timestamp | `<event>_at`, in UTC and RFC 3339 (AIP-142 uses `create_time`) | `created_at`, `shipped_at` |
| Money | an integer in minor units plus a currency code | `total_amount_cents`, `currency_code` |
| Boolean (AIP-140 omits the `is_` prefix) | `is_` or `has_` plus a word in this guide | `is_active` |
| Request id | `X-Request-Id` (a legacy form that is still common) | `X-Request-Id: 7d9a...` |
| Idempotency | `Idempotency-Key` (Stripe, and an IETF draft) | `Idempotency-Key: 9c1f...` |
| Concurrency | `ETag`, `If-Match` | `If-Match: "v3"` |
| Custom header | a clear name; avoid `X-` for new ones (RFC 6648) | `Request-Id`, `Deprecation` |

Conflict: the JSON style guide of Google uses `camelCase`. The AIP rules use `snake_case` in the protocol definition and `camelCase` in the JSON form. Many public APIs use `snake_case`. The choice matters less than the rule that all fields use the same one.

## Versioning

| Style | Example | Notes |
|---|---|---|
| Path | `/v1/orders`, `/v2/orders` | AIP-185 puts the major version in the path. Easy to see in logs. |
| Header | `Stripe-Version: 2024-06-20` | Stripe uses date-based versions in a header. Azure uses an `api-version` query parameter. |
| Media type | `Accept: application/vnd.shop.v2+json` | Hard to try in a browser. |
| Package | `shop.orders.v1` | Used in Protobuf and gRPC. |

!!! info "See also"

    - [Systems overview](index.md) and [Naming patterns](../patterns/index.md)
    - [Google AIP-122](https://google.aip.dev/122) for resource names, [AIP-131 to AIP-135](https://google.aip.dev/131) for standard methods, [AIP-136](https://google.aip.dev/136) for custom methods, [AIP-158](https://google.aip.dev/158) for pagination, [AIP-160](https://google.aip.dev/160) for filtering
    - [Microsoft REST API guidelines](https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md) and [JSON:API](https://jsonapi.org/format/)
