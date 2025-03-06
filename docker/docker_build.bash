#!/usr/bin/env bash

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXEC_PATH="$PWD"

cd "$ROOT_DIR" || { echo "Failed to cd into $ROOT_DIR"; exit 1; }

docker build -t ros_course2023-img \
             -f "$ROOT_DIR/Dockerfile" \
             --network=host \
             --build-arg from_image=ubuntu:20.04 \
             "$ROOT_DIR"

cd "$EXEC_PATH" || { echo "Failed to cd back to $EXEC_PATH"; exit 1; }

