---
status: new
---

# Languages

!!! success "General patterns"

    - Follow the style guide of the language. A reader of that language expects its case style
    - Keep the meaning of a name the same in every language. Only the case style changes: `order_total` in Python, `orderTotal` in Java, `OrderTotal` in C#
    - Use the formatter and the linter of the language to enforce case. A tool is more reliable than a review comment

!!! tip "Useful tips"

    - Start with the matrix below. Open the page of the language for details and examples
    - When code crosses a language border (an API, a database, a message), the border format wins. See [Naming patterns](../patterns/index.md) and [Databases](../databases/index.md)
    - A style guide that is not official is marked in the matrix. Pick the one that your team uses and write it down

!!! danger "General anti-patterns"

    - Copying the case style of one language into another: `get_user_name()` in Java, `UserName` for a local variable in Go
    - Mixing two styles in one project, for example `camelCase` and `snake_case` JSON keys in one API

## Case styles

| Name | Look | Example |
|---|---|---|
| `snake_case` | lower case, words split by `_` | `order_total` |
| `SCREAMING_SNAKE_CASE` | upper case, words split by `_` | `MAX_RETRY_COUNT` |
| `camelCase` | first word lower case, other words capitalized | `orderTotal` |
| `PascalCase` (also `UpperCamelCase`, `CapWords`) | every word capitalized | `OrderTotal` |
| `kebab-case` | lower case, words split by `-` | `order-total` |

## Matrix

Each cell holds the usual convention of the language. A cell with two answers marks a real conflict between style guides.

| Identifier | Python | JavaScript / TypeScript | Java / Kotlin | C# | Go | Rust |
|---|---|---|---|---|---|---|
| Local variable | `snake_case` | `camelCase` | `camelCase` | `camelCase` | `camelCase`, short | `snake_case` |
| Function or method | `snake_case` | `camelCase` | `camelCase` | `PascalCase` | `PascalCase` if exported, `camelCase` if not | `snake_case` |
| Class or type | `PascalCase` | `PascalCase` | `PascalCase` | `PascalCase` | `PascalCase` | `PascalCase` |
| Interface or trait | `PascalCase` (a class, often with a `Protocol` base) | `PascalCase`, no `I` prefix | `PascalCase`, no `I` prefix (common practice, not a rule of the guides) | `I` plus `PascalCase`: `IOrderRepository` | `PascalCase`, one-method names often end in `-er`: `Reader` | `PascalCase` (trait) |
| Constant | `SCREAMING_SNAKE_CASE` | `SCREAMING_SNAKE_CASE` | `SCREAMING_SNAKE_CASE` | `PascalCase` | `PascalCase` or `camelCase`, not all caps | `SCREAMING_SNAKE_CASE` |
| Enum member | `SCREAMING_SNAKE_CASE` (Python enum docs; PEP 8 is silent) | `PascalCase` (TypeScript handbook) or `SCREAMING_SNAKE_CASE` (Google guide) | `SCREAMING_SNAKE_CASE` (Java); either style (Kotlin) | `PascalCase` | `PascalCase`, often with the type as a prefix: `ColorRed` | `PascalCase` |
| Package, module or namespace | short `lowercase` for a package, `lower_case` allowed for a module | `lowercase` or `kebab-case` (npm names are lower case) | `lowercase`, no underscores | `PascalCase`, dotted: `Shop.Orders` | one short `lowercase` word | `snake_case` |
| Source file | `snake_case.py` | `kebab-case.ts` (Google guide: lower case with `-` or `_`); `camelCase.ts` in other guides | `PascalCase.java` equal to the public class; `PascalCase.kt` | `PascalCase.cs` equal to the main type | `snake_case.go` (community practice) | `snake_case.rs` |
| Private member | `_leading_underscore` | `#field` (JavaScript); the `private` keyword (TypeScript, and the only choice in the Google guide) | no prefix (Java); `_name` for a backing property (Kotlin) | `_camelCase` for fields (C# coding conventions); the naming guidelines target public API and do not use underscores | lower-case first letter | no prefix; the `pub` keyword sets the scope |
| Type parameter | `T`, or `PascalCase` | `T`, `TKey` | `T`; Google Java also allows `RequestT` | `T`, `TKey` | `T`, `K`, `V` | `T`, short `PascalCase` |

!!! warning "Rows with a real conflict"

    The enum member, private member and source file rows show that style guides of one language can disagree. The acronym row below is the largest conflict. Check the guide that your project follows before you copy a name from this table.

## Where the rules differ most

| Topic | Python | JavaScript / TypeScript | Java / Kotlin | C# | Go | Rust |
|---|---|---|---|---|---|---|
| Acronym in a name | all capitals: `HTTPServerError` | words: `HttpClient` (Google guide) | words: `HttpClient` (Google Java); Kotlin conventions keep two-letter acronyms in capitals: `IOStream` | two letters in capitals: `IOStream`; longer as words: `HtmlParser` | all capitals: `HTTPClient`, `userID` | words: `Uuid` |
| Constant case | all capitals | all capitals | all capitals | `PascalCase` | `MixedCaps`, no capitals | all capitals |
| Name of a getter | `order.total` (property) | `order.total` or `getTotal()` | `getTotal()` (JavaBeans); `total()` (records, newer APIs); property `total` (Kotlin) | property `Total` | `Total()`, no `Get` prefix | `total()`, no `get_` prefix |

For `is_`, `has_` and other word choices that do not depend on the language, see [Booleans, collections, units and time](../patterns/booleans-collections-units-time.md) and [Action and context](../patterns/action-context.md).

## Sources

| Language | Guide |
|---|---|
| Python | [PEP 8](https://peps.python.org/pep-0008/#naming-conventions) and the [enum documentation](https://docs.python.org/3/library/enum.html) |
| JavaScript / TypeScript | [Google TypeScript style guide](https://google.github.io/styleguide/tsguide.html). It is not an official language standard. The [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/enums.html) shows enum member style. |
| Java | [Google Java style guide](https://google.github.io/styleguide/javaguide.html) and [Oracle naming conventions](https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html) |
| Kotlin | [Kotlin coding conventions](https://kotlinlang.org/docs/coding-conventions.html#naming-rules) |
| C# | [.NET naming guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/naming-guidelines) and [C# coding conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names) |
| Go | [Effective Go](https://go.dev/doc/effective_go#names) and [Go code review comments](https://go.dev/wiki/CodeReviewComments) |
| Rust | [Rust API guidelines: naming](https://rust-lang.github.io/api-guidelines/naming.html) and [RFC 430](https://rust-lang.github.io/rfcs/0430-finalizing-naming-conventions.html) |

## Pages

| Language | Page |
|---|---|
| Python | [General rules](../python/index.md), [Variables](../python/variables.md), [Functions](../python/functions.md), [Classes](../python/classes.md), [Class methods](../python/class_methods.md), [Tests](../python/tests.md), [Modules](../python/modules.md), [Constants](../python/constants.md), [Exceptions](../python/exceptions.md), [Enums](../python/enums.md), [Special functions](../python/special_functions.md) |
| JavaScript / TypeScript | [JavaScript and TypeScript](javascript-typescript.md) |
| Java / Kotlin | [Java and Kotlin](java-kotlin.md) |
| C# | [C# and .NET](csharp-dotnet.md) |

!!! info "See also"

    - [Common rules](../common/index.md) for rules that do not depend on a language
    - [Naming patterns](../patterns/index.md) for patterns that hold in every language
    - [References and glossary](../common/references-and-glossary.md) for sources and terms
