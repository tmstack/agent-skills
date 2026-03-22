---
name: wechat-article
description: WeChat Official Account (公众号) article fetcher and interpreter. Fetch article content as Markdown, summarize, and answer questions about it.
metadata: {"emoji": "📰"}
read_when:
  - User asks to fetch or summarize a WeChat article (mp.weixin.qq.com)
  - User provides a WeChat article URL and wants it read/analyzed
  - User mentions "微信文章", "公众号文章", "WeChat article"
---

# WeChat Article Fetcher & Interpreter

## Overview

This skill fetches articles from WeChat Official Accounts (mp.weixin.qq.com) using Playwright + BeautifulSoup, converts them to Markdown, and provides interpretation/summarization.

## Installation

```bash
# Install Python dependencies
pip install playwright beautifulsoup4 lxml

# Install Playwright browser
playwright install chromium
```

## Setup

1. Save the fetch script to your workspace:
```bash
mkdir -p ~/.openclaw/workspace/skills/wecom-article/scripts
cp /path/to/fetch_weixin.py ~/.openclaw/workspace/skills/wecom-article/scripts/
chmod +x ~/.openclaw/workspace/skills/wecom-article/scripts/fetch_weixin.py
```

2. Verify installation:
```bash
python3 ~/.openclaw/workspace/skills/wecom-article/scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/example"
```

## Usage

### Fetch an Article

When user provides a WeChat article URL:

```bash
# Fetch as Markdown
python3 ~/.openclaw/workspace/skills/wecom-article/scripts/fetch_weixin.py "$URL"

# Fetch as JSON (for programmatic use)
python3 ~/.openclaw/workspace/skills/wecom-article/scripts/fetch_weixin.py "$URL" --json
```

### Save Fetched Content

After fetching, save to a file for reference:

```bash
python3 ~/.openclaw/workspace/skills/wecom-article/scripts/fetch_weixin.py "$URL" > /tmp/article.md
```

## Common Issues & Solutions

### 1. Captcha/Verification Wall
**Problem:** WeChat shows a verification page requiring user interaction.

**Solutions:**
- Try adding a delay before fetching:
  ```python
  await page.wait_for_timeout(3000)  # Wait 3 seconds
  ```
- Use a non-headless browser temporarily to debug:
  ```python
  browser = await p.chromium.launch(headless=False)
  ```
- Some articles require following the official account first — inform the user

### 2. Content Not Found
**Problem:** Script returns "Could not find article content (#js_content)"

**Causes:**
- Article has been deleted
- URL is invalid
- Access restrictions (need to follow author)

**Solution:** Inform user and ask them to verify the URL or copy content directly.

### 3. Timeout Errors
**Problem:** Page load times out

**Solution:** Increase timeout in the script:
```python
await page.goto(url, wait_until="domcontentloaded", timeout=60000)  # 60 seconds
```

### 4. Missing Images
**Problem:** Images don't display in output

**Reason:** WeChat uses lazy-loading with `data-src` attribute

**Current handling:** Script already extracts `data-src`, but images may still fail if:
- Images require authentication
- Images have expired
- Images have external hotlinking protection

## Workflow

When user asks to fetch/summarize a WeChat article:

1. **Validate URL** — Ensure it's from mp.weixin.qq.com
2. **Fetch content** — Run the fetch script
3. **Handle errors** — If captcha/verification:
   - Take a screenshot to show user
   - Ask user to copy content or provide alternative
4. **Process content** — If successful:
   - Save article to /tmp/ for reference
   - Provide summary/analysis as requested
   - Answer follow-up questions

## Example Conversation

**User:** "Summarize this article https://mp.weixin.qq.com/s/xxxxx"

**Assistant:**
```bash
# Fetch the article
python3 ~/.openclaw/workspace/skills/wecom-article/scripts/fetch_weixin.py "https://mp.weixin.qq.com/s/xxxxx" > /tmp/article.md
```

Then read and summarize:
```bash
# Read the fetched content
read /tmp/article.md
```

Provide summary in own words, highlighting key points.

## Output Format

The script returns Markdown with frontmatter:

```markdown
---
title: "Article Title"
author: "Author Name"
date: "Publish Date"
url: "Original URL"
---

# Article Title

Article content in Markdown format...
```

## Security Notes

- WeChat articles may contain tracking scripts — Playwright helps avoid executing them
- Some articles are paywalled or require login — respect these restrictions
- Always inform user when content cannot be accessed due to restrictions

## Related Skills

- **tencent-docs** — For Tencent Docs (docs.qq.com)
- **agent-browser** — For general web scraping when this script fails
- **summarize** — For summarizing other types of content
