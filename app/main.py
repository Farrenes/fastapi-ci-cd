from fastapi import FastAPI

app = FastAPI(title="My CI/CD App")
@app.get("/")

def read_root():
    return {"message": "Hello, CI/CD!"}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/sum")
def sum_numbers(a: int, b: int):
    return {"result": a + b}