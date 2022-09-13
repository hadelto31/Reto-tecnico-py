from fastapi import APIRouter, File, Form, UploadFile


blob_routes = APIRouter()


@blob_routes.post("/upload")
def upload(container: str = Form(...), file: UploadFile = File(...));

