from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bienvenue dans l'application de gestion des matchs de basket !"}
