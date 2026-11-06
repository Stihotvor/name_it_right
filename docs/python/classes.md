!!! success "General patterns"
    
    - Use CamelCase in the class names  
    - The class represents an object with a complex, encapsulated (or not) functionality. Use nouns to reflect it.
    
!!! tip "Useful tips"  

    - Use a consistent naming convention throughout your code, so it's easy to understand and navigate. If you're 
      working on a team, agree on a naming convention to use across all your code.
    - Class names should be concise and easy to type, but also descriptive enough to convey their purpose. Avoid 
      excessively long names that are difficult to read or type. 
    - Use mnemonics: If your class name is hard to remember or pronounce, consider using a mnemonic or an acronym 
      to help people remember it. Just make sure the mnemonic or acronym is easy to understand and related to 
      the purpose of the class.
    - When choosing a class name, consider the future scalability of your code. Choose a name that can easily 
      accommodate potential future changes or additions to your code, without requiring a complete rewrite.

!!! danger "General anti-patterns"
    
    - Avoid using abbreviations in your class names, unless they are commonly understood within your domain. 
      Abbreviations can be confusing and make your code harder to read.
    - Avoid the `Manager` or `Service` suffix on every class — not every class manages something. Use precise suffixes: `Validator`, `Builder`, `Parser`, `Gateway`, `Mapper`
    - Avoid including a pattern name in the class name unless the pattern is the public API: `UserFactory` is fine; `UserSingletonFactoryProxy` is not
    - Avoid `Utils` / `Helper` classes — they are dumping grounds for unrelated logic. Split into domain-specific classes

## Suffix glossary

A suffix tells the reader the role of the class. Use a suffix only when the class really has that role. The examples use an e-commerce checkout.

| Suffix | Use it when | Example | Avoid |
|---|---|---|---|
| `Validator` | The class checks input against rules and reports problems. | `OrderValidator`, `AddressValidator` | `OrderChecker` next to `OrderValidator` |
| `Parser` | The class reads text into a structure. | `CouponCodeParser`, `PriceParser` | `PriceReader` |
| `Serializer` | The class turns an object into a transfer format and back. | `OrderSerializer`, `InvoiceSerializer` | `OrderConverter` for the same job |
| `Builder` | The class builds a complex object step by step. | `InvoiceBuilder`, `SearchQueryBuilder` | `InvoiceMaker` |
| `Factory` | The class creates objects of a family or picks the type. | `PaymentMethodFactory`, `NotifierFactory` | A factory that only calls a constructor |
| `Repository` | The class stores and loads one kind of record, like a collection. | `OrderRepository`, `CustomerRepository` | `OrderManager`, `OrderDao` in the same code base |
| `Gateway` | The class is the domain-facing entry to an external system. | `PaymentGateway`, `ShippingGateway` | `PaymentHelper` |
| `Client` | The class is the low-level caller of a remote API. | `TaxApiClient`, `CarrierApiClient` | `Client` alone |
| `Adapter` | The class implements one interface on top of another system. | `LegacyOrderAdapter`, `StripeAdapter` | `Wrapper` |
| `Mapper` | The class converts between two models. | `OrderMapper`, `AddressMapper` | `OrderUtil` |
| `Policy` | The class holds one business rule that can change. | `RefundPolicy`, `FreeShippingPolicy` | Rule flags spread over many functions |
| `Strategy` | The class is one swappable algorithm. | `FlatRateShippingStrategy`, `PercentDiscountStrategy` | `ShippingType` with `if` chains |
| `Handler` | The class receives a raw message, a webhook or a command. | `CancelOrderHandler`, `PaymentWebhookHandler` | `OrderHandler` for everything |
| `Controller` | The class receives web requests and calls the code that runs the use cases. | `OrderController`, `CartController` | A controller that holds business rules |
| `Listener` | The class reacts to one named event. | `OrderCreatedListener`, `PaymentFailedListener` | `OrderObserver` next to `OrderListener` |
| `Publisher` | The class sends events to subscribers. | `OrderEventPublisher`, `PaymentEventPublisher` | `OrderNotifier` for event publishing |
| `Provider` | The class supplies a value or a dependency on request, such as the current time or a rate. | `TaxRateProvider`, `ClockProvider` | A `Factory` that builds domain objects |
| `Registry` | The class holds named entries for lookup. | `PaymentMethodRegistry`, `HandlerRegistry` | A bare module-level dict changed from many places |
| `Resolver` | The class maps a symbolic name or key to a concrete target by rules, such as aliases or fallbacks. It is not a store: use `Repository` for records by id. | `TaxRuleResolver`, `CarrierResolver` | `Finder` |
| `Coordinator` | The class runs several collaborators in one workflow. | `CheckoutCoordinator`, `RefundCoordinator` | `CheckoutManager` |
| `Processor` | The class is a stage in a pipeline that transforms items. | `ReceiptLineProcessor`, `ImageResizeProcessor` | `Processor` for any class that has a `process` method |
| `Engine` | The class is a core component that runs complex logic by its own rules. | `PricingEngine`, `RuleEngine` | `Engine` for a small helper |
| `Job` | The class is scheduled or recurring work. Do not use both `Job` and `Task` in one code base. | `ExpireCartsJob`, `SendDigestJob` | `CartCleanup` |
| `Worker` | The class is a process or thread that runs jobs. | `EmailWorker`, `ImportWorker` | `Runner` |
| `Task` | The class is one queued unit of work. | `SendReceiptTask`, `SyncStockTask` | `Task` for a plain function |
| `Command` | The object is a request to change something. | `CancelOrderCommand`, `ApplyCouponCommand` | `CancelOrderData` |
| `Query` | The object is a request to read something. | `ListOpenOrdersQuery`, `ListRefundsQuery` | `OrderFilterData` |
| `Result` | The object is the outcome of an operation. | `RefundResult`, `ValidationResult` | A bare `tuple` |
| `Snapshot` | The object is a frozen copy at one time. | `OrderSnapshot`, `PriceSnapshot` | `Order2` |
| `Config` | The object holds the settings of one component. | `GatewayConfig`, `RetryConfig` | Both `Settings` and `Config` in one code base |
| `Options` | The object holds optional parameters of one call. | `SearchOptions`, `ExportOptions` | `Params` |
| `Context` | The object holds data shared during one call or request. | `CheckoutContext`, `RequestContext` | `Context` for any dict |
| `Session` | The object holds the state of one interaction with a start and an end. | `ShoppingSession`, `CheckoutSession` | `Session` for a user record |
| `State` | The type represents the states of a state machine. | `OrderState`, `PaymentState` | Both `Status` and `State` for the same concept in one code base |
| `Cursor` | The object marks a position in a sequence. | `OrderCursor`, `EventCursor` | `Pointer` |
| `Page` | The object is one slice of a paged result. | `OrderPage`, `ProductPage` | `OrderList` |
| `Dto` | The object carries data across a boundary and has no behaviour. | `OrderDto`, `CustomerDto` | `OrderData` |

