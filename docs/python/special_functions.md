# Special functions

## Generators

!!! success "General patterns"

    - Prefer a noun or noun phrase when the generator yields objects of a known type: `def active_users():` yields user objects
    - Use the `iter_` prefix when the generator provides iteration over something: `iter_pages()`, `iter_chunks()`
    - Use the `generate_` or `yield_` prefix when the creation process is the focus: `generate_report()`, `yield_batches()`

!!! tip "Useful tips"

    - Name generators so the caller intuitively knows to iterate: `def unprocessed_orders():` → `for order in unprocessed_orders():`
    - If a generator wraps another iterator, use `wrap_` or prefix the wrapped name: `def wrap_lines(file_path):`

!!! danger "General anti-patterns"

    - Verb-only names that sound like a function with side effects: `process()` (does it return a generator? modify state?)
    - Using `Generator` in the name: `def user_generator():` → prefer `def users():`

    ```py
    def unprocessed_orders() -> Generator[Order, None, None]:
        for order in OrderRepository.find_all(status="pending"):
            yield order

    def iter_pages(cursor: str | None = None) -> Iterator[list[Record]]:
        while cursor:
            page = fetch_page(cursor)
            yield page.items
            cursor = page.next_cursor
    ```

---

## Async functions and coroutines

!!! success "General patterns"

    - Prefix network I/O coroutines with `fetch_`, `read_`, `download_`, `listen_`, `poll_`
    - Prefix data-processing coroutines with `process_`, `transform_`, `aggregate_`
    - When both sync and async versions exist, name them identically and let the import distinguish them

!!! tip "Useful tips"

    - Avoid adding an `async_` prefix — the `async def` keyword already signals the function is a coroutine
    - For long-running coroutines that produce a stream of values, use `async for` semantics and name as a noun: `def event_stream():`

!!! danger "General anti-patterns"

    - Redundant prefixes: `async def async_fetch_data():` → `async def fetch_data():` is enough
    - Blocking I/O inside a coroutine without documenting it

    ```py
    async def fetch_order_summary(order_id: str) -> OrderSummary:
        data = await api_client.get(f"/orders/{order_id}")
        return OrderSummary.parse(data)

    async def poll_payment_status(transaction_id: str) -> PaymentStatus:
        while True:
            status = await gateway.check(transaction_id)
            if status in (PaymentStatus.COMPLETED, PaymentStatus.FAILED):
                return status
            await asyncio.sleep(2)
    ```

---

## Decorators

!!! success "General patterns"

    - Use lowercase names, often adjectives or past participles: `@lru_cache`, `@dataclass`, `@retry`, `@logged`, `@deprecated`
    - If the decorator takes arguments, name it as a verb or prepositional phrase: `@timeout(5)`, `@rate_limit("10/min")`

!!! tip "Useful tips"

    - Name the decorator for the behavior it adds, not the implementation mechanism: `@logged` (not `@with_logger`)
    - Use `functools.wraps` to preserve the wrapped function's name and docstring
    - For decorator factories, prefer a descriptive name that includes the parameter hint: `@retry(tries=3)`

!!! danger "General anti-patterns"

    - `CamelCase` in decorators — they are functions, not classes: `@RetryOnFailure` → `@retry_on_failure`
    - Naming a decorator after its implementation detail: `@wraps_logger` instead of `@logged`

    ```py
    @retry(tries=3, delay=0.5)
    @rate_limit(max_calls=10, per=60)
    @logged
    def process_payment(order_id: str) -> PaymentResult:
        ...
    ```

---

## Context managers

!!! success "General patterns"

    - Name context managers after the resource they manage: `open_file()`, `database_session()`, `lock()`
    - If the context manager is a class, use `CamelCase` and a noun: `class TemporaryDirectory:`, `class Timeout:`

!!! tip "Useful tips"

    - Use `@contextlib.contextmanager` to turn a single-yield generator into a context manager without writing a class
    - Name context managers so `with` reads naturally: `with database_session():` or `with temporary_file():`

!!! danger "General anti-patterns"

    - Names that describe the setup/teardown mechanism: `class ContextManagerForDB:` → `database_session()`
    - Skipping a docstring — context managers have invisible `__enter__`/`__exit__` behavior that must be documented

    ```py
    from contextlib import contextmanager

    @contextmanager
    def database_session():
        session = Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    @contextmanager
    def temporary_file(suffix: str = ".tmp"):
        path = Path(f"/tmp/{uuid4()}{suffix}")
        try:
            yield path
        finally:
            path.unlink(missing_ok=True)
    ```
