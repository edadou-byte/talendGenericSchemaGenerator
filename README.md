# Generic Schema Generator

Outil Python permettant d'analyser un fichier de données (CSV actuellement), de détecter automatiquement les types de colonnes et de générer une représentation XML du schéma correspondant pour Talend.

## Fonctionnalités

- Lecture de fichiers CSV
- Détection automatique du type des colonnes
- Génération d'un schéma XML à partir des colonnes détectées
- Gestion des erreurs et journalisation complète (logging)
- Architecture extensible pour supporter d'autres formats (XML, JSON)

## Prérequis

- Python 3.10 ou supérieur (utilisation du mot-clé `match`)
- Environnement virtuel recommandé

## Installation

### Cloner le dépôt

```bash
git clone https://github.com/<username>/generic-schema-generator.git
cd generic-schema-generator
```

### Créer un environnement virtuel

Linux / Mac :

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows :

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

## Structure du projet

```text
.
├── main.py
├── processors
│   ├── csv_processor.py
│   └── generic_schema_generator.py
├── requirements.txt
└── README.md
```

## Utilisation

### Exécution avec un argument

```bash
python main.py data.csv
```

### Exécution interactive

```bash
python main.py
```

L'application demandera alors :

```text
Veuillez saisir le chemin du fichier :
```

## Formats supportés

| Extension | Support |
|-----------|----------|
| CSV | ✅ |
| XML | 🚧 Non implémenté |
| JSON | 🚧 Non implémenté |

## Fonctionnement

### 1. Validation du fichier

L'application vérifie :

- L'existence du fichier
- L'extension du fichier

Extensions actuellement autorisées :

```python
{".csv", ".xml", ".json"}
```

### 2. Lecture des données

Le fichier CSV est chargé via :

```python
open_csv_file()
```

### 3. Détection des types

Les types de données sont déterminés grâce à :

```python
get_columns_types()
```

### 4. Génération du schéma XML

Les métadonnées détectées sont transformées en structures XML via :

```python
create_xml_rows()
```

## Logs

L'application utilise le module standard `logging`.

Exemple :

```text
2025-01-01 10:00:00 - INFO - __main__ - Démarrage de l'application
2025-01-01 10:00:00 - INFO - __main__ - Début du traitement du CSV
2025-01-01 10:00:02 - INFO - __main__ - Traitement terminé avec succès
```

## Gestion des erreurs

Les erreurs suivantes sont gérées :

### Fichier introuvable

```text
FileNotFoundError
```

### Extension non supportée

```text
ValueError
```

### Fonctionnalité non implémentée

```text
NotImplementedError
```

## Exemple de flux d'exécution

```text
Démarrage de l'application
    ↓
Validation du fichier
    ↓
Lecture du CSV
    ↓
Détection des colonnes
    ↓
Détermination des types
    ↓
Génération du schéma XML
    ↓
Fin du traitement
```

## Évolutions prévues

- Support du format XML
- Support du format JSON
- Export automatique du schéma généré dans un fichier
- Support de fichiers volumineux
- Optimisations de performance pour l'analyse des colonnes
- Tests unitaires et intégration continue

## Contribution

Les contributions sont les bienvenues.

1. Fork du projet
2. Création d'une branche de fonctionnalité

```bash
git checkout -b feature/ma-fonctionnalite
```

3. Commit des modifications

```bash
git commit -m "Ajout de ma fonctionnalité"
```

4. Push

```bash
git push origin feature/ma-fonctionnalite
```

5. Création d'une Pull Request

## Licence

Ce projet est distribué sous licence MIT.