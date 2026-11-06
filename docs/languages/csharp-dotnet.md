---
status: new
---

# C# and .NET

!!! success "General patterns"

    - Use `PascalCase` for types, methods, properties, events, constants and namespaces: `OrderService`, `CalculateTotal`, `MaxRetryCount`
    - Use `camelCase` for local variables and parameters: `orderTotal`, `couponCode`
    - Start an interface name with `I`: `IOrderRepository`
    - Use a verb first for methods and a noun for properties, as in the [action and context pattern](../patterns/action-context.md)
    - Name a file after the main type in it: `OrderService.cs`. This is common practice, and StyleCop checks it (SA1649)

!!! tip "Useful tips"

    - Use `_camelCase` for private fields if your team follows the C# coding conventions. The .NET naming guidelines target public API and do not use underscores
    - End an async method name with `Async`: `GetOrderAsync`. This is a strong convention of the .NET libraries
    - Use an analyzer to enforce the rules (`.editorconfig` naming rules with the IDE1006 diagnostic, or StyleCop)

!!! danger "General anti-patterns"

    - `SCREAMING_SNAKE_CASE` for constants. C# uses `PascalCase`: `MaxRetryCount`
    - Hungarian notation: `strName`, `iCount`
    - Underscores in type and method names: `Order_Service`. Test method names are a common exception
    - A boolean that is not a statement: `Status`, `Flag`, `Check`

## Names by kind

| Kind | Rule | Examples | Why this name |
|---|---|---|---|
| Namespace | `PascalCase`, dotted: `Company.Product.Feature` | `Shop.Orders`, `Contoso.Billing.Invoices` | The guidelines use this form, so a type name is unique across libraries. |
| Class | `PascalCase` noun | `OrderService`, `PaymentGateway` | The guidelines ask for `PascalCase` for every public type. |
| Static class | `PascalCase` noun | `OrderIds`, `Guard` | A class without instances. |
| Extension class (community practice) | the extended type plus `Extensions` | `StringExtensions`, `EnumerableExtensions` | Common practice in the .NET libraries. |
| Struct | `PascalCase` noun | `Money`, `OrderId` | A struct is a type, so it follows the type rule. |
| Record | `PascalCase` noun | `OrderLine` | A record is a type, so it follows the type rule. |
| Interface | `I` plus `PascalCase` | `IOrderRepository`, `IDisposable` | The `I` is a firm .NET convention. |
| Enum | singular `PascalCase` noun | `OrderStatus` | One value is one status. |
| Flags enum | plural `PascalCase` noun | `FilePermissions` | Several values can combine. |
| Enum member | `PascalCase` | `OrderStatus.Pending` | Same style as a constant. |
| Constant | `PascalCase` | `MaxRetryCount`, `DefaultTimeout` | The .NET guidelines use `PascalCase`. |
| Static readonly field, public or internal | `PascalCase` | `DefaultOptions` | It acts like a constant. A private one is `s_camelCase`; see Private names. |
| Method | verb first, `PascalCase` | `CalculateTotal`, `FindOrders` | An action. |
| Async method | method name plus `Async` | `GetOrderAsync`, `SaveAsync` | Callers see that they must await. |
| Property | `PascalCase` noun | `Total`, `CustomerEmail` | The guidelines ask for `PascalCase` for public members. |
| Boolean property | `Is`, `Has`, `Can` plus a word | `IsActive`, `HasGiftWrap`, `CanRefund` | A boolean reads as a statement. |
| Event | verb phrase, past or present | `OrderPlaced`, `Closing` | Past tense for after, `-ing` for before. |
| Event raiser | `On` plus the event name | `OnOrderPlaced` | The protected virtual method that raises the event (guidelines). |
| Event handler method | source, `_`, event | `Button_Click` | The IDE designer form. It is not a guideline rule. |
| Delegate for an event | the event name plus `EventHandler` | `OrderPlacedEventHandler` | The guidelines use this suffix for event delegates. |
| Delegate for a callback | the purpose plus `Callback` | `RetryCallback` | The guidelines use this suffix for delegates passed to methods. |
| Attribute | `PascalCase` plus `Attribute` | `RequiredAttribute` | The suffix can be dropped at use: `[Required]`. |
| Exception | `PascalCase` plus `Exception` | `OrderNotFoundException` | The guidelines require the suffix. |
| Generic parameter | `T` when it is clear; otherwise `T` plus a descriptive name | `T`, `TKey`, `TValue` | The guidelines use a single `T` only when it is self-explanatory. |
| Local variable | `camelCase` noun | `orderTotal`, `customerEmail` | The guidelines ask for `camelCase` for parameters, and the coding conventions use it for locals. |
| Parameter | `camelCase` noun | `orderId`, `couponCode` | The guidelines ask for `camelCase` for parameters. |
| Private field | `_camelCase` | `_orderRepository`, `_cache` | The C# coding conventions page (identifier names). |
| Private static field | `s_camelCase` | `s_instanceCount` | The C# coding conventions and the .NET runtime style use this form. |
| Collection (community practice) | plural noun | `Orders`, `LineItems` | A plural shows a list. |
| Test class (community practice) | class under test plus `Tests` | `OrderServiceTests` | Readers and file search find the tests of a class. |
| Test method | `Method_Condition_Result` (community practice) | `CalculateTotal_WithCoupon_AppliesDiscount` | The underscores split three parts. Test names are the usual exception to the no-underscore rule. |

