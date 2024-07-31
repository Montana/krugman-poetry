#!/bin/bash

retry_count=0
max_retries=5
retry_interval=10  # seconds

while [ $retry_count -lt $max_retries ]; do
  "$@" 2>&1 | grep -v "Timeout waiting for network availability."
  if [ $? -eq 0 ]; then
    exit 0
  fi
  echo "Command failed. Retrying in $retry_interval seconds..."
  retry_count=$((retry_count + 1))
  sleep $retry_interval
done

echo "Command failed after $max_retries attempts."
exit 1
