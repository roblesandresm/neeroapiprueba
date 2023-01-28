from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastApi, Resquest, Response
from fastapi.responses import JSONResponse

class ErrorHandler(BaseHTTPMiddleware):
    
    def __init__(self, app: FastApi):
        super().__init__(app)

    async def dispatch(self, request: Resquest, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)})
    
    