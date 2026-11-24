# pyrefly-lsp

[Pyrefly](https://pyrefly.org) language server for Claude Code, providing type errors and code intelligence for `.py` and `.pyi` files.

## Installation

Pyrefly must be on your `PATH`:

```bash
pip install pyrefly
```

Then, in Claude Code:

```
/plugin marketplace add pyrefly-org/pyrefly
/plugin install pyrefly-lsp@pyrefly
```

Pyrefly reads your project's `pyrefly.toml` or `pyproject.toml`, as it does on the command line.
