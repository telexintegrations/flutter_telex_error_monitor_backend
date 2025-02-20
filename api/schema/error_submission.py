from pydantic import BaseModel


class ErrorSubmission(BaseModel):
    app_name: str
    telex_channel_webhook_Url: str
    error: str
    location: str