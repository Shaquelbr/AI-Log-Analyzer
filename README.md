# NVIDIA Log Analyzer with Cloud Inference

A production ready log investigation tool that blends traditional signature matching with cloud level intelligence from NVIDIA NIM. This project demonstrates real ability to build developer tooling, integrate enterprise grade AI inference, package software professionally, and ship end to end solutions suitable for real world engineering environments.

This is a showcase project designed to highlight modern software craftsmanship, cloud AI integration, containerization, testing discipline, observability, and CLI ergonomics. If you are reviewing this for technical ability, the project structure, technology choices, and implementation quality reflect a strong focus on reliability and maintainability.

## Project Overview

This tool performs two categories of analysis:

### Local Analysis

* Signature based pattern matching
* Lightweight summarization for long logs
* Instant feedback with no network requirement

### NVIDIA Cloud Analysis

* Cloud inference through NVIDIA NIM
* Uses the Meta Llama 3.1 Instruct family
* Provides deep reasoning and root cause insight
* Handles unstructured logs of any size

This demonstrates practical integration of frontier model APIs in a clean Python toolkit designed for operational use.

## Key Features

* Developer friendly CLI with Click
* FastAPI server for REST level usage
* NVIDIA NIM inference support through the integrate API
* Clean modular architecture under the analyzer package
* Docker ready for immediate deployment
* Full pytest suite
* GitHub Actions continuous integration
* Local pattern matching engine for immediate diagnosis
* NIM powered cloud analysis for difficult investigations

## Tech Stack

### Core

* Python
* Click
* FastAPI
* Pydantic
* Requests

### Cloud

* NVIDIA NIM integrate API
* Meta Llama 3.1 models

### Packaging

* Python project metadata through pyproject
* Editable install for development
* CLI entry points defined at install time

### DevOps

* Docker image
* GitHub Actions
* Automated testing and linting

## Installation

Clone the repository:

```
git clone https://github.com/<yourname>/nvda_log_analyzer
cd nvda_log_analyzer
```

Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install the package:

```
pip install .
```

Set your NVIDIA API key:

```
export NVIDIA_API_KEY="your key"
```

## CLI Usage

### Local analysis

```
log_analyzer analyze path/to/logfile.log
```

### NVIDIA cloud analysis

```
log_analyzer nim path/to/logfile.log
```

## API Usage

Start the server:

```
uvicorn analyzer.api:app reload
```

Open API documentation:

```
http://127.0.0.1:8000/docs
```

## Docker

Build the container:

```
docker build . t nvda_log_analyzer
```

Run the container:

```
docker run p 8000:8000 nvda_log_analyzer
```

## Architecture Overview

The analyzer package includes:

* parser for log preprocessing
* signature engine for pattern recognition
* ai client for NIM inference
* api server with FastAPI
* cli wrapper

## Roadmap

Future enhancements may include:

* Streaming token responses through NIM
* Model selection flags
* Structured log format support
* Automatic severity scoring
* Export to HTML or PDF reports
* GPU enabled local inference
