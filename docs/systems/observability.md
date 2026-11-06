---
status: new
---

# Observability

!!! success "General patterns"

    - Name a metric for what it measures, with its unit as a suffix: `http_request_duration_seconds`
    - Use base units: seconds, bytes, ratios from 0 to 1. Do not use milliseconds or percent in the name of a metric
    - End a counter with `_total`: `orders_placed_total`
    - Use `snake_case` for metric names and label names (Prometheus). Use dotted lower case for OpenTelemetry names: `http.server.request.duration`
    - Keep the number of label values small. Never use a user id or a request id as a label

!!! tip "Useful tips"

    - Put the name of the thing first and the unit last: `memory_usage_bytes`, `payment_amount_cents_total`. A value with no unit has no unit suffix: `queue_depth`
    - Use the same label name for the same thing in every metric: `status_code`, not `code` in one and `status` in another
    - Name a span for the operation, not the data: `GET /v1/orders/{order_id}`, not `GET /v1/orders/12345`
    - Write log fields in one style and use the same names as in the API: `order_id`, `customer_id`

!!! danger "General anti-patterns"

    - A unit that is not a base unit: `request_duration_ms`, `memory_mb`
    - A counter without `_total`: `orders_placed`
    - A high-cardinality label: `user_id`, `email`, `request_id`, a raw URL
    - A name with the service in it: `shop_orders_service_requests` (use a label for the service)
    - A name with a type or a statistic in it: `request_duration_histogram`, `avg_latency`

The examples use an e-commerce shop. The metric rules come from the Prometheus naming guide and the OpenTelemetry semantic conventions. The label choices and the log field names are community practice.

## Metric names (Prometheus)

| Kind | Pattern | Examples | Why this name |
|---|---|---|---|
| Counter | `<thing>_<event>_total` | `http_requests_total`, `orders_placed_total` | A counter only goes up, and `_total` says so. |
| Counter with a unit | `<thing>_<unit>_total` | `payment_amount_cents_total`, `sent_bytes_total` | The unit is before `_total`. |
| Gauge | `<thing>_<unit>` | `queue_depth`, `memory_usage_bytes` | A value that goes up and down. A value with no unit has no suffix. |
| Info metric | `<thing>_info` | `build_info` | Prometheus practice: a constant 1 with the data in labels. |
| Gauge for a state (community practice) | `<thing>_state` | `circuit_breaker_state` | A state with labels. |
| Histogram | `<thing>_<unit>` | `http_request_duration_seconds`, `response_size_bytes` | The buckets use the base unit. |
| Ratio | `<thing>_ratio` | `cache_hit_ratio` | A value from 0 to 1. |
| Timestamp | `<thing>_timestamp_seconds` | `last_success_timestamp_seconds` | Unix time in seconds. |
| Process metric | `process_<thing>` | `process_cpu_seconds_total` | The client library names. |
| Application prefix | `<app>_<thing>` | `shop_orders_placed_total` | One prefix for the whole application. |

## Labels

| Label | Meaning | Examples | Why this name |
|---|---|---|---|
| `method` | The HTTP method. | `GET`, `POST` | A small set. |
| `route` | The route template, not the path. | `/v1/orders/{order_id}` | Few values. |
| `status_code` | The HTTP status. | `200`, `404` | A small set. |
| `service` | The service that sent the data. | `orders`, `payments` | Better than a prefix. |
| `env` | The environment. | `prod`, `staging` | Set by the platform. |
| `result` | The outcome. | `success`, `error` | A small set. |
| `error_code` | A stable error code. | `PAYMENT_DECLINED` | See [Errors](errors.md). |

Do not use as a label: `user_id`, `email`, `order_id`, `request_id`, a full URL, a free-text message.

## OpenTelemetry names

| Kind | Pattern | Examples | Why this name |
|---|---|---|---|
| Metric | dotted lower case, a namespace first | `http.server.request.duration`, `db.client.operation.duration` | The semantic conventions use dotted names. |
| Metric unit | in the metadata, not the name | unit `s`, unit `By` | The name has no unit suffix. |
| Attribute | dotted lower case, a namespace first | `http.request.method`, `http.response.status_code`, `db.system.name` | A shared vocabulary. |
| Custom attribute | your domain as a namespace | `shop.order.id`, `shop.customer.tier` | Avoids a clash with the standard names. |
| Span name | the operation, low cardinality | `GET /v1/orders/{order_id}`, `SELECT orders` | Few distinct names. |
| Resource attribute | `service.name`, `service.version` | `service.name=shop-orders` | Names the source of the data. |

Conflict: Prometheus writes `http_request_duration_seconds`. OpenTelemetry writes `http.server.request.duration` with the unit in the metadata. When OpenTelemetry data goes to Prometheus, the dots become underscores and the unit becomes a suffix: `http_server_request_duration_seconds`.

## Log fields

| Field | Meaning | Examples | Why this name |
|---|---|---|---|
| `timestamp` | When the log line was made. | `2026-11-07T10:15:00Z` | A standard name. |
| `level` | The severity. | `info`, `error` | A small set. |
| `message` | The text for a person. | `Order placed` | A constant text. |
| `logger` | The name of the source. | `shop.orders.service` | The module or class. |
| `trace_id`, `span_id` | Links a log to a trace. | `4bf92f35...` | The OpenTelemetry names. |
| `order_id`, `customer_id` | Ids of the domain. | `order_id=12345` | The same names as in the API. |
| `error_code` | A stable error code. | `ORDER_NOT_FOUND` | See [Errors](errors.md). |
| `duration_ms` or `duration_seconds` | The time taken. | `duration_ms=120` | A unit in the name. |

Log levels: `trace`, `debug`, `info`, `warn`, `error`, `fatal`. Use the levels of your library and write them in lower case.

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `request_duration_ms` | `http_request_duration_seconds` | A base unit. |
| `orders_placed` | `orders_placed_total` | A counter ends with `_total`. |
| `avg_latency` | `http_request_duration_seconds` (a histogram) | Compute the average in the query. |
| `request_duration_histogram` | `http_request_duration_seconds` | Do not put the type in the name. |
| `shop_orders_service_requests` | `http_requests_total{service="orders"}` | The service is a label. |
| `user_id` as a label | a log field or a span attribute | Too many values. |
| span `GET /v1/orders/12345` | `GET /v1/orders/{order_id}` | A low-cardinality name. |
| `memory_mb` | `memory_usage_bytes` | A base unit. |

!!! info "See also"

    - [Systems overview](index.md), [Feature flags](feature-flags.md) and [Errors](errors.md)
    - [Prometheus: metric and label naming](https://prometheus.io/docs/practices/naming/), [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/), [OpenTelemetry: metric naming](https://opentelemetry.io/docs/specs/semconv/general/naming/)
