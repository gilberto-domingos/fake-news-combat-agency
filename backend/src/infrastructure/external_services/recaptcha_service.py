from dotenv import load_dotenv
import httpx
import os

load_dotenv()

RECAPTCHA_SECRET = os.getenv("RECAPTCHA_SECRET")
GOOGLE_RECAPTCHA_URL = "https://www.google.com/recaptcha/api/siteverify"

print(GOOGLE_RECAPTCHA_URL)

async def verify_recaptcha(token: str, remote_ip: str | None = None) -> bool:
    data = {
        "secret": RECAPTCHA_SECRET,
        "response": token
    }
    if remote_ip:
        data["remoteip"] = remote_ip

    async with httpx.AsyncClient() as client:
        response = await client.post(GOOGLE_RECAPTCHA_URL, data=data)
        result = response.json()
        return result.get("success", False)