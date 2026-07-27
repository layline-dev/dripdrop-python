#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GENERATOR_VERSION="${OPENAPI_GENERATOR_VERSION:-$(tr -d '[:space:]' < "$ROOT_DIR/.openapi-generator/VERSION")}"
GENERATOR_VERSION="${GENERATOR_VERSION//[[:space:]]/}"
CONFIG_FILE="${OPENAPI_GENERATOR_CONFIG:-openapi-generator-config.yaml}"
SCHEMA_FILE="${OPENAPI_SCHEMA_FILE:-Drip Drop API.yaml}"

cd "$ROOT_DIR"

if [[ ! -f "$SCHEMA_FILE" ]]; then
  echo "Schema file not found: $SCHEMA_FILE" >&2
  exit 1
fi

if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "Generator config not found: $CONFIG_FILE" >&2
  exit 1
fi

run_generator() {
  if command -v openapi-generator-cli >/dev/null 2>&1; then
    openapi-generator-cli version | grep -Fx "$GENERATOR_VERSION" >/dev/null || {
      echo "openapi-generator-cli is not version $GENERATOR_VERSION" >&2
      exit 1
    }
    openapi-generator-cli generate --config "$CONFIG_FILE"
    return
  fi

  if command -v docker >/dev/null 2>&1; then
    docker run --rm \
      -u "$(id -u):$(id -g)" \
      -v "$ROOT_DIR:/local" \
      -w /local \
      "openapitools/openapi-generator-cli:v${GENERATOR_VERSION}" \
      generate --config "$CONFIG_FILE"
    return
  fi

  echo "Install openapi-generator-cli $GENERATOR_VERSION or Docker to regenerate the SDK." >&2
  exit 1
}

run_generator
