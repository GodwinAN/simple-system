"""This code returns odd or even"""
from fastapi import FastAPI
import uvicorn

app = FastAPI()
"""This code returns odd or even"""
@app.get("/oddoreven/{num}")
def oddoreven(num: int):
    """This code returns odd or even"""
    if (num % 2) == 0:
        return{"{0}".format(num): "is Even"}
    return{"{0}".format(num): "is Odd"}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
