from fastapi import FastAPI


class InputFastAPI:
    def __init__(self, kubernetes):
        self.api = FastAPI()
        self._kubernetes = kubernetes
