# Flutter Telex Error Monitor Backend

A FastAPI service that bridges Flutter applications and Telex channels for real-time error reporting.

## Overview

This backend service receives error data from Flutter applications (using the `flutter_telex_error_monitor` package) and forwards formatted error reports to Telex channels. It serves as the crucial middleware component in the error monitoring pipeline.

## Features

- Receives and processes error data from Flutter applications
- Formats error messages in a standardized, readable format
- Routes errors to the appropriate Telex channels via webhooks
- Supports custom application names for error source identification
- Provides consistent error reporting across multiple applications

## API Reference

### POST `/submit-error`

**Purpose:** Receive error data from Flutter applications and forward to Telex

**Request Parameters:**
- `app_name`: Name of the Flutter application (used for identification in reports)
- `telex_channel_webhook_Url`: The specific Telex channel webhook URL
- `error`: The error message or exception details
- `location`: Where the error occurred (file, line number, method)

**Response:**
- Status code `200` with `{"status": "success"}` on successful processing

## Error Format

Errors are formatted in a consistent, readable structure:
```
Error: {error details}
Location: {where the error occurred}

```

## Setup

1. Clone this repository
2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies from requirements.txt:
   ```
   pip install -r requirements.txt
   ```
4. Run the server:
   ```
   uvicorn main:app --reload
   ```

To install all dependencies:
```
pip install -r requirements.txt
```

## Deployment

This service can be deployed to any platform supporting Python:
- Render
- Railway
- Heroku
- AWS
- Google Cloud

## Integration with Flutter

This backend is designed to work with the `flutter_telex_error_monitor` package. When properly configured, Flutter applications will automatically send errors to this backend, which then forwards them to Telex.

## Security Considerations

- This service accepts webhook URLs from clients
- Implement appropriate validation in production environments
- Consider adding authentication for secure deployments
- Use HTTPS for all communications

## Requirements

- Python 3.7+
- FastAPI
- httpx
- Pydantic