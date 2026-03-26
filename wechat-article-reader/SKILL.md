---
name: wechat-article-reader
description: WeChat Official Account article interpretation skill. Uses scripts to fetch WeChat Official Account article content and generate structured analysis. Triggered when users mention "interpret WeChat official account", "article interpretation", "official account interpretation", "interpret article" or provide a WeChat Official Account link. Supports extracting article title, author, publish time, and content, and outputs structured interpretation including overview, key points, notable takeaways, engagement context, and summary.
---

# WeChat Official Account Article Interpretation

## Workflow

### 1. Fetch Article Content

When the user provides a WeChat Official Account article link, use `scripts/fetch_article.py` to fetch the article:

```bash
python3 ./scripts/fetch_article.py "<article URL>"
```

Script dependencies:
- `playwright` - Browser automation
- `beautifulsoup4` - HTML parsing
- `lxml` - Parser

First-time setup requires installing dependencies:
```bash
pip install playwright beautifulsoup4 lxml
playwright install chromium
```

### 2. Generate Structured Interpretation

After fetching the article content, output the interpretation in the following format:

---
**<Title>**

**Overview** (Overview)
- What is the main topic/purpose?
- The author and their background
- Broader context

**Key Points** (Key Points)
- Extract 3-5 main themes or arguments
- Identify important insights or learnings
- Note technical concepts or frameworks discussed

**Notable Takeaways** (Notable Takeaways)
- Why this article is interesting or valuable
- Controversial or thought-provoking viewpoints
- Practical applications or lessons learned

**Engagement Context** (Engagement Context)
- Audience reaction (likes, replies, citations)
- High engagement indicates broad interest or controversy
- Reply count reflects discussion quality

**Summary** (Summary)
- 2-3 sentence overview
- Who should read this article and why?

---

## Interpretation Guidelines

- **Overview**: Briefly state the article's main idea and context
- **Key Points**: Extract the essence, avoid being verbose
- **Takeaways**: Highlight unique perspectives and practical value
- **Engagement**: Analyze reader feedback if available
- **Summary**: Help readers quickly determine if it's worth reading

## Script Documentation

`scripts/fetch_article.py` supports two output formats:

- Default: Markdown format
- `--json`: JSON format (easier for programmatic processing)

Examples:
```bash
# Markdown output
python3 scripts/fetch_article.py "https://mp.weixin.qq.com/s/xxx"

# JSON output
python3 scripts/fetch_article.py "https://mp.weixin.qq.com/s/xxx" --json
```
