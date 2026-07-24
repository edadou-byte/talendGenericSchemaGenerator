import csv
import logging

from processors.type_assessor import detect_type
from collections import Counter

# Configuration des logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def open_csv_file(path: str) -> dict:
    logger.info("Ouverture du fichier CSV : %s", path)

    columns = {}

    with open(path, 'r', encoding='utf-8') as f:
        sample = f.read(4096)
        dialect = csv.Sniffer().sniff(sample)

        logger.info(
            "Délimiteur détecté : '%s'",
            dialect.delimiter
        )

        f.seek(0)

        reader = csv.DictReader(f, dialect=dialect)

        logger.info(
            "Colonnes détectées : %s",
            ", ".join(reader.fieldnames)
        )

        for col_name in reader.fieldnames:
            columns[col_name] = []

        row_count = 0

        for line in reader:
            row_count += 1

            for col_name in reader.fieldnames:
                columns[col_name].append(line[col_name])

        logger.info(
            "Lecture terminée : %s lignes chargées",
            row_count
        )

    return columns


def get_columns_types(columns: dict) -> list:
    logger.info("Début de la détection des types")

    types = []
    detected_type = []

    for col_name in columns:
        logger.info(
            "Analyse de la colonne '%s' (%s valeurs)",
            col_name,
            len(columns[col_name])
        )

        int = 0
        final_detected_type = ""

        counts = {}
        max_value = None
        max_count = 0

        for item in columns[col_name]:
            detected_type = detect_type(item)
            count = counts.get(detected_type, 0) + 1
            counts[detected_type] = count

            if count > max_count:
                max_count = count
                max_value = detected_type

            if detected_type == 'id_String':
                max_value = detected_type
                break


        types.append(f"{col_name}&&{max_value}")

        logger.debug(
            "Types détectés pour '%s' : %s",
            col_name,
            set(
                detect_type(value)
                for value in columns[col_name]
            )
        )

    logger.info(
        "Détection terminée : %s types analysés",
        len(types)
    )

    return types