---
status: new
---

# Command line

!!! success "General patterns"

    - Write a long option in lower case with hyphens: `--output-format`, `--dry-run`
    - Write a short option as one letter with one hyphen: `-o`, `-v`
    - Give each common option a long and a short form: `-h` and `--help`, `-V` and `--version`
    - Name a subcommand with a verb or a noun in lower case: `init`, `build`, `config`
    - Use the same word for the same thing in every command and in the environment: `--timeout` and `SHOP_TIMEOUT_SECONDS`

!!! tip "Useful tips"

    - Support `--help` and `--version` in every program. Print help to standard output and exit with code `0`
    - Write a switch as a positive word (`--color`) and a negation with `--no-` (`--no-color`)
    - Put the unit in the name or the help text when a value has one: `--timeout 30s`, `--max-size-bytes`
    - Keep a long option short enough to type: two or three words at most

!!! danger "General anti-patterns"

    - A single hyphen with a long name: `-output` (users read it as `-o -u -t ...`)
    - `camelCase` or `snake_case` in options: `--outputFormat`, `--output_format`
    - A negative switch with a negation: `--no-disable-cache`
    - Different words for one thing: `--dir` in one command and `--folder` in another
    - A subcommand that is a flag: `--build`

The examples use a command-line tool for an e-commerce shop called `shopctl`.

## Options

| Kind | Rule | Examples | Why this name |
|---|---|---|---|
| Long option | `--` and lower-case words with `-` | `--output-format`, `--dry-run` | The GNU long-option style. Hyphens make words easy to read. |
| Short option | `-` and one letter | `-o`, `-v`, `-n` | Fast to type. |
| Short options joined | `-` and several letters | `-abc` means `-a -b -c` | POSIX allows it. |
| Option with a value | `--name value` or `--name=value` | `--output json`, `--output=json` | Support both forms. |
| Short option with a value | `-n value`; `-nvalue` also works with `getopt` | `-o json` | The separate form is the clear one. |
| Switch (a flag with no value) | a noun or a verb | `--verbose`, `--force`, `--recursive` | The option turns something on. |
| Negation | `--no-<name>` | `--no-color`, `--no-cache` | A common style (not a GNU rule). |
| Repeated option | the same option many times | `-v -v`, `--tag a --tag b` | Each use adds one value. |
| Option end marker | `--` | `shopctl run -- --not-an-option` | Everything after is an argument. |
| Option with a unit | the unit in the name or in the value | `--timeout 30s`, `--max-size-bytes 1048576` | No guess about the unit. |
| Option for a path | `--file`, `--dir`, `--config` | `--config ./shop.toml` | The kind of path in the name. |
| Option for a mode | `--mode`, `--format` | `--format json` | A choice from a list. |
| Option for a count | `--limit`, `--count`, `--max-<thing>` | `--limit 50`, `--max-retries 3` | A number. |
| Option for time | `--since`, `--until`, `--timeout` | `--since 2026-11-01`, `--timeout 30s` | A moment or a duration. |

## Standard options

These options have the same meaning in most tools. Use them as they are.

| Short | Long | Meaning | Note |
|---|---|---|---|
| `-h` | `--help` | Show help and exit. | Exit code `0`. |
| `-V` | `--version` | Show the version and exit. | Many tools use `-v` for verbose and `-V` for version. |
| `-v` | `--verbose` | Show more output. | May repeat: `-vv`. |
| `-q` | `--quiet` | Show less output. | The opposite of verbose. |
| `-f` | `--force` | Do not ask; overwrite. | Dangerous. Document it. |
| `-n` | `--dry-run` | Show what would happen; do nothing. | The form of `make -n`. |
| `-r`, `-R` | `--recursive` | Include subfolders. | The case varies by tool. |
| `-o` | `--output` | The output file or format. | |
| `-i` | `--input` | The input file. | |
| `-y` | `--yes` | Answer yes to all questions. | For scripts. |
| | `--json` | Print the result as JSON. | A common switch. |
| | `--no-color` | Turn off color. | See also the `NO_COLOR` variable. |
| | `--config` | The path of a config file. | |
| | `--debug` | Show internal details. | |

