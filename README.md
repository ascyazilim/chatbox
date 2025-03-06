# LLaMA 3.1 Chatbox Servisi

## 📌 Proje Hakkında
- **Amaç:** LLaMA 3.1 ile çalışan bir chatbox servisi.
- **Teknolojiler:** Python, FastAPI, Java Spring Boot, Postman.

## 🚀 Kurulum
### 1. LLaMA 3.1 API (Python)
```bash
cd llama-api
pip install -r requirements.txt
uvicorn llama_api:app --reload

## 2. Backend (Java Spring Boot)
```bash
cd backend
mvn clean install
mvn spring-boot:run

## 🛠️ Test Et
- **URL:** `http://localhost:8080/api/chat`  
- **Method:** `POST`  
- **Body:** (JSON)
```json
{
    "message": "Merhaba LLaMA!"
}

## 📋 API Endpoint’leri

### 🐍 LLaMA API (Python)
- **POST:** `/chat` - LLaMA 3.1 ile mesaj gönder

### ☕ Backend API (Java Spring Boot)
- **POST:** `/api/chat` - LLaMA 3.1 ile mesaj gönder
