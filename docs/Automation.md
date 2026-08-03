# Public API schema automation

This SDK can be regenerated from the public OpenAPI schema published by `layline-dev/dripdrop`.

## Manual regeneration

```sh
scripts/regenerate-sdk.sh
scripts/bump-version.py   # patch-bumps the package version after meaningful SDK changes
python -m build
```

`openapi-generator-config.yaml` pins the generator inputs and package settings. The default generator version is read from `.openapi-generator/VERSION` (`7.20.0`). The regeneration script uses a matching local `openapi-generator-cli` when available, or Docker image `openapitools/openapi-generator-cli:v7.20.0`.

## GitHub Actions flow

`.github/workflows/public-api-schema-updated.yml` runs on:

- `repository_dispatch` type `public-api-schema-updated`
- manual `workflow_dispatch`

The dispatch payload may include:

```json
{
  "source_repo": "layline-dev/dripdrop",
  "source_sha": "<commit-sha>",
  "source_ref": "main",
  "schema_path": "backend/public_api_schema.yaml"
}
```

The workflow downloads the schema into `Drip Drop API.yaml`, regenerates the SDK, exits cleanly when there is no diff, patch-bumps the package version when there is a diff, runs tests/build, and commits the result back to the checked-out branch.

The dispatching workflow in `layline-dev/dripdrop` needs a token that can call `repository_dispatch` on this repository. This SDK workflow only needs the default `GITHUB_TOKEN` with `contents: write` so it can commit regenerated SDK changes. It does not create GitHub releases or publish to PyPI.

## Publishing

Publishing remains manual: review the automated commit, create/publish a GitHub release when ready, and the existing release-triggered PyPI trusted publishing workflow publishes the package.
