"""
API do Sistema de Gestão da Mergington High School

Uma aplicação FastAPI bem simples que permite aos estudantes visualizar e se
inscrever em atividades extracurriculares da Mergington High School.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import json
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API para visualizar e se inscrever em atividades extracurriculares")

BASE_DIR = Path(__file__).resolve().parent
TEACHERS_FILE = BASE_DIR / "teachers.json"


def load_teachers():
    if not TEACHERS_FILE.exists():
        return {}

    with TEACHERS_FILE.open("r", encoding="utf-8") as file:
        payload = json.load(file)

    teachers = payload.get("teachers", [])
    return {
        entry["username"]: entry["password"]
        for entry in teachers
        if entry.get("username") and entry.get("password")
    }


def is_valid_teacher(username: str | None, password: str | None) -> bool:
    if username is None or password is None:
        return False
    return load_teachers().get(username) == password


def require_teacher_auth(username: str | None, password: str | None):
    if not is_valid_teacher(username, password):
        raise HTTPException(
            status_code=403,
            detail="Autenticação de professor necessária"
        )


# Monta o diretório de arquivos estáticos
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# Banco de dados de atividades em memória
activities = {
    "Chess Club": {
        "description": "Aprenda estratégias e dispute torneios de xadrez",
        "schedule": "Sextas-feiras, 15h30 - 17h00",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Aprenda os fundamentos de programação e construa projetos de software",
        "schedule": "Terças e quintas-feiras, 15h30 - 16h30",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Educação física e atividades esportivas",
        "schedule": "Segundas, quartas e sextas-feiras, 14h00 - 15h00",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Entre para o time de futebol da escola e dispute partidas",
        "schedule": "Terças e quintas-feiras, 16h00 - 17h30",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Treine e jogue basquete com o time da escola",
        "schedule": "Quartas e sextas-feiras, 15h30 - 17h00",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore sua criatividade por meio da pintura e do desenho",
        "schedule": "Quintas-feiras, 15h30 - 17h00",
        "max_participants": 15,
        "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
    },
    "Drama Club": {
        "description": "Atue, dirija e produza peças e apresentações",
        "schedule": "Segundas e quartas-feiras, 16h00 - 17h30",
        "max_participants": 20,
        "participants": ["ella@mergington.edu", "scarlett@mergington.edu"]
    },
    "Math Club": {
        "description": "Resolva problemas desafiadores e participe de competições de matemática",
        "schedule": "Terças-feiras, 15h30 - 16h30",
        "max_participants": 10,
        "participants": ["james@mergington.edu", "benjamin@mergington.edu"]
    },
    "Debate Team": {
        "description": "Desenvolva habilidades de oratória e argumentação",
        "schedule": "Sextas-feiras, 16h00 - 17h30",
        "max_participants": 12,
        "participants": ["charlotte@mergington.edu", "henry@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/login")
async def login(request: Request):
    payload = await request.json() if request.headers.get("content-type") == "application/json" else {}
    username = payload.get("username") or request.query_params.get("username")
    password = payload.get("password") or request.query_params.get("password")

    if not is_valid_teacher(username, password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    return {
        "message": "Login realizado com sucesso",
        "role": "teacher",
        "username": username,
    }


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(
    activity_name: str,
    email: str,
    username: str | None = None,
    password: str | None = None,
):
    """Inscreve um estudante em uma atividade apenas quando o professor estiver autenticado."""
    require_teacher_auth(username, password)

    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")

    activity = activities[activity_name]

    if email in activity["participants"]:
        raise HTTPException(
            status_code=400,
            detail="Estudante já está inscrito"
        )

    activity["participants"].append(email)
    return {"message": f"{email} inscrito em {activity_name}"}


@app.delete("/activities/{activity_name}/unregister")
def unregister_from_activity(
    activity_name: str,
    email: str,
    username: str | None = None,
    password: str | None = None,
):
    """Cancela a inscrição de um estudante em uma atividade apenas quando o professor estiver autenticado."""
    require_teacher_auth(username, password)

    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")

    activity = activities[activity_name]

    if email not in activity["participants"]:
        raise HTTPException(
            status_code=400,
            detail="Estudante não está inscrito nesta atividade"
        )

    activity["participants"].remove(email)
    return {"message": f"Inscrição de {email} em {activity_name} cancelada"}
