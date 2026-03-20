from fastapi import FastAPI

app = FastAPI()
# 우리서버/hello 라는 주소로 get요청이 들어오면
#hello 함수를 실행해라
@app.get("/hello")
def hello():
    return {"message": "안녕하세요"}


count = 0
# 2. /count 로 post 요청이 오면, 
@app.post("/count")
def increase_count():
    global count
    count +=1
    return {"message": "count 변수 증가 성공!"}


#3. /count로  get 요청이 오면
@app.get("/count")
def print_count():
    return {"message": f" guswo count "}