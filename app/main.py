from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue !"}

@app.post("/matches/")
def create_match(match: dict):
    return {"message": "Match créé avec succès", "match": match}
