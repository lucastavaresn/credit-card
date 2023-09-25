from fastapi import Request
from fastapi.responses import JSONResponse
import os


class AuthMiddleware:
    async def __call__(self, request: Request, call_next):
        if request.url.path == "/docs" or request.url.path == "/openapi.json":
            return await call_next(request)
    
        auth = request.headers.get("Authorization", None)

        if not auth:
            return JSONResponse(status_code=401, content="No credentials provided")

        auth_type, credetial = auth.split(" ")

        if auth_type != "Bearer" or credetial != os.getenv("AUTH_HASH"):
            return JSONResponse(status_code=401, content="Invalid credentials provided")

        response = await call_next(request)

        return response