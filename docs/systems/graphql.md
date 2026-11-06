---
status: new
---

# GraphQL

!!! success "General patterns"

    - Use `PascalCase` for type names: `Order`, `OrderStatus`, `CreateOrderInput`
    - Use `camelCase` for fields, arguments and operation names: `orderTotal`, `customerId`, `createOrder`
    - Use `SCREAMING_SNAKE_CASE` for enum values: `PENDING`, `SHIPPED`
    - Name a mutation with a verb first: `createOrder`, `cancelOrder`
    - Name a query with a noun: `order`, `orders`, `viewer`
    - Give each mutation one input type and one payload type: `CancelOrderInput`, `CancelOrderPayload`

!!! tip "Useful tips"

    - Name a field after what it is, not after where it comes from: `customer`, not `customerFromCrm`
    - Use the same word for the same thing in every type. `id` is the global identifier of an object
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
| Interface | `PascalCase` noun or adjective | `Node`, `Timestamped` | Names a shared shape. |
| Union | `PascalCase` noun for the choice | `SearchResult`, `PaymentMethod` | Names the group of types. |
| Input type (Apollo and GitHub style) | mutation name plus `Input` | `CreateOrderInput`, `CancelOrderInput` | Ties the input to its mutation. |
| Payload type (Apollo and GitHub style) | mutation name plus `Payload` | `CreateOrderPayload`, `CancelOrderPayload` | Ties the result to its mutation. |
| Enum | singular `PascalCase` noun | `OrderStatus`, `Currency` | One value is one status. |
| Enum value | `SCREAMING_SNAKE_CASE` | `PENDING`, `PARTIALLY_SHIPPED` | The spec examples and Apollo use this style. |
| Scalar | `PascalCase` noun | `DateTime`, `Money`, `Url` | A custom value type. |
| Field | `camelCase` noun | `totalAmount`, `shippedAt` | Fields are properties. |
| Boolean field | `is`, `has` plus a word | `isActive`, `hasGiftWrap` | A boolean reads as a statement. |
| Timestamp field | `<event>At` | `createdAt`, `shippedAt` | The same suffix as in the database and REST. |
| List field | plural noun | `items`, `orders` | A plural shows a list. |
| Argument | `camelCase` noun | `first`, `after`, `status` | The spec examples use short nouns. |
| Query, one item | singular noun | `order(id: ID!)`, `customer(id: ID!)` | One object by id. |
| Query, a list | plural noun | `orders(first: Int)`, `products` | A set of objects. |
| Query, current user | `viewer` or `me` | `viewer`, `me` | A common alias. |
| Mutation | verb plus noun | `createOrder`, `cancelOrder`, `addOrderItem` | An action on a resource. |
| Subscription (community practice) | noun plus past event | `orderUpdated`, `shipmentDelivered` | An event stream. |
| Directive | `camelCase` | `@deprecated`, `@auth` | The spec uses lower camel case. |
| Fragment | the type plus a purpose | `OrderSummaryFields` | Clear in a client file. |
| Operation name | verb or noun, `PascalCase` | `GetOrderDetails`, `CancelOrder` | Shows in logs and tools. |

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
