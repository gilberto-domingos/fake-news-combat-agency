from fastapi import Request
from fastapi.responses import JSONResponse
import traceback


async def global_exception_handler(request: Request, exc: Exception):
    print("ERROR CAPTURED !")
    print(traceback.format_exc())

    return JSONResponse(
        status_code=500,
        content={
            "error": "InternalServerError",
            "detail": str(exc),
            "type": type(exc).__name__
        }
    )
