import io
import logging
from csv import DictReader

from django.core.management import BaseCommand

from accounts.models import СategoryExpense, СategoryIncome

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    def handle(self, *args, **options):
        logging.info("Loading")
        if СategoryIncome.objects.exists():
            logging.warning("child data already loaded...exiting.")
            raise Exception(ALREDY_LOADED_ERROR_MESSAGE)

        logging.info("Loading - data a table - СategoryIncome")
        for row in DictReader(io.open(
            "static/data/categoryincome.csv", mode="r", encoding="utf-8"
        )):
            СategoryIncome.objects.get_or_create(name=row["name"])
        logging.info("Successfully - loading data table - СategoryIncome")

        logging.info("Loading - data a table - СategoryExpense")
        for row in DictReader(io.open(
            "static/data/categoryexpense.csv", mode="r", encoding="utf-8"
        )):
            СategoryExpense.objects.get_or_create(name=row["name"])
        logging.info("Successfully - loading data table - СategoryExpense")

        return logging.info("Successfully loading data")
