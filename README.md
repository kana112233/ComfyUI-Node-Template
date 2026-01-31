# ComfyUI Custom Node Template

这是一个面向 **ComfyUI Registry** 标准设计的自定义节点模版。它为人类开发者和 AI 助手（如 Antigravity）提供了一套标准化的操作流程，确保项目从初始化到发布都能遵循最佳实践。

## 🚀 快速开始 (AI & Humans)

如果你是 AI 助手或正在指导 AI 助手开始一个新项目，请遵循以下标准化流程：

### 1. 项目初始化
- **重命名文件夹**: 将此模版文件夹复制并重命名为你的项目名（例如 `ComfyUI-My-Awesome-Node`）。
- **初始化 Git**: 在新目录下运行 `git init`。

### 2. 配置元数据 (核心步骤)
修改 `pyproject.toml` 中的以下字段：
- `name`: 节点的唯一标识符（建议使用 `comfyui-<your-id>` 格式）。
- `version`: 初始版本建议为 `0.0.1`。
- `PublisherId`: 你在 [registry.comfy.org](https://registry.comfy.org) 上的 Publisher ID。
- `DisplayName`: 在 ComfyUI 菜单中显示的名称。

### 3. 开发节点代码
- **`nodes.py`**: 在此类中实现你的节点逻辑。遵循 `INPUT_TYPES`, `RETURN_TYPES`, `FUNCTION`, `CATEGORY` 规范。
- **`__init__.py`**: 确保 `NODE_CLASS_MAPPINGS` 包含你的新类，以便 ComfyUI 加载。

### 4. 发布与分发
- **GitHub Secret**: 在仓库设置中添加 `REGISTRY_ACCESS_TOKEN`（从 Registry 网站获取）。
- **自动发布**: 每次更新 `pyproject.toml` 中的 `version` 并推送到 `main` 分支时，GitHub Action 会自动将节点发布到 ComfyUI Registry。

---

## 🤖 AI 助手集成提示词 (Copy-Paste)

如果你使用的是代编码 AI 助手，可以粘贴以下指令来启动项目：

> "请基于 `ComfyUI-Node-Template` 模版为我创建一个新的 ComfyUI 节点。
> 1. 修改 `pyproject.toml`：项目名设为 `comfyui-<描述>`, PublisherId 设为 `<你的ID>`。
> 2. 在 `nodes.py` 中实现一个功能为 `<描述功能>` 的节点。
> 3. 确保输入参数包含 `<参数1>, <参数2>`，输出为 `<类型>`。
> 4. 更新 `__init__.py` 完成注册。
> 5. 检查 `.gitignore` 和 GitHub Action 配置是否正确。"

---

## 📁 目录结构说明
- `.github/workflows/publish.yml`: 自动发布脚本，仅监听 `pyproject.toml` 的变动。
- `.gitignore`: 预配置了 Python 缓存、虚拟环境及 ComfyUI 数据目录的忽略规则。
- `nodes.py`: 包含了一个带有常用输入类型（图像、数值、字符串、开关）的示例节点。
- `pyproject.toml`: 符合 [ComfyUI Registry Specifications](https://docs.comfy.org/registry/specifications) 的配置文件。
