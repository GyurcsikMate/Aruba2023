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

        @self.app.post("/create/{name}/{docker_image}/{port}")
        async def create_deployment(name: str, docker_image: str, port: int):
            print(f"Creating deployment with name: {name}, docker image: {docker_image}, port: {port}")
            self._kubernetes.create_deployment(name, docker_image, port)
            return "OK"
        @self.app.post("/delete/{name}")
        async def delete_deployment(name: str):
            print(f"Deleting deployment with name: {name}")
            self._kubernetes.delete_deployment(name)
            return "OK"

        @self.app.get("/active/{namespace}")
        async def get_active_pods(namespace: str):
            if namespace == "all":
                pods = self._kubernetes.list_all_pods()
            else:
                pods = self._kubernetes.list_all_pods_by_namespace(namespace)
            pod_list = [pod.metadata.name for pod in pods.items if pod.status.phase == "Running"]
            result = {"active_pods": len(pod_list)}
            return result

        @self.app.get("/count/{namespace}")
        async def get_pods_count(namespace: str):
            if namespace == "all":
                pods = self._kubernetes.list_all_pods()
            else:
                pods = self._kubernetes.list_all_pods_by_namespace(namespace)
            result = {"pods_count": len(pods.items)}
            return result

    def run(self, host="0.0.0.0", port=8000):
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)