## Acronyms

| Length | Rule | Examples |
|---|---|---|
| Two letters | Both letters in capitals, except at the start of a camelCase name | `IOStream`, `DBConnection`, `ioStream` |
| Three letters or more | A word | `HtmlParser`, `XmlReader`, `UriBuilder` |
| In a variable | The same rule, with the first word in lower case | `htmlParser`, `ioStream` |

Conflict: Java treats every acronym as a word, and Go capitalizes every acronym. `Id` and `Ok` are abbreviations, not acronyms, so the name is `OrderId`, not `OrderID`.

## Private names

| Style | Where | Examples | Notes |
|---|---|---|---|
| `_camelCase` | Private instance field | `_cache` | The C# coding conventions. |
| `s_camelCase` | Private static field | `s_count` | The C# coding conventions and the .NET runtime code style. |
| `t_camelCase` | Thread-static field | `t_buffer` | The C# coding conventions and the runtime style. |
| No prefix | Locals and parameters | `cache` | A local is not a field, so it needs no mark. |

Conflict: the .NET naming guidelines target public API and do not use underscores. The C# coding conventions use `_camelCase` for private fields. Choose one and write it in `.editorconfig`.

## Conversion names

These patterns come from the .NET base class library (BCL). They are practice, not rules of the guidelines.

| Pattern | Meaning | Examples |
|---|---|---|
| `To<Type>` | Makes a new value of another type. | `ToString`, `ToList`, `ToArray` |
| `As<Type>` | A view of the same data, with no copy. | `AsEnumerable`, `AsSpan` |
| `From<Type>` | A static method that builds a value from another. | `TimeSpan.FromSeconds`, `Convert.FromBase64String` |
| `Parse` | Reads text and throws on failure. | `int.Parse` |
| `TryParse` | Reads text and returns `false` on failure. | `int.TryParse` |
| `Create` | A factory. | `Order.Create(...)` |

## Async and LINQ

| Case | Rule | Examples |
|---|---|---|
| Async method | the `Async` suffix | `FetchOrdersAsync` |
| Cancellation token | `cancellationToken`, last parameter | `GetOrderAsync(id, cancellationToken)` |
| LINQ query variable (community practice) | a plural noun | `activeOrders`, `overdueInvoices` |
| Lambda parameter | a short singular word | `orders.Where(order => order.IsActive)` |

!!! info "See also"

    - [Languages overview](index.md) for the matrix of all languages
    - [Naming patterns](../patterns/index.md) and the [cookbook](../patterns/cookbook.md)
    - [.NET naming guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/naming-guidelines), [C# identifier names](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names), [.NET runtime coding style](https://github.com/dotnet/runtime/blob/main/docs/coding-guidelines/coding-style.md)
