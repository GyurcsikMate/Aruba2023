from kubernetes import client, config
from kubernetes.client.rest import ApiException


class OutputKubernetes:
    def __init__(self):
        config.load_kube_config()
        self.configuration = client.Configuration()

    def list_all_pods(self):
        try:
            print("GET list_all_pods")
            v1 = client.CoreV1Api()
            print("Listing pods with their IPs:")
            ret = v1.list_pod_for_all_namespaces(watch=False)
            return ret
        except ApiException as e:
            print("Exception when calling %s\n" % e)

    def list_namespaces(self):
        try:
            print("GET list_namespaces")
            v1 = client.CoreV1Api()
            ret = v1.list_namespace(watch=False)
            return ret
        except ApiException as e:
            print("Exception when calling %s\n" % e)

    def list_all_pods_by_namespace(self, namespace):
        try:
            print(f"GET list_all_pods_by_namespace: {namespace}")
            v1 = client.CoreV1Api()
            ret = v1.list_namespaced_pod(namespace, watch=False)
            return ret
        except ApiException as e:
            print("Exception when calling %s\n" % e)

    def create_deployment(self, name, docker_image, port):
        deployment = client.V1Deployment(
            metadata=client.V1ObjectMeta(name=name),
            spec=client.V1DeploymentSpec(
                replicas=1,
                selector=client.V1LabelSelector(
                    match_labels={"app": name}
                ),
                template=client.V1PodTemplateSpec(
                    metadata=client.V1ObjectMeta(labels={"app": name}),
                    spec=client.V1PodSpec(
                        containers=[
                            client.V1Container(
                                name=name,
                                image=docker_image,
                                ports=[client.V1ContainerPort(container_port=port)]
                            )
                        ]
                    )
                )
            )
        )
        api_instance = client.AppsV1Api()

        try:
            api_instance.create_namespaced_deployment(
                namespace="default", body=deployment)
            print("Deployment created.")
        except Exception as e:
            print(f"Deployment creation failed: {str(e)}")


    def delete_deployment(self, name):
        api_instance = client.AppsV1Api()
        try:
            api_instance.delete_namespaced_deployment(
                name=name, namespace="default", body=client.V1DeleteOptions())
            print("Deployment deleted.")
        except Exception as e:
            print(f"Deployment deletion failed: {str(e)}")
