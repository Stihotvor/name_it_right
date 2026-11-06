# Class methods

## Method patterns

The tables use an e-commerce checkout. For function names outside classes, see [Functions](functions.md). For class names, see [Classes](classes.md).

### Mutating and non-mutating

A method that changes the object and a method that returns a changed copy need different names. Python itself shows the pair: `list.sort()` changes the list and returns `None`, and `sorted()` returns a new list.

| Mutates the object | Returns a new object | Why |
|---|---|---|
| `cart.add_item(item)` | `cart.with_item(item)` | `add` changes the cart. `with_` returns a changed copy. |
| `order.apply_coupon(code)` | `order.with_coupon(code)` | The `with_` form is safe for frozen objects. |
| `cart.sort_items()` | `cart.sorted_items()` | The Python pair: `sort` changes, `sorted` returns. |
| `cart.reverse_items()` | `cart.reversed_items()` | `reverse` changes the list in place. `reversed()` returns an iterator, so `reversed_items()` should return a new list. |
| `address.normalize()` | `address.normalized()` | The past participle marks a new, normalized copy. The original stays unchanged. |
| `cart.attach_note(text)` | `cart.with_note(text)` | `pathlib` uses `with_name` and `with_suffix` for the same idea. |

!!! tip "Rule of thumb"

    - A method that changes the object uses an imperative verb: `sort`, `add`, `clear`. The reverse is not true: `calculate_tax` is a verb and does not change the object.
    - A past participle or a `with_` prefix returns a new object: `sorted`, `normalized`, `with_item`.
    - A mutating method usually returns `None`. Do not return `self` unless the class is a builder.

### Conversions

| Pattern | Use it when | Examples |
|---|---|---|
| `to_<target>` | The object converts itself. | `order.to_dict()`, `money.to_decimal()`, `address.to_label()` |
| `as_<view>` | The method is a thin wrapper over the same data. This is a project convention, not a Python rule. | `cart.as_read_only()`, `order.as_line_items()` |
| `to_summary` | The method builds a new summary object. | `order.to_summary()` |
| `from_<source>` | A class method builds an object from another shape. | `Order.from_cart(cart)`, `Money.from_cents(1999, "EUR")`, `Address.from_dict(data)` |
| `parse` | A class method reads text. | `CouponCode.parse("SAVE10")`, `Money.parse("19.99 EUR")` |
| `<source>_to_<target>` | A function converts between two other types. | `cart_to_order`, `order_to_invoice` |

### Predicates

| Pattern | Use it when | Examples |
|---|---|---|
| `is_<state>()` | The method checks a state. | `order.is_paid()`, `cart.is_empty()`, `coupon.is_expired()` |
| `has_<thing>()` | The method checks ownership. | `order.has_discount()`, `customer.has_saved_card()` |
| `can_<action>()` | The method checks ability. | `order.can_cancel()`, `payment.can_refund()` |
| `should_<action>()` | The method checks a decision. | `payment.should_retry()`, `order.should_ship()` |

A predicate returns a `bool` and does not change the object. A cheap predicate without arguments may be a property (`order.is_paid`). Use a method (`order.can_cancel()`) when the check takes arguments or does work. Pick one form per code base, because a forgotten `()` on a method makes `if order.is_paid:` always true. See [Booleans, collections, units and time](../patterns/booleans-collections-units-time.md).

### Properties and methods

| Use a property when | Use a method when | Examples |
|---|---|---|
| The value is cheap and has no arguments. | The work costs time or needs arguments. | `order.total_cents` and `order.calculate_tax(region)` |
| The name is a noun. | The name is a verb. | `cart.item_count` and `cart.merge(other_cart)` |
| Reading has no side effect. | The call has a side effect or does input and output. | `customer.full_name` and `customer.send_welcome_email()` |
| The value looks like a field. | The call may fail or wait. | `order.status` and `order.fetch_tracking()` |

### Dunder methods

Python reserves the names with double underscores at both ends. Use the standard ones. Do not invent names of the form `__something__`, such as `__calc__`.

