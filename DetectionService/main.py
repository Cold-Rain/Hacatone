from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    #return {"message": "Hello World"}
    return HTMLResponse(content=f"""
<h2>Detection service ready!</h2>
<a href="/docs" target="_blank">Service description</a>
""")

@app.get("/detect")
def detect(b64img, name):
    description = ''
    result = False

    return {
        "result":      result, 
        "description": description
    }
