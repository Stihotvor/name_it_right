---
status: new
---

# References and Glossary

## References

Annotated bibliography of authoritative naming sources grouped by area. Use these for specific claims and version guidance.

### Languages

| Title | Use for | URL |
|---|---|---|
| PEP 8: Python Style Guide | Python identifier conventions, including acronyms in CapWords | https://peps.python.org/pep-0008/#naming-conventions |
| Google Python Style Guide | Python naming conventions, avoiding abbreviations and descriptive names | https://google.github.io/styleguide/pyguide.html#316-naming |
| Google Java Style Guide | Java naming, constants, and privacy conventions | https://google.github.io/styleguide/javaguide.html#s5-naming |
| Kotlin Coding Conventions | Kotlin-specific naming, data classes, and coroutines | https://kotlinlang.org/docs/coding-conventions.html#naming-rules |
| .NET Design Guidelines | C#/.NET naming, PascalCase, acronym length rules, constants | https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/general-naming-conventions |
| Go Code Review Comments | Go package names, initialisms, receivers, and error strings | https://go.dev/wiki/CodeReviewComments |
| Rust API Guidelines | Rust naming conventions, conversion prefixes, and iterator names | https://rust-lang.github.io/api-guidelines/naming.html |
| Airbnb JavaScript Style Guide | JavaScript/TypeScript naming conventions, including acronyms | https://github.com/airbnb/javascript#naming-conventions |
| Swift API Design Guidelines | Swift naming, acronym casing, and protocol naming | https://www.swift.org/documentation/api-design-guidelines/#naming |

### Databases

| Title | Use for | URL |
|---|---|---|
| SQL Style Guide | SQL identifier conventions, table names, column names, and limits | https://www.sqlstyle.guide/ |
| PostgreSQL Documentation | PostgreSQL identifier length limits (63 bytes), case folding | https://www.postgresql.org/docs/current/sql-syntax-lexical.html |
| PostgreSQL "Don't Do This" | PostgreSQL-specific naming pitfalls, timestamp vs timestamptz | https://wiki.postgresql.org/wiki/Don%27t_Do_This |
| Rails Active Record | Rails table naming conventions and foreign keys | https://guides.rubyonrails.org/active_record_basics.html |
| Django Model Options | Django model naming and db_table overrides | https://docs.djangoproject.com/en/5.1/ref/models/options/ |
| dbt Project Structure | dbt layer naming, staging prefixes, and intermediate models | https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview |
| Databricks Medallion | Bronze/silver/gold layer naming conventions | https://docs.databricks.com/aws/en/lakehouse/medallion |

### APIs and Events

| Title | Use for | URL |
|---|---|---|
| Google AIP-122 | REST resource naming and resource names | https://google.aip.dev/122 |
| Google AIP-136 | REST custom methods and RPC verbs | https://google.aip.dev/136 |
| Google AIP-141 | Quantities, units, and time conventions | https://google.aip.dev/141 |
| Google AIP-158 | REST pagination with page tokens | https://google.aip.dev/158 |
| Google AIP-193 | REST error codes and ErrorInfo structure | https://google.aip.dev/193 |
| Zalando RESTful API Guidelines | REST URL conventions, kebab-case, and pagination | https://opensource.zalando.com/restful-api-guidelines/ |
| GraphQL Naming and Design | GraphQL schema and query naming conventions | https://graphql.org/learn/naming-design/ |
| GraphQL Pagination | Relay pagination conventions | https://graphql.org/learn/pagination/ |
| CloudEvents Specification | Event envelope structure and naming | https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md |
| CloudEvents Primer | Events as facts vs commands as intents | https://github.com/cloudevents/spec/blob/main/cloudevents/primer.md |
| AsyncAPI Channels | Messaging channel and topic naming | https://www.asyncapi.com/docs/concepts/channel |

### Configuration and Operations

| Title | Use for | URL |
|---|---|---|
| 12-Factor App | Environment variable and configuration naming | https://12factor.net/config |
| Kubernetes Naming | Object names, labels, and conventions | https://kubernetes.io/docs/concepts/overview/working-with-objects/names/ |
| Kubernetes Common Labels | Standard label keys and values | https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/ |
| LaunchDarkly Flag Conventions | Feature flag naming and lifecycle | https://launchdarkly.com/docs/guides/flags/flag-conventions |
| GNU Coding Standards | Command-line option conventions | https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html |
| POSIX Utility Conventions | POSIX command-line interface standards | https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap08.html |
| BEM Naming | CSS block, element, and modifier naming | https://getbem.com/naming/ |

