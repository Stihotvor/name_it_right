---
status: new
---

# JavaScript and TypeScript

!!! success "General patterns"

    - Use `camelCase` for variables, functions, methods and properties: `orderTotal`, `fetchOrders`
    - Use `PascalCase` for classes, interfaces, type aliases, enums and React components: `OrderService`, `OrderSummary`
    - Use `SCREAMING_SNAKE_CASE` for module-level constants that never change: `MAX_RETRY_COUNT`
    - Use a verb first for functions and a noun for values, as in the [action and context pattern](../patterns/action-context.md)
    - Treat an acronym as a word: `userId`, `HttpClient`, `parseXml`

!!! tip "Useful tips"

    - Pick one style for file names and keep it: `kebab-case.ts` is the most common, and `order-service.ts` works on every file system
    - Do not put `I` in front of an interface, and do not put `Type` or `Interface` behind it: `OrderRepository`, not `IOrderRepository`
    - Use a formatter and a linter (ESLint with `@typescript-eslint/naming-convention`) to enforce the rules

!!! danger "General anti-patterns"

    - Hungarian notation: `strName`, `arrItems`, `objUser`
    - A leading underscore for a private member in new code. Use the `private` keyword, or `#field` in plain JavaScript
    - Names that repeat the type: `userObject`, `ordersArray`
    - A boolean that is not a statement: `status`, `flag`, `check`

All TypeScript rules are valid JavaScript rules too. The sections below mark what is only TypeScript.

## Names by kind

| Kind | Rule | Examples | Why this name |
|---|---|---|---|
| Variable | `camelCase` noun | `orderTotal`, `customerEmail` | The usual style of the language. |
| Boolean | `is`, `has`, `can`, `should` plus a word | `isActive`, `hasGiftWrap`, `canRefund` | A boolean reads as a statement. |
| Collection | plural noun | `orders`, `lineItems` | A plural shows a list. |
| Map or record | `<value>By<Key>` | `ordersById`, `customersByEmail` | Says what the key is. |
| Function | verb first, `camelCase` | `calculateTotal`, `fetchOrders` | A function does something. |
| Predicate function | `is`, `has`, `can` plus a word | `isExpired(coupon)`, `hasStock(item)` | Returns a boolean. |
| Async function | the same name as a sync function | `fetchOrders` | Do not add `Async`. The `Promise` return type shows it. |
| Event handler | `handle` plus event, or `on` plus event for a prop | `handleSubmit`, `onSubmit` | `handle` is the function, `on` is the slot it fills. |
| Class | `PascalCase` noun | `OrderService`, `PaymentGateway` | The usual style of the language. |
| Interface (TypeScript) | `PascalCase` noun, no `I` | `OrderRepository`, `PaymentGateway` | The TypeScript handbook does not use a prefix. |
| Type alias (TypeScript) | `PascalCase` noun | `OrderId`, `OrderStatus` | The same style as other types. |
| Generic parameter (TypeScript) | `T`, or `T` plus a word | `T`, `TKey`, `TResponse` | A short name for a short scope. |
| Enum (TypeScript) | singular `PascalCase` noun | `OrderStatus` | One value is one status. |
| Enum member (TypeScript) | `PascalCase` | `OrderStatus.Pending` | The TypeScript handbook uses `PascalCase`. |
| Constant | `SCREAMING_SNAKE_CASE` | `MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT_MS` | A module-level value that never changes. |
| Local constant | `camelCase` | `const orderTotal = ...` | `const` alone does not make a value a constant of the module. |
| Private field (JavaScript) | `#name` | `#cache`, `#apiKey` | A real private field of JavaScript. The Google TypeScript guide does not allow it in TypeScript. |
| Private member (TypeScript) | `private` keyword, no prefix | `private cache` | The keyword already says it. |
| Module file | `kebab-case.ts` | `order-service.ts` | Works on every file system. |
| React component file | `PascalCase.tsx` | `OrderSummary.tsx` | The file name equals the component. |
| Test file | `<unit>.test.ts` or `<unit>.spec.ts` | `order-service.test.ts` | Test runners find these names. |
| Package (npm) | lower case, `kebab-case` | `order-utils`, `@shop/orders` | npm package names must be lower case. |
| Environment variable | `SCREAMING_SNAKE_CASE` | `DATABASE_URL`, `NODE_ENV` | A convention of operating systems. |

