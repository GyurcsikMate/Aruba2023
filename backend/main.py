from InputFastAPI import InputFastAPI
from OutputKubernetes import OutputKubernetes

if __name__ == "__main__":
    kube = OutputKubernetes()
    fastapi = InputFastAPI(kube)
    fastapi.run(host="0.0.0.0", port=8000)
    #kube.list_all_pods()