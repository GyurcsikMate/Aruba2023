import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class InputFastAPI:
    _origins = [
        "*"
    ]

    def __init__(self, kubernetes):
        self.app = FastAPI()
        self._kubernetes = kubernetes
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=InputFastAPI._origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        @self.app.get("/list")
        async def get_pods():
            pods = self._kubernetes.list_all_pods()
            pod_list = [pod.metadata.name for pod in pods.items]
            result = json.dumps({"pods": pod_list})
            return result

    def run(self, host="0.0.0.0", port=8000):
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)
