from app.InputFastAPI import InputFastAPI
from app.OutputKubernetes import OutputKubernetes

if __name__ == "__main__":
    kube = OutputKubernetes()
    app = InputFastAPI(kube)