"""
Configuration du Data Lake
"""
import os
from pathlib import Path

# Chemins du Data Lake
BASE_PATH = Path(__file__).parent.parent
DATA_PATH = BASE_PATH / "data"

# Architecture Medallion
BRONZE_PATH = DATA_PATH / "raw"    # Données brutes
SILVER_PATH = DATA_PATH / "stagging"    # Données nettoyées
GOLD_PATH = DATA_PATH / "curated"        # Données agrégées/business

# Sources de données
SOURCES = {
    "csv1": DATA_PATH / "cards_data" / "csv",
    "csv2": DATA_PATH / "Europe Sales Records" / "csv",
    "csv3": DATA_PATH / "rba-dataset" / "csv",
    "json": DATA_PATH / "mcc_codes" / "json"
}

# Configuration Spark
SPARK_CONFIG = {
    "spark.app.name": "DataLakeWorkshop",
    "spark.master": "local[*]",
    "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
    "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    "spark.driver.memory": "4g",
    "spark.executor.memory": "4g",
}