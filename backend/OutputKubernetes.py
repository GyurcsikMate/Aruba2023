from kubernetes import client, config
from kubernetes.client.rest import ApiException

config.load_kube_config()
configuration = client.Configuration()

def list_all_pods():

    with client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = client.WellKnownApi(api_client)

        try:
            v1 = client.CoreV1Api()
            print("Listing pods with their IPs:")
            ret = v1.list_pod_for_all_namespaces(watch=False)
            for i in ret.items:
                print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        except ApiException as e:
            print("Exception when calling sajt%s\n" % e)

list_all_pods()