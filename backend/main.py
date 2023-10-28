from backend.InputFastAPI import InputFastAPI
from backend.OutputKubernetes import OutputKubernetes

if __name__ == "__main__":
    kube = OutputKubernetes()
    InputFastAPI(kube)
    kube.list_all_pods()