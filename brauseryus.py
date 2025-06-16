from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import BrowserSession, Agent
import os
from dotenv import load_dotenv
load_dotenv()

import asyncio
import logging

# Minimize logs from libraries
logging.getLogger("browser_use").setLevel(logging.WARNING)
logging.getLogger("langchain").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("backoff").setLevel(logging.ERROR)

# Check for Google API Key
if not os.getenv("GOOGLE_API_KEY"):
    raise EnvironmentError("GOOGLE_API_KEY environment variable is not set. Please set it in your .env file or environment.")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

import json

async def main():
    browser_session = BrowserSession(
        browser_name="chrome",
        playwright_options={
            "headless": True,
            "args": [
                "--disable-gpu",
                "--disable-software-rasterizer",
                "--disable-dev-shm-usage",
                "--no-sandbox",
                "--disable-features=VizDisplayCompositor",
                # --- Anti-bot/CAPTCHA/Cloudflare options ---
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars",
                "--disable-web-security",
                "--disable-site-isolation-trials",
                "--disable-extensions",
                "--window-size=1920,1080",
                # You may also want to use a proxy or rotate IPs for some sites
            ],
            # Set a realistic user-agent
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            # Enable stealth mode if supported by browser_use
            "stealth": True,
            # Example: Use a residential proxy (replace with your proxy details)
            # "proxy": {
            #     "server": "http://username:password@proxy_ip:proxy_port"
            # }
        }
    )
    agent = Agent(
        task="Tolong carikan pendapat warga di komentar youtube terkait masalah KTP dan tanah dan sentimennya",
        llm=llm,
        browser_session=browser_session,
    )
    import json
    import logging
    # Completely suppress all logs and warnings
    logging.disable(logging.CRITICAL)

    result = await agent.run()

    # Try to extract and prettify Instagram comments from the agent output
    def prettify_comments(res):
        import re
        if isinstance(res, dict):
            text = json.dumps(res)
        else:
            text = str(res)
        # Try to extract JSON list from markdown/code block
        match = re.search(r"```json\\n([\s\S]+?)```", text)
        if match:
            try:
                comments = json.loads(match.group(1))
                if isinstance(comments, list):
                    lines = ["Komentar Instagram terkait KTP dan tanah:"]
                    for i, item in enumerate(comments, 1):
                        src = item.get("source", "-")
                        content = item.get("content", "-")
                        lines.append(f"{i}. [Sumber: {src}] {content}")
                    return "\n".join(lines)
            except Exception:
                pass
        # Try to extract all comment-like lines (with source or mentioning KTP/tanah)
        lines = []
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            if re.search(r"(Instagram|source|sumber|ktp|tanah|comment|komentar)", line, re.I):
                # Remove leading bullets or numbers
                line = re.sub(r"^[\-*\d.\s]+", "", line)
                lines.append(line)
        if lines:
            pretty = ["Komentar terkait KTP dan tanah:"]
            for idx, l in enumerate(lines, 1):
                pretty.append(f"{idx}. {l}")
            return "\n".join(pretty)
        # Fallback: just pretty print the whole result, removing excess blank lines
        text = re.sub(r"\n{2,}", "\n", text)
        return text.strip() or "Tidak ada komentar yang ditemukan."

    pretty = prettify_comments(result)
    print(pretty)

if __name__ == "__main__":
    asyncio.run(main())