## Subcommands

| Pattern | Rule | Examples | Why this name |
|---|---|---|---|
| Command, then subcommand | `<tool> <noun> <verb>` | `shopctl order list`, `shopctl order cancel 123` | Group by the thing. |
| Command, then verb | `<tool> <verb> <noun>` | `shopctl list orders`, `shopctl cancel order 123` | Group by the action. |
| Standard verbs | `list`, `get`, `create`, `update`, `delete` | `shopctl customer create` | The same set as in a REST API. |
| Setup | `init`, `login`, `logout`, `config` | `shopctl login` | Short and common. |
| Info | `version`, `status`, `help` | `shopctl status` | Common. |
| Alias | a short form of a command | `shopctl ls` for `list` | Document the main name. |
| Plural or singular | choose one | `shopctl orders list` or `shopctl order list` | Do not mix. |
| Plugin | `<tool>-<name>` on the path | `shopctl-export` | Git style: `git-lfs`. |

Conflict: some tools put the noun first (`kubectl get pods`, `gh pr list`, `aws s3 cp`). Others put the verb first (`git commit`, `docker run`). Choose one and keep it in the whole tool.

## Arguments

| Kind | Rule | Examples | Why this name |
|---|---|---|---|
| Positional argument | a noun in upper case in help (common style) | `shopctl order get ORDER_ID` | The help shows the kind. |
| Optional argument | in square brackets in help | `[PATH]` | The usual help style. |
| Many arguments | three dots | `FILE...` | One or more. |
| Choice | braces in help | `{json,yaml,table}` | A list of allowed values. |
| Default | stated in help | `--limit N (default: 50)` | No guess. |

## Environment variables and config

| Source | Rule | Examples | Why this name |
|---|---|---|---|
| Environment variable for an option | the tool name, then the option, in capitals | `SHOPCTL_OUTPUT_FORMAT` for `--output-format` | The same word in three places. |
| Config file key | the option name without `--` | `output-format = "json"` | Match the option. |
| Order of priority | flag, then environment, then config, then default | `--output json` wins over `SHOPCTL_OUTPUT_FORMAT` | A common rule. |
| `NO_COLOR` | a community standard | `NO_COLOR=1` | Turns off color when set and not empty (no-color.org). |
| Standard names | `HOME`, `EDITOR`, `PAGER`, `TERM` | `EDITOR=vim` | Defined by the system. |

For the names of environment variables, see [Configuration](configuration.md).

## Exit codes

| Code | Meaning | Note |
|---|---|---|
| `0` | Success | |
| `1` | A general error | |
| `2` | A wrong use of the command | Common for a bad option. |
| `126`, `127` | The shell could not run or find the command | Set by the shell. |
| `130` | Stopped by `Ctrl-C` | `128` plus signal `2`. |

## Bad → better

| Bad | Better | Why |
|---|---|---|
| `-output` | `--output` or `-o` | One hyphen is for a one-letter option. |
| `--outputFormat` | `--output-format` | Long options use hyphens. |
| `--output_format` | `--output-format` | Same rule. |
| `--disable-cache` | `--no-cache` | A positive name with a standard negation. |
| `--nocolor` | `--no-color` | Hyphen before `color`. |
| `--folder` and `--dir` in one tool | `--dir` everywhere | One word for one thing. |
| `--build` | `shopctl build` | An action is a subcommand. |
| `-help` | `-h`, `--help` | The standard names. |
| `--timeout 30` | `--timeout 30s` or `--timeout-seconds 30` | The unit is clear. |
| `--verbose=true` | `--verbose` | A switch needs no value. |

!!! info "See also"

    - [Systems overview](index.md), [Configuration](configuration.md) and [Naming patterns](../patterns/index.md)
    - [POSIX utility conventions](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html), [GNU standards: command-line interfaces](https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html), [Command Line Interface Guidelines](https://clig.dev/), [NO_COLOR](https://no-color.org/)