### Domain Vocabularies

| Title | Use for | URL |
|---|---|---|
| Shopify Admin API | E-commerce entity naming and status values | https://shopify.dev/docs/api/admin-rest |
| Stripe Payment Intents | Payment entity lifecycle and state values | https://docs.stripe.com/api/payment_intents/object |
| ISO 20022 | Financial message and field naming standards | https://www.iso20022.org/iso-20022-message-definitions |
| HL7 FHIR R4 | Healthcare resource and status naming | https://hl7.org/fhir/R4/resourcelist.html |
| GS1 EPCIS | Logistics and supply chain event naming | https://www.gs1.org/standards/epcis |
| MLflow Model Registry | Machine learning experiment and model naming | https://mlflow.org/docs/latest/model-registry.html |

### Naming Research

| Title | Use for | URL |
|---|---|---|
| Naming Guidelines for Professional Programmers | Empirical studies on naming and readability | https://ppig.org/files/2017-PPIG-28th-hilton.pdf |
| How Developers Choose Names | Naming convergence and model effectiveness study | https://arxiv.org/abs/2103.07487 |
| What's in a Name? A Study of Identifiers | Description, confidence, and style studies | https://hank.feild.org/publications/icpc06-name.pdf |
| Identifier style, effort and comprehension | Eye-tracking and comprehension studies | https://ramblinations.com/hack-better-with-science/studies/2013%20-%20Impact%20of%20identifier%20style%20on%20effort%20and%20comprehension.pdf |
| kettanaito/naming-cheatsheet | Action/context patterns and prefixes | https://github.com/kettanaito/naming-cheatsheet |

## Glossary

!!! tip "See also"

    Use the verbs with [Functions](../python/functions.md) and [Class methods](../python/class_methods.md). Use the nouns and suffixes with [Classes](../python/classes.md) and [Variables](../python/variables.md). Test names follow the same words: see [Tests](../python/tests.md).

### Verbs

A curated reference of action verbs for naming functions, methods, and operations. Pick a verb and pair it with a domain noun — `add_order()`, `validate_email()`, `to_json()`, `from_row()`.

#### A
| Verb | Meaning | Example name |
|---|---|---|
| accept | Take or receive something offered | accept_invitation() |
| access | Gain entry to or use of something | access_database() |
| acquire | Obtain something, especially after an effort | acquire_lock() |
| activate | Make something active or operational | activate_account() |
| add | Bring together or unite to increase the number, quantity, or importance | add_item() |
| adjust | Alter or move something slightly to achieve the desired fit or result | adjust_brightness() |
| aggregate | Collect into a mass or whole | aggregate_sales() |
| alert | Warn or notify about a problem or danger | alert_admin() |
| align | Place or arrange things in a straight line or in a proper position | align_text() |
| allocate | Distribute or assign for a particular purpose | allocate_resources() |
| analyze | Examine methodically and in detail the constitution or structure of | analyze_pattern() |
| append | Add something to the end of a document or piece of data | append_data() |
| apply | Put into operation or effect | apply_discount() |
| archive | Move data to long-term storage | archive_records() |
| arrange | Organize or put in order | arrange_columns() |
| assign | Allocate or distribute a task or responsibility | assign_task() |
| associate | Connect someone or something with something else in memory or imagination | associate_tag() |
| attach | Fasten, join, or connect something to something else | attach_file() |
| attempt | Make an effort to achieve or complete something | authenticate_user() |
| audit | Conduct a systematic examination of books, accounts, or records | audit_log() |
| authenticate | Verify the identity of a user or system | authenticate_request() |
| authorize | Give official permission or approval to | authorize_payment() |
| average | Calculate the mean value of a set of numbers | average_score() |

#### B
| Verb | Meaning | Example name |
|---|---|---|
| backup | Create a duplicate copy for safety or recovery | backup_database() |
| balance | Make or keep things in a steady state | balance_load() |
| batch | Process multiple items as a single group | batch_insert() |
| bind | Tie together or hold together | bind_values() |
| block | Prevent something from happening or progressing | block_user() |
| bootstrap | Start a system or process that initializes other parts | bootstrap_app() |
| borrow | Take and use something with the intention of returning it | borrow_resource() |
| branch | Split into different directions or paths | branch_logic() |
| broadcast | Send out a message or signal to multiple recipients | broadcast_event() |
| browse | Look through or examine something casually | browse_directory() |
| buffer | Temporarily store data to balance processing rates | buffer_stream() |
| build | Construct or create something by putting parts together | build_query() |
| bundle | Combine items into a single package or unit | bundle_products() |
| burn | Process or destroy data intentionally | burn_image() |
| bypass | Go around or avoid a particular step or obstacle | bypass_cache() |

