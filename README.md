# Airflow Data Platform

## Overview
A production-style Airflow data orchestration platform designed to handle
batch pipelines with retries, backfills, cross-DAG dependencies, and cost-aware execution.

## Key Features
- Modular DAG design
- Idempotent and backfill-safe pipelines
- Deferrable sensors using Triggerer
- Cross-DAG orchestration patterns
- Failure handling and observability

## Tech Stack
- Apache Airflow 2.x
- Python
- AWS (conceptual)
- Spark / Snowflake (triggered, not executed)

## Design Philosophy
Airflow is used strictly as an orchestrator.
All heavy compute is delegated to external systems.
