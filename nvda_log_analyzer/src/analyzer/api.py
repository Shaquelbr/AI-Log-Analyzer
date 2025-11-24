from fastapi import FastAPI
from pydantic import BaseModel
from analyzer.parser import parse_log
from analyzer.ai_client import summarize_logs
from analyzer.patterns.signatures import match_signatures
from analyzer.ai_client import analyze_with_nim
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

class LogInput(BaseModel):
    log_text: str


@app.post("/analyze_nim")
async def analyze_nim_endpoint(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf8")

    result = analyze_with_nim(text)

    return {"analysis": result}    

@app.post("/analyze")
def analyze_logs(input_data: LogInput):
    temp_path = "/tmp/input.log"

    with open(temp_path, "w", encoding="utf8") as f:
        f.write(input_data.log_text)

    result = parse_log(temp_path)
    raw = result
    compressed = result["compressed"]

    matches = match_signatures(raw)

    if matches:
        return{
            "mode":"signature_match",
            "result": matches
        }
    ai_output = summarize_logs(compressed)
    return {
        "mode": "ai_summary",
        "result": ai_output
    }

