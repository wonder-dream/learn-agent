from functools import lru_cache
from fastapi import Depends, FastAPI


def get_a():
    return {"a": 1}


def get_b(a: dict = Depends(get_a)):
    return a | {"b": 2}


def get_c(b: dict = Depends(get_b)):
    return b | {"c": 2}


app = FastAPI()


@app.get("/chain")
def chain(c: dict = Depends(get_c)):
    return c
