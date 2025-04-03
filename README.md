# Extracting OpenAI Pricing Data Using LLM and AsyncWebCrawler

## Overview
This project demonstrates how to extract structured pricing data for OpenAI models using the `crawl4ai` library. The script leverages an LLM-powered extraction strategy to crawl OpenAI's pricing page and retrieve details on model names and their associated token fees.

## Features
- Uses `crawl4ai` for asynchronous web crawling.
- Extracts structured data using an LLM-based approach.
- Supports multiple LLM providers (e.g., OpenAI, Anthropic).
- Configurable extraction parameters such as temperature, top-p, and max tokens.

## Requirements
- Python 3.8+
- API access to an LLM provider (Anthropic)
- Required Python libraries:
  - `crawl4ai`
  - `pydantic`
  - `asyncio`

## Run
```sh
pip install crawl4ai
crawl4ai-setup
python3 main.py
export ANTHROPIC_API_KEY=your-anthropic-api-key
