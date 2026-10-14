from fastapi import FastAPI
import random
app = FastAPI()
movies = ["The Shawshank Redemption (1994)", "The Godfather (1972)", "The Dark Knight (2008)", "Pulp Fiction (1994)", "Fight Club (1999)"]
@app.get("/")
def read_root():
    idx = random.randrange(0, len(movies))
    return {"status": "success", "recommendation": movies[idx]}
