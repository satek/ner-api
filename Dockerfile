FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8001
ENV HOST="0.0.0.0"

WORKDIR /app

# Install Python
RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  build-essential \
  && rm -rf /var/lib/apt/lists/*

# Make python == python3 (optional but sane)
RUN ln -sf /usr/bin/python3 /usr/bin/python

COPY requirements.txt .

# ALWAYS use python -m pip
RUN python -m pip install --upgrade pip \
  && python -m pip install --no-cache-dir \
  torch --index-url https://download.pytorch.org/whl/cu121 \
  && python -m pip install --no-cache-dir -r requirements.txt \
  && python -m spacy download en_core_web_trf

COPY app ./app

EXPOSE ${PORT}

CMD ["sh", "-c", "python -m uvicorn app.main:app --host ${HOST} --port ${PORT}"]

