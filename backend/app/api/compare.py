from fastapi import APIRouter

from app.database.db import get_connection

router = APIRouter()


@router.get("/compare/{id1}/{id2}")
def compare_reports(
    id1: int,
    id2: int
):

    conn = get_connection()

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

    return {
        "report1": dict(report1),
        "report2": dict(report2)
    }