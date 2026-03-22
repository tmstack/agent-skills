---
name: wechat-article-reader
description: 微信公众号文章解读技能。使用脚本获取公众号文章内容，并生成结构化分析解读。当用户提到"解读公众号"、"文章解读"、"公众号解读"、"解读文章"或提供微信公众号链接时触发。支持提取文章标题、作者、发布时间、正文内容，并输出包含概述、核心要点、值得注意的收获、互动情况、总结的结构化解读。
---

# 微信公众号文章解读

## 工作流程

### 1. 获取文章内容

当用户提供微信公众号文章链接时，使用 `scripts/fetch_article.py` 获取文章：

```bash
python3 ./scripts/fetch_article.py "<文章URL>"
```

脚本依赖：
- `playwright` - 浏览器自动化
- `beautifulsoup4` - HTML 解析
- `lxml` - 解析器

首次使用需安装依赖：
```bash
pip install playwright beautifulsoup4 lxml
playwright install chromium
```

### 2. 生成结构化解读

获取文章内容后，按以下格式输出解读：

---
**<标题>**

**概述** (Overview)
- 主要话题/目的是什么？
- 作者及其背景
- 更广泛的背景

**核心要点** (Key Points)
- 提取 3-5 个主要主题或论点
- 识别重要见解或学习内容
- 记录讨论的技术概念或框架

**值得注意的收获** (Notable Takeaways)
- 这篇文章有趣或有价值的原因
- 有争议或发人深省的观点
- 实际应用或经验教训

**互动情况** (Engagement Context)
- 受众反应（点赞、回复、引用）
- 高互动表明广泛兴趣或争议
- 回复数量反映讨论质量

**总结** (Summary)
- 2-3 句话的概述
- 谁应该阅读这篇文章以及为什么？

---

## 解读要点

- **概述**：简明扼要说明文章主旨和背景
- **核心要点**：提炼精华，避免流水账
- **收获**：突出独特观点和实用价值
- **互动**：如果可以获取，分析读者反馈
- **总结**：帮助读者快速判断是否值得阅读

## 脚本说明

`scripts/fetch_article.py` 支持两种输出格式：

- 默认：Markdown 格式
- `--json`：JSON 格式（便于程序处理）

示例：
```bash
# Markdown 输出
python3 scripts/fetch_article.py "https://mp.weixin.qq.com/s/xxx"

# JSON 输出
python3 scripts/fetch_article.py "https://mp.weixin.qq.com/s/xxx" --json
```
