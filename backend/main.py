import json
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# --- Pydantic Models ---
class Card(BaseModel):
    id: int
    title: str
    content: Optional[str] = None

class Column(BaseModel):
    id: int
    title: str
    cards: List[Card]

class Board(BaseModel):
    columns: List[Column]

# --- FastAPI App ---
app = FastAPI()

# --- CORS Middleware ---
# This allows the frontend to communicate with the backend
origins = [
    "http://localhost:5173",  # Default Vite dev server port
    "http://127.0.0.1:5173",
    "http://localhost:3000", # Common alternative port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import os

# --- Constants ---
# Use an absolute path to ensure the DB file is found regardless of CWD
BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BACKEND_DIR, "db.json")

def read_db() -> Board:
    """Reads the entire board state from the JSON file."""
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return Board(**data)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is empty/corrupt, return an empty board
        return Board(columns=[])


def write_db(board: Board):
    """Writes the entire board state to the JSON file."""
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(board.dict(), f, ensure_ascii=False, indent=2)


@app.get("/api/board", response_model=Board)
def get_board():
    """Endpoint to retrieve the current state of the board."""
    return read_db()


@app.put("/api/board")
def update_board(board: Board):
    """Endpoint to update the entire state of the board."""
    try:
        write_db(board)
        return {"message": "Board updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Welcome to the Agile Project Management API"}
