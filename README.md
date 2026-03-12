# Orion Crawl Engine

Orion Crawl Engine is an asynchronous web crawling framework implemented in Python.  
It is designed to demonstrate scalable crawling architecture with modular components for URL scheduling, page retrieval, parsing, and persistent storage.

## Overview

The crawler follows a worker-based architecture where multiple asynchronous workers retrieve pages concurrently while maintaining a shared URL frontier.

## Key Characteristics

- asynchronous networking
- modular crawler architecture
- URL deduplication using fingerprints
- persistent storage layer
- extensible processing pipeline
- scalable worker pool

## Architecture

```
Seed URL
   │
URL Frontier
   │
Worker Pool
   │
HTTP Fetcher
   │
HTML Parser
   │
Processing Pipeline
   │
Storage Layer
```

## Installation

Clone the repository.

```
git clone https://github.com/YOUR_USERNAME/orion-crawl-engine
cd orion-crawl-engine
```

Install dependencies.

```
pip install -r requirements.txt
```

## Running

```
python run.py https://example.com
```

## Repository Layout

```
crawler/
network/
pipeline/
storage/
utils/
```

## License

MIT License

## Author

Yonathan
