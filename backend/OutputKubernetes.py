from kubernetes import client, config
from kubernetes.client.rest import ApiException


class OutputKubernetes:
    def __init__(self):
        config.load_kube_config()
        self.configuration = client.Configuration()

    def list_all_pods(self):
        try:
            v1 = client.CoreV1Api()
            print("Listing pods with their IPs:")
            ret = v1.list_pod_for_all_namespaces(watch=False)
            return ret
        except ApiException as e:
            print("Exception when calling %s\n" % e)

    def list_namespaces(self):
        try:
            v1 = client.CoreV1Api()
            print("Listing namespaces:")
            ret = v1.list_namespace(watch=False)
            return ret
        except ApiException as e:
            print("Exception when calling %s\n" % e)

    def list_all_pods_by_namespace(self, namespace):
        try:
            v1 = client.CoreV1Api()
            print("Listing pods with their IPs:")
            ret = v1.list_namespaced_pod(namespace, watch=False)
            return ret
        except ApiException as e:
            print("Exception when calling %s\n" % e)

