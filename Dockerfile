FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir fastapi uvicorn openai
COPY app.py profil.md ./
COPY static ./static
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
