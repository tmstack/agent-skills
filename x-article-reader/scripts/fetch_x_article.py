#!/usr/bin/env python3
"""
Fetch X (Twitter) article using Twitter API.

Usage:
    python fetch_x_article.py <post_url_or_id>

Examples:
    python fetch_x_article.py 2027463795355095314
    python fetch_x_article.py https://x.com/trq212/status/2027463795355095314
"""

import sys
import json
import re
import os
import urllib.request
import urllib.error

API_URL = "https://api.twitterapi.io/twitter/article"
API_KEY = os.environ.get("TWITTER_API_KEY")


def extract_tweet_id(input_str):
    """Extract tweet ID from URL or return as-is if it's already an ID."""
    # Try to match x.com/status/{id} pattern
    x_pattern = r'x\.com/[^/]+/status/(\d+)'
    match = re.search(x_pattern, input_str)
    if match:
        return match.group(1)

    # Try to match twitter.com/status/{id} pattern
    twitter_pattern = r'twitter\.com/[^/]+/status/(\d+)'
    match = re.search(twitter_pattern, input_str)
    if match:
        return match.group(1)

    # If it looks like a numeric ID, return as-is
    if input_str.strip().isdigit():
        return input_str.strip()

    raise ValueError(f"Could not extract tweet ID from: {input_str}")


def fetch_article(tweet_id):
    """Fetch article from Twitter API."""
    if not API_KEY:
        raise ValueError("TWITTER_API_KEY 环境变量未设置，请先设置该环境变量")

    url = f"{API_URL}?tweet_id={tweet_id}"
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json',
        'User-Agent': 'curl/7.64.1'
    }

    req = urllib.request.Request(url, headers=headers, method='GET')

    try:
        with urllib.request.urlopen(req) as response:
            response_text = response.read().decode('utf-8')
            # Handle empty response
            if not response_text.strip():
                raise Exception("Empty response from API")
            data = json.loads(response_text)
            return data
    except urllib.error.HTTPError as e:
        try:
            error_msg = json.loads(e.read().decode('utf-8'))
            raise Exception(f"API Error ({e.code}): {error_msg}")
        except:
            raise Exception(f"API Error ({e.code}): {e.reason}")
    except Exception as e:
        raise Exception(f"Failed to fetch article: {str(e)}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_x_article.py <post_url_or_id>")
        print("Example: python fetch_x_article.py 2027463795355095314")
        print("Example: python fetch_x_article.py https://x.com/trq212/status/2027463795355095314")
        sys.exit(1)

    input_str = sys.argv[1]

    try:
        # Extract tweet ID
        tweet_id = extract_tweet_id(input_str)
        print(f"Fetching article for tweet ID: {tweet_id}", file=sys.stderr)

        # Fetch article
        data = fetch_article(tweet_id)

        # Print JSON result
        print(json.dumps(data, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
