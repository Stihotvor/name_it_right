# Functions

!!! success "General patterns"
    
    - Use `snake_case` in function names ONLY. Don't look at some bad examples, even if they have 1k+ stars on GitHub  
    - Functions which validate or check something and return boolean should start with `is_`, `has_`: `has_tax_applied()`, `is_valid()`  
    - Functions not covered by the above rule should have executable names: `compile()`, `collect()`, `process()`, `fetch()`  
    - If the function has `and` in the name, there is a high chance it does multiple things. Split it.  
    - Name CRUD functions after the resource and action: `create_order()`, `fetch_customer_orders()`, `update_shipping_address()`, `delete_expired_carts()`  
    - Name query functions by what they return: `get_pending_payments()`, `find_user_by_email()`, `search_products()`, `list_active_discounts()`
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
    - Pick one verb per operation and never mix. If the codebase uses `fetch_`, use `fetch_` everywhere — no `retrieve_` or `get_`.  
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
*[fetch]: Retrieve data from a remote or persistent source
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
*[check]: Test a condition and return a boolean result
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