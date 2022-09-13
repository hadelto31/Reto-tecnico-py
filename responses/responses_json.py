from fastapi.responses import JSONResponse


def responses_json(message: str, status: int = 200)-> JSONResponse:
    return JSONResponse(content={"message": message}, status_code=status)
