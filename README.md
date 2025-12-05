# GitSync-API

GitSync-API est une API en Python utilisant FastAPI qui permet de lire et modifier un fichier JSON stocké sur un dépôt GitHub.  
Elle utilise un Personal Access Token GitHub pour sécuriser l'accès et effectuer des commits sur le fichier.

---

## Fonctionnalités

- Lire le contenu du fichier JSON sur GitHub via l'endpoint `/read`.
- Mettre à jour le fichier JSON via l'endpoint `/update`.
- Gestion sécurisée du token GitHub via un fichier `.env`.
- Structure modulaire avec dossiers `app/routes`, `app/core`, etc.

---

## Prérequis

Pour utiliser GitSync-API, vous devez disposer de :

- Python 3.11 ou supérieur
- Git pour cloner et gérer le projet
- Un compte GitHub
- Un Personal Access Token GitHub avec les permissions `repo` pour lire et écrire sur le dépôt

---

## Installation et configuration

1. **Cloner le dépôt**

```bash
git clone https://github.com/rakou-fr/GitSync-API.git
cd GitSync-API
```

2. **Créer un environement virtuel**
```bash
python -v venv venv
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Créer fichier .env à la racine du projet avec dedans**
```bash
GITHUB_TOKEN=ghp_votre_token_icii
REPO=githubUsername/RepoName
FILE_PATH=data.json
```

---

## Lancement de l'API

```bash
uvicorn app.main:app --reload
```
L'API sera accessible à l'adresse : http://127.0.0.1:8000

--- 

## Endpoints disponibles

- **GET `/read`** : Lit le contenu actuel du fichier JSON sur GitHub.

- **POST `/update`** : Met à jour le fichier JSON.  
  Exemple de corps de requête JSON :

```json
{
  "data": {
    "test": "hello",
    "value": 42
  }
}
```

---

## Structure du projet

```bash
GitSync-API/
│
├─ app/
│  ├─ routes/        # Endpoints FastAPI
│  ├─ core/          # Gestion GitHub et configuration
│  ├─ data/          # Fichier JSON à synchroniser
│  └─ main.py        # Point d’entrée FastAPI
│
├─ .gitignore        # Fichiers à ignorer pour Git (ex: .env)
├─ requirements.txt  # Dépendances Python
├─ README.md         # Ce fichier
└─ .env              # Contient le token (non pushé)
```
