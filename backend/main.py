from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 프론트엔드 연동을 위한 CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 서비스 시 프론트엔드 URL로 제한
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    # AI 연동 전까지 사용할 임시 응답 (Mock API)
    return {"answer": f"[Mock 응답] 서버가 '{req.message}' 메시지를 정상적으로 수신했습니다."}

@app.get("/")
async def root():
    return {"message": "LoL RAG Server (Mock) is running."}
