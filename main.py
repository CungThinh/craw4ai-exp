import os
import json
import asyncio
from typing import Dict
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy

class OpenAIModelFee(BaseModel):
    model_name: str = Field(..., description="Name of the OpenAI model.")
    input_fee: str = Field(..., description="Fee for input token for the OpenAI model.")
    output_fee: str = Field(
        ..., description="Fee for output token for the OpenAI model."
    )

async def extract_structured_data_using_llm(
    provider: str, api_token: str = None, extra_headers: Dict[str, str] = None
):
    print(f"\n--- Extracting Structured Data with {provider} ---")

    if api_token is None and provider != "ollama":
        print(f"API token is required for {provider}. Skipping this example.")
        return

    browser_config = BrowserConfig(headless=True)

    extra_args = {"temperature": 0, "top_p": 0.9, "max_tokens": 2000}
    if extra_headers:
        extra_args["extra_headers"] = extra_headers

    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        word_count_threshold=1,
        page_timeout=80000,
        extraction_strategy=LLMExtractionStrategy(
            llm_config = LLMConfig(provider=provider,api_token=api_token),
            schema=OpenAIModelFee.model_json_schema(),
            extraction_type="schema",
            instruction="""From the crawled content, extract all mentioned model names along with their fees for input and output tokens. 
            Do not miss any models in the entire content.""",
            extra_args=extra_args,
        ),
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://openai.com/api/pricing/", config=crawler_config
        )
        print(result.extracted_content)

if __name__ == "__main__":

    asyncio.run(
        extract_structured_data_using_llm(
            provider="anthropic/claude-3-5-sonnet-20240620", api_token=os.getenv("ANTHROPIC_API_KEY")
        )
    )