#### C
| Verb | Meaning | Example name |
|---|---|---|
| cache | Store duplicate copies of data for faster access | cache_response() |
| calculate | Determine a result by mathematical or logical means | calculate_total() |
| cancel | Decide or announce that an arranged event will not take place | cancel_order() |
| capture | Take into one's possession or control | capture_output() |
| cast | Convert one data type to another | cast_to_int() |
| catch | Intercept and handle an exception or error | catch_exception() |
| check | Examine or test something to ensure it meets requirements | check_status() |
| clean | Remove unwanted elements or make something orderly | clean_data() |
| clear | Make something empty or free from obstruction | clear_cache() |
| clone | Make an exact copy of something | clone_repository() |
| close | Shut down or end a connection or process | close_connection() |
| collect | Gather or bring together things from different sources | collect_feedback() |
| combine | Join or mix together to form a single entity | combine_datasets() |
| commit | Save changes permanently to a repository or database | commit_transaction() |
| compare | Examine the similarities and differences between | compare_versions() |
| compile | Translate source code into machine code or an executable | compile_code() |
| complete | Bring to an end or fulfill all requirements | complete_task() |
| compose | Create something by combining different parts | compose_message() |
| compute | Calculate or determine something mathematically | compute_average() |
| configure | Set up or arrange the parts of a system or process | configure_system() |
| connect | Join or establish a relationship or communication link | connect_database() |
| consume | Use up or absorb resources or data | consume_api() |
| convert | Change from one form, purpose, or use to another | convert_currency() |
| copy | Create a duplicate of something | copy_file() |
| count | Determine the number of elements in a collection | count_items() |
| create | Bring something into existence or make something new | create_user() |

#### D
| Verb | Meaning | Example name |
|---|---|---|
| deactivate | Make something inactive or no longer functional | deactivate_account() |
| debug | Find and remove errors from a program or system | debug_code() |
| decrypt | Convert encoded data back to its original form | decrypt_message() |
| deduplicate | Remove duplicate entries from a collection | deduplicate_list() |
| default | Provide a fallback value when no other is specified | default_setting() |
| define | State or describe the nature, scope, or meaning of | define_schema() |
| delete | Remove something permanently | delete_record() |
| derive | Obtain something from a source or origin | derive_key() |
| deserialize | Convert a serialized format back to an object | deserialize_json() |
| destroy | Cause to be destroyed or no longer exist | destroy_session() |
| detach | Separate or unconnect something from something else | detach_resource() |
| detect | Discover or identify the presence of something | detect_anomaly() |
| disable | Make something inactive or unable to function | disable_feature() |
| disconnect | Break the connection between two systems or components | disconnect_network() |
| discover | Find something previously unknown or unseen | discover_services() |
| dispatch | Send a message or item to a destination | dispatch_event() |
| display | Show or present something on a screen or interface | display_results() |
| dispose | Get rid of something no longer needed | dispose_connection() |
| distribute | Scatter or spread over a wide area or to multiple recipients | distribute_tasks() |
| download | Transfer data from a remote system to a local one | download_file() |
| drain | Remove gradually or completely | drain_pool() |
| draw | Pull or cause to move in a particular direction | draw_sample() |
| drop | Remove an element from a collection or database | drop_column() |
| dump | Write the full content of data to an external location | dump_database() |

#### E
| Verb | Meaning | Example name |
|---|---|---|
| emit | Send out a signal or event to listeners | emit_event() |
| encode | Convert data into another representation | encode_payload() |
| enqueue | Add an item to the end of a queue | enqueue_job() |
| evaluate | Determine the value or outcome of an expression or rule | evaluate_policy() |
| execute | Carry out a command, plan, or query | execute_query() |
| export | Write data out of the system in an external format | export_report() |
| extract | Pull a part out of a larger whole | extract_fields() |

#### F
| Verb | Meaning | Example name |
|---|---|---|
| fetch | Retrieve data from a remote or slow source | fetch_customer_orders() |
| filter | Keep only the items that match a condition | filter_active_users() |
| find | Look for an item and return it, or nothing if it is absent | find_user_by_email() |
| flush | Force buffered data to be written or cleared | flush_buffer() |
| format | Arrange data into a defined textual layout | format_address() |

#### G
| Verb | Meaning | Example name |
|---|---|---|
| generate | Produce new data or an artifact from rules or input | generate_invoice() |
| get | Return a value that is already available in memory | get_total() |
| group | Collect items that share a key into sets | group_orders_by_status() |

