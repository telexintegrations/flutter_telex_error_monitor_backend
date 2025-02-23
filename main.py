import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.integration import integration_router
from api.routes.submit_error import submit_error_router

version = 'v1'

app = FastAPI(
   title="Flutter Error Monitor",
   description="A REST API that captures Flutter application errors and formats them for display in Telex channels",
   version=version,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(integration_router, prefix=f'/api')
app.include_router(submit_error_router, prefix=f'/api/{version}')


# Health check endpoint
@app.get("/")
async def health_check():
    """Health check endpoint for keep-alive pings."""
    return {"status": "alive"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)