## Acronyms

Treat an acronym as a word. The Google TypeScript guide says to do this.

| Bad | Better | Why |
|---|---|---|
| `userID` | `userId` | An acronym is a word. |
| `parseXML` | `parseXml` | Same rule. |
| `HTTPClient` | `HttpClient` | Same rule. |
| `getURL` | `getUrl` | Same rule. |

Conflict: many projects, and some built-in names (`innerHTML`, `XMLHttpRequest`, `JSON`), keep capitals. Names from the platform stay as they are. Names that you write follow one rule in the whole project.

## Constants

| Case | Rule | Examples |
|---|---|---|
| Module-level, never changes | `SCREAMING_SNAKE_CASE` | `MAX_RETRY_COUNT`, `API_BASE_URL` |
| Object that is frozen or `as const` | `SCREAMING_SNAKE_CASE` for the name, `camelCase` for the keys | `DEFAULT_OPTIONS = { retryCount: 3 }` |
| Local `const` | `camelCase` | `const total = items.length` |
| Enum-like object | `PascalCase` name, `PascalCase` keys | `const OrderStatus = { Pending: 'pending' } as const` |

Conflict: the Google guide uses `SCREAMING_SNAKE_CASE` for enum values. The TypeScript handbook uses `PascalCase`. Choose one and enforce it with the lint rule.

## Private names

| Style | Where | Examples | Notes |
|---|---|---|---|
| `#name` | JavaScript classes (and TypeScript, unless the guide forbids it) | `#cache` | Truly private at run time. The Google TypeScript guide says to use the `private` keyword instead. |
| `private` keyword | TypeScript | `private cache` | Private at compile time only. |
| `_name` | Older code | `_cache` | A convention without a check. Avoid in new code. |
| `_` alone | Unused argument | `(_event, value) => value` | Signals that an argument is not used. |

## TypeScript names

| Feature | Rule | Examples |
|---|---|---|
| Interface for data | noun | `Order`, `OrderLine` |
| Interface for behavior | role noun | `PaymentGateway`, `OrderRepository` |
| Props type | component name plus `Props` | `OrderSummaryProps` |
| State type | component name plus `State` | `OrderListState` |
| Union of strings | `PascalCase` type with literal members | `type Currency = 'EUR' \| 'USD'` |
| Type guard | `is` plus a type | `isOrder(value): value is Order` |
| Utility type | noun that says the shape | `Partial<Order>`, `OrderSummary` |
| Declaration file | the module name plus `.d.ts` | `order-service.d.ts` |
| Branded type | `PascalCase` name of the concept | `type OrderId = string & { readonly __brand: 'OrderId' }` |

## Modules and exports

| Case | Rule | Examples |
|---|---|---|
| Named export | the name of the thing | `export function calculateTotal` |
| Default export | avoid it. Use a named export | `export class OrderService` |
| Barrel file | `index.ts` | `orders/index.ts` |
| Import alias | short, clear, `camelCase` or `PascalCase` by kind | `import * as orderApi from './order-api'` |

## Tests

| Kind | Rule | Examples |
|---|---|---|
| Test suite | the unit name | `describe('calculateTotal', ...)` |
| Test case | `it('<does>', ...)` or `test('<does>', ...)` | `it('adds tax to the total', ...)` |
| Mock | `mock` plus the replaced object | `mockPaymentGateway` |
| Spy | `spy` plus the wrapped object | `spyLogger` |
| Fixture | the object it builds | `buildOrder()`, `orderFixture` |

!!! info "See also"

    - [Languages overview](index.md) for the matrix of all languages
    - [Naming patterns](../patterns/index.md) and the [cookbook](../patterns/cookbook.md)
    - [Google TypeScript style guide](https://google.github.io/styleguide/tsguide.html#naming), [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/enums.html), [MDN: JavaScript guidelines](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Code_style_guide/JavaScript)