!!! note "Acronyms in class names"

    PEP 8 asks for all letters of an acronym in capitals in CapWords, as in `HTTPServerError`, so `OrderDTO` and `TaxAPIClient` follow PEP 8. The examples on this page use `Dto`, `Api` and `Id` on purpose, for readability. Choose one form and keep it in the whole code base. See [Abbreviations](../common/abbreviations.md).

## Manager and Service

`Manager` and `Service` are the most overused suffixes. Use them with care.

| Suffix | Fine when | Better when | Examples |
|---|---|---|---|
| `Service` | The class holds domain logic that fits no entity, and the name states the domain. | The class is mostly a wrapper around one entity or one store. | `PricingService` is fine. Use `OrderRepository` for storage. |
| `Manager` | Rarely. A framework may require it. | The class has a real job. | `OrderManager` (schedules orders) → `OrderScheduler`. (Stores orders) → `OrderRepository`. (Runs the checkout steps) → `CheckoutCoordinator`. |
| `Helper`, `Util`, `Utils` | Never. | Split the class by job, or use module functions. | `OrderUtil` → module `order_rules` |

## Structural types

The base class or the decorator also shapes the name.

| Kind | Naming rule | Examples |
|---|---|---|
| `Protocol` | Name the capability. Use an adjective, an `-able` word or a `Supports` prefix. | `Refundable`, `SupportsRefund`, `Cancellable` |
| `ABC` | Use a plain noun for the contract. Avoid `Abstract` as a prefix unless the code base already uses it. | `PaymentMethod`, `ShippingCarrier` |
| `Mixin` | End the name with `Mixin`. Name the added ability. | `TimestampMixin`, `SoftDeleteMixin`, `AuditMixin` |
| `@dataclass` | Use a singular noun for the record. Add `frozen=True` for a value object. | `OrderLine`, `Address`, `Money` |
| `TypedDict` | Name the shape of the payload. | `OrderPayload`, `CouponPayload` |
| `NamedTuple` | Use a short noun for a small fixed record. | `PriceRange`, `GeoPoint` |
| `Generic` | Use a short CapWords name for a type variable, such as `T` or `KeyT`. Add `_co` or `_contra` for variance. Name the class for its job. | `T`, `OrderT`, `Repository[OrderT]` |
| `Enum` | Use a singular noun. Members are upper case. See [Enums](enums.md). | `OrderStatus`, `ShippingMethod` |
| `Exception` | End the name with `Error` (`Warning` for warnings). See [Exceptions](exceptions.md). | `PaymentDeclinedError`, `OutOfStockError` |
| `NewType` | Name the meaning of the id or the value. The string must match the name: `OrderId = NewType("OrderId", int)`. | `OrderId`, `CustomerId`, `CurrencyCode` |

