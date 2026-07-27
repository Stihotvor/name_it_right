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

