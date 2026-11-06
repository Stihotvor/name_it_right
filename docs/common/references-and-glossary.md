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

### Suffixes

A reference of common suffixes with their meanings and usage examples.

#### _at
**Meaning**: Timestamp or specific point in time  
**Example**: `created_at`, `updated_at`, `expires_at`  
**Avoid**: `when` or `time` suffixes which are redundant

#### _by
**Meaning**: The entity that performed an action  
**Example**: `created_by`, `modified_by`, `processed_by`  
**Avoid**: `author` or `user` when the meaning is about who performed the action

#### _count
**Meaning**: The number of items in a collection  
**Example**: `item_count`, `error_count`, `retry_count`  
**Avoid**: Using `number` or `total` when referring to a count

#### _date
**Meaning**: A calendar date without time component  
**Example**: `birth_date`, `order_date`, `expiry_date`  
**Avoid**: `day` which is ambiguous (could mean day of month or calendar day)

#### _id
**Meaning**: Identifier for a specific entity  
**Example**: `user_id`, `order_id`, `session_id`  
**Avoid**: Bare `id` when there might be ambiguity about what is being identified

#### _index
**Meaning**: Position in an ordered sequence  
**Example**: `page_index`, `record_index`, `current_index`  
**Avoid**: `position` which is longer and less precise

#### _list
**Meaning**: A collection or array of items  
**Example**: `product_list`, `error_list`, `pending_tasks`  
**Avoid**: `array` which is implementation-specific

#### _map
**Meaning**: A key-value data structure  
**Example**: `user_map`, `settings_map`, `cache_map`  
**Avoid**: `dictionary` or `hash` which are language-specific terms

#### _total
**Meaning**: The sum of all values in a collection  
**Example**: `order_total`, `price_total`, `amount_total`  
**Avoid**: Using bare `total` without specifying what is being totaled

#### _url
**Meaning**: A uniform resource locator  
**Example**: `api_url`, `base_url`, `endpoint_url`  
**Avoid**: `link` or `address` which are less specific

### States

A reference of common states and status values for entities and processes.

#### A
| State | Meaning | Example |
|---|---|---|
| active | Currently in use or operational | account.active |
| archived | Stored for historical reference but not in active use | file.archived |
| available | Ready to be used or accessed | resource.available |

#### C
| State | Meaning | Example |
|---|---|---|
| cancelled | Intentionally stopped or terminated | order.cancelled |
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
| expired | No longer valid or effective | token.expired |
| expired_at | Timestamp when validity ended | session.expired_at |
| error | In a failed or invalid state | transaction.error |

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

#### O
| State | Meaning | Example |
|---|---|---|
| open | Available for more entries or actions | ticket.open |
| ongoing | Currently in progress | project.ongoing |
| outdated | No longer current or relevant | document.outdated |

#### P
| State | Meaning | Example |
|---|---|---|
| pending | Awaiting action or decision | payment.pending |
| processing | Currently being handled or worked on | application.processing |
| published | Made available to the public | post.published |

#### R
| State | Meaning | Example |
|---|---|---|
| rejected | Not accepted or approved | application.rejected |
| removed | Taken away but not permanently deleted | item.removed |
| resolved | Successfully addressed or fixed | issue.resolved |

#### S
| State | Meaning | Example |
|---|---|---|
| scheduled | Planned to occur at a specific time | maintenance.scheduled |
| sent | Dispatched and in transit | email.sent |
| started | Initiated and currently running | task.started |
| submitted | Presented for consideration or processing | form.submitted |

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