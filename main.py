from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/oddoreven/{num}")
def oddoreven(num: int):
            if (num % 2) == 0:
                return{"{0}".format(num): "is Even"}
            else:
                return{"{0}".format(num): "is Odd"}
               

#@app.get("/")
#async def root():
#    return {"message": "Hello World"}

#@app.get("/test")
#async def goddy_funct():
#    return {"message": "Hello Godwin"}

#@#app.get("/items/{item_id}")
#def read_item(item_id: int, q: Optional[str] = None):
 #   return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
