# 机器人材料学：从选材到制造

中文学习站，围绕机器人零件的选材、制造、连接和验证展开。包含 16 个内容页面、三类机器人零件案例，以及构建时实际执行的质量、挠度和热膨胀计算。

在线阅读：https://tiansongyu.github.io/robot-materials/

内容入口：[docs/index.md](docs/index.md)。建议从学习路线开始，依次阅读基础、材料、工艺、选材与实验。案例参数明确标为教学假设，材料数据附原始来源；内容不替代具体零件的设计与验证。

## 本地构建

需要 Python 3.10 或更高版本；首次安装与准备渲染资源需要联网。

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-docs.txt
.venv/bin/python scripts/vendor_assets.py
.venv/bin/python -m sphinx -E -a -W --keep-going -n -D nb_execution_mode=force -b html docs docs/_build/html
.venv/bin/python scripts/check_links.py
.venv/bin/python -m http.server 8000 --bind 127.0.0.1 --directory docs/_build/html
```

打开 http://127.0.0.1:8000/ 。Windows 将 `.venv/bin/python` 换为 `.venv\Scripts\python`。

站点使用 Sphinx、Read the Docs 官方主题、MyST-NB 和 Mermaid。Notebook 在构建时执行；网页不是在线 Python 环境。Mermaid 11.12.2 与 MathJax 3.2.2 从 npm 官方注册表下载到忽略提交的目录，并随 HTML 部署，读者无需访问第三方 CDN。相应许可证随资源保留。下载脚本固定版本，但未做独立供应链完整性审计。

## 发布与维护

`.github/workflows/pages.yml` 在 main 分支更新后严格构建、强制执行计算、检查本地链接，再部署 GitHub Pages。PR 只构建验证。仓库 Pages 发布方式须设为 GitHub Actions。

正文使用 MyST Markdown。新增页面需登记在 `docs/index.md` 的目录中；引用数据时保留牌号、状态、温湿度、试验方向和资料版本。数据来源见 [docs/sources.md](docs/sources.md)。

修改计算假设时同时检查正文解释和断言。构建成功不代表外部链接长期可用或所有材料结论均经过实物试验。
