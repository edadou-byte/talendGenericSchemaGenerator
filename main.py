import logging
import sys
from pathlib import Path

from processors.csv_processor import get_columns_types
from processors.csv_processor import open_csv_file
from processors.generic_schema_generator import create_xml_rows


SUPPORTED_EXTENSIONS = {".csv", ".xml", ".json"}

# Configuration des logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)


def get_file_path() -> str:
    logger.info("Récupération du chemin du fichier")

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        logger.info("Chemin récupéré depuis les arguments : %s", file_path)
    else:
        file_path = input("Veuillez saisir le chemin du fichier : ").strip()
        logger.info("Chemin saisi par l'utilisateur : %s", file_path)

    path = Path(file_path)

    if not path.exists():
        logger.error("Le fichier n'existe pas : %s", file_path)
        raise FileNotFoundError(
            f"Le fichier n'existe pas : {file_path}"
        )

    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        logger.error(
            "Extension non supportée : %s",
            path.suffix
        )
        raise ValueError(
            f"Extension non supportée : {path.suffix}. "
            f"Extensions autorisées : {', '.join(SUPPORTED_EXTENSIONS)}"
        )

    logger.info("Fichier validé : %s", file_path)

    return str(path)


def process_csv(file_path: str) -> None:
    logger.info("Début du traitement du CSV")

    cols = open_csv_file(file_path)

    logger.info(
        "%d colonnes détectées",
        len(cols)
    )

    column_types = get_columns_types(cols)

    logger.info(
        "%d types détectés",
        len(column_types)
    )

    rows = create_xml_rows(column_types)

    logger.info(
        "%d lignes XML générées",
        len(rows)
    )

    for row in rows:
        logger.debug("Ligne XML : %s", row.write_xml())

    logger.info("Traitement terminé avec succès")


if __name__ == '__main__':
    try:
        logger.info("Démarrage de l'application")

        file_path = get_file_path()
        extension = Path(file_path).suffix.lower()

        match extension:
            case ".csv":
                process_csv(file_path)

            case ".xml":
                logger.warning(
                    "Le traitement XML n'est pas encore implémenté"
                )
                raise NotImplementedError(
                    "Traitement XML non implémenté"
                )

            case ".json":
                logger.warning(
                    "Le traitement JSON n'est pas encore implémenté"
                )
                raise NotImplementedError(
                    "Traitement JSON non implémenté"
                )

            case _:
                logger.error(
                    "Extension inattendue : %s",
                    extension
                )
                raise ValueError(
                    f"Extension non supportée : {extension}"
                )

    except Exception as e:
        logger.exception("Erreur lors de l'exécution")
        sys.exit(1)