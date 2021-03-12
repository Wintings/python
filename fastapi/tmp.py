

# import requests
#from requests.api import get

import requests
from requests import post

class K8S_CLUSTER():
    def __init__(self, apiserver_address, token) -> None:
        self.token = "Bearer " + token
        self.headers = {"Authorization": self.token}
        self.apiserver_address = apiserver_address

    
    
    def get_cluster_resource(self, namespace, resource_name):
        if resource_name == 'deployment':
            url_path = '/apis/apps/v1/namespaces/{}/deployments?limit=500'.format(namespace)
        if resource_name == 'pod':
            url_path = '/api/v1/namespaces/{}/pods?limit=500'.format(namespace)
        
            
        r = requests.get(self.apiserver_address + url_path, headers=self.headers, verify=False)
        return r.json()    
    


# apiserver_address = "https://192.168.16.52:6443"
# token = "1odcnK68ISa6cPZTQDkZKC8vOY8"
# cert_path = "/Volumes/chaolei/vscode/ca.crt"

# k8s_cluster = K8S_CLUSTER(apiserver_address, token)
# print(k8s_cluster.get_cluster_resource("cpaas-system", "deployment"))
# print(k8s_cluster.get_cluster_resource("cpaas-system", "pod"))

