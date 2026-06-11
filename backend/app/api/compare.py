from fastapi import APIRouter
from app.database.db import get_connection
import json

router = APIRouter()


@router.get("/compare/{id1}/{id2}")
def compare_reports(
    id1: int,
    id2: int
):

    conn = get_connection()

    conn.row_factory = lambda cursor, row: {
        col[0]: row[idx]
        for idx, col in enumerate(cursor.description)
    }

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM startup_reports WHERE id=?",
        (id1,)
    )

    report1 = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM startup_reports WHERE id=?",
        (id2,)
    )

    report2 = cursor.fetchone()

    conn.close()

    if report1 and report1.get("report_json"):
        report1["report_json"] = json.loads(
            report1["report_json"]
        )

    if report2 and report2.get("report_json"):
        report2["report_json"] = json.loads(
            report2["report_json"]
        )

    return {
        "report1": report1,
        "report2": report2
    }