# Project-local MCP delivery rules

When creating or modifying a project-local MCP server, also update the global Codex MCP registry at `C:\Users\wang_\.codex\config.toml` with the matching `[mcp_servers.<name>]` entry, unless the user explicitly says not to.

Keep secrets such as API keys in the project `.env` file when the server can load them there. Put only non-sensitive runtime paths and required launch environment variables in `config.toml`.

For each MCP server delivery, verify these items:
- Server code exists in the project directory.
- Dependencies are installed in the project virtual environment.
- A local smoke test can import the server and list tools.
- `C:\Users\wang_\.codex\config.toml` contains the server registration.
- The user is told to restart or reload Codex so the new MCP server appears.
