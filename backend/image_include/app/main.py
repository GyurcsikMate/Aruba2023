from InputFastAPI import InputFastAPI
from OutputKubernetes import OutputKubernetes

if __name__ == "__main__":
    kube = OutputKubernetes()
    app = InputFastAPI(kube)
