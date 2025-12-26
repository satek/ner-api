# spaCy NER API (GPU-enabled)

A minimal, containerized **Named Entity Recognition (NER) service** built with **FastAPI** and **spaCy’s transformer backend**.  
Designed for **high-accuracy NER**, **GPU acceleration**, and **batch processing**.

The service exposes a small HTTP API that accepts text and returns extracted named entities as JSON.

---

## Features

- Transformer-based NER (`en_core_web_trf`)
- GPU support via NVIDIA CUDA
- Single-text and batch endpoints
- Simple JSON in / JSON out
- Configurable port via environment variable
- Self-contained Docker image

---

## API Endpoints

### `POST /ner`

Extract entities from a single text.

**Request**

```json
{
  "text": "Apple acquired a startup in London for $1B"
}
```

**Response**

```json
{
  "entities": [
    { "text": "Apple", "label": "ORG", "start": 0, "end": 5 },
    { "text": "London", "label": "GPE", "start": 28, "end": 34 },
    { "text": "$1B", "label": "MONEY", "start": 39, "end": 42 }
  ]
}
```

### `POST /ner/batch`

Process multiple texts efficiently using batching.

**Request**

```json
{
  "texts": [
    "Apple bought a company in London.",
    "Microsoft announced earnings in Seattle."
  ],
  "batch_size": 16
}
```

**Response**

```json
{
  "results": [
    [
      { "text": "Apple", "label": "ORG", "start": 0, "end": 5 },
      { "text": "London", "label": "GPE", "start": 28, "end": 34 }
    ],
    [
      { "text": "Microsoft", "label": "ORG", "start": 0, "end": 9 },
      { "text": "Seattle", "label": "GPE", "start": 32, "end": 39 }
    ]
  ]
}
```

## Requirements

### Runtime

- Docker
- NVIDIA GPU with CUDA support (for GPU acceleration)
- NVIDIA Container Toolkit (docker run --gpus all)

### Host sanity check

```bash
nvidia-smi
docker run --gpus all nvidia/cuda:12.1.1-base-ubuntu22.04 nvidia-smi
```

If this works, the service will too.

## Build

```bash
docker build -t ner-api .
```

## Run

```bash
docker run --gpus all -d -p 8001:8001 ner-api
```

Custom port:

```bash
docker run --gpus all -d -p 9000:9000 -e PORT=9000 ner-api
```

## License

Provided as-is.
spaCy models and dependencies are subject to their respective licenses.
