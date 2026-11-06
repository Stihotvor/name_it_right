---
status: new
---

# Go

!!! success "General patterns"

    - Use `MixedCaps` and no underscores in Go names: `orderTotal`, `OrderTotal`, not `order_total`. The exceptions are test names (`TestX_WithCoupon`), example names (`Example_suffix`) and file name suffixes (`_test.go`, `_linux.go`)
    - Start an exported name with a capital letter and an unexported name with a lower-case letter. The case sets the visibility
    - Keep a name short when its scope is short: `i`, `r`, `ctx`. Use a longer name when the scope is long
    - Write an acronym in one case: `HTTPClient`, `userID`, `parseURL`
    - Use one short lower-case word for a package name: `orders`, `payment`. Do not use underscores or `camelCase`
    - Do not repeat the package name in a name: `orders.Service`, not `orders.OrdersService`

!!! tip "Useful tips"

    - Name a one-method interface after the method plus `-er`: `Reader`, `Writer`, `Stringer`
    - Do not put `Get` in front of a getter: `Total()`, not `GetTotal()`. A setter is `SetTotal`
    - Name an error value with `Err` first, and an error type with `Error` last: `ErrNotFound`, `NotFoundError`
    - Use `gofmt` for layout. Use a linter to enforce names: `staticcheck` (ST1003, ST1012) or `revive` (`var-naming`)

!!! danger "General anti-patterns"

    - `snake_case` and `SCREAMING_SNAKE_CASE`: `max_retry_count`, `MAX_RETRY_COUNT`
    - A package name that repeats its folder path or is too generic: `util`, `common`, `helpers`
    - A package name that says nothing: `models`, `types`, `base`
    - An `I` prefix on an interface: `IOrderRepository`

## Names by kind

| Kind | Rule | Examples | Why this name |
|---|---|---|---|
| Exported function | `MixedCaps`, first letter capital | `CalculateTotal`, `NewOrder` | A capital letter exports the name. |
| Unexported function | `mixedCaps`, first letter lower case | `parseLine`, `validate` | A lower-case letter keeps the name inside the package. |
| Local variable | short `mixedCaps` | `i`, `n`, `order`, `ctx` | A short scope allows a short name. |
| Long-lived variable | descriptive `mixedCaps` | `defaultTimeout`, `orderRepository` | A long scope needs a clearer name. |
| Boolean | a plain statement; `ok` for a lookup | `ok`, `found`, `isActive` | Go code uses `ok` for the second return value of a map lookup or a type assertion. |
| Constant | `MixedCaps`, not capitals | `MaxRetryCount`, `defaultTimeout` | The Google Go style guide asks for `MixedCaps` and no all-capital names. Effective Go has examples with capitals (`KB`, `MB`). |
| Enum-like constants (community practice) | the type name as prefix | `ColorRed`, `ColorGreen`, `StatusPending` | Go has no enum, so the prefix groups the values. The standard library uses a prefix for groups: `http.MethodGet`, `http.StatusOK`. |
| Struct type | `MixedCaps` noun | `Order`, `PaymentGateway` | Effective Go: `MixedCaps` for multi-word names. |
| Interface | `MixedCaps`; `-er` for one method | `Reader`, `Closer`, `OrderStore` | Effective Go: a one-method interface takes the method name plus `-er`. |
| Package | one short lower-case word | `orders`, `payment` | Callers write the package name often. |
| Package, test | package name plus `_test` | `orders_test` | An external test package. |
| Source file | lower case with `_` | `order_service.go`, `order_service_test.go` | Community practice. `_test.go` is required for tests. |
| Receiver | one or two letters from the type, the same in every method | `func (o *Order) Total()`, `func (s *Service) Run()` | Short, and does not use `this` or `self`. |
| Getter | the property name, no `Get` | `Total()`, `Owner()` | Effective Go advises no `Get`. |
| Setter | `Set` plus the property | `SetOwner(...)` | Effective Go: the setter is likely called `SetOwner`. |
| Constructor | `New` plus the type, or `New` alone | `NewOrder`, `orders.New` | Effective Go gives `ring.New` for a package with one main type. |
| Error value | `Err` plus a description | `ErrNotFound`, `ErrInvalidInput` | Standard library practice (`io.EOF`, `os.ErrNotExist`) and `staticcheck` ST1012. |
| Error type | description plus `Error` | `NotFoundError`, `ValidationError` | Effective Go: error types are named `FooError`. |
| Error string | not capitalized, no end punctuation (except for proper nouns and acronyms) | `"order not found"` | The code review comments: messages are often wrapped into longer ones. |
| Context parameter | `ctx`, first parameter | `func Fetch(ctx context.Context, id string)` | A strong convention. |
| Generic type parameter (community practice) | one capital letter, or a short name | `T`, `K`, `V`, `E`, `S` | A short scope. The `slices` package uses `S ~[]E`. There is no official rule. |
| Channel | the thing that moves; `Ch` only to avoid a clash (community practice) | `jobs`, `results`, `doneCh` | Name the content. |
| Test function | `Test` plus a name that does not start with a lower-case letter | `TestCalculateTotal`, `TestCalculateTotal_WithCoupon` | `go test` finds `Test` followed by a non-lower-case character. |
| Benchmark | `Benchmark` plus the unit | `BenchmarkCalculateTotal` | `go test -bench` finds it. |
| Example | `Example`, `ExampleF`, `ExampleT_M`; add `_suffix` with a lower-case first letter for more than one | `ExampleCalculateTotal`, `ExampleOrder_Total`, `Example_basic` | `go test` runs an example that has an `// Output:` comment and compares the output. |
| File name constraint | name plus `_GOOS` or `_GOARCH` | `order_linux.go`, `order_amd64.go` | The Go tool reads the suffix and builds the file only for that target. |

