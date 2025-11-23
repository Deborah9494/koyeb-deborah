from fastapi import FastAPI

password = "123" # Hardcoded password

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Hola desde Koyeb"}

@app.get("/health")
def health():
    return{"status":"ok"}