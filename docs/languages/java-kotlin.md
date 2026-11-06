---
status: new
---

# Java and Kotlin

!!! success "General patterns"

    - Use `camelCase` for variables, parameters, methods and properties: `orderTotal`, `findOrders`
    - Use `PascalCase` for classes, interfaces, enums and annotations: `OrderService`, `PaymentGateway`
    - Use `SCREAMING_SNAKE_CASE` for constants: `MAX_RETRY_COUNT`
    - Use all lower case for packages: `com.example.shop.orders`. Java forbids underscores. The Kotlin conventions only discourage them
    - Use a verb first for methods and a noun for values, as in the [action and context pattern](../patterns/action-context.md)

!!! tip "Useful tips"

    - Treat an acronym as a word in Java: `HttpClient`, `XmlParser`, `userId`. Kotlin keeps a two-letter acronym in capitals: `IOStream`
    - Do not put `I` in front of an interface and do not put `Impl` behind a class when a better name exists: `OrderRepository` and `JpaOrderRepository`, not `IOrderRepository` and `OrderRepositoryImpl`
    - Use a formatter and a checker to enforce the rules (Checkstyle or Spotless for Java, ktlint or detekt for Kotlin)

!!! danger "General anti-patterns"

    - Hungarian notation: `strName`, `lstItems`
    - `get` and `set` prefixes on Kotlin properties: write `val total`, not `fun getTotal()`
    - Underscores in method names outside tests: `calculate_total()`. The Google Java guide allows underscores in test method names
    - A boolean that is not a statement: `status`, `flag`, `check`

Both languages run on the JVM and call each other, so a shared style is useful. The sections below mark what only one language does.

## Names by kind

| Kind | Rule | Examples | Why this name |
|---|---|---|---|
| Local variable | `camelCase` noun | `orderTotal`, `customerEmail` | The Google Java and Kotlin guides both ask for `camelCase`. |
| Parameter | `camelCase` noun | `orderId`, `couponCode` | The same style as a local variable. |
| Boolean | `is`, `has`, `can`, `should` plus a word | `isActive`, `hasGiftWrap`, `canRefund` | A boolean reads as a statement. |
| Collection | plural noun | `orders`, `lineItems` | A plural shows a list. |
| Map | `<value>By<Key>` | `ordersById`, `customersByEmail` | Says what the key is. |
| Method or function | verb first, `camelCase` | `calculateTotal`, `findOrders` | An action. |
| Predicate | `is`, `has`, `can` plus a word | `isExpired()`, `hasStock()` | Returns a boolean. |
| Class | `PascalCase` noun | `OrderService`, `PaymentGateway` | Both guides ask for `PascalCase` for a type. |
| Interface | `PascalCase` noun or adjective | `OrderRepository`, `Comparable`, `Closeable` | Name the role. The JDK has no `I` prefix. Community practice follows the JDK. |
| Abstract class | `PascalCase`; add `Abstract` only when a class and an interface share a name | `AbstractOrderProcessor` | The JDK uses this form (`AbstractList` next to `List`). |
| Enum | singular `PascalCase` noun | `OrderStatus` | One value is one status. |
| Enum constant | `SCREAMING_SNAKE_CASE` | `OrderStatus.PENDING` | The Java form. Kotlin also allows `PascalCase`; see Constants. |
| Constant (Java) | `static final` and deeply immutable, `SCREAMING_SNAKE_CASE` | `MAX_RETRY_COUNT` | The Google Java style guide limits constant case to deeply immutable values. |
| Constant (Kotlin) | `const val` or top-level `val`, `SCREAMING_SNAKE_CASE` | `const val MAX_RETRY_COUNT = 3` | Kotlin conventions use the same case for deeply immutable values. |
| Type parameter | one capital letter, or a class-style name plus `T` | `T`, `K`, `V`, `RequestT` | A short name for a short scope. |
| Package | all lower case, no underscores | `com.example.shop.orders` | Reverse domain name, then the module. |
| Annotation | `PascalCase` noun | `@Transactional`, `@NotNull` | Same style as a class. |
| Exception | `PascalCase` plus `Exception` | `OrderNotFoundException` | The suffix marks a type that can be thrown. `Error` types use `Error`. |
| Builder | the target plus `Builder` | `OrderBuilder` | Says what it builds. |
| Test class | class under test plus `Test` | `OrderServiceTest` | The Google Java style guide asks for the `Test` suffix. Maven Surefire matches it by default. |
| Test method | a sentence in `camelCase`; underscores allowed in Java (Google guide); backticks allowed in Kotlin tests | `calculateTotalAddsTax()`, `calculateTotal_addsTax()`, `` `adds tax to the total`() `` | A test reads as a sentence. |
| Java source file | equal to the public class | `OrderService.java` | The compiler requires it. |
| Kotlin source file | `PascalCase.kt` | `OrderService.kt`, `OrderExtensions.kt` | A file with one class has the class name. A file with many declarations has a descriptive name. |

