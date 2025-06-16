import logging
# Suppress all noisy logs as early as possible
logging.basicConfig(level=logging.CRITICAL)
logging.getLogger("browser_use").setLevel(logging.CRITICAL)
logging.getLogger("langchain_ollama").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)
logging.getLogger("backoff").setLevel(logging.CRITICAL)
logging.disable(logging.CRITICAL)

from langchain_ollama import ChatOllama
from browser_use import Agent
import os
from dotenv import load_dotenv
load_dotenv()
import asyncio

llm = ChatOllama(model="qwen3:8b")

async def main():
    try:
        agent = Agent(
            task="cari UU terkait ktp dan tanah",
            llm=llm,
        )
        result = await agent.run()
        print(result)
    except Exception as e:
        msg = str(e)
        if "ResourceExhausted" in msg or "quota" in msg or "exhausted" in msg:
            print("[ERROR] Kuota LLM Google Gemini Anda sudah habis atau dibatasi. Silakan cek API key dan kuota Anda di Google Cloud Console.")
        elif "API key" in msg or "connect to LLM" in msg:
            print("[ERROR] Tidak bisa terhubung ke LLM. Pastikan GOOGLE_API_KEY sudah benar dan koneksi internet aktif.")
        else:
            print(f"[ERROR] Terjadi kesalahan: {msg}")

asyncio.run(main())