#### H
| Verb | Meaning | Example name |
|---|---|---|
| handle | Respond to an event, request, or error | handle_payment_failed() |
| hash | Compute a fixed-size digest of data | hash_password() |

#### I
| Verb | Meaning | Example name |
|---|---|---|
| import | Bring data into the system from an external source | import_products() |
| increment | Increase a number by a step, usually one | increment_retry_count() |
| initialize | Set something to its starting state | initialize_cache() |
| inject | Supply a dependency or value from outside | inject_clock() |
| insert | Put an item at a specific position or in a store | insert_row() |
| invalidate | Mark data as no longer valid | invalidate_session() |

#### J
| Verb | Meaning | Example name |
|---|---|---|
| join | Combine two sources on a shared key or separator | join_tables() |

#### L
| Verb | Meaning | Example name |
|---|---|---|
| list | Return a collection of items, possibly paged | list_active_discounts() |
| load | Read stored data into memory | load_settings() |
| lock | Prevent concurrent access to a resource | lock_account() |
| log | Write a record of an event for later review | log_error() |

#### M
| Verb | Meaning | Example name |
|---|---|---|
| map | Transform each item or convert one shape into another | map_row_to_order() |
| mark | Set a flag or state on an item | mark_as_read() |
| merge | Combine several items into one | merge_profiles() |
| migrate | Move data or schema to a new version or place | migrate_schema() |

#### N
| Verb | Meaning | Example name |
|---|---|---|
| normalize | Convert values to one standard form | normalize_phone_number() |
| notify | Tell a user or system that something happened | notify_customer() |

#### O
| Verb | Meaning | Example name |
|---|---|---|
| open | Start access to a resource | open_connection() |

#### P
| Verb | Meaning | Example name |
|---|---|---|
| parse | Read text and turn it into structured data | parse_date() |
| patch | Apply a partial update to an existing item | patch_profile() |
| poll | Check a source repeatedly for changes | poll_status() |
| process | Run an item through a series of steps | process_payment() |
| publish | Make something available to subscribers or readers | publish_message() |
| purge | Remove all items permanently | purge_expired_sessions() |
| push | Send data to a remote destination or add to the end of a stack | push_notification() |

#### Q
| Verb | Meaning | Example name |
|---|---|---|
| query | Ask a data store for matching records | query_orders() |

#### R
| Verb | Meaning | Example name |
|---|---|---|
| read | Get data from a file, stream, or device | read_config() |
| refresh | Update a value or token with fresh data | refresh_token() |
| register | Record an entity so the system knows it | register_handler() |
| release | Give back a held resource | release_lock() |
| render | Produce visible output from a template or model | render_template() |
| replace | Substitute one item with another | replace_item() |
| reset | Return something to its initial state | reset_password() |
| resolve | Find the concrete target for a reference or name | resolve_dependency() |
| restore | Bring something back to an earlier state | restore_backup() |
| retry | Run an operation again after a failure | retry_request() |
| revoke | Withdraw a permission, token, or grant | revoke_access() |
| rollback | Undo changes made in a transaction | rollback_transaction() |
| run | Start and carry out a task or program | run_migrations() |

#### S
| Verb | Meaning | Example name |
|---|---|---|
| save | Write an item to persistent storage | save_draft() |
| schedule | Plan an action for a later time | schedule_report() |
| search | Look for items that match free-form criteria | search_products() |
| select | Choose one or more items from options | select_shipping_method() |
| send | Transmit a message to a recipient | send_receipt() |
| serialize | Convert an object into a storable or transmittable form | serialize_order() |
| set | Assign a value to a property | set_timeout_seconds() |
| sort | Put items in order | sort_by_date() |
| split | Divide something into parts | split_name() |
| start | Begin running a process or task | start_worker() |
| stop | End a running process or task | stop_worker() |
| store | Keep data in a place for later use | store_attachment() |
| subscribe | Register to receive future events | subscribe_to_topic() |
| sync | Make two sources hold the same data | sync_inventory() |

#### T
| Verb | Meaning | Example name |
|---|---|---|
| toggle | Switch between two states | toggle_feature_flag() |
| track | Record progress or occurrences over time | track_shipment() |
| transform | Change data from one form to another | transform_payload() |
| trigger | Cause an action to begin | trigger_webhook() |
| trim | Remove unwanted edges from a value | trim_whitespace() |

