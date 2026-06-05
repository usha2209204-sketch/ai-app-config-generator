# AI App Config Generator

## Overview

This project converts natural language application requirements into structured application configurations.

The system generates:

* UI Schema
* API Schema
* Database Schema
* Authentication Rules

## Multi-Stage Pipeline

User Prompt

↓

Intent Extraction

↓

System Design Layer

↓

Schema Generation

↓

Validation Engine

↓

Repair Engine

↓

Runtime Validation

↓

Final JSON Output

## Features

* Modular architecture
* Deterministic generation flow
* Validation and repair system
* Runtime verification
* Structured schema generation

## Example Input

Build a CRM with login, contacts, dashboard, premium subscriptions and admin analytics.

## Example Output

```json
{
  "ui": {
    "pages": [
      "dashboard",
      "contacts"
    ]
  },
  "api": {
    "endpoints": [
      "/login",
      "/contacts"
    ]
  },
  "database": {
    "tables": [
      "users",
      "contacts"
    ]
  },
  "auth": {
    "roles": [
      "admin",
      "user"
    ]
  }
}
```

## Pipeline Components

1. Intent Extraction
2. System Design
3. Schema Generation
4. Validation
5. Repair
6. Runtime Validation

## Future Improvements

* LLM-powered intent extraction
* JSON Schema enforcement
* Cross-layer consistency checking
* Evaluation dashboard
* Live deployment

```
```

