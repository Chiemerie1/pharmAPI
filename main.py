from typing import Optional
from fastapi import FastAPI
import uvicorn


app = FastAPI()



@app.get("/", tags=["Index"])
def index():
    return {"data": "Drugs"}


@app.get("/drugs", tags=["Drugs"])
def get_drugs():
    return Drugs

Drugs = [
    {"idx": 1, "drug": "Panadol"},
    {"idx": 2, "drug": "peroxicam"}
]

@app.post("/drugs", tags=["Drugs"])
def addDrugs(drug: dict):
    Drugs.append(drug)
    return drug

@app.put("/drugs/{id}", tags=["Drugs"])
def updateDrugs(id: int, med: dict):
    for drug in Drugs:
        if int(drug["idx"]) == id:
            drug["drug"] = med["drug"]
            return Drugs
    return error

error = "wrong index"

@app.delete("/drugs", tags=["Drugs"])
def deleteDrug(drug_name: dict, id: Optional[int] = None):
    for drug in Drugs:
        if id == int(drug["idx"]) or drug_name["drug"] == drug["drug"]:
            Drugs.remove(drug)
            return Drugs
    return error
