from fastapi import APIRouter
from app.services.history_service import HistoryService

router = APIRouter()


@router.get("/history")
def get_history():

    return HistoryService.get_all_reports()


@router.get("/history/{report_id}")
def get_history_report(report_id: int):

    return HistoryService.get_report(report_id)