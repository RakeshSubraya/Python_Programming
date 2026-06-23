from datetime import date
from datetime import timedelta


class DateParser:

    @staticmethod
    def resolve(relative_date: str) -> str:

        today = date.today()

        if relative_date.lower() == "today":
            return str(today)

        if relative_date.lower() == "yesterday":
            return str(today - timedelta(days=1))

        return str(today)