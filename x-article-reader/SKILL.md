---
name: x-article-reader
description: Fetch and analyze X (Twitter) articles/posts using the Twitter API. Use when user provides an X post URL or post ID and wants to retrieve the article content and get an analysis/interpretation of the post. Handles both URL formats (x.com or twitter.com) and direct post IDs.
---

# X Article Reader

## Quick Start

Fetch an X article and analyze its content:

```bash
# Using post ID
scripts/fetch_x_article.py 2027463795355095314

# Using post URL
scripts/fetch_x_article.py https://x.com/trq212/status/2027463795355095314
```

The script returns JSON with article data including `title`, `contents` (array of paragraphs), `author` info, and engagement metrics.

## Setup

Before using this skill, set the Twitter API key environment variable:

```bash
export TWITTER_API_KEY=your_api_key_here
```

To make it persistent, add this to your shell profile (e.g., `~/.bashrc`, `~/.zshrc`):

```bash
echo 'export TWITTER_API_KEY=your_api_key_here' >> ~/.bashrc
source ~/.bashrc
```

The script will fail if `TWITTER_API_KEY` is not set.

## Analyzing the Article

After fetching, use the article data to provide a comprehensive interpretation:

### 1. Extract Key Information

From the API response:

- **Title**: `article.title` - The article headline
- **Contents**: `article.contents` - Array of text blocks (combine for full text)
- **Author**: `article.author.name` (@username) - Who wrote it
- **Engagement**: `article.replyCount`, `article.likeCount`, `article.quoteCount`, `article.viewCount`
- **Context**: `article.preview_text` - Brief summary

### 2. Structure Your Analysis

Provide a structured interpretation that includes:

**Overview**
- What is the main topic/purpose of the article?
- Who is the author and their background?
- What's the broader context?

**Key Points**
- Extract 3-5 main themes or arguments
- Identify important insights or learnings
- Note any technical concepts or frameworks discussed

**Notable Takeaways**
- What makes this article interesting or valuable?
- Any controversial or thought-provoking ideas?
- Practical applications or lessons

**Engagement Context**
- How has the audience responded (likes, replies, quotes)?
- High engagement suggests broad interest or controversy
- Reply count indicates discussion quality

**Summary**
- 2-3 sentence capsule summary
- Who should read this and why?

### 3. Tone and Style

- **Be concise**: Focus on substance, not fluff
- **Add context**: Connect to related topics when relevant
- **Be objective**: Present the author's views accurately
- **Use structure**: Bullets and headers make it readable
- **Add value**: Go beyond paraphrasing - provide interpretation

### 4. Language Style

- Match the user's language (Chinese if asked in Chinese)
- Use appropriate technical terminology
- Explain complex concepts clearly
- Use formatting (bold, code blocks) for emphasis

## Error Handling

Common issues and solutions:

**Invalid URL/ID**: The script will report "Could not extract tweet ID"
**API Error (403)**: API key issue or rate limiting
**Empty Response**: Network or API downtime

Always check the `status` field in the response (`success` vs `error`).

## Notes

- API key is read from `TWITTER_API_KEY` environment variable
- Supports both `x.com` and `twitter.com` URL formats
- Works with long-form articles and regular posts
- Author verification status is included (`isVerified`, `isBlueVerified`)