#### U
| Verb | Meaning | Example name |
|---|---|---|
| unlock | Allow access to something that was locked | unlock_account() |
| update | Change an existing item with new data | update_shipping_address() |
| upload | Transfer data from a local system to a remote one | upload_avatar() |
| upsert | Update an item if it exists, otherwise insert it | upsert_customer() |

#### V
| Verb | Meaning | Example name |
|---|---|---|
| validate | Check that data meets the rules and report problems | validate_email() |
| verify | Confirm that a claim is true | verify_signature() |

#### W
| Verb | Meaning | Example name |
|---|---|---|
| wait | Pause until a condition is met | wait_for_job() |
| watch | Observe a source and react to changes | watch_directory() |
| write | Put data into a file, stream, or device | write_log() |

### Nouns

A reference of entity nouns for naming classes, tables, variables, and data structures.

#### A
| Noun | Meaning | Example name |
|---|---|---|
| account | A record of financial transactions or a personal user record | user_account |
| address | A place where someone lives or an electronic destination | shipping_address |
| aggregation | A collection of items grouped together | order_aggregation |
| algorithm | A process or set of rules to be followed in calculations or problem-solving operations | sort_algorithm |
| api | Application Programming Interface for software communication | payment_api |
| application | A program or software designed for a specific purpose | web_application |
| array | A data structure that contains a group of elements | message_array |
| artifact | A tangible byproduct of development or a deliverable | build_artifact |
| attribute | A quality or feature regarded as a characteristic of something | user_attribute |
| audit | A systematic inspection or examination of records | audit_log |

#### B
| Noun | Meaning | Example name |
|---|---|---|
| batch | A group of items processed together | payment_batch |
| buffer | A temporary storage area for data | output_buffer |
| bundle | A package of items sold together | service_bundle |
| business | An organization or commercial enterprise | business_rule |

#### C
| Noun | Meaning | Example name |
|---|---|---|
| cache | A hardware or software component that stores data for faster access | request_cache |
| calculation | A mathematical result or the process of computing it | tax_calculation |
| catalog | A complete list of items, typically arranged systematically | product_catalog |
| client | A computer or program that requests services from another program or computer | api_client |
| collection | A group of items that can be treated as a single entity | order_collection |
| command | An instruction given to a computer program or system | delete_command |
| component | A part or element of a larger system | ui_component |
| configuration | The arrangement of parts or elements in something | app_configuration |
| connection | A relationship or link between two things | database_connection |
| context | The circumstances or surrounding information | request_context |
| contract | A formal agreement between parties | service_contract |
| controller | A mechanism that controls or regulates the operation of a machine | traffic_controller |
| credential | A qualification or achievement that provides access to privilege | user_credential |
| cursor | A movable indicator on a screen showing the position where input will appear | database_cursor |

#### D
| Noun | Meaning | Example name |
|---|---|---|
| dataset | A named collection of related data | training_dataset |
| dependency | Something another component needs in order to work | service_dependency |
| deployment | A release of software to an environment | production_deployment |
| document | A self-contained unit of stored content | invoice_document |

#### E
| Noun | Meaning | Example name |
|---|---|---|
| endpoint | A network address where a service accepts requests | payment_endpoint |
| entity | A thing with its own identity in the domain | customer_entity |
| environment | A place where software runs, such as staging | staging_environment |
| error | A failure or invalid result | validation_error |
| event | A fact that happened at a point in time | order_created_event |

#### F
| Noun | Meaning | Example name |
|---|---|---|
| factory | An object that creates other objects | order_factory |
| feature | A distinct capability of a product | feature_flag |
| field | A named piece of data in a record | email_field |

#### G
| Noun | Meaning | Example name |
|---|---|---|
| gateway | A point that connects to an external system | payment_gateway |
| group | A set of items that belong together | user_group |

#### H
| Noun | Meaning | Example name |
|---|---|---|
| handler | Code that responds to an event or request | error_handler |
| history | A record of past changes | order_history |

#### I
| Noun | Meaning | Example name |
|---|---|---|
| identifier | A value that names one item uniquely | external_identifier |
| index | A position in a sequence or a lookup structure | search_index |
| instance | One concrete object of a class or service | server_instance |
| invoice | A bill that lists goods or services and the amount due | customer_invoice |

#### J
| Noun | Meaning | Example name |
|---|---|---|
| job | A unit of work that runs in the background | export_job |

#### K
| Noun | Meaning | Example name |
|---|---|---|
| key | A value that identifies an item or unlocks access | api_key |

