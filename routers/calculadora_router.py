from fastapi import APIRouter
from models.request_models import SumaRequest
from services.operaciones_service import sumar

router = APIRouter()

@router.post("/suma")
def ruta_suma(datos: SumaRequest):
    resultado = sumar(datos.a, datos.b)
    return {"resultado": resultado}