from kubernetes import client, config
from kubernetes.client.rest import ApiException


class OutputKubernetes:
    def __init__(self):
        config.load_kube_config()
        self.configuration = client.Configuration()

    def list_all_pods(self):

        with client.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            api_instance = client.WellKnownApi(api_client)

            try:
                v1 = client.CoreV1Api()
                print("Listing pods with their IPs:")
                ret = v1.list_pod_for_all_namespaces(watch=False)
                for i in ret.items:
                    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
                return ret.items
            except ApiException as e:
                print("Exception when calling sajt%s\n" % e)