#### L
| Noun | Meaning | Example name |
|---|---|---|
| layer | A level in a layered design | storage_layer |
| ledger | An append-only record of financial entries | payment_ledger |
| limit | A maximum allowed value | rate_limit |

#### M
| Noun | Meaning | Example name |
|---|---|---|
| message | A unit of data sent between parties | email_message |
| metric | A measured value tracked over time | latency_metric |
| migration | A scripted change to a schema or data | schema_migration |
| model | A representation of a domain concept | order_model |
| module | A file or unit of code with a clear purpose | billing_module |

#### N
| Noun | Meaning | Example name |
|---|---|---|
| notification | A message that tells a user something happened | push_notification |

#### O
| Noun | Meaning | Example name |
|---|---|---|
| operation | A single action that the system performs | refund_operation |
| option | A choice that changes behaviour | retry_option |
| order | A request to buy goods or services | customer_order |

#### P
| Noun | Meaning | Example name |
|---|---|---|
| package | A distributable bundle of code or goods | shipping_package |
| page | A slice of results or a screen in a UI | result_page |
| parameter | An input value that changes how something works | query_parameter |
| payload | The data carried by a request or message | webhook_payload |
| payment | A transfer of money for goods or services | card_payment |
| permission | Approval to perform an action | write_permission |
| pipeline | A chain of steps that process data in order | build_pipeline |
| policy | A set of rules that guide decisions | retention_policy |
| profile | A set of attributes that describe a user or setting | user_profile |
| provider | A component that supplies a service or value | identity_provider |

#### Q
| Noun | Meaning | Example name |
|---|---|---|
| query | A request for data from a store | search_query |
| queue | An ordered list where items wait for processing | email_queue |

#### R
| Noun | Meaning | Example name |
|---|---|---|
| record | One row or entry in a data store | audit_record |
| repository | A component that stores and loads entities | order_repository |
| request | A call that asks a service to do something | http_request |
| resource | A thing that a service exposes by name | order_resource |
| response | The answer to a request | api_response |
| result | The outcome of an operation | search_result |
| role | A named set of permissions | admin_role |
| route | A path that maps a request to a handler | checkout_route |

#### S
| Noun | Meaning | Example name |
|---|---|---|
| schema | A formal description of structure | database_schema |
| secret | A confidential value such as a password | client_secret |
| service | A component that offers a defined capability | billing_service |
| session | A period of connected interaction | user_session |
| setting | A value that configures behaviour | notification_setting |
| snapshot | A copy of state at a point in time | inventory_snapshot |
| source | The place where data comes from | data_source |
| subscription | A recurring agreement or a registration for events | monthly_subscription |

#### T
| Noun | Meaning | Example name |
|---|---|---|
| task | A small piece of work to be done | cleanup_task |
| template | A pattern used to produce similar items | email_template |
| tenant | A customer organization in a shared system | tenant_id |
| token | A value that proves identity or access | access_token |
| transaction | A group of operations that succeed or fail together | payment_transaction |

#### U
| Noun | Meaning | Example name |
|---|---|---|
| user | A person who uses the system | active_user |

#### V
| Noun | Meaning | Example name |
|---|---|---|
| version | A numbered state of something that changes | api_version |

#### W
| Noun | Meaning | Example name |
|---|---|---|
| webhook | An HTTP callback that a service sends when an event happens | payment_webhook |
| worker | A process that executes jobs | queue_worker |
| workflow | A defined sequence of steps for a business process | approval_workflow |

### Suffixes

A reference of common suffixes with their meanings and usage examples.

#### _at
**Meaning**: Timestamp or specific point in time<br>
**Example**: `created_at`, `updated_at`, `expires_at`<br>
**Avoid**: `when` or `time` suffixes which are redundant

#### _by
**Meaning**: The entity that performed an action<br>
**Example**: `created_by`, `modified_by`, `processed_by`<br>
**Avoid**: `author` or `user` when the meaning is about who performed the action

#### _bytes
**Meaning**: A size measured in bytes<br>
**Example**: `file_size_bytes`, `payload_bytes`, `memory_limit_bytes`<br>
**Avoid**: `size` alone, which hides the unit

#### _cents
**Meaning**: A money amount in the smallest currency unit<br>
**Example**: `price_cents`, `refund_cents`, `fee_cents`<br>
**Avoid**: Float amounts such as `price` with no unit

#### _code
**Meaning**: A short coded value from a fixed set<br>
**Example**: `country_code`, `error_code`, `currency_code`<br>
**Avoid**: `type` when the value is a code

#### _count
**Meaning**: The number of items in a collection<br>
**Example**: `item_count`, `error_count`, `retry_count`<br>
**Avoid**: Using `number` or `total` when referring to a count

