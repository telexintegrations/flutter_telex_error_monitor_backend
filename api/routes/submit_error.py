import httpx
from fastapi import APIRouter

from api.schema.error_submission import ErrorSubmission

submit_error_router = APIRouter()


@submit_error_router.post("/submit-error")
async def submit_error(error_log: ErrorSubmission):

    clean_location = error_log.location.replace("<fn>", "").replace("</fn>", "")

    formatted_error = f"""❌ 𝗘𝗿𝗿𝗼𝗿: {error_log.error}
    📍 𝗟𝗼𝗰𝗮𝘁𝗶𝗼𝗻: {clean_location}"""

    payload = {
        "event_name": "Flutter Telex Error Monitor",
        "message": formatted_error,
        "status": "success",
        "username": error_log.app_name
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            error_log.telex_channel_webhook_Url,
            json=payload,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        )

        print(response)

    return {"status": "success"}