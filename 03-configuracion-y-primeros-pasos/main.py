# Contexto de FastAPI
from fastapi import FastAPI
app = FastAPI()

@app.get("/") # Decoradores
async def root(): # Función asíncrona
  return 'Hello, FastAPI!'

@app.get("/url") # Decoradores
async def url(): # Función asíncrona
  return {"url": "https://mouredev.com/python"}