#### _date
**Meaning**: A calendar date without time component<br>
**Example**: `birth_date`, `order_date`, `expiry_date`<br>
**Avoid**: `day` which is ambiguous (could mean day of month or calendar day)

#### _days
**Meaning**: A duration in days<br>
**Example**: `retention_days`, `trial_days`, `grace_days`<br>
**Avoid**: `duration` or `period` with no unit

#### _hash
**Meaning**: A digest of other data<br>
**Example**: `password_hash`, `content_hash`, `commit_hash`<br>
**Avoid**: `checksum` unless it is a real checksum

#### _hours
**Meaning**: A duration in hours<br>
**Example**: `valid_hours`, `ttl_hours`, `sla_hours`<br>
**Avoid**: `hours` alone for a duration

#### _id
**Meaning**: Identifier for a specific entity<br>
**Example**: `user_id`, `order_id`, `session_id`<br>
**Avoid**: Bare `id` when there might be ambiguity about what is being identified

#### _ids
**Meaning**: A collection of identifiers<br>
**Example**: `order_ids`, `user_ids`, `parent_ids`<br>
**Avoid**: `id_list` which repeats `_list`

#### _index
**Meaning**: Position in an ordered sequence<br>
**Example**: `page_index`, `record_index`, `current_index`<br>
**Avoid**: `position` which is longer and less precise

#### _key
**Meaning**: A value that identifies or looks up an item<br>
**Example**: `api_key`, `cache_key`, `partition_key`<br>
**Avoid**: `id` when the value is a lookup key

#### _limit
**Meaning**: A maximum that the system enforces<br>
**Example**: `rate_limit`, `size_limit`, `retry_limit`<br>
**Avoid**: `max` when the system rejects values above it

#### _list
**Meaning**: A collection or array of items<br>
**Example**: `product_list`, `error_list`, `pending_tasks`<br>
**Avoid**: `array` which is implementation-specific

#### _map
**Meaning**: A key-value data structure<br>
**Example**: `user_map`, `settings_map`, `cache_map`<br>
**Avoid**: `dictionary` or `hash` which are language-specific terms

#### _max
**Meaning**: The highest allowed or observed value<br>
**Example**: `retry_max`, `price_max`, `length_max`<br>
**Avoid**: `high` or `top`

#### _min
**Meaning**: The lowest allowed or observed value<br>
**Example**: `price_min`, `length_min`, `age_min`<br>
**Avoid**: `low` or `bottom`

#### _minutes
**Meaning**: A duration in minutes<br>
**Example**: `timeout_minutes`, `lock_minutes`, `delay_minutes`<br>
**Avoid**: `mins` or bare `minutes`

#### _ms
**Meaning**: A duration in milliseconds<br>
**Example**: `latency_ms`, `timeout_ms`, `elapsed_ms`<br>
**Avoid**: `time` or `delay` with no unit

#### _name
**Meaning**: A human-readable label<br>
**Example**: `first_name`, `file_name`, `team_name`<br>
**Avoid**: `title` or `label` for the same meaning in one codebase

#### _path
**Meaning**: A location in a file system or tree<br>
**Example**: `config_path`, `output_path`, `json_path`<br>
**Avoid**: `url` when the value is not a URL

#### _percent
**Meaning**: A value from 0 to 100<br>
**Example**: `discount_percent`, `cpu_percent`, `fill_percent`<br>
**Avoid**: `rate` or `pct` when the scale is unclear

#### _rate
**Meaning**: A quantity per unit of time or per base amount<br>
**Example**: `error_rate`, `tax_rate`, `sample_rate`<br>
**Avoid**: `ratio` when the value is a rate

#### _ratio
**Meaning**: A value from 0 to 1 that compares two quantities<br>
**Example**: `hit_ratio`, `discount_ratio`, `fail_ratio`<br>
**Avoid**: `percent` when the scale is 0 to 1

#### _seconds
**Meaning**: A duration in seconds<br>
**Example**: `timeout_seconds`, `ttl_seconds`, `interval_seconds`<br>
**Avoid**: `timeout` alone, which hides the unit

#### _size
**Meaning**: The number of elements or the capacity<br>
**Example**: `page_size`, `batch_size`, `pool_size`<br>
**Avoid**: `length` or `count` when it means capacity

#### _status
**Meaning**: The current state of a process or entity<br>
**Example**: `payment_status`, `order_status`, `sync_status`<br>
**Avoid**: `state` and `status` mixed in one codebase

