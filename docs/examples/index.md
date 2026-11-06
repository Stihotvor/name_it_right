---
status: new
---

# Examples by domain

!!! success "General patterns"

    - Use the words of the business. A name in the code is the same word that people use in the domain
    - Name the entity, then its states, then its actions. The three lists give the vocabulary of a domain
    - Check the traps. Most naming mistakes come from words that look the same and mean different things
    - Use the same name in the database, the API, the events and the code. See [Systems](../systems/index.md) and [Databases](../databases/index.md)

!!! tip "Useful tips"

    - Start with a glossary of 10 to 20 terms before you write any code
    - Write down the states of the main entity as a list. Each state has one name and one meaning
    - Ask the domain experts when two words seem to mean the same. They often do not

!!! danger "General anti-patterns"

    - Two names for one thing: `customer` and `user` for the same person
    - One name for two things: `status` for the state of an order and the state of a payment
    - A generic word where a domain word exists: `item` for an order line, `type` for a payment method

## What each page has

| Section | What it gives |
|---|---|
| Entities | The nouns of the domain, with a short meaning. |
| States | The lifecycle of the main entities, one name for each state. |
| Actions | The verbs of the domain, in the form of a function name. |
| Traps | Words that are easy to confuse, with the better name. |
| Worked example | A small data model with SQL, API paths and code. |

## Pages

| Domain | Page |
|---|---|
| E-commerce | [E-commerce](ecommerce.md) |

!!! info "See also"

    - [Naming patterns](../patterns/index.md) for the rules that hold in every domain
    - [Languages](../languages/index.md) for the case style of each language
    - [References and glossary](../common/references-and-glossary.md) for sources and terms
