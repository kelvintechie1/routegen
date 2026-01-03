# Nix

Jargen includes a basic devshell for the nix-included/enabled.

It mainly patches nix compatibility but also includes some developments tools like pre-commit hooks.
The shell mainly patches/shims compatbility and lets python dependency management be handled by uv under its lock.
This enables single source of dependency management and total cross system compatbility, among Windows/Linux/MacOS with or without nix.

## Suggsted Requirements

- Nix
- Direnv (with nix-direnv as well)

Direnv is a 


## Suggested `.envrc`

Here is the file I use:

```
watch_file nix/shell.nix
use flake
layout python3
export UV_PROJECT_ENVIRONMENT="$VIRTUAL_ENV"
uv sync --all-groups
```
