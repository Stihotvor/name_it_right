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

    - Pick one style for file names and keep it: `kebab-case.ts` works on every file system. The Google guide asks for lower case with `-` or `_`
    - Do not put `I` in front of an interface, and do not put `Type` or `Interface` behind it: `OrderRepository`, not `IOrderRepository`
    - Use a formatter and a linter (ESLint with `@typescript-eslint/naming-convention`) to enforce the rules

!!! danger "General anti-patterns"

    - Hungarian notation: `strName`, `arrItems`, `objUser`
    - A leading underscore for a private member in new code. Use the `private` keyword, or `#field` in plain JavaScript
    - Names that repeat the type: `userObject`, `ordersArray`
    - A boolean that is not a statement: `status`, `flag`, `check`

The JavaScript rules also apply to TypeScript. The sections below mark what is only TypeScript. Where a rule comes from community practice and not from a style guide, the text says so.

## Names by kind

| Kind | Rule | Examples | Why this name |
|---|---|---|---|
| Variable | `camelCase` noun | `orderTotal`, `customerEmail` | The usual style of the language. |
| Boolean | `is`, `has`, `can`, `should` plus a word | `isActive`, `hasGiftWrap`, `canRefund` | A boolean reads as a statement. |
| Collection | plural noun | `orders`, `lineItems` | A plural shows a list. |
| Map or record | `<value>By<Key>` | `ordersById`, `customersByEmail` | Says what the key is. |
| Function | verb first, `camelCase` | `calculateTotal`, `fetchOrders` | A function does something. |
| Predicate function | `is`, `has`, `can` plus a word | `isExpired(coupon)`, `hasStock(item)` | Returns a boolean. |
| Async function | the same name as a sync function | `fetchOrders` | Community practice: do not add `Async`. In TypeScript the `Promise` return type shows it. Node marks the synchronous variant instead: `readFileSync`. |
| Event handler | `handle` plus event, or `on` plus event for a prop | `handleSubmit`, `onSubmit` | The React documentation uses `handle` for the function and `on` for the prop that it fills. DOM properties are lower case: `onclick`. |
| Class | `PascalCase` noun | `OrderService`, `PaymentGateway` | The usual style of the language. |
| Interface (TypeScript) | `PascalCase` noun, no `I` | `OrderRepository`, `PaymentGateway` | The TypeScript handbook does not use a prefix. |
| Type alias (TypeScript) | `PascalCase` noun | `OrderId`, `OrderStatus` | The same style as other types. |
| Generic parameter (TypeScript) | `T`, or a descriptive `PascalCase` name | `T`, `Key`, `TResponse` | A short name for a short scope. The `T` prefix on a longer name is community practice. |
| Enum (TypeScript) | singular `PascalCase` noun | `OrderStatus` | One value is one status. |
| Enum member (TypeScript) | `PascalCase` or `SCREAMING_SNAKE_CASE` | `OrderStatus.Pending` or `OrderStatus.PENDING` | The handbook examples use `PascalCase`, and the Google guide asks for constant case. See "Constants" below. |
| Constant | `SCREAMING_SNAKE_CASE` | `MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT_MS` | A module-level value that never changes. |
| Local constant | `camelCase` | `const orderTotal = ...` | `const` alone does not make a value a constant of the module. |
| Private field (JavaScript) | `#name` | `#cache`, `#apiKey` | A real private field of JavaScript. The Google TypeScript guide forbids it in TypeScript. Other projects may allow it. |
| Private member (TypeScript) | `private` keyword, no prefix | `private cache` | The keyword already says it. |
| Module file | `kebab-case.ts` | `order-service.ts` | Works on every file system. |
| React component file | `PascalCase.tsx` | `OrderSummary.tsx` | Community practice (for example Airbnb). The file name equals the component. It conflicts with the Google rule for lower-case file names. |
| Test file | `<unit>.test.ts` or `<unit>.spec.ts` | `order-service.test.ts` | Test runners find these names. |
| Package (npm) | lower case; `kebab-case` is usual | `order-utils`, `@shop/orders` | npm requires lower case and at most 214 characters. |
| Environment variable | `SCREAMING_SNAKE_CASE` | `DATABASE_URL`, `NODE_ENV` | The POSIX shell convention. |

## Acronyms

Treat an acronym as a word. The Google TypeScript guide says to do this.

| Bad | Better | Why |
|---|---|---|
| `userID` | `userId` | An acronym is a word. |
| `parseXML` | `parseXml` | The Google guide: treat abbreviations as whole words. |
| `HTTPClient` | `HttpClient` | The same guide rule for a class name. |
| `getURL` | `getUrl` | The same guide rule for a function name. |

Conflict: many projects, and some built-in names (`innerHTML`, `XMLHttpRequest`, `JSON`), keep capitals. Names from the platform stay as they are. Names that you write follow one rule in the whole project.

## Constants

| Case | Rule | Examples |
|---|---|---|
| Module-level, never changes | `SCREAMING_SNAKE_CASE` | `MAX_RETRY_COUNT`, `API_BASE_URL` |
| Object that is frozen or `as const` | `SCREAMING_SNAKE_CASE` for the name, `camelCase` for the keys | `DEFAULT_OPTIONS = { retryCount: 3 }` |
| Local `const` | `camelCase` | `const total = items.length` |
| Enum-like object (community practice) | `PascalCase` name, `PascalCase` keys | `const OrderStatus = { Pending: 'pending' } as const` |

An enum-like object acts as an enum, so it follows the enum style and not the constant style. Conflict: the Google guide uses `SCREAMING_SNAKE_CASE` for enum values. The TypeScript handbook examples use `PascalCase` but state no rule. Choose one and enforce it with the lint rule.

## Private names

| Style | Where | Examples | Notes |
|---|---|---|---|
| `#name` | JavaScript classes | `#cache` | Truly private at run time. In TypeScript, the Google guide forbids `#` and asks for the `private` keyword. Other projects may allow it. |
| `private` keyword | TypeScript | `private cache` | Private at compile time only. |
| `_name` | Older code | `_cache` | A convention without a check. Avoid in new code. |
| `_` alone | Unused argument | `(_event, value) => value` | Signals that an argument is not used. The compiler option `noUnusedParameters` ignores parameters that start with `_`. |

## TypeScript names

| Feature | Rule | Examples |
|---|---|---|
| Interface for data | noun | `Order`, `OrderLine` |
| Interface for behavior | role noun | `PaymentGateway`, `OrderRepository` |
| Props type | component name plus `Props` | `OrderSummaryProps` |
| State type | component name plus `State` | `OrderListState` |
| Union of strings | `PascalCase` type with literal members | `type Currency = 'EUR' \| 'USD'` |
| Type guard | `is` plus a type | `isOrder(value): value is Order` |
| Utility type use | a built-in utility type applied to a named type | `Partial<Order>`, `Pick<Order, 'id'>` |
| Declaration file | the name of the `.js` file that it describes, plus `.d.ts` | `order-service.d.ts` next to `order-service.js` |
| Branded type (community practice) | `PascalCase` name of the concept | `type OrderId = string & { readonly __brand: 'OrderId' }` |

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
| Spy | the wrapped object plus `Spy` | `loggerSpy` |
| Fixture | the object it builds | `buildOrder()`, `orderFixture` |

!!! info "See also"

    - [Languages overview](index.md) for the matrix of all languages
    - [Naming patterns](../patterns/index.md) and the [cookbook](../patterns/cookbook.md)
    - [Google TypeScript style guide](https://google.github.io/styleguide/tsguide.html#naming), [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/enums.html), [MDN: JavaScript guidelines](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Code_style_guide/JavaScript)
