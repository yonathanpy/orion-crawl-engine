<p align="center">
  <img src="https://img.icons8.com/fluency/512/search.png" width="200" alt="ORION-CRAWL-ENGINE" />
</p>

# ORION‑CRAWL‑ENGINE


Orion Crawl Engine is an asynchronous web crawling framework implemented in Python. The project is designed to explore the architecture of scalable crawling systems used for large scale information retrieval and automated data acquisition.

The repository focuses on the internal structure of a crawler rather than simple page downloading. The system separates networking, URL scheduling, worker orchestration, document processing, and storage into independent layers. This separation allows the crawler to be extended, scaled, or modified without altering core components.

The implementation demonstrates common crawler design patterns used in distributed data collection systems and search engine pipelines.

---

# System Overview

The crawler operates as a pipeline composed of several independent subsystems. Each subsystem performs a specific task in the crawling lifecycle.

```
Seed URL
   │
URL Frontier
   │
Scheduler
   │
Worker Runtime
   │
HTTP Fetch Layer
   │
HTML Parser
   │
Content Processing Pipeline
   │
Persistent Storage
```

The architecture allows the crawler to scale by increasing worker concurrency while maintaining centralized URL management.

---

# Core Subsystems

## Crawl Engine

The crawl engine coordinates the lifecycle of the crawling process. It initializes all subsystems and manages the asynchronous runtime environment.

Responsibilities include:

- initializing the URL frontier
- spawning the worker pool
- maintaining runtime configuration
- coordinating crawl execution

The engine operates on top of the Python asyncio runtime, enabling efficient concurrent network operations.

---

## URL Frontier

The URL frontier manages the queue of URLs waiting to be crawled. It acts as the scheduler responsible for determining which resources should be fetched next.

The frontier implements the following mechanisms:

- asynchronous queue scheduling
- URL fingerprint deduplication
- visited resource tracking
- safe concurrent queue access

Deduplication is implemented using hashed URL fingerprints to ensure that identical resources are not crawled multiple times.

---

## Worker Runtime

The worker runtime executes multiple concurrent crawling workers. Each worker retrieves URLs from the frontier, fetches remote content, and extracts additional links.

Worker execution cycle:

1. request next URL from frontier
2. perform asynchronous HTTP request
3. validate response
4. parse HTML document
5. process extracted data
6. submit discovered links to frontier

Workers operate as asynchronous tasks managed by the event loop.

---

## Network Fetch Layer

The network layer performs HTTP communication with remote servers. It handles connection management, request scheduling, and response retrieval.

Key properties include:

- asynchronous HTTP requests
- connection timeout handling
- response status validation
- network error isolation

The implementation uses aiohttp to support concurrent network operations without blocking the event loop.

---

## HTML Parsing System

The parsing layer converts raw HTML documents into structured representations.

Processing operations include:

- document title extraction
- hyperlink discovery
- raw textual content extraction
- metadata collection

HTML parsing is performed using BeautifulSoup which provides flexible document traversal and extraction capabilities.

---

## Content Processing Pipeline

After parsing, documents are passed through a processing pipeline responsible for transforming raw page data into structured records.

Processing stages include:

- metadata extraction
- content normalization
- document structuring
- optional transformation hooks

The pipeline architecture allows additional processing modules to be added without modifying the crawler core.

---

## Persistent Storage Layer

The storage layer persists crawled content and metadata. The current implementation uses SQLite for simplicity and portability.

Stored attributes include:

- page URL
- page title
- extracted text
- crawl timestamp

The storage module is designed to be replaceable with more advanced backends such as document stores or distributed databases.

---

# Concurrency Model

The crawler uses an event driven concurrency model based on Python's asyncio framework.

Advantages of this model include:

- efficient handling of network I/O
- reduced thread overhead
- scalable worker concurrency
- simplified asynchronous programming model

Each worker runs as a coroutine that interacts with the shared URL frontier.

---

# Repository Layout

```
crawler/
    engine.py
    frontier.py
    worker_pool.py
    scheduler.py

network/
    fetcher.py
    html_parser.py

pipeline/
    processor.py

storage/
    repository.py

utils/
    url_tools.py
    fingerprint.py
```

Each module is isolated and can be extended independently.

---

# Installation

Clone the repository.

```
git clone https://github.com/YOUR_USERNAME/orion-crawl-engine
cd orion-crawl-engine
```

Install dependencies.

```
pip install -r requirements.txt
```

---

# Running the Crawler

Start a crawl session using a seed URL.

```
python run.py https://example.com
```

Optional parameters allow configuration of:

- worker pool size
- crawl depth
- request timeout
- frontier queue size

---

# Potential Extensions

The system architecture allows many advanced extensions.

Examples include:

- distributed crawling clusters
- URL prioritization algorithms
- domain politeness policies
- content indexing systems
- machine learning based document classification
- large scale document storage systems

---

# License

MIT License

---

# Author

Yonathan  
aka Witwizard
