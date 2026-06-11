from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.services.pdf_export_service import (
    export_report_pdf
)

router = APIRouter()


@router.get("/export/{report_id}")
def export_report(report_id: int):

    pdf_file = export_report_pdf(
        report_id
    )

    return FileResponse(
        pdf_file,
        media_type="application/pdf",
        filename=f"startup_report_{report_id}.pdf"
    )