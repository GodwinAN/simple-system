from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/oddoreven/{num}")
def oddoreven(num: int):
            if (num % 2) == 0:
                        return{"{0}".format(num): "is Even"}
            else:
                        return{"{0}".format(num): "is Odd"}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
