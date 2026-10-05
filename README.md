# Tanya tentang Yusuf

Chatbot tanya-jawab yang menjawab pertanyaan soal latar belakang dan hasil proyek saya.
Live di [tanya.yusufleo.my.id](https://tanya.yusufleo.my.id), salah satu tab di
[yusufleo.my.id](https://yusufleo.my.id).

## Kenapa tanpa RAG

Pilihan desain yang paling layak dibahas di repo ini justru yang tidak ada: tidak ada
vector store, tidak ada chunking, tidak ada embedding.

Seluruh materi tentang saya, yaitu CV, catatan proyek, dan angka hasil skripsi, totalnya
sekitar 6.000 token. Itu masuk utuh ke satu system prompt dan masih jauh di bawah jendela
konteks model yang dipakai. Menambahkan RAG di atas korpus sebesar ini berarti menambah
tiga komponen yang bisa gagal, retriever yang bisa salah ambil, dan satu layanan lagi yang
harus dijaga hidup di VPS 2 GB, tanpa satu pun perbaikan akurasi yang bisa saya ukur.

RAG mulai masuk akal ketika korpusnya tidak lagi muat di konteks, atau ketika sitasi ke
dokumen sumber jadi keharusan. Dua kondisi itu belum berlaku di sini. Saya pernah membangun
chatbot RAG betulan dengan LangChain dan Azure OpenAI saat magang di Telkom, jadi keputusan
ini bukan karena tidak bisa, tapi karena tidak perlu.

## Cara kerjanya

    static/index.html   kotak chat, tanpa build step
    app.py              FastAPI: POST /chat, rate limit, fallback model
    profil.md           satu-satunya sumber pengetahuan

- **Prompt dikunci.** Model hanya boleh menjawab dari `profil.md`, wajib bilang tidak tahu
  kalau informasinya tidak ada, dan wajib menyebut batasan proyek, bukan cuma metriknya.
- **Fallback model.** Gateway yang saya pakai punya ketersediaan per model yang naik-turun,
  jadi `/chat` mencoba tiga model berurutan sebelum menyerah dengan 503.
- **Rate limit.** 20 pertanyaan per IP per jam, dihitung di memori proses, cukup untuk
  melindungi kuota API dari penyalahgunaan.
- **Riwayat dipangkas** ke enam pesan terakhir agar biaya per permintaan tetap datar.

## Batasan yang diketahui

- Pengetahuannya berhenti di `profil.md`. Pertanyaan di luar itu akan dijawab tidak tahu.
- Hitungan rate limit hilang setiap kontainer restart, dan akan bocor kalau nanti dijalankan
  lebih dari satu replika. Perlu Redis kalau sampai di situ.
- Belum ada streaming, jadi jawaban baru muncul setelah model selesai menulis.
- Gateway LLM-nya pihak ketiga. Kalau layanannya turun, chatbot ikut mati.

## Menjalankan sendiri

    pip install fastapi uvicorn openai
    export TP_KEY=...        # API key gateway OpenAI-compatible
    uvicorn app:app --reload

Di produksi ia berjalan sebagai kontainer di belakang Caddy, bareng demo proyek lain di
satu VPS 2 vCPU dan 2 GB RAM yang saya kelola sendiri.
