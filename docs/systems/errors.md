---
status: new
---

# Errors

!!! success "General patterns"

    - Give each error a stable code that a program can read: `ORDER_NOT_FOUND`, `CARD_DECLINED`
    - Write the code in `SCREAMING_SNAKE_CASE` (AIP-193 asks for this in `reason`) or in `lower_snake_case` (Stripe uses `card_declined`). Use one style in the whole API
    - Name the thing and the problem: `<RESOURCE>_<PROBLEM>`
    - Keep a code the same for ever. Change the message, not the code
    - Write the message for a person and the code for a program

!!! tip "Useful tips"

    - Use the HTTP status for the class of the error and the code for the exact reason: `404` with `ORDER_NOT_FOUND`
    - Name an exception class after the problem, with the suffix `Error` or `Exception`, as the language asks: `OrderNotFoundError`
    - Put the code, the message and the field in a fixed shape (see RFC 9457)
    - Keep a list of all codes in one file and in the documentation

!!! danger "General anti-patterns"

    - A numeric code without a name: `E1042`
    - A code that is a sentence: `THE_ORDER_WAS_NOT_FOUND_IN_DB`
    - A code that leaks the implementation: `NULL_POINTER`, `SQL_ERROR`
    - One generic code for everything: `ERROR`, `FAILED`
    - A message that a program has to parse

The examples use an e-commerce shop. The name patterns below are community practice, except where the text names a standard. For field names inside the error body, see [REST](rest.md).

## Error code names

| Kind | Pattern | Examples | Why this name |
|---|---|---|---|
| Not found | `<RESOURCE>_NOT_FOUND` | `ORDER_NOT_FOUND`, `CUSTOMER_NOT_FOUND` | The resource and the problem. |
| Already exists | `<RESOURCE>_ALREADY_EXISTS` | `COUPON_ALREADY_EXISTS` | Same pattern. |
| Invalid value | `INVALID_<FIELD>` | `INVALID_EMAIL`, `INVALID_QUANTITY` | The field is in the name. |
| Missing value | `MISSING_<FIELD>` | `MISSING_CURRENCY_CODE` | Different from invalid. |
| State conflict | `<RESOURCE>_<STATE>` | `ORDER_ALREADY_SHIPPED`, `ORDER_NOT_CANCELLABLE` | The state that blocks the action. |
| Permission | `PERMISSION_DENIED`, `UNAUTHENTICATED` | `PERMISSION_DENIED` | The gRPC names are well known. |
| Limit | `<THING>_LIMIT_EXCEEDED` | `RATE_LIMIT_EXCEEDED`, `CART_ITEM_LIMIT_EXCEEDED` | The limit and the fact. |
| Payment | `PAYMENT_<REASON>` | `PAYMENT_DECLINED`, `PAYMENT_EXPIRED_CARD` | Groups related codes. |
| Dependency | `<SERVICE>_UNAVAILABLE` | `PAYMENT_GATEWAY_UNAVAILABLE` | Says which service failed. |
| Precondition | `FAILED_PRECONDITION` (gRPC and AIP-193) | `FAILED_PRECONDITION` | The system is not in a state for this call. |
| Internal | `INTERNAL` (gRPC) | `INTERNAL` | A bug in the server. The client cannot fix it. |

## HTTP status and code

| HTTP status | gRPC code | Example code | Meaning |
|---|---|---|---|
| `400` | `INVALID_ARGUMENT` | `INVALID_EMAIL` | The request is wrong. |
| `401` | `UNAUTHENTICATED` | `TOKEN_EXPIRED` | The caller is not known. |
| `403` | `PERMISSION_DENIED` | `ORDER_ACCESS_DENIED` | The caller is known and not allowed. |
| `404` | `NOT_FOUND` | `ORDER_NOT_FOUND` | The resource does not exist. |
| `409` | `ALREADY_EXISTS`, `ABORTED` | `COUPON_ALREADY_EXISTS` | A conflict with the state. |
| `422` | no standard mapping | `QUANTITY_OUT_OF_RANGE` | The request is well formed but not valid. Many APIs use `400` instead. |
| `429` | `RESOURCE_EXHAUSTED` | `RATE_LIMIT_EXCEEDED` | Too many requests. |
| `500` | `INTERNAL` | `INTERNAL` | A server bug. |
| `503` | `UNAVAILABLE` | `PAYMENT_GATEWAY_UNAVAILABLE` | A temporary failure. |

## Problem details (RFC 9457)

RFC 9457 (which replaces RFC 7807) defines a JSON body for an HTTP error with standard member names.

| Member | Meaning | Example |
|---|---|---|
| `type` | A URI that names the kind of problem. | `https://api.shop.example/problems/order-not-found` |
| `title` | A short summary that does not change. | `Order not found` |
| `status` | The HTTP status. | `404` |
| `detail` | An explanation for this case. | `Order 12345 does not exist.` |
| `instance` | A URI for this case. | `/v1/orders/12345` |
| `code` | An extension: the stable code. | `ORDER_NOT_FOUND` |
| `errors` | An extension: a list of field problems. | `[{ "field": "email", "code": "INVALID_EMAIL" }]` |

The media type is `application/problem+json`.

## Exception names

| Language | Pattern | Examples | Notes |
|---|---|---|---|
| Python | `<Problem>Error` | `OrderNotFoundError`, `InvalidCouponError` | PEP 8: use the suffix `Error` for an error. |
| Java | `<Problem>Exception` | `OrderNotFoundException` | The Java suffix. |
| C# | `<Problem>Exception` | `OrderNotFoundException` | The .NET guidelines require the suffix. |
| JavaScript, TypeScript | `<Problem>Error` | `OrderNotFoundError` | `Error` is the base class. |
| Go | `Err<Problem>`, `<Problem>Error` | `ErrNotFound`, `NotFoundError` | A value or a type. |
| Rust | `<Problem>Error` and variants | `OrderError::NotFound` | The type says `Error`. |

For the language rules, see the [Languages overview](../languages/index.md).

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `E1042` | `ORDER_NOT_FOUND` | A name is readable. |
| `error` | `INVALID_EMAIL` | A generic word says nothing. |
| `NULL_POINTER` | `INTERNAL` | Do not leak the implementation. |
| `ORDER_NOT_FOUND_IN_DATABASE` | `ORDER_NOT_FOUND` | The caller does not need to know about the database. |
| `Order not found` as a code | `ORDER_NOT_FOUND` | A code is not a sentence. |
| `404` only | `404` plus `ORDER_NOT_FOUND` | The status gives the class. The code gives the reason. |
| `orderError` | `OrderNotFoundError` | The class names the problem. |
| `Failure` | `PaymentDeclinedError` | Say what failed. |

!!! info "See also"

    - [Systems overview](index.md), [REST](rest.md) and [Configuration](configuration.md)
    - [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457), [Google AIP-193: errors](https://google.aip.dev/193), [gRPC status codes](https://grpc.github.io/grpc/core/md_doc_statuscodes.html)
