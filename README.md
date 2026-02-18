# ComfyUI Custom Node Template

A standardized custom node template designed for the **ComfyUI Registry**. It provides a streamlined workflow for both human developers and AI assistants (e.g. Antigravity), ensuring best practices from project initialization to publishing.

> 一个面向 ComfyUI Registry 标准设计的自定义节点模版，为开发者和 AI 助手提供标准化的操作流程。

## Quick Start

### 1. Initialize Project
- **Copy & rename** this template folder to your project name (e.g. `ComfyUI-My-Awesome-Node`).
- Run `git init` in the new directory.

### 2. Configure Metadata
Edit the following fields in `pyproject.toml`:
- `name` — Unique identifier for your node (use `comfyui-<your-id>` format).
- `version` — Start with `0.0.1`.
- `PublisherId` — Your Publisher ID from [registry.comfy.org](https://registry.comfy.org).
- `DisplayName` — Name shown in the ComfyUI menu.

### 3. Develop Your Node
- **`nodes.py`** — Implement your node logic following the `INPUT_TYPES`, `RETURN_TYPES`, `FUNCTION`, `CATEGORY` conventions.
- **`__init__.py`** — Make sure `NODE_CLASS_MAPPINGS` includes your new class so ComfyUI can load it.

### 4. Publish
- Add `REGISTRY_ACCESS_TOKEN` as a GitHub repository secret (obtain it from the Registry website).
- The included GitHub Action automatically publishes your node to the ComfyUI Registry whenever you bump the `version` in `pyproject.toml` and push to `main`.

## AI Assistant Prompt (Copy-Paste)

If you are using a coding AI assistant, paste the following prompt to bootstrap your project:

> "Create a new ComfyUI node based on the `ComfyUI-Node-Template`.
> 1. Update `pyproject.toml`: set name to `comfyui-<description>`, PublisherId to `<your-id>`.
> 2. Implement a node in `nodes.py` that does `<describe functionality>`.
> 3. Inputs should include `<param1>, <param2>`, output type is `<type>`.
> 4. Update `__init__.py` to register the node.
> 5. Verify `.gitignore` and GitHub Action configs are correct."

## Project Structure

```
.
├── .github/workflows/publish.yml  # Auto-publish action, triggers on pyproject.toml changes
├── .gitignore                     # Pre-configured for Python, venvs, ComfyUI data dirs
├── __init__.py                    # Node registration (NODE_CLASS_MAPPINGS)
├── nodes.py                       # Example node with common input types (IMAGE, INT, FLOAT, STRING)
├── pyproject.toml                 # Registry-compliant config (https://docs.comfy.org/registry/specifications)
└── examples/                      # Workflow examples
    └── basic_workflow.json        # Example workflow for ExampleNode
```

## License

MIT
