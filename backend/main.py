from InputFastAPI import InputFastAPI
from OutputKubernetes import OutputKubernetes

if __name__ == "__main__":
    kube = OutputKubernetes()
    fastapi = InputFastAPI(kube)
    #fastapi.run()
    kube.list_all_pods()