# Functions

!!! success "General patterns"

    - Use `snake_case` in function names ONLY. Don't look at some bad examples, even if they have 1k+ stars on GitHub
    - Functions which validate or check something and return boolean should start with `is_`, `has_`: `has_tax_applied()`, `is_valid()`
    - Functions not covered by the above rule should have executable names: `compile()`, `collect()`, `process()`, `fetch()`
    - If the function has `and` in the name, there is a high chance it does multiple things. Split it.
    - Name CRUD functions after the resource and action: `create_order()`, `list_customer_orders()`, `update_shipping_address()`, `delete_expired_carts()`
    - Name query functions by what they return: `list_pending_payments()`, `find_user_by_email()`, `search_products()`, `list_active_discounts()`
    - Name action functions by the side effect: `apply_discount_to()`, `refund_payment()`, `cancel_subscription()`, `dispatch_order()`
    - Use domain vocabulary consistently — if you say `fetch` throughout, never mix in `retrieve` or `get` for the same operation

    ```py
    # E-commerce function naming in practice
    def calculate_order_total(order_id: int) -> Decimal:
        ...

    def apply_promo_discount(order: Order, code: str) -> Order:
        ...

    def send_order_confirmation_email(user_email: str, order: Order) -> bool:
        ...

    def is_product_in_stock(sku: str) -> bool:
        ...

    def refund_line_item(transaction_id: str, amount: Decimal) -> RefundReceipt:
        ...
    ```

!!! tip "Useful tips"

    - Good function arguments can help to shorten the function name: `add_car_to_catalog(name: str)` → `add_car_to(catalog: Catalog)`
    - Pick one verb per operation and never mix. If the codebase uses `fetch_` for remote reads, use `fetch_` for all remote reads — no `retrieve_`.
    - Use the module name to shorten function names:
    ```py
    # Before
    from food import create_french_fries

    create_french_fries()
    ...

    # After
    from food import france

    france.create_fries()
    ...

    # Or even shorter
    from food.france import create_fries

    create_fries()
    ...
    ```

!!! danger "General anti-patterns"

    - Abbreviations: `compile_frst()`
    - One-letter functions: `v()`

## Verb families

