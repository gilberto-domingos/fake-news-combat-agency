#!/usr/bin/env bash

echo "Starting application..."

exec uvicorn src.api.main:app \
  --host 0.0.0.0 \
  --port ${PORT:-8000} \
  --workers 2
#  workers = (CPU * 2) + 1

