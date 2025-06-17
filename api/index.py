from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/api/")
async def virtual_ta(request: Request):
    data = await request.json()
    question = data.get("question", "")
    image = data.get("image", None)

    # 🔁 Replace this with real retriever logic later
    return JSONResponse({
        "answer": f"(Mocked) You asked: {question}",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/example",
                "text": "Example source from discourse"
            }
        ]
    })

# Required by Vercel
handler = app
