# main.py
import asyncio
from fastapi import FastAPI

from MessageQueue.consumer import listen_to_queue
from router import process_dqa

# FastAPI app
app = FastAPI()


# Run the listener in the background
@app.on_event("startup")
def startup_event():
    asyncio.create_task(listen_to_queue())


app.include_router(process_dqa.router, tags=['DQA'], prefix='/dqa')

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
