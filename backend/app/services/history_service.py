from app.database.db import get_connection


class HistoryService:

    @staticmethod
    def save_report(report):
        # existing code
        pass

    @staticmethod
    def get_all_reports():

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                created_at,
                opportunity_score,
                investor_readiness,
                overall_score
            FROM startup_reports
            ORDER BY id DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return [dict(row) for row in rows]

    @staticmethod
    def get_report(report_id):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM startup_reports
            WHERE id = ?
        """, (report_id,))

        row = cursor.fetchone()

        conn.close()

        if row:
            return dict(row)

        return None