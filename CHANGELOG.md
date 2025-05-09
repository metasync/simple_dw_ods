# Changelog

## [0.1.0] - 2025-04-17

  - Initial release for simple dw:
    - dbt seed from Jaffle Shop
    - dbt models for ods, dwd & dws layers

## [0.2.0] - 2025-04-27

  - Implemented ods datasets ingestion via a separate dagster code location instead of dbt seeding
  - Refactored dw dagster code location to support multiple dagster stages/environments
  - Fixed issued identified by Ruff (Python linter)

## [0.2.1] - 2025-05-09

  - Refactored from simple dw project to extract the ods layer as a separate project
