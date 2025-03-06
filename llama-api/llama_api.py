from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import json
import re

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chatbox(input_message: Message):
    try:
        process = subprocess.Popen(
            ["ollama", "run", "llama3.1"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output, error = process.communicate(input=input_message.message.encode('utf-8'))

        ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
        output = ansi_escape.sub('', output.decode("utf-8", errors="ignore")).strip()
        error = ansi_escape.sub('', error.decode("utf-8", errors="ignore")).strip()

        print("---- Debug Başlangıcı ----")
        print("Çıktı:", repr(output))
        print("Hata:", repr(error))
        print("---- Debug Sonu ----")

        if error:
            print("Hata (Yoksayılıyor):", error)  # Hata çıktısını sadece göster ama HTTP 500 döndürme


        return {"response": output.strip()}
    except Exception as e:
        print("Exception:", str(e))  
        raise HTTPException(status_code=500, detail=str(e))