#### _total
**Meaning**: The sum of all values in a collection<br>
**Example**: `order_total`, `price_total`, `amount_total`<br>
**Avoid**: Using bare `total` without specifying what is being totaled

#### _type
**Meaning**: The kind of an item from a fixed set<br>
**Example**: `event_type`, `account_type`, `media_type`<br>
**Avoid**: `kind` and `type` mixed in one codebase

#### _url
**Meaning**: A uniform resource locator<br>
**Example**: `api_url`, `base_url`, `endpoint_url`<br>
**Avoid**: `link` or `address` which are less specific

#### _uuid
**Meaning**: A universally unique identifier<br>
**Example**: `request_uuid`, `session_uuid`, `trace_uuid`<br>
**Avoid**: `_id` when the format is a UUID and the format matters

#### _version
**Meaning**: A numbered revision<br>
**Example**: `schema_version`, `api_version`, `app_version`<br>
**Avoid**: `rev` or `ver`

### States

A reference of common states and status values for entities and processes.

#### A
| State | Meaning | Example |
|---|---|---|
| active | Currently in use or operational | account.active |
| approved | Accepted by an authorized person | request.approved |
| archived | Stored for historical reference but not in active use | file.archived |
| available | Ready to be used or accessed | resource.available |

#### B
| State | Meaning | Example |
|---|---|---|
| blocked | Prevented from proceeding | account.blocked |

#### C
| State | Meaning | Example |
|---|---|---|
| cancelled | Intentionally stopped or terminated | order.cancelled |
| closed | Finished and no longer accepting changes | ticket.closed |
| completed | Finished and all requirements met | task.completed |
| confirmed | Verified and approved | booking.confirmed |
| created | Successfully brought into existence | user.created |

#### D
| State | Meaning | Example |
|---|---|---|
| deleted | Removed permanently | record.deleted |
| deprecated | No longer recommended for use but still available | api.deprecated |
| disabled | Turned off and not functional | feature.disabled |
| draft | Incomplete work not yet ready for use | article.draft |

#### E
| State | Meaning | Example |
|---|---|---|
| error | In a failed or invalid state | transaction.error |
| expired | No longer valid or effective | token.expired |
| expired_at | Timestamp when validity ended | session.expired_at |

#### F
| State | Meaning | Example |
|---|---|---|
| failed | Did not complete successfully | job.failed |
| fulfilled | Request or obligation met | order.fulfilled |
| future | Scheduled or planned for later | appointment.future |

#### I
| State | Meaning | Example |
|---|---|---|
| inactive | Not in active use or operation | account.inactive |
| invalid | Does not meet requirements or constraints | token.invalid |
| invoked | Called or triggered for execution | function.invoked |

#### L
| State | Meaning | Example |
|---|---|---|
| locked | Protected from changes or access | account.locked |

#### O
| State | Meaning | Example |
|---|---|---|
| ongoing | Currently in progress | project.ongoing |
| open | Available for more entries or actions | ticket.open |
| outdated | No longer current or relevant | document.outdated |

#### P
| State | Meaning | Example |
|---|---|---|
| paid | Payment was received in full | invoice.paid |
| paused | Temporarily stopped and able to resume | subscription.paused |
| pending | Awaiting action or decision | payment.pending |
| processing | Currently being handled or worked on | application.processing |
| published | Made available to the public | post.published |

#### Q
| State | Meaning | Example |
|---|---|---|
| queued | Waiting in line to be processed | job.queued |

#### R
| State | Meaning | Example |
|---|---|---|
| refunded | Money was returned to the payer | payment.refunded |
| rejected | Not accepted or approved | application.rejected |
| removed | Taken away but not permanently deleted | item.removed |
| resolved | Successfully addressed or fixed | issue.resolved |

#### S
| State | Meaning | Example |
|---|---|---|
| scheduled | Planned to occur at a specific time | maintenance.scheduled |
| sent | Dispatched and in transit | email.sent |
| shipped | Handed over to a carrier | order.shipped |
| started | Initiated and currently running | task.started |
| submitted | Presented for consideration or processing | form.submitted |
| suspended | Stopped for a reason and not yet ended | account.suspended |

#### U
| State | Meaning | Example |
|---|---|---|
| unavailable | Not ready or accessible for use | service.unavailable |
| updated | Modified with new information | profile.updated |
| used | Consumed or applied | coupon.used |

#### V
| State | Meaning | Example |
|---|---|---|
| valid | Meets all requirements and is acceptable | token.valid |
| voided | Made legally invalid or cancelled | contract.voided |
