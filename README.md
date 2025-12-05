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