!!! info "See also"

    - [Functions](functions.md) and [Class methods](class_methods.md) for the methods of these classes
    - [Variables](variables.md) for the instances
    - [Bad → better cookbook](../patterns/cookbook.md) for more rewrites
    - [Glossary](../common/references-and-glossary.md) for verbs and nouns

## Naming examples by the context or use-case

### Validation

| ──              | ──                 | ──                 | ──               |
| --------------- | ------------------ | ------------------ | ---------------- |
| Validator | InputChecker | DataVerifier | FormValidator |
| ParamValidator | RequestValidator | ModelValidator | SchemaValidator |
| InputValidator | VerificationEngine | Verifier | RuleValidator |
| IntegrityValidator | TypeChecker | ValueValidator | ValidationEngine |
| AssertionValidator | ConstraintValidator | DataIntegrityChecker | FormatValidator |

### Services / Managers

These names are common. Prefer the job-based names from the suffix glossary above where the class has a clear job.

| ──              | ──                 | ──                 | ──               |
| --------------- | ------------------ | ------------------ | ---------------- |
| OrderService | UserManager | PaymentProcessor | NotificationService |
| InventoryManager | CacheService | SyncOrchestrator | WorkflowManager |
| ReportingService | QueueManager | SessionManager | FileProcessor |
| HealthMonitor | AuditService | ImportManager | ExportService |
| EmailDispatcher | TaskScheduler | SubscriptionManager | BillingService |

### Factories / Builders

| ──              | ──                 | ──                 | ──               |
| --------------- | ------------------ | ------------------ | ---------------- |
| UserFactory | OrderFactory | PaymentGatewayFactory | ReportBuilder |
| QueryBuilder | ResponseBuilder | ConfigurationFactory | NotificationBuilder |
| ConnectionFactory | ModelFactory | SerializerFactory | ParserFactory |
| CacheBuilder | IndexBuilder | WorkflowBuilder | SchemaFactory |
| WidgetFactory | FormBuilder | TestDataFactory | ViewFactory |

### Repositories / Data access

| ──              | ──                 | ──                 | ──               |
| --------------- | ------------------ | ------------------ | ---------------- |
| UserRepository | OrderRepository | ProductRepository | CustomerRepository |
| SessionStore | CacheRepository | AuditLogStore | EventStore |
| DocumentRepository | FileRepository | ConfigRepository | MetricRepository |
| UserPreferencesStore | NotificationStore | TokenRepository | PaymentMethodRepository |

### Strategies / Policies

| ──              | ──                 | ──                 | ──               |
| --------------- | ------------------ | ------------------ | ---------------- |
| DiscountStrategy | ShippingStrategy | PaymentStrategy | PricingStrategy |
| AuthenticationStrategy | TaxCalculationStrategy | NotificationStrategy | RetryStrategy |
| EncryptionPolicy | CacheEvictionPolicy | ValidationPolicy | RateLimitPolicy |
| NamingConventionStrategy | SerializationStrategy | CompressionStrategy | RoutingStrategy |

### Controllers / Handlers

| ──              | ──                 | ──                 | ──               |
| --------------- | ------------------ | ------------------ | ---------------- |
| UserController | OrderController | PaymentController | AdminController |
| EventHandler | ExceptionHandler | RequestHandler | CommandHandler |
| WebhookController | CallbackHandler | StreamHandler | MessageHandler |
| HealthCheckController | FileUploadController | ApiGatewayController | RedirectHandler |

### DTOs / Data classes

| ──              | ──                 | ──                 | ──               |
| --------------- | ------------------ | ------------------ | ---------------- |
| UserDto | OrderRequest | PaymentResponse | CustomerProfile |
| LoginCredentials | RegistrationForm | ProductFilter | SearchResult |
| PaginationParams | SortCriteria | ApiResponse | ErrorPayload |
| ShippingAddressDto | InvoiceLineItem | SubscriptionPlan | UserPreferences |

### Adapters / Gateways / Clients

| ──              | ──                 | ──                 | ──               |
| --------------- | ------------------ | ------------------ | ---------------- |
| PaymentGatewayAdapter | StripeClient | EmailServiceAdapter | SmsGateway |
| DatabaseAdapter | FileSystemAdapter | CacheClient | HttpClient |
| LdapClient | OAuthProvider | MessageQueueAdapter | CloudStorageAdapter |
| SearchClient | MetricsCollector | ThirdPartyApiClient | FtpGateway |

### Mappers / Converters / Presenters

| ──              | ──                 | ──                 | ──               |
| --------------- | ------------------ | ------------------ | ---------------- |
| UserMapper | OrderConverter | EntityMapper | DataPresenter |
| ModelSerializer | ResponseFormatter | TypeConverter | DateFormatter |
| DocumentMapper | ObjectMapper | HtmlPresenter | JsonTransformer |
| CsvSerializer | XmlExporter | ValueConverter | StatusPresenter |

