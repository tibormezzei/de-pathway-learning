import os
import sys

import pytest
from pyspark.sql import SparkSession

# Make Spark's Python workers use this interpreter (the venv), not whatever `python` is on PATH.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)


@pytest.fixture(scope="session")
def spark():
    """One local SparkSession for the whole test run (starting Spark is slow)."""
    session = (
        SparkSession.builder.master("local[1]")
        .appName("tests")
        .config("spark.sql.shuffle.partitions", "1")   # small data: avoid 200 empty partitions
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )
    session.sparkContext.setLogLevel("ERROR")
    yield session
    session.stop()