| Method | Purpose | Example |
|---|---|---|
| `__init__` | Set up a new instance. | `Order`, `Cart` |
| `__post_init__` | Check or derive fields after a dataclass `__init__`. | `Money` |
| `__repr__` | Show a developer-friendly text. | `Order(id=7, status="paid")` |
| `__str__` | Show a human-friendly text. | `Address` as a label |
| `__eq__` | Compare for equality. | `Money` |
| `__hash__` | Make the object hashable for sets and dict keys. Define it with `__eq__`, on an immutable class. | `Money`, `Address` |
| `__len__` | Return the number of items. | `Cart` |
| `__iter__` | Loop over the items. | `Cart`, `Order` |
| `__contains__` | Support `in`. | `Cart` with `sku in cart` |
| `__enter__` / `__exit__` | Support `with`. | `CheckoutSession` |
| `__call__` | Make the object callable. | `PricingStrategy` |

See also [Special functions](special_functions.md).

### classmethod and staticmethod

| Kind | Naming rule | Examples |
|---|---|---|
| `@classmethod` constructor | `from_<source>`, `parse`, or a noun for a named instance. | `Order.from_cart`, `Money.zero`, `Address.parse` |
| `@classmethod` named instance | A noun for the instance. Use `create_` only if the method stores the object. | `Coupon.percent_off(10)`, `Order.draft()` |
| `@staticmethod` helper | Name it by what it checks or computes. No `self`, no `cls`. | `Sku.is_valid_format(text)`, `Money.round_to_cents(value)` |
| Module function | Use it when the code needs no class. | `order_to_invoice(order)` |

If a static method has no real tie to the concept of the class, make it a module-level function.

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `cart.get_sorted()` that sorts in place | `cart.sort_items()` | The name must match the change. |
| `cart.sort()` that returns a copy | `cart.sorted_items()` | `sort` suggests a change in place. |
| `order.paid()` | `order.is_paid()` | The prefix shows a boolean. |
| `order.total()` that reads a stored field | `order.total_cents` (property) | A cheap value fits a property. |
| `customer.get_name()` | `customer.name` (property) | Python style prefers attributes and properties to getters. |
| `order.convert()` | `order.to_invoice()` | Name the target. |
| `Order.make(cart)` | `Order.from_cart(cart)` | `from_` is the common name for an alternative constructor. |
| `Money.parse_static()` | `Money.parse()` | Do not put the decorator in the name. |
| `order.__calc__()` | `order.calculate_total()` | Do not invent dunder names. |
| `cart.items_count()` | `cart.item_count` (property) | A count is cheap and noun-like. |

!!! info "See also"

    - [Functions](functions.md) for the verb families
    - [Classes](classes.md) for the class suffixes
    - [Variables](variables.md) for attribute names
    - [Symmetry](../patterns/symmetry.md) for paired methods such as `open` and `close`

## Glossary

A curated reference of verbs commonly used as class method names. Pick a verb and pair it with a domain noun — `add_order()`, `validate_email()`, `to_json()`, `from_row()`.

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
| block              | bootstrap           | borrow               | broadcast |
| browse             | buffer              | build                | bundle |

### C
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| cache              | calculate           | cancel               | capture |
| cast               | catch               | check                | clean |
| clear              | clone               | close                | collect |
| combine            | commit              | compare              | compile |
| complete           | compose             | compute              | configure |
| confirm            | connect             | consume              | convert |
| copy               | count               | create               | |

### D
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| deactivate         | debug               | decrypt              | deduplicate |
| default            | define              | delete               | derive |
| deserialize        | destroy             | detach               | detect |
| disable            | disconnect          | dispatch             | display |
| dispose            | dump                | duplicate            | |

### E
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| emit               | enable              | encode               | encrypt |
| enforce            | ensure              | enumerate            | erase |
| estimate           | evaluate            | exclude              | execute |
| exist              | expand              | expire               | export |
| expose             | extend              | extract              | |

### F
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| fetch              | filter              | finalize             | find |
| finish             | fix                 | flatten              | flush |
| format             | forward             | freeze               | fulfill |

### G
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| gather             | generate            | get                  | grant |
| group              | guard               |                      | |

### H
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| handle             | hash                | hide                 | hold |
| hook               | hydrate             |                      | |

### I
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| identify           | ignore              | import               | increment |
| index              | infer               | initialize           | inject |
| inline             | insert              | inspect              | install |
| intercept          | invalidate          | invert               | invoke |
| isolate            |                     |                      | |

### J
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| join               | jump                |                      | |

### K
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| keep               | key                 |                      | |

### L
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| list               | load                | locate               | lock |
| log                | login               | logout               | lookup |

### M
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| map                | mark                | match                | measure |
| merge              | migrate             | mock                 | modify |
| monitor            | mount               | move                 | mutate |

