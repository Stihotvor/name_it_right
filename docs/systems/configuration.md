---
status: new
---

# Configuration

!!! success "General patterns"

    - Write an environment variable in `SCREAMING_SNAKE_CASE`: `DATABASE_URL`, `LOG_LEVEL`
    - Start the name with the app or the area, then the setting: `SHOP_DATABASE_URL`, `SHOP_PAYMENT_TIMEOUT_SECONDS`
    - Put the unit at the end when a value has one: `_SECONDS`, `_MS`, `_BYTES`
    - Write a boolean as a positive word and accept clear values: `FEATURE_X_ENABLED=true`
    - Keep the secret out of the name and out of the value in the repository: name `STRIPE_API_KEY`, store the value in a secret store

!!! tip "Useful tips"

    - Use the same word in the variable, in the config file and in the code: `payment_timeout_seconds`, `PAYMENT_TIMEOUT_SECONDS`
    - Use a prefix for each service in a shared environment, so names do not collide
    - Document the default value and the unit of each variable in one file
    - Use `kebab-case` for Kubernetes resource names and keys of labels

!!! danger "General anti-patterns"

    - A name without a unit: `TIMEOUT` (seconds or milliseconds?)
    - A negative boolean: `DISABLE_CACHE=false`
    - A name that contains the value: `USE_PG14`
    - A secret value in a default or a name: `DB_PASSWORD_DEFAULT=hunter2`
    - A mixed style in one file: `dbHost`, `DB_PORT`

The examples use an e-commerce shop. For the case styles of the languages, see the [Languages overview](../languages/index.md).

## Environment variables

| Kind | Pattern | Examples | Why this name |
|---|---|---|---|
| Connection string | `<SERVICE>_URL` | `DATABASE_URL`, `REDIS_URL` | One variable holds the whole address. |
| Host and port | `<SERVICE>_HOST`, `<SERVICE>_PORT` | `DB_HOST`, `DB_PORT` | When the parts are separate. |
| Timeout | `<THING>_TIMEOUT_<UNIT>` | `HTTP_TIMEOUT_SECONDS`, `DB_CONNECT_TIMEOUT_MS` | The unit is in the name. |
| Size | `<THING>_MAX_<UNIT>` | `UPLOAD_MAX_BYTES` | The unit is in the name, and `MAX` is after the thing as for counts. |
| Count | `<THING>_COUNT`, `<THING>_MAX_<UNIT>` | `RETRY_COUNT`, `CONNECTIONS_MAX` | A total, or a limit with the word `MAX` after the thing. |
| Switch | `<FEATURE>_ENABLED` | `CACHE_ENABLED`, `DEBUG_LOGGING_ENABLED` | A positive boolean. |
| Mode | `<AREA>_MODE` | `CACHE_MODE=read_through` | A choice from a list of behaviors. |
| Level | `LOG_LEVEL` | `LOG_LEVEL=info` | A common name. |
| Environment (community practice) | `APP_ENV`; `NODE_ENV` in Node | `NODE_ENV=production` | The deployment stage. Do not branch the code on it. Set each variable on its own (Twelve-Factor App). |
| Path | `<THING>_DIR`, `<THING>_PATH`, `<THING>_FILE` | `DATA_DIR`, `CONFIG_FILE` | The kind of path is in the name. |
| Prefix for one app | `<APP>_<SETTING>` | `SHOP_DATABASE_URL`, `SHOP_LOG_LEVEL` | Avoids a clash. |
| Prefix for a framework | the framework prefix | `SPRING_PROFILES_ACTIVE`, `DJANGO_SETTINGS_MODULE` | The framework reads them. |

By POSIX convention, the names that utilities use are upper case, with digits and the underscore, and they do not start with a digit. POSIX keeps lower-case names for applications. Most projects still use upper case for application variables.

## Secrets

