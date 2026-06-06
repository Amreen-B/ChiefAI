from fastapi import APIRouter
from pydantic import BaseModel

from app.services.pdf_service import PDFService
from app.orchestrator import StartupOrchestrator

router = APIRouter()

class AnalyseRequest(BaseModel):
    path: str

@router.post("/analyse")
async def analyze_document(request: AnalyseRequest):

    text = PDFService.extract_text(
        request.path
    )

    report = StartupOrchestrator().run(
        text
    )

    return report