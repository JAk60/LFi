
import csv
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import traceback

# Import from our new module
from Expertrules import Scenario, predict_scenario_logic
from utility.utils import DependabilityCalculator
app = FastAPI()
import pyodbc


try:
    # Establish the connection to the local SQL Server instance
    cnxn = pyodbc.connect(
        driver="{ODBC Driver 18 for SQL Server}",
        server="localhost",  # or "127.0.0.1"
        database="Utility",
        uid="sa",
        pwd="Camlab110",
        port=1433,
        TrustServerCertificate="yes",
        Timeout=300
    )
    print("Connection successful!")
except pyodbc.Error as ex:
    # Handle connection errors
    sqlstate = ex.args[1]
    print(f"Connection failed: {sqlstate}")



cursor = cnxn.cursor()
# Enable CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/predict")
def predict_scenario(request: Scenario):
    try:
        results = predict_scenario_logic(request.scenario, request.version)
        return results
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.get("/get_dependability")
def Calculate_dependability():
    try:
        inst=DependabilityCalculator()
        result = inst.calculate_dependability()
        print(result)  # Call the function from the other file
        return {"dependability": result[0], "phase_wise_weighted_dependability_values":result[1]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")




# Pydantic Model
class User(BaseModel):
    id: int
    username: str
    role: str


# Fetch a single user by username
@app.get("/users/{username}", response_model=User)
def get_user(username: str):
    cursor.execute("SELECT id, username, role FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()


    if not row:
        raise HTTPException(status_code=404, detail="User not found")

    return {"id": row[0], "username": row[1], "role": row[2]}
class ScenarioParagraph(BaseModel):
    ParagraphText: str
    ParaCreatedDate: str

@app.post("/paragraphs/")
async def create_paragraph(paragraph: ScenarioParagraph):
    """Inserts a new paragraph."""
    try:
        cursor.execute(
            "INSERT INTO ScenarioParagraphs (ParagraphText, ParaCreatedDate) VALUES (?, ?)",
            paragraph.ParagraphText,
            paragraph.ParaCreatedDate,
        )
        cnxn.commit()
        return {"message": "Paragraph created successfully"}
    except pyodbc.Error as e:
        cnxn.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    except Exception as general_exception:
        cnxn.rollback()
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {general_exception}")


@app.get("/paragraphs/")
async def get_all_paragraphs():
    """Fetches all paragraphs."""
    try:
        cursor.execute("SELECT ParagraphID, ParagraphText, ParaCreatedDate FROM ScenarioParagraphs")
        rows = cursor.fetchall()
        results = [{"ParagraphID": row.ParagraphID, "ParagraphText": row.ParagraphText, "ParaCreatedDate": str(row.ParaCreatedDate)} for row in rows] #convert dates.
        return results
    except pyodbc.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    except Exception as general_exception:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {general_exception}")

@app.post("/insert_csv_fixed_path/")
async def insert_csv_fixed_path():
    """
    Reads the first column of a CSV file from a fixed path, gets the first 10 rows, and inserts them into the ScenarioParagraphs table.
    """
    file_path = "/home/user/IITB/LFi/data/processed/version8/full.csv"  # Replace with your fixed file path

    try:
        paragraphs = []
        count = 0
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if count < 10:
                    if row: #check for empty row.
                        paragraphs.append(row[0])  # Get the first column
                        count += 1
                else:
                    break

        for paragraph in paragraphs:
            try:
                cursor.execute(
                    "INSERT INTO ScenarioParagraphs (ParagraphText, ParaCreatedDate) VALUES (?, GETDATE())",
                    paragraph,
                )
            except pyodbc.Error as e:
                cnxn.rollback()
                raise HTTPException(status_code=500, detail=f"Database error during insertion: {e}")
            except Exception as general_exception:
                cnxn.rollback()
                raise HTTPException(status_code=500, detail=f"An unexpected error occurred during insertion: {general_exception}")

        cnxn.commit()
        return {"message": f"{count} rows inserted successfully."}

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing CSV: {e}")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)