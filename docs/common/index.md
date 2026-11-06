# Common

Naming conventions that apply across **every** language — Python, SQL, JavaScript, Go, or C#. Fix these first before diving into language-specific rules.

!!! success "General patterns"

    - Name for the reader, not the writer. Code is read 10× more than it is written
    - A name should reveal intent without needing a comment: `orders_awaiting_shipment` not `temp2`
    - Be precise: `customer_email` is better than `email` (which email? the customer's? the sender's?)
    - Be consistent: establish a vocabulary and use it across the entire project
    - Prefer clarity over brevity: `delete_expired_sessions()` over `del_ses()`

!!! tip "Useful tips"

    - When you struggle to name something, it is often a sign that the design is wrong — simplify first
    - Keep a shared glossary of chosen verbs and nouns for your team or project
    - Read your code aloud — if a name sounds awkward, it probably is
    - Use code review to enforce naming conventions early, before they become habits

---

<div class="grid cards" markdown>

-   __Abbreviations and shorts__

    ---

    One-letter names, cryptic abbreviations, and why brevity is not clarity.

    [:octicons-arrow-right-24: Abbreviations](abbreviations.md)

-   __Meaning and clarity__

    ---

    Misleading names, generic names, and names that ignore the domain.

    [:octicons-arrow-right-24: Meaning](meaning.md)

-   __Consistency__

    ---

    Inconsistent naming, sound-alike names, and shadowing built-ins.

    [:octicons-arrow-right-24: Consistency](consistency.md)

-   __Structure__

    ---

    Hungarian notation, redundant prefixes, and naming that leaks implementation details.

    [:octicons-arrow-right-24: Structure](structure.md)

-   __References and glossary__

    ---

    Sources, verbs, nouns, suffixes, and states to choose names from.

    [:octicons-arrow-right-24: References and glossary](references-and-glossary.md)

</div>

!!! info "See also"

    - [Naming patterns](../patterns/index.md) for rules that hold in every language
    - [Languages](../languages/index.md) for case styles and names by kind
    - [Databases](../databases/index.md) for names of tables, columns and indexes
    - [Systems](../systems/index.md) for names in APIs, events and configuration
    - [Examples](../examples/index.md) for full vocabularies of a business domain
