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
                return ret
            except ApiException as e:
                print("Exception when calling sajt%s\n" % e)

    def create_deployment(self, name, docker_image, port):
        deployment = client.V1Deployment(
            metadata=client.V1ObjectMeta(name=name),
            spec=client.V1DeploymentSpec(
                replicas=1,
                selector=client.V1LabelSelector(
                    match_labels={name: "my-app"}
                ),
                template=client.V1PodTemplateSpec(
                    metadata=client.V1ObjectMeta(labels={name: f"from:{docker_image} docker image"}),
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