# Yeqiao Fu · Research & Systems

个人研究与工程作品集：[fyq5166.github.io](https://fyq5166.github.io/)。保留 Jekyll / GitHub Pages 框架；主页使用原生 HTML、CSS、JavaScript，无前端打包步骤。

## 唯一内容源

**直接修改本仓库，不再维护独立的设计预览副本。**

| 位置 | 用途 |
| --- | --- |
| `index.html` | 主页内容、样式、交互。保留顶部 `layout: null` 的 Jekyll front matter |
| `assets/reports/` | 对外公开的项目报告与摘要；更新前检查私人信息、链接与版本 |
| `assets/*.svg` | 项目说明图：统一视觉语言，不用图号 |
| `assets/profile-pics/yeqiao-fu.png` | 头像，避免嵌入大段 base64 |
| `research-resume.pdf` | 主页简历入口 |
| `assets/cv/Resume_Yeqiao.pdf` | 旧简历链接；更新时与上一文件同步，保持字节一致 |
| `_config.yml` | Jekyll 配置；开发脚本与维护文档不发布 |
| `_projects/`, `_layouts/`, `_data/`, `libs/` | 旧站内容/路径与资源；不是新主页的内容源，不随意删除 |

`__deploy.sh` 是旧模板的大学服务器部署脚本，**不是本站发布流程，不要执行**。

## 固定工作流

1. 确认分支和现有改动；从开发分支开始。不要覆盖不属于本次任务的修改。
2. 根据用户确认的简历/项目叙述修改主页。原始私有材料不复制进公开仓库。
3. 运行结构检查与编号回归测试：
   ```sh
   python3 scripts/check_site.py
   node tests/project_index.cjs
   ```
   Python 需要 3.9+；Node 只用于测试，不是网站运行依赖。不自动安装依赖。
4. 从仓库启动主页预览：
   ```sh
   python3 scripts/preview.py --port 8766
   ```
   打开 <http://127.0.0.1:8766/>。端口占用时换一个端口；不要终止未知进程。此脚本只在本机监听、隐藏仓库内部文件，并在响应中移除 front matter。**它不是完整 Jekyll 构建，不验证旧项目页面或 Liquid 模板。**
5. 完成下方浏览器验收，再让用户看本地版。
6. 只有用户明确同意后才提交、推送或发布。检查最终 diff；使用 Conventional Commit。GitHub Pages 当前从 `master` 根目录构建，开发分支不会直接替代线上站点。
7. 发布后检查 GitHub Pages 构建结果，再确认线上主页、项目直达链接、图和简历可用。推送成功不等于发布成功。

### 完整 Jekyll 构建环境

本机使用独立的 Homebrew Ruby 3.3（验证版本 3.3.12），不替换 macOS 系统 Ruby。Bundler 2.4.22 和锁定的 Jekyll 3.10.0 依赖安装在 `~/.local/share/portfolio-build/`，不进入仓库或网站。

环境补齐后，每次直接运行：
```sh
sh scripts/jekyll.sh build --trace
sh scripts/jekyll.sh doctor
python3 tests/check_build.py
# 完整站点预览（含旧项目页面）：
sh scripts/jekyll.sh serve --host 127.0.0.1 --port 4000
```

新机器首次安装（会访问网络，须经设备使用者批准）：
```sh
brew install ruby@3.3
export PATH="$(brew --prefix ruby@3.3)/bin:$PATH"
export GEM_HOME="$HOME/.local/share/portfolio-build/tooling"
export GEM_PATH="$GEM_HOME"
export BUNDLE_PATH="$HOME/.local/share/portfolio-build/bundle"
export BUNDLE_FROZEN=true
gem install bundler -v 2.4.22 --no-document
"$GEM_HOME/bin/bundle" _2.4.22_ install
```

构建脚本不会自动安装、升级或修改依赖锁定文件。其他 Ruby 安装位置可通过 `PORTFOLIO_RUBY_BIN` 指定；专用依赖目录可通过 `PORTFOLIO_BUILD_HOME` 指定。生成的 `_site/` 不提交。GitHub Pages 云端构建环境由 GitHub 管理，本地通过后仍需验证云端构建结果。

依赖缺失时应如实记录“完整 Jekyll 构建未验证”，不要把主页预览成功说成整站构建成功。新增/升级依赖需要单独批准。

## 内容与表达约定

- 首页卡片先说明**解决什么问题**，不要只列技术名词。短摘要讲贡献与已实现的程度。
- 所有详情统一顺序：**The goal → My contribution → 可选说明图 → Outcome → What I learned → Tools → Resources**。
- Goal 是研究动机，不是成果保证；Contribution 明确本人工作和合作者边界；Outcome 写交付物、观察和验证范围；Lessons 写实际获得的认识，避免重复结果。
- 让大一学生能读懂：首次出现的必要术语用日常语言解释，不堆实现细节。每项贡献以简短加粗重点开头，通常 2–3 条。
- 不把局部原型写成生产系统，不把目标写成证明，不虚构指标/隐私保障/训练收益。公开但未清理的代码注明 development branch；不开源不等于没有完整工作，但不能暴露内部资料。
- 角色与 supervisor/group 的表述在卡片、详情、时间线保持一致。时间线大标题为 work，小标题为职位及 supervisor/group；教育条目不强行套用研究角色。
- 图解释关键工作流程，不能盖过内容；保持纸白/森林绿、字体、线条风格一致。图要有说明、alt、固定尺寸，必要时提供原图入口。
- 可公开的代码、论文和项目站链接同时放在详情顶部与底部。没有公开资源时诚实说明，不制造占位链接或为私有项目添加假的公开入口。

## 添加或调整一个项目

1. 在 `.work-grid` 中复制一种已有 `.work-card` 结构，填写类别、日期、标题、定位、角色/背景、摘要。
2. 为项目选一个**稳定 slug**。卡片按钮的 `data-dialog="detail-SLUG"` 指向唯一 `<dialog id="detail-SLUG" class="project-dialog">`。同步唯一标题 ID、`aria-labelledby`、关闭按钮的可访问名称。
3. 按统一详情结构填充内容；保留 `.detail-lead`、`.detail-results`、`.detail-learning` 和返回/分享元素。复制按钮的 `data-copy-project="SLUG"` 及备用链接 `?project=SLUG#work` 必须一致。
4. 如有对应经历，时间线按钮使用同一个 `data-dialog`，不要复制另一份详情。按日期排列时间线；按希望访客阅读的顺序排列 Work。
5. **不要手写 `01 of 08`、总项目数或图号。** `syncProjectIndex()` 从 Work 卡片顺序自动生成编号/总数/详情位置；时间线中的重复入口不增加计数。增删/重排卡片后重新加载即可。
6. 旧 slug 是分享链接的一部分，不为显示名变化随意改 slug。链接形式：`https://fyq5166.github.io/?project=SLUG#work`。
7. 更新资源链接时同时检查详情顶部和底部。资源路径须在仓库内存在；外链新标签使用 `rel="noopener noreferrer"`。
8. 跑检查并复核新项目不比现有项目更密、更长或使用另一套格式。

## 浏览器验收清单

- 桌面与窄屏（如 390px）：无横向溢出；导航、卡片、图和详情可读。
- Work 与时间线的每个入口打开正确详情；关闭/Escape/点击遮罩返回原浏览位置及焦点。
- 浏览器后退关闭详情，前进重新打开；刷新项目 URL 仍打开正确项目。
- 新标签直接访问分享链接，关闭后留在本站；未知 slug 不导致页面报错。
- Copy project link 成功；剪贴板不可用时提供可手动复制的链接。
- Tab 焦点在弹窗内，关闭后回到入口；按钮焦点可见。
- 项目数和次序正确；公共资源链接、简历、原图入口正确；浏览器无新增错误。
- `check_site.py` 是结构与本地资源检查，**不验证事实真实性、外网链接可用性或浏览器交互**；这些仍需人工/浏览器验收。
