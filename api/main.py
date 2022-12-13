from typing import Optional
import requests
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/api/")
def read_root():
    return {"Manchester": "Red"}


@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"no": item_id, "name": q}


@app.get("/authorize")
def authorize():
    # redirect to auth0
    # https://sonph-test-project.us.auth0.com/authorize?client_id=Tb9LLZi45LdweuQnmTgSJLQq5UWx1vjM&state=xxxxx&response_type=token&scope=openid&redirect_uri=http://localhost:8081/&audience=https://sonph-test-project.us.auth0.com/api/v2/
    auth_url = "https://sonph-test-project.us.auth0.com/authorize?"
    auth_url += "client_id=Tb9LLZi45LdweuQnmTgSJLQq5UWx1vjM"
    auth_url += "&state=xxxxxxxxxxxx"
    auth_url += "&response_type=code"
    auth_url += "&redirect_uri=http://localhost:8081/oauth-callback/"
    auth_url += "&scope=openid%20profile%20email%20offline_access"
    auth_url += "&audience=https://sonph-test-project.us.auth0.com/api/v2/"
    return RedirectResponse(auth_url)


@app.get("/oauth-callback")
def oauth_callback(code: str):
    res = requests.post(
        "https://sonph-test-project.us.auth0.com/oauth/token",
        data={
            'grand_type': 'authorization_code',
            'client_secret': 'wO75Sxziz6z19wicpnq5T-dq79j_rVyYMLOEuwIcXE46FoSbPV26z-epW52gf4p9',
            'client_id': 'Tb9LLZi45LdweuQnmTgSJLQq5UWx1vjM',
            'code': code,
            'redirect_uri': 'http://localhost:8081/',
        })
    return res.json()
