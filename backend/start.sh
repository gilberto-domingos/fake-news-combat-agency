#!/usr/bin/env bash

echo "Starting application..."

uvicorn src.main:app \
  --host 0.0.0.0 \
  --port $PORT \
  --workers 2
#  workers = (CPU * 2) + 1