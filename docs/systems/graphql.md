---
status: new
---

# GraphQL

!!! success "General patterns"

    - Use `PascalCase` for type names: `Order`, `OrderStatus`, `CreateOrderInput`
    - Use `camelCase` for fields, arguments and mutation fields: `orderTotal`, `customerId`, `createOrder`
    - Use `SCREAMING_SNAKE_CASE` for enum values: `PENDING`, `SHIPPED`
    - Name a mutation with a verb first: `createOrder`, `cancelOrder`
    - Name a query field with a noun: `order`, `orders`
    - Give each mutation one input type and one payload type: `CancelOrderInput`, `CancelOrderPayload`. This is a GitHub-style convention

!!! tip "Useful tips"

    - Name a field after what it is, not after where it comes from: `customer`, not `customerFromCrm`
    - Use the same word for the same thing in every type. `id` is an opaque global identifier of an object (Relay `Node`). The `order_id` of the REST API maps to `orderId` when a field needs the plain key
    - Return the changed object in the payload, so the client needs no second call
    - Use a linter, for example `graphql-eslint` with the `naming-convention` rule

!!! danger "General anti-patterns"

    - A verb in a query: `getOrder`, `fetchOrders`
    - A type name with a noise suffix: `OrderType`, `OrderObject`
    - A mutation that returns only a boolean: `cancelOrder: Boolean`
    - Names with the version in them: `OrderV2`. Evolve the schema instead

The examples use an e-commerce shop.

## Names by kind

| Kind | Rule | Examples | Why this name |
|---|---|---|---|
| Object type | `PascalCase` noun | `Order`, `Customer`, `OrderLine` | Apollo and the public GraphQL APIs use `PascalCase`. The spec only requires a valid name. |
| Interface | `PascalCase` noun or adjective | `Node`, `Timestamped` | An interface names a shape that many types share. `Node` is the Relay interface for objects with a global id. |
| Union | `PascalCase` noun for the choice | `SearchResult`, `PaymentMethod` | The name states what the member types have in common. |
| Input type (Apollo and GitHub style) | mutation name plus `Input` | `CreateOrderInput`, `CancelOrderInput` | Ties the input to its mutation. |
| Payload type (Apollo and GitHub style) | mutation name plus `Payload` | `CreateOrderPayload`, `CancelOrderPayload` | Ties the result to its mutation. |
| Enum | singular `PascalCase` noun | `OrderStatus`, `Currency` | One value is one status. |
| Enum value | `SCREAMING_SNAKE_CASE` | `PENDING`, `PARTIALLY_SHIPPED` | The spec examples and Apollo use this style. |
| Scalar | `PascalCase` noun | `DateTime`, `Url` | A custom value type. For money, use an object: `Money { amountCents currencyCode }`. |
| Field | `camelCase` noun | `totalAmountCents`, `shippedAt` | The unit is in the name, as in the REST API and the database. |
| Boolean field | `is`, `has` plus a word | `isActive`, `hasGiftWrap` | A boolean reads as a statement. |
| Timestamp field | `<event>At` | `createdAt`, `shippedAt` | The same suffix as in the database and REST. |
| List field | plural noun | `items`, `orders` | A plural tells the client that the value is a list. |
| Argument | `camelCase` word | `first`, `after`, `status` | Arguments follow the field style. Relay fixes `first`, `after`, `last` and `before`. |
| Query, one item | singular noun | `order(id: ID!)`, `customer(id: ID!)` | One object by id. |
| Query, a list | plural noun | `orders(first: Int)`, `products` | A set of objects. |
| Query, current user (community practice) | `viewer` (GitHub, Relay) or `me` | `viewer`, `me` | An alias for the caller, so the client needs no id. |
| Mutation | verb plus noun (Shopify uses noun first: `orderCancel`) | `createOrder`, `cancelOrder`, `addOrderItem` | An action on a resource. Choose one order and keep it. |
| Subscription (community practice) | noun plus past event | `orderShipped`, `shipmentDelivered` | A stream of events. Use the event names from [Events](events.md). |
| Directive | `camelCase` | `@deprecated`, `@specifiedBy` | The spec directives use lower camel case. |
| Fragment | the type plus a purpose | `OrderSummaryFields` | A client file may hold many fragments, so the name says the type and the use. |
| Operation name (client side) | `PascalCase`; a verb is fine here | `GetOrderDetails`, `CancelOrder` | It shows in logs and tools. The no-verb rule is for query fields, not for operation names. |

## Mutations

| Pattern | Rule | Examples |
|---|---|---|
| Create | `create` plus a noun | `createOrder`, `createCustomer` |
| Update | `update` plus a noun | `updateOrder`, `updateCustomer` |
| Delete | `delete` plus a noun | `deleteAddress` |
| Action | a verb plus a noun | `cancelOrder`, `shipOrder`, `refundPayment` |
| Add or remove from a list | `add` or `remove` plus a noun | `addOrderItem`, `removeOrderItem` |
| One input | `input: <Mutation>Input!` | `createOrder(input: CreateOrderInput!)` |
| Payload | the changed object plus errors for the user (Shopify uses `userErrors`) | `{ order { id } userErrors { field message } }` |

## Relay connections

The Relay specification defines paged lists. Its names are part of the contract.

| Name | Meaning | Examples |
|---|---|---|
| `<Type>Connection` | The paged list. | `OrderConnection` |
| `<Type>Edge` | One item and its cursor. | `OrderEdge` |
| `edges` | The list of edges. | `orders { edges { node { id } } }` |
| `node` | The item in an edge. | `edge.node` |
| `cursor` | The position of an edge. | `edge.cursor` |
| `pageInfo` | The paging data. | `PageInfo` |
| `hasNextPage`, `hasPreviousPage` | Whether more items exist. | `pageInfo.hasNextPage` |
| `startCursor`, `endCursor` | The first and last cursor. | `pageInfo.endCursor` |
| `first`, `after` | Forward paging arguments. | `orders(first: 10, after: "abc")` |
| `last`, `before` | Backward paging arguments. | `orders(last: 10, before: "abc")` |
| `totalCount` | A common extra field. It is not part of the Relay specification. | `orders { totalCount }` |

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `getOrder` | `order` | A query is a noun. |
| `OrderType` | `Order` | The word `Type` repeats what the schema says. |
| `order_total` | `orderTotal` | Fields use `camelCase`. |
| `pending` as enum value | `PENDING` | Enum values use capitals. |
| `cancelOrder(id: ID!): Boolean` | `cancelOrder(input: CancelOrderInput!): CancelOrderPayload!` | The client gets the changed order. |
| `OrderInput` for create and update | `CreateOrderInput`, `UpdateOrderInput` | The inputs differ. |
| `orderList` | `orders` | A plural noun is enough. |
| `isNotActive` | `isActive` | A positive name. |
| `createdTime` | `createdAt` | The same suffix as the other APIs. |

!!! info "See also"

    - [Systems overview](index.md), [REST](rest.md) and [Events](events.md)
    - [GraphQL specification](https://spec.graphql.org/), [Relay connections](https://relay.dev/graphql/connections.htm), [Apollo naming conventions](https://www.apollographql.com/docs/graphos/schema-design/guides/naming-conventions)
