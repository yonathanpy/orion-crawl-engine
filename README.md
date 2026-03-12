# Orion Crawl Engine

Orion Crawl Engine is an asynchronous web crawling framework implemented in Python.  
The project focuses on demonstrating the internal architecture of a scalable crawler system including URL frontier management, concurrent page retrieval, HTML parsing pipelines, and persistent storage.

The design separates networking, crawling coordination, processing pipelines, and storage components into independent modules.

The repository serves as a reference implementation for studying crawler architecture and distributed data collection systems.

---

# System Architecture

The crawler follows a modular layered architecture.

```
Seed URL
   │
Frontier Manager
   │
Worker Pool
   │
Network Fetch Layer
   │
HTML Parsing
   │
Processing Pipeline
   │
Storage Repository
```

Each component is designed to remain independent and replaceable.

---

# Core Components

## Crawl Engine

The engine coordinates the full crawling lifecycle.  
It initializes the frontier, manages worker processes, and controls the event loop responsible for concurrent operations.

Responsibilities:

- bootstrap crawl session
- manage worker lifecycle
- coordinate frontier scheduling
- maintain crawl limits and runtime configuration

---

## URL Frontier

The frontier is responsible for scheduling URLs that still need to be crawled.

Features:

- asynchronous queue
- URL deduplication
- fingerprint based uniqueness
- scalable queue abstraction

The frontier ensures that each unique resource is visited only once.

---

## Worker Pool

The worker pool manages multiple asynchronous workers responsible for retrieving pages and discovering new links.

Each worker performs the following sequence:

1. request next URL from frontier
2. download HTML document
3. process page content
4. extract hyperlinks
5. submit discovered links back to frontier

Workers operate concurrently using Python's asyncio runtime.

---

## Network Fetch Layer

The fetch layer performs HTTP retrieval operations.

Key aspects:

- asynchronous HTTP requests
- request timeout control
- response validation
- error isolation

This layer is implemented using aiohttp to support concurrent network operations.

---

## HTML Parsing Layer

Downloaded documents are parsed to extract structured information.

Parsing includes:

- document title extraction
- hyperlink discovery
- raw text extraction
- metadata preparation

BeautifulSoup is used as the HTML parsing backend.

---

## Processing Pipeline

The processing pipeline transforms raw HTML into structured data records.

Responsibilities:

- page metadata extraction
- text normalization
- structured document creation
- pipeline extension hooks

The pipeline architecture allows additional processing stages to be inserted.

---

## Storage Layer

The storage layer persists crawled content.

The default implementation uses SQLite for simplicity, though the architecture allows other storage backends.

Stored attributes include:

- page URL
- page title
- extracted textual content

---

# Concurrency Model

The crawler uses an event driven concurrency model built on top of Python asyncio.

Key benefits:

- efficient I/O utilization
- non blocking network operations
- scalable worker model
- simplified concurrency control

Workers run as asynchronous tasks managed by the event loop.

---

# Repository Layout

```
crawler/
    engine.py
    frontier.py
    worker_pool.py

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

Configuration parameters include:

- worker pool size
- crawl limit
- request timeout

---

# Potential Extensions

The architecture allows several advanced extensions.

Examples include:

- distributed crawling across multiple nodes
- advanced URL prioritization algorithms
- politeness policies and domain throttling
- document indexing systems
- machine learning based content classification

---

# License

MIT License

---

# Author

Yonathan,aka Witwizard
