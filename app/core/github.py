import requests
import base64
import json
from .config import settings

def read_json():
    url = f"https://raw.githubusercontent.com/{settings.REPO}/main/{settings.FILE_PATH}"
    res = requests.get(url)
    print(url)
    if res.status_code != 200:
        raise Exception("Impossible de lire le fichier")
    return res.json()


def update_json(new_data: dict):
    headers = {"Authorization": f"token {settings.GITHUB_TOKEN}"}

    url_get = f"https://api.github.com/repos/{settings.REPO}/contents/{settings.FILE_PATH}"
    file_res = requests.get(url_get, headers=headers).json()

    sha = file_res.get("sha")
    if not sha:
        raise Exception("Impossible de récupérer le SHA")

    encoded_content = base64.b64encode(
        json.dumps(new_data, indent=2).encode()
    ).decode()

    payload = {
        "message": "Mise à jour via API FastAPI",
        "content": encoded_content,
        "sha": sha
    }

    res = requests.put(url_get, headers=headers, data=json.dumps(payload))
    return res.json()
