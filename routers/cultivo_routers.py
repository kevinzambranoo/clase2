from fastapi import APIRouter

from schemas.cultivo_schemas import CultivoData
from services.cultivo_service import cultivo_prediction


router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello Word"}

@router.post("/predict")
async def patient_predict(data: CultivoData):

    prediction = cultivo_prediction(data)


    return {"prediction": prediction}