### N
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| navigate           | nest                | next                 | normalize |
| notify             |                     |                      | |

### O
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| observe            | obtain              | open                 | optimize |
| order              | organize            | output               | override |

### P
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| pack               | parse               | partition            | pause |
| perform            | persist             | pipe                 | poll |
| populate           | prepare             | present              | prevent |
| process            | produce             | project              | prune |
| publish            | pull                | purge                | push |
| put                |                     |                      | |

### Q
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| query              | queue               | quit                 | |

### R
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| read               | rebuild             | receive              | recognize |
| recommend          | record              | recover              | redirect |
| reduce             | refresh             | register             | reject |
| release            | reload              | remove               | rename |
| render             | reorder             | repeat               | replace |
| report             | request             | reset                | resolve |
| respond            | restore             | restrict             | resume |
| retain             | retrieve            | return               | reuse |
| review             | revise              | rewind               | rewrite |
| rotate             | route               | run                  | |

### S
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| save               | scan                | schedule             | search |
| secure             | seed                | select               | send |
| serialize          | set                 | setup                | share |
| show               | shut                | sign                 | simplify |
| simulate           | skip                | sort                 | spawn |
| split              | start               | stop                 | store |
| stream             | stringify           | strip                | submit |
| subscribe          | subtract            | sum                  | summarize |
| swap               | sync                | synthesize           | |

### T
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| tag                | tear_down           | test                 | timeout |
| track              | transform           | translate            | transmit |
| trigger            | trim                | truncate             | tune |
| turn               |                     |                      | |

### U
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| unblock            | undo                | unify                | ungroup |
| unlock             | unregister          | unsubscribe          | update |
| upgrade            | upload              | use                  | |

### V
|                    |                     |                      |               |
|--------------------|---------------------|----------------------| ------------- |
| validate           | verify              | view                 | |

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
*[authenticate]: Verify the identity of a user or system
*[authorize]: Verify that a user or system has permission to act
*[cache]: Store computed results for reuse
*[commit]: Finalize a transaction or make changes permanent
*[deserialize]: Convert a serialized format back to an object
*[dispatch]: Send a command or event to its destination
*[encode]: Convert data into a specific format for transmission or storage
*[enqueue]: Add an item to the end of a queue
*[hydrate]: Populate an object with data from a persistence layer
*[infer]: Deduce a type or value from context
*[intercept]: Capture and potentially modify a call or event
*[invalidate]: Mark a cached value or session as stale
*[mutate]: Change the state of an object in-place
*[normalize]: Transform data into a standard form
*[persist]: Save data to durable storage
*[populate]: Fill a data structure or database with initial data
*[purge]: Permanently remove data that is no longer needed
*[resolve]: Convert a symbolic name or identifier to its concrete target
*[sanitize]: Remove dangerous or unwanted content from input
*[serialize]: Convert an object to a format suitable for storage or transmission
*[stringify]: Convert a value to its string representation
*[tear_down]: Clean up resources after a test or operation completes
*[validate]: Check that data meets required constraints or rules
*[build]: Construct a complex object step by step with configuration
*[cancel]: Abort a planned or running operation
*[check]: Test a condition and return a boolean result
*[close]: Release an open resource or connection
*[configure]: Set up with given parameters
*[convert]: Change the format, type, or representation
*[count]: Determine the number of elements
*[create]: Instantiate a new entity or record
*[delete]: Remove an entity permanently
*[export]: Send data to an external system or format
*[filter]: Keep only matching elements
*[find]: Locate and return an item matching criteria
*[format]: Arrange data into a specified layout
*[get]: Retrieve a value by identifier
*[import]: Bring data in from an external source
*[list]: Return a collection of items
*[load]: Read data from storage into memory
*[lock]: Restrict concurrent access to a resource
*[map]: Transform each element of a collection
*[merge]: Combine multiple entities into one
*[open]: Access a resource for reading or writing
*[process]: Perform a series of operations on input
*[read]: Read and return data from a source
*[refresh]: Reload or renew stale data
*[save]: Persist data to storage
*[search]: Look for items matching criteria
*[set]: Assign a value to a property or setting
*[sort]: Arrange items by a key or comparator
*[split]: Divide an entity into multiple parts
*[start]: Begin execution of a process
*[stop]: Terminate execution of a process
*[update]: Modify an existing entity with new values
*[write]: Write data to storage or output