Choose one verb per operation and keep it in the whole code base. The tables group the verbs by the job they do. For the word order inside a name, see [Action and context](../patterns/action-context.md). For more verbs, see the [Glossary](#glossary) below and the [master glossary](../common/references-and-glossary.md).

### Query

| Verb | Use it when | Examples |
|---|---|---|
| `get` | You read data from memory or by a cheap lookup. It raises an error if the item is missing, unlike `dict.get`. | `get_order`, `get_user_email`, `get_order_total` (a stored value) |
| `find` | You return one item by key or criteria, or `None`. No result is a normal answer. | `find_user_by_email`, `find_product_by_sku`, `find_open_cart` |
| `list` | You return a collection, often filtered or paged. | `list_open_orders`, `list_active_discounts`, `list_user_addresses` |
| `fetch` | You read over a network or from a slow API. | `fetch_exchange_rates`, `fetch_carrier_tracking`, `fetch_customer_profile` |
| `load` | You read stored data from a file or a database into memory. | `load_cart`, `load_pricing_rules`, `load_tax_table` |
| `search` | You return many matches, possibly ranked, as a list. | `search_products`, `search_orders_by_note` |
| `count` | You return the number of matches. | `count_open_orders`, `count_unread_notices` |

One rule decides between the read verbs: `get` for memory or a cheap lookup, `load` for local storage, `fetch` for a network or a slow API. Do not use `get_` and `fetch_` for the same operation.

### Command

| Verb | Use it when | Examples |
|---|---|---|
| `create` | You make a new record. | `create_order`, `create_refund`, `create_shipment` |
| `update` | You change a record. | `update_shipping_address`, `update_cart_item`, `update_payment_method` |
| `save` | You persist a record, new or changed. It pairs with `load`. | `save_order`, `save_cart`, `save_user` |
| `delete` | You remove a record. | `delete_expired_carts`, `delete_draft_order`, `delete_saved_card` |
| `cancel` | You stop a planned or running operation. | `cancel_order`, `cancel_subscription`, `cancel_shipment` |
| `send` | You cause a message to go out. | `send_receipt_email`, `send_shipping_notice`, `send_payment_reminder` |
| `apply` | You put a rule or an effect on data. | `apply_coupon`, `apply_tax_rule`, `apply_shipping_discount` |
| `refund` | You give money back. | `refund_payment`, `refund_line_item`, `refund_shipping` |

### Boolean

| Prefix | Use it when | Examples |
|---|---|---|
| `is_` | You check a state. | `is_cart_empty`, `is_order_paid`, `is_in_stock` |
| `has_` | You check ownership. | `has_discount`, `has_saved_card`, `has_open_order` |
| `can_` | You check ability or permission. | `can_cancel_order`, `can_refund_payment`, `can_ship_express` |
| `should_` | You check a decision. | `should_retry_payment`, `should_send_receipt` |
| `must_` | You check a requirement. | `must_validate_address`, `must_accept_terms` |

For all boolean prefixes, including `was_`, `will_` and `allows_`, see [Booleans, collections, units and time](../patterns/booleans-collections-units-time.md).

### Conversion

| Pattern | Use it when | Examples |
|---|---|---|
| `<source>_to_<target>` | You convert one shape to another. | `order_to_invoice`, `cents_to_decimal`, `cart_to_order` |
| `to_<target>` | A method converts its own object. | `order.to_dict`, `money.to_decimal`, `address.to_label` |
| `from_<source>` | A class method builds an object. | `Order.from_cart`, `Money.from_cents`, `Address.from_dict` |
| `parse_<thing>` | You read text into a structure. | `parse_coupon_code`, `parse_delivery_date`, `parse_price` |
| `format_<thing>` | You write a structure as text. | `format_price`, `format_address`, `format_tracking_number` |
| `serialize` / `deserialize` | You convert to and from a transfer format. | `serialize_order`, `deserialize_order` |

### Lifecycle

| Verb | Use it when | Examples |
|---|---|---|
| `open` / `close` | You acquire and release a resource, as a pair. | `open_session`, `close_session`, `open_connection` |
| `start` / `stop` | You run a process. | `start_worker`, `stop_worker`, `start_scheduler` |
| `pause` / `resume` | A process continues later. | `pause_subscription`, `resume_subscription` |
| `initialize` | You set up state before first use. `setup` overlaps, so keep one of the two. | `initialize_cart`, `initialize_gateway` |
| `reset` | You return to the initial state. | `reset_cart`, `reset_retry_count` |
| `dispose` | You free what an object owns, with no matching `open`. Where there is an `open`, use `close`. | `dispose_connection_pool`, `dispose_temp_files` |

### Event handler

| Pattern | Use it when | Examples |
|---|---|---|
| `on_<owner>_<event>` | The callback for one named event. | `on_order_created`, `on_payment_failed`, `on_cart_expired` |
| `handle_<source>` | An entry point receives a raw message, such as a webhook or a queue message, and calls the `on_` functions. | `handle_payment_webhook`, `handle_refund_message` |
| `emit_<event>` | You publish an event. | `emit_order_created`, `emit_payment_captured` |
| `subscribe_to_<topic>` | You register for events. | `subscribe_to_orders`, `subscribe_to_refunds` |

### Validation

| Verb | Use it when | Examples |
|---|---|---|
| `validate` | You read the input and return or raise a list of problems. It never changes state. | `validate_order`, `validate_address`, `validate_coupon` |
| `verify` | You confirm that a claim is genuine and raise if it is not. A boolean form is `is_signature_valid`. | `verify_signature`, `verify_email_token`, `verify_webhook_secret` |
| `ensure` | You raise on the first failure of a condition that must hold. It does not repair anything. | `ensure_cart_has_items`, `ensure_stock_available` |
| `check` | You run a test and return a report or an outcome, not a bare boolean. | `check_fraud_risk`, `check_address_deliverability` |
| `sanitize` | You remove unsafe content. | `sanitize_order_note`, `sanitize_search_query` |

### Calculation

| Verb | Use it when | Examples |
|---|---|---|
| `calculate` | You compute a value from inputs. Prefer `calculate_` to `compute_`. | `calculate_order_total`, `calculate_cart_tax`, `calculate_shipping_cost` |
| `estimate` | The result is approximate. | `estimate_delivery_date`, `estimate_shipping_weight` |
| `sum` | You add numbers. It is a narrow case of `calculate`. | `sum_line_item_cents`, `sum_refunds` |
| `round` | You change precision. | `round_to_cents`, `round_price_up` |
| `convert` | You change a currency with a rate. For other units, use the `_to_` form: `grams_to_ounces`. | `convert_currency`, `convert_price_to_eur` |

## Name by return type

| Returns | Pattern | Examples |
|---|---|---|
| `bool` | `is_`, `has_`, `can_`, `should_`, `must_` | `is_cart_empty`, `has_discount` |
| One item that must exist | `get_<item>` | `get_order`, `get_customer` |
| One item or `None` | `find_<item>` | `find_coupon`, `find_user_by_email` |
| A list | `list_<items>`, `search_<items>` | `list_open_orders`, `search_products` |
| A number | `count_<items>`, `calculate_<value>` | `count_open_orders`, `calculate_order_total` |
| A new object | `create_<thing>` (stored), `build_<thing>` (in memory only) | `create_order`, `build_invoice` |
| Nothing | a verb for the side effect | `cancel_order`, `send_receipt_email` |
| An iterator | `iter_<items>` | `iter_order_rows`, `iter_pending_refunds` |
| A converted value | `<source>_to_<target>`, `parse_`, `format_` | `order_to_invoice`, `parse_price` |

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `order_cancel()` | `cancel_order()` | Verb first reads as a command. |
| `check_stock(sku)` returning a boolean | `is_in_stock(sku)` | A boolean function uses `is_`, `has_`, `can_` or `should_`. |
| `do_checkout()` (if it completes the checkout) | `complete_checkout()` | `do` adds no meaning. |
| `get_and_save_user()` | `get_user()` and `save_user()` | `and` often hides two jobs. |
| `get_coupon()` that may return `None` | `find_coupon()` | `find` says that no result is a normal answer. |
| `get_all_orders()` that returns a list | `list_orders()` | `list` states the return shape. |
| `fetch_total()` that adds numbers locally | `calculate_order_total()` | `fetch` suggests a remote read. |
| `validate_order()` that saves | `validate_order()` and `save_order()` | A check must not change state. |
| `handle_data(order)` (if it applies a coupon) | `apply_coupon(order)` | Bare `handle_` names no action. |
| `process()` (if it captures a payment) | `capture_payment()` | `process` hides the action. |
| bare `convert(order)` (if it builds an invoice) | `order_to_invoice(order)` | Name both the source and the target. |
| `email(order)` (if it sends an email) | `send_order_email(order)` | `email` could be a noun or a verb. |

!!! info "See also"

    - [Variables](variables.md) for the values these functions take and return
    - [Class methods](class_methods.md) for methods on objects
    - [Bad → better cookbook](../patterns/cookbook.md) for more rewrites
    - [Symmetry](../patterns/symmetry.md) for matching pairs such as `open` and `close`

## Glossary
### A
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| accept             | access              | acquire              | activate |
| add                | adjust              | aggregate            | alert |
| align              | allocate            | analyze              | append |
| apply              | archive             | arrange              | assign |
| associate          | attach              | attempt              | audit |
| authenticate       | authorize           | average              | await |

### B
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| backup             | balance             | batch                | bind |
| block              | bootstrap           | borrow               | branch |
| broadcast          | browse              | buffer               | build |
| bundle             | burn                | bypass               | |

### C
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| cache              | calculate           | cancel               | capture |
| cast               | catch               | certify              | check |
| chunk              | clean               | clear                | clone |
| close              | coerce              | collect              | combine |
| commit             | compare             | compile              | complete |
| compose            | compress            | compute              | confirm |
| configure          | connect             | consume              | convert |
| copy               | correct             | count                | create |
| crop               | cut                 |                      | |

### D
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| deactivate         | debug               | decrypt              | deduplicate |
| default            | define              | delete               | deliver |
| deny               | derive              | deserialize          | destroy |
| detach             | detect              | determine            | diagnose |
| disable            | disconnect          | discover             | dispatch |
| display            | dispose             | distribute           | download |
| drain              | draw                | drop                 | dump |
| duplicate          |                    |                      |               |

### E
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| emit               | enable              | encode               | encrypt |
| enforce            | ensure              | enumerate            | erase |
| estimate           | evaluate            | exchange             | exclude |
| execute            | exhaust             | exist                | exit |
| expand             | expect              | expire               | export |
| expose             | extend              | extract              | extrapolate |

### F
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| fail               | fallback            | fetch                | filter |
| finalize           | find                | finish               | fire |
| fix                | flatten             | flush                | fold |
| forbid             | force               | forecast             | fork |
| format             | forward             | freeze               | fulfill |

### G
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| gather             | generate            | get                  | grant |
| group              | grow                | guard                | guess |
| guide              |                    |                      |               |

### H
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| halt               | handle              | harvest              | hash |
| hide               | highlight           | hold                 | hook |
| hydrate            |                    |                      |               |

### I
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| identify           | ignore              | implement            | import |
| increment          | index               | infer                | initialize |
| inject             | inline              | insert               | inspect |
| install            | intercept           | intersect            | invalidate |
| invert             | invoke              | isolate              | issue |

### J
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| join               | jump                | justify              | |

### K
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| keep               | key                 | kick                 | kill |

### L
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| launch             | lay                 | lead                 | leave |
| link               | list                | load                 | locate |
| lock               | log                 | login                | logout |
| lookup             | loop                | lower                | |

### M
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| map                | mark                | match                | measure |
| merge              | migrate             | mimic                | minimize |
| mirror             | mock                | modify               | monitor |
| mount              | move                | multiply             | mutate |

### N
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| navigate           | negate              | nest                 | next |
| normalize          | notify              |                      | |

### O
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| observe            | obtain              | open                 | operate |
| optimize           | order               | organize             | output |
| override           | overwrite           |                      | |

### P
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| pack               | parse               | partition            | pass |
| pause              | perform             | persist              | pipe |
| poll               | populate            | postpone             | prepare |
| present            | preserve            | pretty_print         | prevent |
| process            | produce             | project              | prompt |
| propagate          | prune               | publish              | pull |
| purge              | pursue              | push                 | put |

### Q
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| qualify            | quantify            | query                | queue |
| quit               | quote               |                      | |

### R
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| raise              | read                | rebuild              | receive |
| recognize          | recommend           | record               | recover |
| redirect           | reduce              | refine               | refresh |
| register           | reject              | release              | reload |
| remove             | rename              | render               | reorder |
| repeat             | replace             | report               | request |
| require            | reset               | resolve              | respond |
| restore            | restrict            | resume               | retain |
| retract            | retrieve            | return               | reuse |
| review             | revise              | rewind               | rewrite |
| rotate             | route               | run                  | |

### S
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| save               | scan                | schedule             | search |
| secure             | seed                | select               | send |
| serialize          | set                 | setup                | share |
| shift              | show                | shut                 | sign |
| simplify           | simulate            | skip                 | sort |
| spawn              | split               | start                | stop |
| store              | stream              | stringify            | strip |
| submit             | subscribe           | subtract             | sum |
| summarize          | swap                | sync                 | synthesize |

### T
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| tag                | tear_down           | test                 | timeout |
| track              | transform           | translate            | transmit |
| trigger            | trim                | truncate             | tune |
| turn               | type                |                      | |

### U
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| unblock            | undo                | ungroup              | unify |
| unlock             | unregister          | unsubscribe          | update |
| upgrade            | upload              | use                  | |

### V
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| validate           | verify              | version              | view |

### W
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| wait               | warn                | watch                | wipe |
| wrap               | write               |                      | |

### Z
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| zero               | zip                 | zone                 | |

*[add]: Append an item to a collection or perform a mathematical addition
*[aggregate]: Combine multiple values into a single summarized result
*[allocate]: Reserve and assign a resource for a specific purpose
*[apply]: Execute a function against data or enact a rule/effect
*[authenticate]: Verify the identity of a user or system
*[authorize]: Verify that a user or system has permission to act
*[backup]: Create a copy of data for recovery purposes
*[batch]: Process multiple items as a single group
*[buffer]: Accumulate data in a temporary storage before processing
*[cache]: Store computed results for reuse
*[cast]: Convert a value to a different type
*[chunk]: Split data into smaller segments
*[coerce]: Force a value to a different type, often with implicit rules
*[commit]: Finalize a transaction or make changes permanent
*[compile]: Transform source code into executable form
*[compute]: Perform a mathematical or logical calculation
*[deduplicate]: Remove duplicate entries from a collection
*[default]: Supply a fallback value when the primary value is absent
*[dequeue]: Remove and return the earliest item from a queue
*[deserialize]: Convert a serialized format (JSON, pickle etc.) back to an object
*[dispatch]: Send a command or event to its destination
*[encode]: Convert data into a specific format for transmission or storage
*[enqueue]: Add an item to the end of a queue
*[enumerate]: Iterate over items with their index
*[extrapolate]: Estimate values beyond the known range
*[fetch]: Retrieve data over a network or from a slow source
*[finalize]: Perform the last required steps to complete a process
*[generate]: Produce data or objects, often lazily or programmatically
*[handle]: Respond to an event, signal, or incoming data
*[hydrate]: Populate an object with data from a persistence layer
*[infer]: Deduce a type or value from context
*[intercept]: Capture and potentially modify a call or event before it reaches its target
*[invalidate]: Mark a cached value or session as stale
*[iterate]: Traverse through items of a collection
*[migrate]: Move data or schema from one version to another
*[mock]: Create a fake implementation for testing
*[mutate]: Change the state of an object in-place
*[normalize]: Transform data into a standard form
*[parse]: Analyze a string or structured input into a meaningful data structure
*[partition]: Split data into subsets based on a condition
*[persist]: Save data to durable storage
*[pipe]: Direct data from one function's output to another's input
*[poll]: Repeatedly check a condition or resource for changes
*[populate]: Fill a data structure or database with initial data
*[propagate]: Spread a change or event through a system
*[purge]: Permanently remove data that is no longer needed
*[queue]: Add to a waiting line for sequential processing
*[resolve]: Convert a symbolic name or identifier to its concrete target
*[sanitize]: Remove dangerous or unwanted content from input
*[serialize]: Convert an object to a format suitable for storage or transmission
*[spawn]: Create a new subprocess or concurrent task
*[stream]: Process data sequentially as it becomes available
*[subscribe]: Register interest to receive a feed of events or data
*[stringify]: Convert a value to its string representation
*[synthesize]: Combine data or signals to produce a new result
*[tear_down]: Clean up resources after a test or operation completes
*[transform]: Convert data from one shape or structure to another
*[truncate]: Shorten data by removing leading or trailing parts
*[validate]: Check that data meets required constraints or rules
*[build]: Construct a complex object step by step, often with configuration
*[cancel]: Abort a planned or running operation before completion
*[check]: Run a test and return a report or an outcome
*[clean]: Remove temporary, invalid, or unwanted data
*[close]: Release an open resource or connection
*[configure]: Set up an object or system with given parameters
*[convert]: Change the format, type, or representation of data
*[count]: Determine the number of elements in a collection
*[create]: Instantiate a new entity, record, or object
*[decrypt]: Convert encrypted data back to its original form
*[delete]: Remove an entity permanently from storage
*[dump]: Write the full content of data, typically for backup or debugging
*[encrypt]: Convert data into a secure encoded form
*[export]: Send data to an external system, file, or format
*[filter]: Keep only elements that match a given predicate
*[find]: Locate and return an item matching search criteria
*[format]: Arrange data into a specified layout or representation
*[get]: Retrieve a value by its identifier, often a simple accessor
*[import]: Bring data in from an external source
*[list]: Return a collection of items, often with filtering or pagination
*[load]: Read data from storage into memory
*[lock]: Restrict concurrent access to a resource
*[log]: Record an event for auditing, monitoring, or debugging
*[map]: Transform each element of a collection using a function
*[measure]: Determine a numeric value, duration, or metric
*[merge]: Combine multiple entities, sets, or data streams into one
*[notify]: Send a message or alert to a user, system, or channel
*[open]: Access a resource and make it ready for reading or writing
*[pause]: Suspend a running operation temporarily
*[process]: Perform a series of operations on input data
*[read]: Read and return data from a source
*[reduce]: Combine a collection of elements into a single value
*[refresh]: Reload or renew data that may have become stale
*[resume]: Continue a paused operation from where it stopped
*[retry]: Attempt an operation again after a failure
*[run]: Execute a process, command, or workflow
*[save]: Persist data to durable storage
*[search]: Look for items that match given criteria
*[set]: Assign a value to a property, setting, or configuration
*[setup]: Prepare an environment, object, or system for use
*[sort]: Arrange items by a specified key or comparator
*[split]: Divide an entity, string, or collection into multiple parts
*[start]: Begin execution of a process or service
*[stop]: Terminate execution of a process or service
*[track]: Follow the state or progress of something over time
*[unlock]: Remove an access restriction from a resource
*[update]: Modify an existing entity with new values
*[write]: Write data to storage, a stream, or an output
*[calculate]: Compute a value from inputs by following fixed rules (preferred over compute)
*[dispose]: Free what an object owns, when there is no matching open
*[emit]: Publish an event or signal to its listeners
*[ensure]: Raise on the first failure of a condition that must hold
*[estimate]: Produce an approximate value
*[initialize]: Set up state before first use
*[reset]: Return an object to its initial state
*[send]: Cause a message to go out to a recipient or destination
*[sum]: Add numbers into one total
*[verify]: Confirm that a claim, such as a signature or a token, is genuine, or raise if it is not
