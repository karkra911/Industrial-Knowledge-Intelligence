from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "status": "uploaded"
    }

@router.get("/ask")
def ask(question: str):
    return {
        "question": question,
        "answer": "Prototype response."
    }
