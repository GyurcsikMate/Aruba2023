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
            result = {"pods": pod_list}
            return result

        @self.app.get("/list/pods/{namespace}")
        async def get_pods_by_namespace(namespace: str):
            pods = self._kubernetes.list_all_pods_by_namespace(namespace)
            pod_list = [pod.metadata.name for pod in pods.items]
            result = {"pods": pod_list}
            return result

        @self.app.get("/list/namespaces")
        async def get_namespaces():
            namespaces = self._kubernetes.list_namespaces()
            namespace_list = [namespace.metadata.name for namespace in namespaces.items]
            result = {"namespaces": namespace_list}
            return result

        @self.app.get("/list/sort/pods")
        async def get_pods_sorted():
            namespaces = self._kubernetes.list_namespaces()
            namespacedict = {}
            for namespace in namespaces.items:
                raw = self._kubernetes.list_all_pods_by_namespace(namespace.metadata.name)
                try:
                    pod_list = [pod.metadata.name for pod in raw.items]
                except AttributeError:
                    pod_list = []
                namespacedict[namespace.metadata.name] = pod_list
            result = {"namespaces": namespacedict}
            return result

    def run(self, host="0.0.0.0", port=8000):
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)
