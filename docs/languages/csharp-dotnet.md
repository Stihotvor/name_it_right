---
status: new
---

# C# and .NET

!!! success "General patterns"

    - Use `PascalCase` for types, methods, properties, events, constants and namespaces: `OrderService`, `CalculateTotal`, `MaxRetryCount`
    - Use `camelCase` for local variables and parameters: `orderTotal`, `couponCode`
    - Start an interface name with `I`: `IOrderRepository`
    - Use a verb first for methods and a noun for properties, as in the [action and context pattern](../patterns/action-context.md)
    - Name a file after the main type in it: `OrderService.cs`

!!! tip "Useful tips"

    - Use `_camelCase` for private fields if your team follows the C# coding conventions. The .NET naming guidelines do not set a rule for private fields
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
| Namespace | `PascalCase`, dotted, from the company or product | `Shop.Orders`, `Contoso.Billing.Invoices` | The path of the project is the namespace. |
| Class | `PascalCase` noun | `OrderService`, `PaymentGateway` | The usual style. |
| Static class | `PascalCase` noun | `OrderIds`, `Guard` | A class without instances. |
| Extension class | the extended type plus `Extensions` | `StringExtensions`, `EnumerableExtensions` | Common practice in the .NET libraries. |
| Struct | `PascalCase` noun | `Money`, `OrderId` | Same as a class. |
| Record | `PascalCase` noun | `OrderLine` | Same as a class. |
| Interface | `I` plus `PascalCase` | `IOrderRepository`, `IDisposable` | The `I` is a firm .NET convention. |
| Enum | singular `PascalCase` noun | `OrderStatus` | One value is one status. |
| Flags enum | plural `PascalCase` noun | `FilePermissions` | Several values can combine. |
| Enum member | `PascalCase` | `OrderStatus.Pending` | Same style as a constant. |
| Constant | `PascalCase` | `MaxRetryCount`, `DefaultTimeout` | The .NET guidelines use `PascalCase`. |
| Static readonly field | `PascalCase` | `DefaultOptions` | Same as a constant. |
| Method | verb first, `PascalCase` | `CalculateTotal`, `FindOrders` | An action. |
| Async method | method name plus `Async` | `GetOrderAsync`, `SaveAsync` | Callers see that they must await. |
| Property | `PascalCase` noun | `Total`, `CustomerEmail` | The usual style. |
| Boolean property | `Is`, `Has`, `Can` plus a word | `IsActive`, `HasGiftWrap`, `CanRefund` | A boolean reads as a statement. |
| Event | verb phrase, past or present | `OrderPlaced`, `Closing` | Past tense for after, `-ing` for before. |
| Event handler | the source plus event | `OnOrderPlaced`, `Button_Click` | `On` plus the event name raises the event. |
| Delegate | `PascalCase` noun or phrase | `OrderHandler` | Same style as a type. |
| Attribute | `PascalCase` plus `Attribute` | `RequiredAttribute` | The suffix can be dropped at use: `[Required]`. |
| Exception | `PascalCase` plus `Exception` | `OrderNotFoundException` | A strong convention. |
| Generic parameter | `T`, or `T` plus a word | `T`, `TKey`, `TValue` | A short name for a short scope. |
| Local variable | `camelCase` noun | `orderTotal`, `customerEmail` | The usual style. |
| Parameter | `camelCase` noun | `orderId`, `couponCode` | Same as a local variable. |
| Private field | `_camelCase` | `_orderRepository`, `_cache` | Coding conventions of .NET. |
| Static private field | `s_camelCase` | `s_instanceCount` | The .NET runtime uses this form. |
| Collection | plural noun | `Orders`, `LineItems` | A plural shows a list. |
| Test class | class under test plus `Tests` | `OrderServiceTests` | Test runners and readers find it. |
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
| `s_camelCase` | Private static field | `s_count` | The .NET runtime code style. |
| `t_camelCase` | Thread-static field | `t_buffer` | Same style. |
| No prefix | Everything else | `cache` | Some teams use `this.cache`. |

Conflict: the .NET naming guidelines do not use underscores. The C# coding conventions allow `_camelCase` for private fields. Choose one and write it in `.editorconfig`.

## Conversion names

| Pattern | Meaning | Examples |
|---|---|---|
| `To<Type>` | Makes a new value of another type. | `ToString`, `ToList`, `ToArray` |
| `As<Type>` | A view of the same data, with no copy. | `AsEnumerable`, `AsSpan` |
| `From<Type>` | A static method that builds a value from another. | `Guid.Parse`, `OrderId.FromString` |
| `Parse` | Reads text and throws on failure. | `int.Parse` |
| `TryParse` | Reads text and returns `false` on failure. | `int.TryParse` |
| `Create` | A factory. | `Order.Create(...)` |

## Async and LINQ

| Case | Rule | Examples |
|---|---|---|
| Async method | the `Async` suffix | `FetchOrdersAsync` |
| Cancellation token | `cancellationToken`, last parameter | `GetOrderAsync(id, cancellationToken)` |
| LINQ query variable | a plural noun | `activeOrders`, `overdueInvoices` |
| Lambda parameter | a short singular word | `orders.Where(order => order.IsActive)` |

!!! info "See also"

    - [Languages overview](index.md) for the matrix of all languages
    - [Naming patterns](../patterns/index.md) and the [cookbook](../patterns/cookbook.md)
    - [.NET naming guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/naming-guidelines), [C# identifier names](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names), [.NET runtime coding style](https://github.com/dotnet/runtime/blob/main/docs/coding-guidelines/coding-style.md)
