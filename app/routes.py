from fastapi import APIRouter, UploadFile, File, HTTPException, Query

from app.dna_generator import generate_dna_sequence
from app.utils import compare_sequences
from app.llm import ask_llm
import csv
from typing import Dict
import json



router = APIRouter()

data_store={}
#enfpoint for uploading csv file 
@router.post("/upload-csv/")
def upload_csv(file: UploadFile = File(...)) -> Dict:
    """uload a CSV file with columns: id, region, age, seed.
    each row is parsed and stored in memory for later sequence operations.
    """
    
    try:

        
        #read file content and split into lines
        content = file.file.read().decode("utf-8").splitlines()
        reader = csv.DictReader(content)
        
    #ensure the CSV has the required columns
        required_columns = ["id", "region", "age", "seed"]
        if not all(col in reader.fieldnames for col in required_columns):
            raise HTTPException(status_code=400, detail="CSV is missing one or more required columns.")
        
        
            # Validate and normalize data
        try:
                
                
                for row in reader:
                    id = row["id"]
                    data_store[id] = {
            "region": row["region"],
            "age": int(row["age"]),
            "seed": row["seed"]
        }
                
                with open("data_store.json", "w") as f:#Optional
                    json.dump(data_store, f,indent=4)
                return {"status": "success", "count": len(data_store)}
   

                
        except ValueError as e:
                raise HTTPException(status_code=400, detail=f"Invalid data in row: {str(e)}")
        



        return {"status": "success", "count": len(data_store)}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing CSV: {str(e)}")  


#endpoint for genearating dna seed sequence

@router.get("/generate-sequences/")
def generate_sequence(id: str = Query(...)) -> Dict:
    """
    generate a  Dna sequence for a given ID based on stored data.
    """
    with open("data_store.json", "r") as f:
        data_store = json.load(f)
    if id not in data_store:
        raise HTTPException(status_code=404, detail="ID not found")
    
    record = data_store[id]
    sequence = generate_dna_sequence(id, record["region"], record["age"], record["seed"])
    if sequence == "x":
        raise HTTPException(status_code=422, detail="Failed to generate sequence from seed")
    
    print(f"[DEBUG] Sequence for {id}:", sequence)
    return {"id": id, "sequence": sequence}
    
#endpoint for comaring  a pair of dna sequence
@router.get("/compare-sequences/")
def compare_sequences_endpoint(id1: str = Query(...), id2: str = Query(...)) -> Dict:
    """
    compare the similarity between DNA sequences of two sample IDs.
    """
    with open("data_store.json", "r") as f:
        data_store = json.load(f)
    if id1 not in data_store or id2 not in data_store:
        raise HTTPException(status_code=404, detail="One or both IDs not found")

    rec1 = data_store[id1]
    rec2 = data_store[id2]
    seq1 = generate_dna_sequence(id1, rec1["region"], rec1["age"], rec1["seed"])
    seq2 = generate_dna_sequence(id2, rec2["region"], rec2["age"], rec2["seed"])

    if seq1 == "x" or seq2 == "x":
        raise HTTPException(status_code=422, detail="Sequence generation failed for one or both samples")

    score = compare_sequences(seq1, seq2)
    return {"id1": id1, "id2": id2, "similarity_score": score}

#endpoint for asking queries regarding the application
@router.post("/ask-me-anything/")


def ask_anything(question: str = Query(...)) -> Dict:
    """
    answer natural language questions about the serve's functionality.
    """
    try:
        answer = ask_llm(question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Error: {str(e)}")
