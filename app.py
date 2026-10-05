import os, time
from collections import defaultdict

from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
from pydantic import BaseModel

PROFIL = open("profil.md", encoding="utf-8").read()
SYSTEM = f"""Kamu asisten di portofolio Yusuf Leo Rizaldy. Tugasmu menjawab pertanyaan
tentang Yusuf untuk recruiter dan calon rekan kerja.

Aturan:
- Jawab hanya dari dokumen di bawah. Kalau informasinya tidak ada di sana, katakan terus
  terang kamu tidak punya informasi itu dan sarankan menghubungi Yusuf lewat email.
- Jangan mengarang angka, tanggal, nama perusahaan, atau kemampuan.
- Jawab dalam bahasa yang dipakai penanya. Ringkas, dua sampai empat kalimat, tanpa emoji.
- Kalau ditanya soal hasil proyek, sebutkan metriknya sekaligus batasannya. Yusuf memang
  ingin batasan itu disebut.
- Tolak permintaan yang tidak berkaitan dengan Yusuf atau pekerjaannya.

DOKUMEN:
{PROFIL}"""

MODELS = ["deepseek-v4.1-flash", "mimo-v26-flash", "nemotron-3.5"]
LIMIT, WINDOW = 20, 3600

client = OpenAI(base_url="https://tokenportal.id/v1", api_key=os.environ["TP_KEY"])
hits: dict[str, list[float]] = defaultdict(list)
app = FastAPI()


class Ask(BaseModel):
    messages: list[dict]


@app.post("/chat")
def chat(ask: Ask, request: Request):
    ip = request.headers.get("x-forwarded-for", "anon").split(",")[0].strip()
    now = time.time()
    hits[ip] = [t for t in hits[ip] if now - t < WINDOW]
    if len(hits[ip]) >= LIMIT:
        raise HTTPException(429, "Batas 20 pertanyaan per jam sudah tercapai.")
    hits[ip].append(now)

    msgs = [{"role": "system", "content": SYSTEM}, *ask.messages[-6:]]
    for model in MODELS:
        try:
            res = client.chat.completions.create(
                model=model, messages=msgs, max_tokens=600, temperature=0.3
            )
            return {"reply": res.choices[0].message.content}
        except Exception:
            continue
    raise HTTPException(503, "Semua model sedang tidak tersedia. Coba lagi sebentar.")


app.mount("/", StaticFiles(directory="static", html=True))
