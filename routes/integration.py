from fastapi import APIRouter, Request

integration_router = APIRouter()


@integration_router.get("/integration.json")
def get_integration_json(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return {
        "data": {
            "date": {
                "created_at": "2025-02-17",
                "updated_at": "2025-02-17"
            },
            "descriptions": {
                "app_name": "Flutter Error Tracker",
                "app_description": "A Flutter error tracking integration that automatically captures and reports application errors in real-time to Telex channels.",
                "app_logo": "https://cdn.prod.website-files.com/6270e8022b05abb840d27d6f/6308d1ab615e60c9047c9d06_AppDev_Flutter-tools.png",
                "app_url": f"{base_url}",
                "background_color": "#fff"
            },
            "is_active": True,
            "integration_type": "modifier",
            "integration_category": "Performance Monitoring",
            "key_features": [
                "Automatic error capture for Flutter framework errors",
                "Real-time error reporting to Telex channels",
                "Specific error location tracking",
                "Formatted error reports for easy reading",
                "Immediate error notifications",
                "Support for multiple error types"
            ],
            "author": "Emmy-Anie",
            "settings": [
                {
                    "label": "Error Format Template",
                    "type": "text",
                    "required": True,
                    "default": "Error Report == {error} -- {location}"
                },
                {
                    "label": "Show Error Location",
                    "type": "checkbox",
                    "required": True,
                    "default": "true"
                }
            ],
            "target_url": f"{base_url}api/v1/error-log",
        }
    }