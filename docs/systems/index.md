---
status: new
---

# Systems

!!! success "General patterns"

    - Name what crosses a system border with care. A name in an API, an event or a command line is a contract. Callers depend on it
    - Use one style inside one interface. Do not mix `snake_case` and `camelCase` in one API
    - Use the same word for the same thing in every interface: `customer_id` in the REST path, in the event and in the database
    - Follow the standard of the interface when one exists: AIP for HTTP APIs, CloudEvents for events, OpenTelemetry for telemetry, POSIX and GNU for command lines

!!! tip "Useful tips"

    - A rename in a language is a refactor. A rename in an API is a breaking change. Choose the name before the first release
    - Write the naming rules of the interface in its style guide, and check them with a linter (for example `buf lint` or `spectral`)
    - Keep a glossary of domain words. The [references and glossary](../common/references-and-glossary.md) page is a start

!!! danger "General anti-patterns"

    - Names that leak the implementation: `/getOrderFromDb`, `OrderEntity`
    - Names that change by endpoint: `userId` in one response and `user_id` in another
    - A verb in a resource path when a standard method fits: `/v1/createOrder`

## Pages

| Interface | Page |
|---|---|
| HTTP APIs (REST) | [REST](rest.md) |

## Where the names meet

| Border | Typical names | See |
|---|---|---|
| Code to database | `snake_case` columns, plural tables | [Databases](../databases/index.md) |
| Code to API | resource paths, field names, parameters | [REST](rest.md) |
| Code to language | case style of the language | [Languages](../languages/index.md) |
| Any name | verbs, booleans, units, symmetry | [Naming patterns](../patterns/index.md) |

!!! info "See also"

    - [Common rules](../common/index.md) for rules that do not depend on a language
    - [Languages overview](../languages/index.md) for the case styles
