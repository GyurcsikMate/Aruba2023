from fastapi import FastAPI


class InputFastAPI:
    def __init__(self, kubernetes):
        self.app = FastAPI()
        self._kubernetes = kubernetes

        @self.app.get("/list")
        async def get_pods():
            pods = self._kubernetes.list_all_pods()
            pod_list = [pod.metadata.name for pod in pods.items]
            return {"pods": pod_list}

    def run(self, host="0.0.0.0", port=8000):
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)