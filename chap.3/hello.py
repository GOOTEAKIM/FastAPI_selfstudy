from fastapi import FastAPI, Header, Body, Response

app = FastAPI()

# @app.get("/hi")
# def greet():
#     return "Hello? World?"

# @app.get("/hi/{who}")
# def greet(who):
#     return f"Hello? {who}?"

@app.get("/hi")
def greet(who):
    return f"Hello? {who}?"

@app.post("/hi")
def greet(who: str = Body(embed = True)):
    return f"Hello? {who}?"

# GET : localhost:8000/

# Key : who, Value : Mom

# p64
@app.get("/agent")
def get_agent(user_agent: str = Header()):
    return user_agent

# p66
@app.get("/happy")
def happy(status_code = 200):
    return ":)"

# localhost:8000/header/marco/polo

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response : Response):
    response.headers[name] = value
    return "normal body"



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload = True)