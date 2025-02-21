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
❌ 𝗘𝗿𝗿𝗼𝗿: {error_log.error}
📍 𝗟𝗼𝗰𝗮𝘁𝗶𝗼𝗻: {clean_location}
```

## Backend Setup

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

## Flutter Package Installation

### Step 1: Set up Telex

Before installing the package, you need to set up a Telex channel:

1. Create an account with [telex.im](https://telex.im)
2. Click on the first tab with your initials to create an organization
3. Go to the "Channels" tab and add a channel
4. In your channel, click the arrow-down button beside your channel name and click on "Webhook Configuration"
5. Copy your webhook URL - you'll need this for initialization

### Step 2: Add the package to your Flutter project

Add the package to your `pubspec.yaml`:

```bash
flutter pub add flutter_telex_error_monitor
```

### Step 3: Initialize the error monitor

In your main.dart:

```dart
import 'package:flutter_telex_error_monitor/flutter_telex_error_monitor.dart';

void main() {
  // Initialize the error monitor before runApp
  FlutterTelexErrorMonitor.init(
    telexChannelWebhookUrl: "YOUR_TELEX_WEBHOOK_URL", // From Step 1
    appName: "YOUR_FLUTTER_APP_NAME",  // Optional
  );
  
  runApp(MyApp());
}
```

## Activating the Telex Integration

To use advanced features with error formatting settings:

1. Log in to your Telex organization
2. Navigate to the "Apps" tab in your organization sidebar
3. Search for "Flutter Telex Error Monitor" in the integrations marketplace
4. Click "Install" to add it to your organization
5. Navigate to the channel where you want to use error tracking
6. Click the channel settings (gear icon)
7. Select "Apps & Integrations"
8. Find "Flutter Telex Error Monitor" and toggle it on for this channel

### Configuring Integration Settings

Once activated, you can configure the integration settings:

1. Click on the "Flutter Telex Error Monitor" integration in your channel's integrations list
2. You'll see the following configuration options:
   - **Error Format Template**: Customize how errors appear in your channel
   - **Show Error Location**: Toggle whether to display file and line information

These settings allow you to:
- Adapt error messages to your team's preferences
- Control the level of detail shown in error reports
- Make error reporting consistent with your organization's standards

## Integration with Flutter

This backend is designed to work with the `flutter_telex_error_monitor` package. When properly configured, Flutter applications will automatically send runtime errors to this backend, which then forwards them to Telex.


## Flow Diagram

```
Flutter App                 Backend Service               Telex
    |                             |                         |
    |-- Error occurs              |                         |
    |-- Captures details          |                         |
    |------- Send error --------->|                         |
    |                             |-- Formats error         |
    |                             |------- Forward -------->|
    |                             |                         |-- Displays in channel
```