| Kind | Pattern | Examples | Why this name |
|---|---|---|---|
| API key | `<SERVICE>_API_KEY` | `STRIPE_API_KEY` | The service and the kind. |
| Secret token | `<SERVICE>_TOKEN` | `GITHUB_TOKEN` | A token for a service. |
| Client secret | `<SERVICE>_CLIENT_SECRET` | `OAUTH_CLIENT_SECRET` | The OAuth name. |
| Password | `<SERVICE>_PASSWORD` | `DB_PASSWORD` | The service and the kind of secret. |
| Signing key | `<PURPOSE>_SIGNING_KEY` | `JWT_SIGNING_KEY` | The purpose of the key. |
| Path to a secret file | `<NAME>_FILE` | `DB_PASSWORD_FILE` | The variable holds a path. Official Docker images read the value from that file, for example `/run/secrets/db_password`. This is a community convention. |
| Secret manager entry | `<app>/<name>`; the store or the account sets the environment | `shop/stripe-api-key` | A path in a secret store, not an environment variable. |

Do not put a secret value in an environment variable name, in a Git repository, or in a log.

## Kubernetes names

| Kind | Rule | Examples | Why this name |
|---|---|---|---|
| Resource name | lower case, digits and `-`; start and end with a letter or a digit | `shop-orders`, `payment-gateway` | Most kinds use a DNS subdomain name (at most 253 characters, `.` allowed). Some kinds use a DNS label (at most 63 characters). A Service name must start with a letter. |
| Namespace | lower case with `-` | `shop-prod`, `shop-staging` | A DNS label. |
| Label key | `prefix/name`; the name part has at most 63 characters, begins and ends with a letter or a digit, and may hold `-`, `_` and `.` | `app.kubernetes.io/name` | A prefix with a domain avoids a clash. The prefixes `kubernetes.io/` and `k8s.io/` are reserved. |
| Recommended labels | `app.kubernetes.io/<field>` | `app.kubernetes.io/name`, `app.kubernetes.io/version`, `app.kubernetes.io/component` | The standard set. |
| Custom label | company prefix | `shop.example.com/team` | Your domain as a prefix. |
| Annotation key | the same form as a label | `shop.example.com/owner` | Annotations are for tools. |
| ConfigMap | the app and the purpose | `shop-orders-config` | The app tells who reads it, and `config` tells what is inside. |
| Secret | the app and the kind | `shop-orders-db-credentials` | The app tells who reads it, and `db-credentials` tells what is inside. Do not put the value in the name. |
| Environment variable in a pod | `SCREAMING_SNAKE_CASE` | `DATABASE_URL` | The same as other environments. |
| Helm value key | `camelCase` | `replicaCount`, `image.repository` | The Helm chart style. |

## Config files

| Format | Key style | Examples | Notes |
|---|---|---|---|
| YAML for a service | `snake_case` or `camelCase`, one style | `payment_timeout_seconds` | Match the language of the app. |
| TOML | no rule in the TOML spec; Cargo and `pyproject.toml` use `kebab-case` | `max-connections` | Match the tool that reads the file. |
| JSON | the style of the API | `maxConnections` | Match the API. |
| Properties (Java) | dotted lower case | `shop.payment.timeout-seconds` | Spring relaxed binding accepts several forms. |
| `.env` file | like environment variables | `DATABASE_URL=...` | Not in the repository when it holds secrets. |

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `TIMEOUT` | `HTTP_TIMEOUT_SECONDS` | The unit is in the name. |
| `DISABLE_CACHE` | `CACHE_ENABLED` | A positive boolean. |
| `dbHost` in an env file | `DB_HOST` | The environment style. |
| `PASS` | `DB_PASSWORD` | `PASS` could mean password or passphrase, and it lacks the service. |
| `USE_PG14` | `DATABASE_URL` | The version is part of the value, not the name. |
| `prod_db_url` | `DATABASE_URL` | The environment is set by the deployment, not the name. The Twelve-Factor App keeps each variable separate from named environments. |
| `MyApp` as a Kubernetes name | `my-app` | Kubernetes names are lower case. |
| `app` as a label that names the application | `app.kubernetes.io/name` | Use the standard key for the name of the application. |

!!! info "See also"

    - [Systems overview](index.md), [Errors](errors.md) and [Naming patterns](../patterns/index.md)
    - [Kubernetes: labels and annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/), [Recommended labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/), [The Twelve-Factor App: config](https://12factor.net/config)
