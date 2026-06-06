from pydantic import BaseModel


class ExecutionReport(BaseModel):

    week_1_tasks: list[str]

    week_2_tasks: list[str]

    week_3_tasks: list[str]

    week_4_tasks: list[str]