## Acronyms

| Language | Rule | Examples | Source |
|---|---|---|---|
| Java | An acronym is a word. | `HttpClient`, `XmlHttpRequest`, `userId` | Google Java style guide. |
| Kotlin | A two-letter acronym stays in capitals. A longer one is a word. | `IOStream`, `HttpClient` | Kotlin coding conventions. |

Conflict: the JDK itself mixes the styles (`HttpURLConnection`, `URL`). Names from a library stay as they are. Names that you write follow one rule in the whole project.

## Constants

| Case | Rule | Examples |
|---|---|---|
| Java `static final` of a deeply immutable type | `SCREAMING_SNAKE_CASE` | `DEFAULT_TIMEOUT_MS` |
| Java `static final` of a mutable type | `camelCase` | `private static final List<String> names = ...` |
| Kotlin `const val` | `SCREAMING_SNAKE_CASE` | `const val API_BASE_URL = "..."` |
| Kotlin `val` that holds an object | `camelCase` if the object can change, `SCREAMING_SNAKE_CASE` if not | `val DEFAULT_OPTIONS = Options(...)` |
| Enum constant in Kotlin | either `SCREAMING_SNAKE_CASE` or `PascalCase` | `PENDING` or `Pending` |

Conflict: a Java field is a constant only if the type is immutable. A `static final List` can still change. The Google Java style guide says to use constant case only for deeply immutable values.

## Private names

| Language | Rule | Examples | Notes |
|---|---|---|---|
| Java | no prefix and no suffix | `private int retryCount` | Google Java style rejects `m` and `_` marks. |
| Kotlin | no prefix; `_name` for a backing property | `private val _orders = mutableListOf<Order>()` | Kotlin conventions allow `_` for a backing property that a public property exposes. |

## Java details

| Feature | Rule | Examples |
|---|---|---|
| Getter (JavaBeans, not a guide rule) | `get` plus the property, or `is` for a boolean; records and newer JDK APIs drop `get` | `getTotal()`, `isActive()`, `total()` |
| Setter | `set` plus the property | `setTotal(...)` |
| Record | `PascalCase` noun; accessors have no `get` | `record OrderLine(String sku, int quantity)` and `line.sku()` |
| Static factory (Effective Java and JDK practice) | `of`, `from`, `valueOf`, `create` | `List.of(...)`, `Instant.from(...)`, `Integer.valueOf(...)`, `Order.create(...)` |
| Functional interface | a verb or a role | `OrderValidator`, `Supplier<T>` |
| Test double (community practice) | `fake`, `stub`, `mock` plus the replaced object | `mockPaymentGateway` |

## Kotlin details

| Feature | Rule | Examples |
|---|---|---|
| Property | `camelCase` noun, no `get` | `val total: Long` |
| Data class | `PascalCase` noun | `data class OrderLine(val sku: String)` |
| Sealed class or interface | `PascalCase` noun; cases are nested | `sealed interface PaymentResult` |
| Object | `PascalCase` noun | `object OrderIds` |
| Companion factory | `of`, `from`, `create`. A factory function may use `PascalCase` when it returns the type of the same name | `Money.of(...)`, `fun Money(cents: Long): Money` |
| Extension function (standard library practice) | verb first; `to` plus the type for a conversion | `fun String.toOrderId()` |
| Coroutine function (community practice) | a `suspend` function has the same name as a blocking function and no suffix; a non-suspending function that returns a `Deferred` or `Future` takes `Async` | `suspend fun fetchOrders()`, `fun fetchOrdersAsync(): Deferred<List<Order>>` |
| Flow property (community practice) | plural noun | `val orderUpdates: Flow<Order>` |
| Backing property | `_` plus the public name | `_orders` and `orders` |
| Top-level function in a file | verb first | `fun calculateTotal(...)` |

!!! info "See also"

    - [Languages overview](index.md) for the matrix of all languages
    - [Naming patterns](../patterns/index.md) and the [cookbook](../patterns/cookbook.md)
    - [Google Java style guide](https://google.github.io/styleguide/javaguide.html#s5-naming), [Kotlin coding conventions](https://kotlinlang.org/docs/coding-conventions.html#naming-rules), [Oracle Java code conventions](https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html)