## Acronyms and initialisms

A word that is an acronym keeps one case in the whole name.

| Bad | Better | Why |
|---|---|---|
| `HttpClient` | `HTTPClient` | An initialism is all capitals. |
| `userId` | `userID` | Same rule. |
| `ParseUrl` | `ParseURL` | Same rule. |
| `xmlHttpRequest` | `xmlHTTPRequest` | In an unexported name, the first word stays lower case. |
| `ServeHttp` | `ServeHTTP` | The standard library writes `ServeHTTP`. |

Conflict: the Go rule is the opposite of the Java rule (`HttpClient`). The Go code review comments give examples: `URL` or `url` but not `Url`, and `appID` but not `appId`. The common initialisms (`API`, `ASCII`, `HTML`, `HTTP`, `ID`, `JSON`, `URL`, `UTF8`) are listed in the `golint` source and in `staticcheck` ST1003. `Id` and `Ok` are not special: Go writes `ID`, and `ok` is a normal word in lower case.

## Package names

| Good | Bad | Why |
|---|---|---|
| `orders` | `ordersPackage`, `orders_pkg` | The Go blog: a package name is lower case, with no `under_scores` or `mixedCaps`. |
| `orderstore` | `order_store`, `orderStore` | The Go blog: one lower-case word, no separators. |
| `payment` | `common`, `util`, `helpers` | The Go blog: a package name says what the package provides. |
| `orders.Service` | `orders.OrdersService` | The caller already writes `orders.`, so the type name need not repeat it. |
| `orders.New` | `orders.NewOrders` | The same rule applies to a constructor. |

## Receivers

| Rule | Examples |
|---|---|
| One or two letters from the type name | `o` for `Order`, `s` for `Service` |
| The same name in every method of the type | `func (o *Order) Total()`, `func (o *Order) Cancel()` |
| Not `this`, `self` or `me` | Go code review comments |
| An omitted name when the receiver is unused | `func (Order) TableName() string` |

## Common name patterns

These patterns come from the standard library. They are practice, not rules of a style guide.

| Pattern | Meaning | Examples |
|---|---|---|
| `To<Form>` | Converts a value to another form. | `strings.ToLower`, `strings.ToUpper` |
| `Parse<Type>` | Reads text. | `ParseInt`, `ParseDuration` |
| `Format<Type>` | Writes text. | `FormatInt`, `FormatFloat` |
| `Must<Name>` or `Must` | Panics on error. | `regexp.MustCompile`, `template.Must` |
| `New<Type>` | A constructor. | `NewReader`, `NewOrder` |
| `With<Option>` | A functional option, or a derived value. | `WithTimeout` and `WithLogger` as options; `context.WithTimeout` derives a context |
| Plural noun, `Values`, `Keys` | A function that returns an iterator (Go 1.23 and later). | `strings.Lines`, `slices.Values`, `maps.Keys` |
| `All` | An iterator over every item with its index or key. | `slices.All`, `maps.All` |

!!! info "See also"

    - [Languages overview](index.md) for the matrix of all languages
    - [Naming patterns](../patterns/index.md) and the [cookbook](../patterns/cookbook.md)
    - [Effective Go: names](https://go.dev/doc/effective_go#names), [Go code review comments](https://go.dev/wiki/CodeReviewComments), [Go blog: package names](https://go.dev/blog/package-names)
