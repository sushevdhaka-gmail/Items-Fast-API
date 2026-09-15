from fastapi import FastAPI

appname = FastAPI()

@appname.get("/home")
def root():
    return("its working")
